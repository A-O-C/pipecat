# Pipecat Phone Chatbot

## Description

       This project is a phone chatbot built using Flask and Twilio. It allows you to receive an inbound call, detects silence for 10+ seconds, and provides a prompt using text-to-speech (TTS). The bot also handles unanswered prompts gracefully and logs basic call statistics such as call duration, silence events, and unanswered prompts.

## Features
    1. Handles inbound calls
    2. Detects silence for 10+ seconds
    3. Plays a TTS prompt when silence is detected
    4. Gracefully terminates the call after 3 unanswered prompts
    5. Logs call statistics (duration, silence events, etc.)


## Installation

### 1. Clone the repository:
    git clone https://github.com/A-O-C/pipecat-phone-chatbot.git
    cd pipecat-phone-chatbot

### 2. Set up a virtual environment:
    python -m venv venv
    source venv/bin/activate

### 3. Install dependencies:
    Copy code
    pip install -r requirements.txt


## Usage

### Run the Flask app:

    python main.py
    Run ngrok to expose your local server to the internet:

### 2. Expose the Local Server Using ngrok:
    ngrok http 5000
    Copy the generated ngrok URL and configure it in the Twilio console.

### 3. Make a Call:
       Once the setup is complete, you can make a call to the Twilio number and interact with the Pipecat Phone Chatbot!


## Technologies Used
    Flask: A lightweight Python web framework for building web applications.

    Twilio: A cloud communications platform for building voice and messaging applications.

    ngrok: A tool that exposes local servers to the internet.




