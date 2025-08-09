#Skills Used:
#Python Programming
#Speech Recognition (speech_recognition library)
#Natural Language Processing (Conceptual understanding of how ChatGPT is used)
#OpenAI API Interaction (openai library)
#Subprocess Management (subprocess module for executing system commands)
#Basic Error Handling
import openai
import subprocess
import speech_recognition as sr

# Set the OpenAI API key
openai.api_key = 'your openai api'


def record_audio(filename, duration=5):
    """Record audio from the microphone and save it to a file."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.record(source, duration=duration)

    with open(filename, "wb") as f:
        f.write(audio.get_wav_data())


def transcribe_audio(filename):
    """Transcribe audio file using Google Web Speech API (requires internet connection)."""
    r = sr.Recognizer()
    with sr.AudioFile(filename) as source:
        audio_data = r.record(source)
        text = r.recognize_google(audio_data)
    return text


def get_chatgpt_response(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Use "gpt-4" if you have access to GPT-4
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message['content'].strip()
    except Exception as e:
        return f"Error: {str(e)}"


def execute_command(command):
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        return result.stdout if result.returncode == 0 else result.stderr
    except Exception as e:
        return f"Error: {str(e)}"


def main():
    print("Welcome! You can give commands to ChatGPT to execute on your Windows system.")

    while True:
        user_input = input("Enter your command (or 'exit' to quit, 'voice' to use voice input): ")

        if user_input.lower() == 'exit':
            print("Goodbye!")
            break

        if user_input.lower() == 'voice':
            record_audio("command.wav")
            user_input = transcribe_audio("command.wav")
            print(f"Transcribed voice command: {user_input}")

        prompt = f"Provide a Windows command to execute for: {user_input}"
        chatgpt_response = get_chatgpt_response(prompt)

        if chatgpt_response.startswith("Error:"):
            print(f"ChatGPT's response: {chatgpt_response}")
            continue

        print(f"ChatGPT's response: {chatgpt_response}")

        execution_result = execute_command(chatgpt_response)
        print(f"Execution result: {execution_result}")


if __name__ == "__main__":
    main()
