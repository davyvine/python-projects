# Create mobile app in python using Kivy library
# UI will be written using kivy languange
# Backend and logics will be python

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior
# built in libraries
import json
import glob
from datetime import datetime
from pathlib import Path
import random
# sub module to support hover functionality - not created by kivy
from hoverable import HoverBehavior


Builder.load_file('design.kv')


# create class with exact same name as in design.kv
class LoginScreen(Screen):
    def sign_up(self):
        self.manager.current = "sign_up_screen"

    def login(self, uname, pword):
        with open("users.json") as file:
            # users will return the dictionary in json file
            users = json.load(file)
        if uname in users and users[uname]['password'] == pword:
            self.manager.current = "login_screen_success"
        else:
            self.ids.login_wrong.text = "Invalid Credentials. Please try again"


class SignUpScreen(Screen):
    def add_user(self, uname, pword):
        # open the users.json file
        with open("users.json") as file:
            users = json.load(file)

        users[uname] = {
            'username': uname,
            'password': pword,
            'created': datetime.now().strftime("%Y-%m-%D %H-%M-%S")
        }

        with open("users.json", 'w') as file:
            json.dump(users, file)

        self.manager.current = "sign_up_screen_success"


class SignUpScreenSuccess(Screen):
    def go_to_login(self):
        self.manager.transition.direction = 'right'
        self.manager.current = "login_screen"


class LoginScreenSuccess(Screen):
    def log_out(self):
        self.manager.transition.direction = "right"
        self.manager.current = "login_screen"

    def get_quote(self, feel):
        feel = feel.lower()
        # glob will get all file of a specified extension
        available_feelings = glob.glob("quotes/*txt")
        # .stem will get the name of a file without the extention, etc
        available_feelings = [Path(filename).stem
                              for filename in available_feelings]
        # open file equal to the feeling entered by user
        if feel in available_feelings:
            with open(f"quotes/{feel}.txt") as file:
                quotes = file.readlines()
            # print(quotes)
            self.ids.quote.text = random.choice(quotes)
        else:
            self.ids.quote.text = "Try another feeling"


class RootWidget(ScreenManager):
    pass


class MainApp(App):
    def build(self):
        return RootWidget()


# class to combine three objects
class ImageButton(ButtonBehavior, HoverBehavior, Image):
    pass


if __name__ == "__main__":
    MainApp().run()

# 1. APP
# 2. RootWidget
# 3. LoginScreen
