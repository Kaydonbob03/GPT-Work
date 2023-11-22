# GPT-Work

## Overview

Welcome to **GPT-Work**, a collection of Python scripts that interface with the GPT API and other related technologies. These tools are designed to showcase the capabilities of AI-driven interactions in various forms.

### Author

Developed by **Kayden Cormier (Kaydonbob03)** and **K-Games Media**.

### Copyright

ⓒ 2023 Kayden Cormier | ⓒ 2023 K-Games Media. All Rights Reserved.

This repository is for personal use and educational purposes. Users are permitted to access, use, and modify the code. **Redistribution or commercial use is strictly prohibited.**

---

## Getting Started

To utilize these scripts, an OpenAI API key is essential. Obtain one from [OpenAI API Keys](https://platform.openai.com/account/api-keys).

For specific functionalities like speech-to-text and text-to-speech, additional keys are required:

- **Azure Key**: Create one at the [Azure Portal](https://portal.azure.com/#home) under speech services.
- **Google Cloud Services Credentials**: Available at [Google Cloud Credentials](https://console.cloud.google.com/apis/credentials).

---

## Included Files

1. **Changelog.md**
   - Documents the updates and changes made to the scripts in this repository.

2. **GPTvoice.py**
   - Transcribes user input from a microphone using Google Cloud, processes it through GPT-4, and then outputs spoken responses via Azure Text-To-Speech.

   Required installations:
   ```shell
   pip install pyaudio numpy azure.cognitiveservices.speech openai threading keyboard google.cloud speech wave
   ```

3. **InputtoResponse.py**
   - Offers two modes: standard GPT chat and GPT chat with a fixed prompt. Toggle between them by commenting out the desired section.

   Dependencies:
   ```shell
   pip install openai
   ```

4. **Imagegeneration.py**
   - Generates images based on user input using OpenAI's Dall-E.

   Install:
   ```shell
   pip install openai requests
   ```

5. **inputtovoice.py**
   - Similar to GPTvoice.py, but takes text input instead of audio.

   Install these packages:
   ```shell
   pip install pyaudio numpy azure.cognitiveservices.speech openai wave
   ```

6. **GPTVoicewithGUI.py**
   - An interactive GUI application that mirrors the functionality of GPTvoice.py but allows users to edit the fixed prompt and start recording with a button click. Currently in the testing phase.

   Dependencies:
   ```shell
   pip install pyaudio numpy azure.cognitiveservices.speech openai threading keyboard google.cloud speech wave
   ```

---

### Thank You

Thank you for exploring my code! Your feedback and contributions are always welcome.

---
