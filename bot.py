from webbot import Browser
import random
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-n', action='store',
                    dest='Number', required=True,
                    help='Phone number')
parser.add_argument('-p', action='store',
                    dest='Password', required=True,
                    help='Password')

results = parser.parse_args()

class BumbleBot:
    def __init__(self):
        self.phoneNumber = results.Number
        self.password = results.Password
        self.web = Browser()
        self.Login()

    def Login(self):
        self.web.go_to('https://bumble.com/app')
        self.web.click('Use cell phone number')
        self.web.type(self.phoneNumber,into='Enter your number')
        self.web.click('Continue')
        self.web.type(self.password,into='Password')
        self.web.click('Sign in')

    def Like(self):
        self.web.click('Like',number=3, classname='encounters-controls__action')

    def Pass(self):
        self.web.click('Pass',classname='encounters-controls__action')

    def LikeLoop(self):
        likeCount = 0
        passCount = 0
        count = random.randint(2,6)
        #3/2 change to like someone so they (hopefully) dont think its a bot
        while(True):
            if (count % 2) == 0:
                self.Like()
                likeCount += 1
            else:
                self.Pass()
                passCount += 1
            count = random.randint(2,6)
            print(f'Likes: {likeCount} Passes: {passCount}', end='\r')


#TO DO#
# -add exception for robot prompt
# -add exception for 'end of the line'
