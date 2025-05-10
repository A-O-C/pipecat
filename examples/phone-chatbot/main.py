#Importing the required modules

from flask import Flask, request, Response
from twilio.twiml.voice_response import VoiceResponse
import time
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

#Tracking the state of the call
call_start_time = None
silence_events = 0
unanswered_prompts = 0
MAX_UNANSWERED = 3

@app.route("/voice", methods=["POST"])
def handle_call():
    global call_start_time, silence_events, unanswered_prompts

    # Reset on first call
    if call_start_time is None:
        call_start_time = time.time()
        silence_events = 0
        unanswered_prompts = 0

    resp = VoiceResponse()

    # Check if we should end the call
    if unanswered_prompts >= MAX_UNANSWERED:
        resp.say("No response received. Ending the call. Goodbye.", voice='alice')
        log_summary()
        return Response(str(resp), mimetype='application/xml')

    # Only say intro on first prompt
    if unanswered_prompts == 0:
        resp.say("Hello, this is Pipecat's bot. How can I assist you today?", voice='alice')

    resp.say("Go ahead and say something.", voice='alice')
    resp.pause(length=10)
    resp.say("I didn't catch that.", voice='alice')

    silence_events += 1
    unanswered_prompts += 1

    resp.redirect("/voice")
    return Response(str(resp), mimetype='application/xml')

#Logging call summary

def log_summary():
    duration = time.time() - call_start_time
    logging.info("=== CALL SUMMARY ===")
    logging.info(f"Call duration: {duration:.2f} seconds")
    logging.info(f"Silence events: {silence_events}")
    logging.info(f"Unanswered prompts: {unanswered_prompts}")
    logging.info("====================")

 #Starting the flask app   
    
if __name__ == "__main__":
    app.run(port=5000)
