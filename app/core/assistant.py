from app.core.language import LanguageProcessor
from app.core.automation import Automation
import pyautogui

class Assistant:
    def __init__(self):
        self.language_processor = LanguageProcessor()
        self.automation = Automation()
    
    def start(self):
        """Starts the assistant logic."""
        while True:
            print("Say something (or type 'exit' to quit):")
            command = input("Type 'voice' for voice input or your command: ").strip().lower()
            
            if command == "voice":
                # Use speech recognition for input
                command = self.language_processor.listen_and_recognize()
            
            if command == "exit":
                print("Goodbye!")
                break
            
            # Process the command
            self.process_command(command)

    def process_command(self, command):
        """Process the given command."""
        if "hello" in command:
            self.language_processor.respond("Hello! How can I assist you today?")
        elif "open browser" in command:
            self.language_processor.respond("Opening browser.")
            self.automation.open_browser()
        else:
            self.language_processor.respond("I didn't understand that. Please try again.")
