import random
import threading
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
from selenium.webdriver.common.by import By
from fake_headers import Headers
import undetected_chromedriver as uc
from fake_useragent import UserAgent

from selenium.webdriver.common.keys import Keys
comments = [
    "Awesome video, really enjoyed it!",
    "Great work, keep it up!",
    "You're doing an amazing job with your content.",
    "Fantastic video, I learned a lot.",
    "Well done! Your videos are always top-notch.",
    "Incredible content as always!",
    "Your hard work really shines through in this video.",
    "This is fantastic, can't wait for more!",
    "You make learning so much fun. Thank you!",
    "You have a unique talent for creating engaging videos."
]

email_account = open('accounts.txt').readlines()
def remove_email(email_to_remove):
    file_path = 'accounts.txt'
    # Read the contents of the file
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Filter out lines that contain the specified email
    filtered_lines = [line for line in lines if email_to_remove not in line]

    # Write the filtered contents back to the file
    with open(file_path, 'w') as file:
        file.writelines(filtered_lines)

# Replace 'file.txt' with the actual path to your file and update the email_to_remove with the email you want to remove



class Booking(uc.Chrome):
    def __init__(self, driver_path='/usr/bin/chromedriver'):
        self.driver_path = driver_path
        os.environ["PATH"] += os.pathsep + self.driver_path

        options = Options()
        #options.add_argument("--disable-application-cache")
        #options.add_argument('--disable-third-party-cookies')


       
       # options.add_argument(f'--user-data-dir=C:/Users/user/AppData/Local/Google/Chrome/User Data')
       # options.add_argument(f'--profile-directory={profile_name}')
        agentsuser = UserAgent().random
        print(agentsuser)
       # headers = Headers(browser="chrome", os="win", headers=True)
        options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36")  # Simulate a mobile user agent
        options.add_argument("accept-language=en-US,en;q=0.5")
        options.add_argument("referer=https://www.youtube.com/")
       # options.add_argument("dnt=1")  # Do Not Track header

        super(Booking, self).__init__(options=options)

    def create_account(self):
       # self.maximize_window()
      email = random.choice(email_account)
      lineemail = email.split()
      sub = lineemail[0]
      passw = lineemail[1]
      recovery = lineemail[2]
      print(sub)
      print(passw)
      print(recovery)
      try :
        self.get('https://www.youtube.com/')
        self.implicitly_wait(30)
        self.find_element(By.XPATH,'/html/body/ytd-app/div[1]/div/ytd-masthead/div[4]/div[3]/div[2]/ytd-button-renderer/yt-button-shape/a/yt-touch-feedback-shape/div/div[2]').click()
        self.implicitly_wait(20)
        self.find_element(By.ID,'identifierId').send_keys(sub)
        self.implicitly_wait(30)
        self.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[2]/div/div[1]/div/div/button').click()
        if self.find_element(By.ID,"password") :
          self.implicitly_wait(20)
          self.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[1]/div/form/span/section[2]/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input').send_keys(passw)

        else :
          try :
             self.find_element('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[2]/div/div/button').click()

        
          except :
              print('pass')
              pass
        sleep(2)
        self.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[2]/div/div[1]/div/div/button').click()
        self.implicitly_wait(20)
        ##recovery email
        try :
           self.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[1]/div/form/span/section[2]/div/div/section/div/div/div/ul/li[3]').click()
           sleep(1)
        ## enter email
           self.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[2]/div[1]/div/div[1]/div/div[1]/input').send_keys(recovery)
           self.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button').click()
           self.implicitly_wait(30)
        except:
           pass
        ## now now 
        try :
           self.execute_script("window.scrollBy(0, 600);")
           self.find_element(By.XPATH,'/html/body/div/c-wiz/div/div/div/div[2]/div[4]/div[1]').click()
           self.implicitly_wait(30)
        except :
           pass
        self.find_element(By.XPATH,'/html/body/ytd-app/div[1]/div/ytd-masthead/div[4]/div[2]/ytd-searchbox/form/div[1]/div[1]/input').send_keys('nav 08 wcc2 batting tips how to hit boundaries')
        sleep(1)
        self.implicitly_wait(30)
        self.find_element(By.ID,'search-icon-legacy').click()
        self.implicitly_wait(30)
        self.find_element(By.XPATH,'/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]').click()
        sleep(1.5)
        try :
           self.implicitly_wait(20)
           self.find_element(By.XPATH,'/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/ytd-watch-metadata/div/div[2]/div[2]/div/div/ytd-menu-renderer/div[1]/ytd-segmented-like-dislike-button-renderer/yt-smartimation/div/div[1]/ytd-toggle-button-renderer/yt-button-shape').click()
        except :
           pass
        self.execute_script("window.scrollBy(0, 400);")

        self.implicitly_wait(30)
        try :
            self.find_element(By.XPATH,'/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/ytd-comments/ytd-item-section-renderer/div[1]/ytd-comments-header-renderer/div[5]/ytd-comment-simplebox-renderer/div[1]/yt-formatted-string').click()
            self.implicitly_wait(20)
            self.find_element(By.XPATH,'/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/ytd-comments/ytd-item-section-renderer/div[1]/ytd-comments-header-renderer/div[5]/ytd-comment-simplebox-renderer/div[3]/ytd-comment-dialog-renderer/ytd-commentbox/div[2]/div/div[2]/tp-yt-paper-input-container/div[2]/div/div[1]/ytd-emoji-input/yt-user-mention-autosuggest-input/yt-formatted-string/div').send_keys(random.choice(comments))
        except:
            try :
                input_element = self.find_element(By.ID, 'simplebox-placeholder')

