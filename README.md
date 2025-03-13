# chatgpt-api-logger

This script attempts to find a working OpenAI API from a list of known endpoints. Internet Required.

# What does it do?
It will try different OpenAI API endpoints endlessly until it finds one that works. It also searches for a model that fits with the API by fetching available models from OpenAI. If fetching models fails, it falls back to a predefined list of OpenAI endpoints.

# Supported OpenAI Models:
- Text-Based:
  - GPT-3.5: A powerful closed-source language model.
  - GPT-4o Mini: A cost-effective and compact variant of the GPT-4o model, designed for smaller tasks and vision tasks.
- Image-Based:
  - DALL-E: A generative AI tool for creating images from text descriptions.
- Speech-Based:
  - Whisper: An automatic speech recognition (ASR) model for transcribing audio into text.
- Other:
  - Jukebox: A generative AI model for music production, currently in an experimental phase.
  - o1 Mini: A fast, cost-efficient reasoning model tailored to coding, math, and science use cases.

# How to use it?
1. Ensure you have Python installed: [Python.org](https://python.org)
2. Install the required dependencies:
   ```sh
   pip install requests
   ```
3. Run the script:
   ```sh
   python main.py
   ```
4. To stop the script, press `Ctrl+C`.

# What if I get caught?
You are responsible for your own actions. Use this script responsibly.

# It won't open, why?
Make sure you have Python installed and the required dependencies!