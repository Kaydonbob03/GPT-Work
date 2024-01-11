# Changelog

Copyright © 2023 Kayden Cormier | Copyright © 2023 K-GamesMedia

## Revision History

### September 30, 2023:

#### GPTvoice.py Update - Version 2.0
- Enhanced conversation continuity: Modified to maintain a running transcript of the dialogue, improving AI's contextual understanding and preventing conversation resets.
- Transcript archival: Implemented functionality to save conversation transcripts as "ChatTranscript_{current_date}.txt", updating after each AI response.

#### Documentation and Maintenance
- Initiated Changelog documentation.
- Updated README file.

---

### October 6, 2023:

#### New Feature: inputtovoice.py
- Introduced a new module for text-based user input, complementing the existing audio input functionality in GPTvoice.

#### Documentation Updates
- Revised Changelog.
- Updated README file.

---

### October 17, 2023:

#### New Development: GPTVoicewithGUI.py
- Launched a GUI version of GPTvoice, offering an interactive interface for customizing the fixed prompt and initiating the conversation thread. (Note: This is currently under development.)

#### Documentation Enhancements
- Updated Changelog.
- Revised README file.

---

### November 23, 2023:

#### GPTvoice.py Enhancement - Version 3.0
- Advanced audio processing: Significantly restructured the 'transcribe_audio' function for improved audio recording and processing. 
- Robust error handling: Integrated comprehensive exception handling for audio recording, speech transcription, and Azure TTS processing.
- GPT-3.5 Turbo fallback: Implemented a fallback mechanism to GPT-3.5 Turbo for scenarios where GPT-4 is unavailable, enhancing system resilience.

#### Release and Documentation
- Updated README file.
- Revised Changelog.
- Published new GitHub release - v5.0. 

> These updates collectively enhance the system's performance, user experience, and reliability, marking significant strides in our ongoing development efforts.

---

### January 11, 2024:

#### InputtoResponse.py Enhancement - Version 2.0
- Updated the API calling logic to the new OpenAi API endpoints for GPT API. It also now tries the user's access to gpt-4-turbo, then if that fails it goes to gpt-4, and if that fails it falls back to gpt-3.5-turbo which all users have access to.

#### Imageneration.py Enhancement - Version 2.0
- Updated the API calling logic to the new OpenAI API endpoints for Dall-E-3

#### Release and Documentation
- Updated README file.
- Revised Changelog.
- Published new GitHub release - v5.1.0 