# Input text into the input field
                input_element.click()
            except :
                pass
            self.find_element(By.ID,'contenteditable-root').send_keys(random.choice(comments))



           
        try :
           self.implicitly_wait(3)
           self.find_element(By.XPATH,"/html/body/ytd-app/ytd-popup-container/tp-yt-paper-dialog/yt-upsell-dialog-renderer/div/div[3]/div[1]/yt-button-renderer/yt-button-shape").click()
        except :
           pass
        
        self.implicitly_wait(4)
        self.find_element(By.XPATH,'/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/ytd-comments/ytd-item-section-renderer/div[1]/ytd-comments-header-renderer/div[5]/ytd-comment-simplebox-renderer/div[3]/ytd-comment-dialog-renderer/ytd-commentbox/div[2]/div/div[4]/div[5]/ytd-button-renderer[2]').click()
        try :
           self.implicitly_wait(2)
           self.find_element(By.XPATH,"//*[text()='Go it']").click()
        except :
           pass
        try :
           self.implicitly_wait(30)
           self.find_element(By.XPATH,"/html/body/ytd-app/ytd-popup-container/tp-yt-paper-dialog/yt-upsell-dialog-renderer/div/div[3]/div[1]/yt-button-renderer/yt-button-shape").click()
        except :
           pass
        
        self.delete_all_cookies()
        remove_email(email)
        self.close()
        print('='*100)
      except:
          self.close()
        
    def automate(self):
        try:
            
            self.execute_script("window.scrollBy(0, 200);")
            self.implicitly_wait(30)
       
        
          
            sleep(3)
            
            link = self.find_element(By.XPATH, '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/ytd-watch-metadata/div/div[4]/div[1]/div/ytd-text-inline-expander/div[1]/span[1]/yt-attributed-string/span/span[2]/span/a')
            

            link.click()

            try:
                self.implicitly_wait(10)
                button = self.find_element(By.CLASS_NAME, 'ytp-large-play-button')
                button.click()
            except:
                pass
            sleep(15)
          
            self.close()
        except Exception as e:
           
           
            self.close()

if __name__ == "__main__":
    num_profiles = int(input('How many profiles do you want to open (recommended 1 To not detected as a BOT): '))
   # profiles = ['Profile 10', 'Profile 12', 'Profile 14', 'Profile 15', 'Profile 16'][:num_profiles]
    while True :
        #profiles = ['Profile 1', 'Profile 2', 'Profile 3', 'Profile 4']


        def bot_task():
          with Booking() as bot :
             bot.create_account()
            
        threads = []
        for _ in range(int(num_profiles)):
           thread = threading.Thread(target=bot_task)
           thread.daemon = True
           thread.start()
           threads.append(thread)
           sleep(4)

        for thread in threads:
           thread.join()