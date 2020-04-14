from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os, time

# function to take care of downloading file
def enable_download_headless(browser,download_dir):
    browser.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')
    params = {'cmd':'Page.setDownloadBehavior', 'params': {'behavior': 'allow', 'downloadPath': download_dir}}
    browser.execute("send_command", params)

# instantiate a chrome options object so you can set the size and headless preference
# some of these chrome options might be uncessary but I just used a boilerplate
# change the <path_to_download_default_directory> to whatever your default download folder is located
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--verbose')
chrome_options.add_experimental_option("prefs", {
        "download.default_directory": "/home/andrej/Desktop",
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing_for_trusted_sources_enabled": False,
        "safebrowsing.enabled": False
})
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--disable-software-rasterizer')

# initialize driver object and change the <path_to_chrome_driver> depending on your directory where your chromedriver should be

try:
	driver = webdriver.Chrome(chrome_options=chrome_options, executable_path="/home/andrej/Downloads/chromedriver79")
except:
	try:
		driver = webdriver.Chrome(chrome_options=chrome_options, executable_path="/home/andrej/Downloads/chromedriver80")
	except:
		try:
			driver = webdriver.Chrome(chrome_options=chrome_options, executable_path="/home/andrej/Downloads/chromedriver81")
		except:
			print("u dont have chrome installed")

# change the <path_to_place_downloaded_file> to your directory where you would like to place the downloaded file
download_dir = "/home/andrej/Desktop"

# function to handle setting up headless download
enable_download_headless(driver, download_dir)

def backup_database(url,master_pass,db_name):
    driver.get(url+"/web/database/manager")
    elem = driver.find_elements_by_class_name("d-block")
    for index,each_elem in enumerate(elem):
        if db_name == each_elem.text:
            elem = driver.find_elements_by_class_name("btn-group-sm")[index-1]
            backup_button = elem.find_elements_by_class_name("o_database_action")[0].click()
            print("yay found it ",index)
            time.sleep(1)
            elem = driver.find_elements_by_class_name("show")[0]
            elem2 = elem.find_element_by_id("form_backup_db")
            elem_mpwd = elem2.find_element_by_name("master_pwd")
            elem_mpwd.send_keys(master_pass)
            print(elem2)
            elem_btn = elem2.find_elements_by_class_name("btn-primary")
            elem_btn[-1].click()
            time.sleep(6)

# get request to target the site selenium is active on
#driver.get("https://www.thinkbroadband.com/download")

# initialize an object to the location on the html page and click on it to download
#search_input = driver.find_element_by_css_selector('#main-col > div > div > div:nth-child(8) > p:nth-child(1) > a > img')
#search_input.click()
