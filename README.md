# **Tricky - AI-Based Personal Assistant**

![Tricky Logo](./resources/images/tricky_logo.png)  
*A smart personal assistant that understands you, performs tasks across your devices, writes code, and more!*

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [Commands and Functionality](#commands-and-functionality)
- [Cross-Device Integration](#cross-device-integration)
- [Development](#development)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [License](#license)

---

## Overview

**Tricky** is a powerful AI-based personal assistant that brings the vision of intelligent, conversational agents to life. Built with Python, it combines advanced speech recognition, task automation, natural language processing, and cross-device integration to help you accomplish your goals efficiently.

Tricky can:
- Recognize and respond to your voice.
- Perform a variety of tasks, from opening applications to writing code.
- Translate languages and handle speech synthesis.
- Operate seamlessly across desktop and mobile devices.

---

## Features

### 🔊 **Speech Recognition**
- Listens to your commands using `SpeechRecognition` and processes them.

### 🎤 **Text-to-Speech & Translation**
- Speaks responses back to you using `pyttsx3` and supports multiple languages using the Google Translate API.

### 🖥️ **Automation**
- Automates routine tasks like opening apps, controlling system functions, and web navigation.

### 🧠 **AI-Assisted Conversations**
- Integrates AI models for natural conversations and ideation support.

### 📱 **Cross-device Support**
- Syncs tasks and assistant commands between your desktop and mobile devices.

---

## Tech Stack

**Languages:**
- ![Python](https://img.shields.io/badge/Python-3.10-blue.svg)
  
**Core Libraries:**
- Speech Recognition: `speech_recognition`
- Text-to-Speech: `pyttsx3`, `gTTS`
- Translation: `googletrans`
- Task Automation: `pyautogui`
- GUI: `PyQt5`, `Tkinter`
- Mobile (Optional): `React Native`, `Kivy`
- Testing: `unittest`, `pytest`

**Other Tools:**
- Virtual Environment: `.venv`
- Package Management: `pip`
  
---

## Installation

Follow these steps to set up **Tricky** on your system.

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/tricky-ai-assistant.git
cd tricky-ai-assistant
```

### 2. Create and Activate Virtual Environment
```bash
python -m venv .venv
source .venv/bin/activate  # For Linux/macOS
.venv\Scripts\activate     # For Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure API Keys
- If you plan to use any APIs (like cloud-based NLP), update the `app/config.py` file with your API keys.

### 5. Run the Application
```bash
python main.py
```

---

## Project Structure

```bash
Tricky/
│
├── .venv/                   # Virtual environment
├── app/
│   ├── __init__.py          # Initializes the app module
│   ├── config.py            # Configuration (API keys, settings)
│   ├── core/
│   │   ├── assistant.py     # Main logic for handling commands
│   │   ├── language.py      # Speech recognition, translation, and TTS
│   │   ├── automation.py    # Task automation (opening apps, etc.)
│   ├── gui/
│   │   ├── main_window.py   # Main GUI (PyQt or Tkinter)
│   └── utils/
│       ├── logger.py        # Logging functionality
├── tests/                   # Unit tests for modules
├── resources/
│   ├── images/              # Store images (like Tricky's logo)
│   └── audio/               # Audio files (if needed)
├── main.py                  # Entry point of the application
├── requirements.txt         # Dependencies
└── README.md                # Project overview (this file)
```

---

## Usage

Once the setup is complete, you can start **Tricky** using voice or text commands. You can invoke different tasks by either typing or speaking them.

```bash
python main.py
```

---

## Commands and Functionality

### 🔍 Example Commands:
- **"Hello"**: Tricky will respond with a greeting.
- **"Open browser"**: Opens a new browser window.
- **"Translate 'Hello' to Spanish"**: Provides translation using `googletrans`.
- **"Write Python code to reverse a list"**: AI code generation for specific tasks.

You can add more commands by extending the `app/core/assistant.py` and `app/core/automation.py` files.

---

## Cross-Device Integration

You can extend **Tricky** to work on both **desktop** and **mobile devices**.

- **For Desktop:** A GUI can be developed using `PyQt5` or `Tkinter`.
- **For Mobile:** You can integrate **React Native** or **Kivy** to make it work seamlessly on phones, utilizing speech-to-text and TTS for interactions.

To sync tasks across devices, implement cloud integration using **Firebase** or **AWS** in `config.py`.

---

## Development

### Adding New Features

You can add custom commands by editing:
- `assistant.py`: For managing the main logic.
- `automation.py`: For task automation (like opening apps or performing system commands).
- `language.py`: For adding speech recognition or translation features.

### Running Tests
```bash
pytest
```

Make sure you test your modules before pushing updates.

---

## Future Enhancements

- **Advanced AI Integration**: Add GPT-like capabilities for intelligent, contextual conversations.
- **Mobile App**: Develop a companion app for mobile use.
- **Cloud Sync**: Sync user data across devices using cloud storage solutions.
- **Voice Customization**: Allow users to choose different voices and languages for TTS.

---

## Contributing

Feel free to contribute to this project by submitting pull requests or reporting issues. Follow the [contributing guidelines](./CONTRIBUTING.md) to get started.

---

## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for more information.

---

## Contact

Developed by **Rachit Bharadwaj**  
Connect with me on [LinkedIn](https://www.linkedin.com/in/rachit-bharadwaj/) or [GitHub](https://github.com/yourusername).

---

### Screenshots:
Add some visual appeal by including screenshots of your assistant in action (optional).

- ![Assistant in Action](./resources/images/assistant_in_action.png)

---

With this **README** file, you now have a visually appealing and structured guide to your project, ready for sharing with others! Let me know if you'd like to make any changes or include additional sections.