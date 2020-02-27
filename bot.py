from webbot import Browser
import random

class BumbleBot:
    def __init__(self):
        #### REMOVE PHONE AND PASSWORD ####
        self.phoneNumber = ''
        self.password = ''
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
