from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

download_dir = r"C:\Users\user\PycharmProjects\PageScraping"  # Directory where you want to save downloaded files

# ~Browser settings change~
options = webdriver.ChromeOptions()

options.add_experimental_option('prefs',  {
    "download.default_directory": download_dir,  # Change default directory for downloads
    "download.prompt_for_download": False,  # To auto download the file
    "download.directory_upgrade": True,
    "plugins.always_open_pdf_externally": True,  # It will not show PDF directly in chrome
    'download.extensions_to_open': 'xml',
    'safebrowsing.enabled': True
    }
)
options.add_argument("start-maximized")
options.add_argument("--disable-extensions")
options.add_argument("--safebrowsing-disable-download-protection")
options.add_argument("safebrowsing-disable-extension-blacklist")

PATH = r"C:\Users\chromedriver.exe"  # path to your chrome driver

driver = webdriver.Chrome(PATH, options=options)

driver.get("http://88.203.232.36:5904/login.aspx")  # Site url

link = driver.find_element_by_id("lnk_login")
link.click()
search_username = driver.find_element_by_id("HeaderControl_LoginControl_UserName")
search_username.send_keys("testuser@example.com")
search_password = driver.find_element_by_id("HeaderControl_LoginControl_Password")
search_password.send_keys("P@intserv_456")
login_button = driver.find_element_by_id("LoginButton")
login_button.click()

try:
    orders = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "MY ORDERS"))
        )
    orders.click()

    view = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "view"))
    )
    view.click()

    paystub_030119pdf = driver.find_element_by_id("rpt_results_paystubs_rpt_links_0_div_wrapper_0")
    paystub_030119pdf.click()

    paystub_030119xml = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "rpt_results_paystubs_rpt_links_0_hl_xml_link_0"))
    )
    paystub_030119xml.click()

    paystub_021519pdf = driver.find_element_by_id("rpt_results_paystubs_rpt_links_0_div_wrapper_1")
    paystub_021519pdf.click()

    paystub_021519xml = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "rpt_results_paystubs_rpt_links_0_div_wrapper_xml_1"))
    )
    paystub_021519xml.click()
    driver.stop_client()
    driver.close()

except:
    driver.quit()