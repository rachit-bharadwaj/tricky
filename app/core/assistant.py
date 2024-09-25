import speech_recognition as sr
import pyttsx3
import pyautogui
from googletrans import Translator

class Assistant:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.translator = Translator()
        self.engine = pyttsx3.init()
        
        # Set properties
        self.engine.setProperty('rate', 150)    # Speed of speech
        self.engine.setProperty('volume', 1)    # Volume (0.0 to 1.0)
        
        # Set voice (0 for male, 1 for female)
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', voices[1].id)  # Female voice

    def listen(self):
        """Listens for voice input."""
        with sr.Microphone() as source:
            print("Listening...")
            audio = self.recognizer.listen(source)
        return audio
    
    def recognize_speech(self, audio):
        """Recognizes and processes the speech input."""
        try:
            print("Recognizing...")
            command = self.recognizer.recognize_google(audio)
            print(f"Command: {command}")
            return command.lower()
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
        except sr.RequestError:
            print("Could not request results; check your internet connection.")
        return ""
    
    def respond(self, text):
        """Generates a text-to-speech response."""
        self.engine.say(text)
        self.engine.runAndWait()

    def start(self):
        """Starts the assistant logic."""
        while True:
            print("Say something (or type 'exit' to quit):")
            command = input("Type 'voice' for voice input or your command: ").strip().lower()
            
            if command == "voice":
                # Use speech recognition for input
                audio = self.listen()
                command = self.recognize_speech(audio)
            
            # Exit condition
            if command == "exit":
                print("Goodbye!")
                break
            
            # Process commands (add more functionality here)
            self.process_command(command)
    
    def process_command(self, command):
        """Process the given command."""
        if "hello" in command:
            self.respond("Hello! How can I assist you today?")
        elif "open browser" in command:
            self.respond("Opening browser.")
            pyautogui.hotkey('ctrl', 'shift', 'n')  # Example of opening a new incognito browser tab
        else:
            self.respond("I didn't understand that. Please try again.")

# Example usage
if __name__ == "__main__":
    assistant = Assistant()
    assistant.start()
