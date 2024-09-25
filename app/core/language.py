import speech_recognition as sr
from gtts import gTTS
from googletrans import Translator
import pygame
import os
from io import BytesIO

class LanguageProcessor:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.translator = Translator()
        pygame.mixer.init()

    def listen_and_recognize(self):
        """Listens for voice input and returns recognized text."""
        with sr.Microphone() as source:
            print("Listening...")
            audio = self.recognizer.listen(source)
        
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
        tts = gTTS(text=text, lang="en")
        
        # Save the speech to an in-memory buffer
        audio_buffer = BytesIO()
        tts.write_to_fp(audio_buffer)
        
        # Save the buffer content to a temporary file
        audio_buffer.seek(0)
        temp_file_path = "temp_response.wav"
        with open(temp_file_path, "wb") as f:
            f.write(audio_buffer.read())
        
        # Play the audio file
        pygame.mixer.music.load(temp_file_path)
        pygame.mixer.music.play()
        
        # Wait until the audio is finished playing
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
        
        # Remove the temporary file
        os.remove(temp_file_path)
