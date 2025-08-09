Voice-Activated System Assistant
This project is a Python-based, voice-activated assistant that transcribes spoken commands, sends them to a large language model (LLM), and executes the returned system command on a Windows machine. It serves as a proof-of-concept for creating an intelligent, hands-free interface for your computer, combining speech recognition, natural language processing, and system automation.

Key Features
Voice Input: Record spoken commands from your microphone.

Speech-to-Text: Transcribe the recorded audio into text using the Google Web Speech API.

AI-Powered Command Generation: Use the OpenAI gpt-3.5-turbo model to convert natural language requests into executable system commands.

Command Execution: Run the generated commands directly on your operating system using the subprocess module.

Interactive Interface: A simple command-line loop allows you to continuously interact with the assistant via text or voice.

Skills Demonstrated
Python Programming

Speech Recognition (speech_recognition library)

Natural Language Processing (Conceptual understanding of LLM usage)

OpenAI API Interaction (openai library)

Subprocess Management (subprocess module for system commands)

Basic Error Handling

Prerequisites
To run this project, you will need Python installed on your system.

1. Python Libraries
Install all the required Python packages using pip:

pip install openai SpeechRecognition pyaudio

Note: pyaudio is necessary for the speech_recognition library to access your microphone.

2. OpenAI API Key
This project requires an OpenAI API key. For security, it is highly recommended to set your API key as an environment variable instead of hardcoding it in the script.

How to set an environment variable:

On Windows (Command Prompt):

set OPENAI_API_KEY=your-api-key-here

Note: This will only last for the current session. To make it permanent, use setx OPENAI_API_KEY "your-api-key-here".

On macOS/Linux (Terminal):

export OPENAI_API_KEY="your-api-key-here"

After setting the key, you can update your script to retrieve it securely:

import os
openai.api_key = os.getenv('OPENAI_API_KEY')

How to Use
Clone the Repository:

git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

Run the Script:
Execute the Python script from your terminal:

python your_script_name.py

Interact with the Assistant:

Text Input: Type a command and press Enter. For example: open google.com or what is the current time?

Voice Input: Type voice and press Enter. The program will listen for 5 seconds, transcribe your command, and then execute it.

Exit: Type exit and press Enter to quit the program.

Troubleshooting
ModuleNotFoundError: Ensure all the required libraries (openai, SpeechRecognition, pyaudio) are installed.

No module named '_portaudio': This error means pyaudio is not correctly installed. You may need to install the PortAudio library on your system before installing pyaudio.

API Key Error: Double-check that your OPENAI_API_KEY is set correctly in your environment variables.

Windows Command Execution: The LLM may sometimes provide commands that are not valid for your specific system. If a command fails, you can refine your prompt to the LLM to get a better result.

License
This project is licensed under the MIT License.
