import pyautogui

class Automation:
    def open_browser(self):
        """Automates opening a browser in incognito mode."""
        pyautogui.hotkey('ctrl', 'shift', 'n')
