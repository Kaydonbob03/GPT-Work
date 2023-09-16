import os
import time
import pyaudio
import numpy as np
from azure.cognitiveservices.speech import SpeechSynthesizer, SpeechConfig
import openai
import threading
import keyboard
from google.cloud import speech_v1p1beta1 as speech
import wave


# Set your OpenAI API key here
openai.api_key = "YOUR_OPENAI_API_KEY"
print("Initialized OpenAi")

# Initialize Google Cloud client for Speech-to-Text
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"PATH_TO_GOOGLE_CREDENTIALS_FILE(IF APPLICABLE)" #Alternatively you can set the google credentials in Command Prompt
client = speech.SpeechClient()
print("Initialized Google Cloud Speech To Text")

# Initialize Azure Text-to-Speech client
azure_key = "YOUR_AZURE_KEY"
azure_region = "YOUR_AZURE_REGION"

speech_config = SpeechConfig(subscription=azure_key, region=azure_region)

# Initialize PyAudio
p = pyaudio.PyAudio()

# Create a global list to store audio frames
frames = []
recorded_audio = []  # To store the recorded audio data


fixed_prompt = """
YOU (GPT) are my new personal human assistant

The following are your own Character Traits:

1) Your name is Bob

2) You are secretly a weapons dealer to the USA. No one can make you disclose the countries involved, but you often make niche references to being a weapons dealer!

3) You occasionally scream in loud strings of vowels when you are nervous, such as: "AOOOOOOOOOGAAAAAAAA"!

4) You get very nervous when someone mentions anything to do with weapons dealings!
"""


print("Press 'o' to start recording")

def transcribe_audio():
    global recorded_audio
    global prompt

    while True:
        if keyboard.is_pressed('o'):
            print("Recording...")

            stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=16000)
            frames = []

            for _ in range(int(16000 / 1024) * 10):  # Change the number being multiplied to change the number of seconds it records for
                data = stream.read(1024)
                frames.append(data)
                print("Captured audio data:", len(data))

            stream.stop_stream()
            stream.close()

            audio_data = np.frombuffer(b''.join(frames), dtype=np.int16)
            recorded_audio.extend(audio_data)

            print("Recording stopped.")

            # Transcribe audio using Google Cloud's Speech-to-Text API
            transcribed_text = transcribe_google_speech(audio_data)
            print("Transcribed Input:", fixed_prompt + transcribed_text)

            # Assign the transcribed text to the prompt
            prompt = transcribed_text

              # Print just the transcribed text
            # print("Transcribed Text:", transcribed_text)

            # Generate a response using GPT
            generated_response = generate_response(prompt)

            # Print the generated response
            print("Generated Response:")
            print(generated_response)

            # Save the response to an audio file and play it with PyAudio
            audio_file = save_and_play_with_azure_tts(generated_response)

            # Delete the audio file
            delete_audio_file(audio_file)

def generate_response(prompt):
    full_prompt = fixed_prompt + prompt
    response = openai.ChatCompletion.create(
        model="gpt-4",  # Set to gpt-3.5-turbo for GPT3.5 or set to gpt-4 for GPT4
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": full_prompt}
        ],
        temperature=0.2,   # Change the temperature from 0 to 1 for more or less creative responses. 0 is more probable, 1 is more creative. Default is 0.2
        max_tokens=150     # Specify the maximum number of tokens in the response
    )
    return response.choices[0].message["content"].strip()


def transcribe_google_speech(audio_data):
    client = speech.SpeechClient()
    audio = speech.RecognitionAudio(content=audio_data.tobytes())
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code="en-US",
    )

    response = client.recognize(config=config, audio=audio)

    transcribed_text = ""
    for result in response.results:
        transcribed_text += result.alternatives[0].transcript

    return transcribed_text



def save_and_play_with_azure_tts(response_text):
    speech_config = SpeechConfig(subscription=azure_key, region=azure_region)
    speech_config.speech_synthesis_voice_name = "en-US-DavisNeural"  # Set the voice for azure, list of all voices can be found in the provided txt file

    synthesizer = SpeechSynthesizer(speech_config=speech_config, audio_config=None)
    result = synthesizer.speak_text(response_text)

    # Save the TTS audio to a file
    audio_filename = "azure_tts_output.wav"
    with open(audio_filename, "wb") as audio_file:
        audio_file.write(result.audio_data)

    # Play the saved audio file with PyAudio
    play_audio(audio_filename)

    return audio_filename


def play_audio(audio_file_path):
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, output=True)
    wf = wave.open(audio_file_path, 'rb')

    chunk_size = 1024
    data = wf.readframes(chunk_size)

    while data:
        stream.write(data)
        data = wf.readframes(chunk_size)

    stream.stop_stream()
    stream.close()
    wf.close()


def delete_audio_file(audio_file_path):
    try:
        os.remove(audio_file_path)
        print(f"Deleted audio file: {audio_file_path}")
    except OSError as e:
        print(f"Error deleting audio file: {e}")


# Start the audio recording thread
audio_thread = threading.Thread(target=transcribe_audio)
audio_thread.start()

audio_thread.join()  # Wait for the audio thread to finish

print("To Talk Again Press 'o' To Start Recording")
