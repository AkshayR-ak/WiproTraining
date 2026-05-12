from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime
import os

def before_scenario(context, scenario):
    context.driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install())
    )
    context.driver.maximize_window()

def after_scenario(context, scenario):
    if scenario.status == "failed":
        if not os.path.exists("screenshots"):
            os.makedirs("screenshots")

        filename = f"screenshots/{scenario.name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        context.driver.save_screenshot(filename)

    context.driver.quit()