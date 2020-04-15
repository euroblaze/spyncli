from .base import Base
from os.path import abspath, dirname
from backup_func import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os, time
from sys import platform

class Backup(Base):
    """Backup Class"""

    # function to take care of downloading file
    def enable_download_headless(self, driver ,download_dir):
        driver.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')
        params = {'cmd':'Page.setDownloadBehavior', 'params': {'behavior': 'allow', 'downloadPath': download_dir}}
        driver.execute("send_command", params)

    @property
    def run(self):

        import requests
        from environs import Env

        env = Env()
        env.read_env()
        API = env.str("API")
        auth_username = env.str("auth_username")
        auth_password = env.str("auth_password")
        dir_path = abspath(dirname(__file__))

        if self.options['create']:
            print("CREATE")
            # instantiate a chrome options object so you can set the size and headless preference
            # some of these chrome options might be uncessary but I just used a boilerplate
            # change the <path_to_download_default_directory> to whatever your default download folder is located
            chrome_options = Options()
            download_dir = self.options['<folder>']
            chrome_options.add_argument("--headless")
            chrome_options.add_argument("--window-size=1920x1080")
            chrome_options.add_argument("--disable-notifications")
            chrome_options.add_argument('--no-sandbox')
            chrome_options.add_argument('--verbose')
            chrome_options.add_experimental_option("prefs", {
                "download.default_directory": download_dir,
                "download.prompt_for_download": False,
                "download.directory_upgrade": True,
                "safebrowsing_for_trusted_sources_enabled": False,
                "safebrowsing.enabled": False
                })
            chrome_options.add_argument('--disable-gpu')
            chrome_options.add_argument('--disable-software-rasterizer')
            # initialize driver object and change the <path_to_chrome_driver> depending on your directory where your chromedriver should be
            # Check for operating system::::
            if platform == "linux" or platform == "linux2":
                print("LINUX")
                try:
                    driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=dir_path+"/chromedriver/chromedriver79")
                except:
                    try:
                        driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=dir_path+"/chromedriver/chromedriver80")
                    except:
                        try:
                            driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=dir_path+"/chromedriver/chromedriver81")
                        except:
                            print("u dont have chrome installed")
            elif platform == "darwin":
                print("OS X")
            elif platform == "win32":
                print("WINDOWS")
                try:
                    driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=dir_path+"/chromedriver/chromedriver79.exe")
                except:
                    try:
                        driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=dir_path+"/chromedriver/chromedriver80.exe")
                    except:
                        try:
                            driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=dir_path+"/chromedriver/chromedriver81.exe")
                        except:
                            print("u dont have chrome installed")

            # change the <path_to_place_downloaded_file> to your directory where you would like to place the downloaded file
            print(download_dir)
            # function to handle setting up headless download
            self.enable_download_headless(driver, download_dir)
            #self.backup_database(self.options['<url>'], self.options['<password>'], self.options['database'], driver)
            driver.get(self.options['<url>']+"/web/database/manager")
            elem = driver.find_elements_by_class_name("d-block")
            for index,each_elem in enumerate(elem):
                if self.options['<database>'] == each_elem.text:
                    elem = driver.find_elements_by_class_name("btn-group-sm")[index-1]
                    backup_button = elem.find_elements_by_class_name("o_database_action")[0].click()
                    print("yay found it ",index)
                    time.sleep(1)
                    elem = driver.find_elements_by_class_name("show")[0]
                    elem2 = elem.find_element_by_id("form_backup_db")
                    elem_mpwd = elem2.find_element_by_name("master_pwd")
                    elem_mpwd.send_keys(self.options['<password>'])
                    elem_btn = elem2.find_elements_by_class_name("btn-primary")
                    elem_btn[-1].click()
                    time.sleep(6)
            #os.rename(download_dir+"/"+self.options['<database>']+"*",self.options['<database>']+".zip")
            #response = requests.post(API + "backups/backup",
					#auth=(auth_username, auth_password),
					#data={'namespace': self.options['<namespace>'],
						#'name': self.options['<name>']})
           #print(response.status_code, response.content.decode())

	if self.options['read']:
		response = requests.get(API + "backups/backup/%s" % self.options['<namespace>'],
					auth=(auth_username, auth_password))
		print(response.status_code, response.content.decode())
