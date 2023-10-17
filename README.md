# GPT-Work

A Repo of Python Scripts Working With The GPT API As Well As Other Programs Including GPT

Hi!

The files contained here are the work of Kayden Cormier (Kaydonbob03) and K-Games Media.

Copyright ⓒ 2023 Kayden Cormier | Copyright ⓒ 2023 K-GamesMedia

The Included Files are as Follows:

1. Changelog.md - A changelog of the updates to the files below

2. GPTvoice.py - This script will get user input from the default microphone and transcribe the audio to text via google cloud services, then sends the text to GPT 4 for a response, collects the response, then sends the response to Azure Text-To-Speech to give the AI a voice.

To use this program make sure to pip install the following:

pyaudio \
numpy \
azure.cognitiveservices.speech \
azure \
openai \
threading \
keyboard \
google.cloud \
speech \
wave

3. InputtoResponse.py - This script has two different varients. Just comment out either or to change it. The two options are just chatting with GPT or chatting with GPT with a Fixed Prompt before your input.

All thats needed for this script is:

openai

4. Imagegeneration.py - This script will use openai's Dall-E image generator to generate an image for the users input

All you need for this is:

openai \
requests

To use any of these programs you will need an openai api key. You can get one [here](https://platform.openai.com/account/api-keys)
To use the GPTaudio script you will also need an azure key. you can get one [here](https://portal.azure.com/#home) and then navigate to speech services and make an api key. You will also need Google Cloud services credentials. Google Cloud credentials can be found [here](https://console.cloud.google.com/apis/credentials)

5. inputtovoice.py - much like GPTvoice.py, this file will provide user input to GPT, get a response, then send the response to azure tts. Althought, instead of getting user input via audio transcrption, it will instead get user input via text

To use this program make sure to pip install the following:

pyaudio \
numpy \
azure.cognitiveservices.speech \
azure \
openai \
wave \

6. GPTVoicewithGUI.py - much like GPTvoice.py, this file will provide user input to GPT, get a response, then send the response to azure tts. Althought, instead of doing everything through the code, this instead is a gui based application. This will allow the user to edit the fixed prompt and then start the recording with the press of a button.

To use this program make sure to pip install the following:

pyaudio \
numpy \
azure.cognitiveservices.speech \
azure \
openai \
threading \
keyboard \
google.cloud \
speech \
wave

Thanks for checking out my code!
