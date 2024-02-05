# NYPD Conversation Analysis with OpenAI Whisper

## Overview
This code utilizes OpenAI's advanced language model, Whisper, to analyze conversations within NYPD communications. 
The primary objective is to detect potential threats or concerns within the communication channel.

## Functionality
The code employs Natural Language Processing techniques, utilizing the Natural Language Toolkit (NLTK) for tokenization. Threat categories, including terrorism, violence, and cybercrime, are identified based on a predefined keyword list.

### 1. Audio Capture (`grabber.py`)
This thread captures the audio stream from the NYPD public channel at the specified Broadcastify URL (`https://broadcastify.cdnstream1.com/27526`) which is related to `NYPD - 109th and 111th Precincts`. Captured audio files in mp3 format are stored in the `grabbed` folder.

### 2. Speech-to-Text Recognition (`recognizer.py`)
Utilizing OpenAI Whisper, this thread converts speech to text. For each mp3-file in the `grabbed` folder, it creates a corresponding metadata-file with the name `NYPD_{timestamp}.json` and places it into the `recognized` folder.

### 3. Communication Analysis (`analyzer.py`)
This thread uses NLTK to analyze the text content from recognized messages, categorizing them into threat categories. If the category is 'REGULAR', the corresponding mp3 file and its metadata are removed. However, if a threat is identified, both files are moved to the `alert` folder, signaling the presence of a threat.

## How to Use
1. Install the required dependencies using `requirements.txt`.
```bash
    pip install -r requirements.txt
```
2. Run the script, using `python main.py` command.
```bash
python main.py
```

## Threat Categories
- Terrorism
- Gang-Related
- Hate Crime
- Weapon
- Shooting
- Car-Related
- Violence
- Criminal
- Hostage
- Crisis
- Cybersecurity

## Troubleshooting
Before running this script, ensure that `FFMPEG` is properly installed on your system, as `OpenAI Whisper` relies on it to read mp3-files. Visit the official `FFMPEG website` and download the appropriate version for your operating system. Then, set up the `PATH` correctly to enable the system to find it when necessary.

## Get in touch
Feel free to ask me on Twitter if you have any questions.
Twitter: https://twitter.com/dmytro_sazonov


