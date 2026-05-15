from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import requests
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = browser.new_page()

    #login
    page.goto("http://192.168.30.17")
    page.fill('input[type="text"]', "distributor")
    page.fill('input[type="password"]', "distributor")
    page.press('input[type="password"]', "Enter")
    page.wait_for_load_state('networkidle')
    
    page.goto("http://192.168.30.17/monitoring/diagnostics")
    page.wait_for_load_state('networkidle')
    page.wait_for_timeout(3000)

    lvlID = {'signal_level': '/Computer/WifiSignal Level'}
    results = {}
    for label, path in lvlID.items():
        ID = f'diagnostics_diagnostics_value_{path}'
        try:
            find = page.locator(f'[id =''{ID}'']')
            find.wait_for(timeout=5000)
            results[label] = find.inner_text()
        except Exception as e:
            results[label] = 'not found'
            
            
    print(results)

    #print(page.content())

    #browser.close()


'''
# Chrome options
options = Options()
options.add_argument("--start-maximized")

# Launch browser
driver = webdriver.Chrome(options=options)
#driver = APImir.mirRequest

#login pagfe
page = 'http://192.168.30.17/?mode=log-in'
pin = 1231

session= requests.Session()

payload = {
    'login_username': 'distributor',
    'login_password': 'distributor'
}

response = session.post(page, payload)
time.sleep(5)
print(response.status_code)
time.sleep(30)

#info page
infoPage =("http://192.168.30.17/monitoring/diagnostics")
time.sleep(5)

# Find the signal level element by ID
findSignal = driver.find_element(
    By.ID,
    "diagnostics_diagnostics_value_/Computer/WifiSignal Level"
)

# Extract text
signalLevel = findSignal.text

print("Signal Level:", signalLevel)

driver.quit()
'''