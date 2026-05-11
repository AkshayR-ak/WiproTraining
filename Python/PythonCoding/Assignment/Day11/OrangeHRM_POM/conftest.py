import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options


@pytest.fixture
def driver():

    edge_options = Options()

    edge_options.add_argument("--ignore-certificate-errors")
    edge_options.add_argument("--allow-insecure-localhost")
    service = Service(
        "D:\\Wipro\\WiproTraining\\Python\\PythonCoding\\Assignment\\Day11\\OrangeHRM_POM\\msedgedriver.exe")
    driver = webdriver.Edge(
        service=service,
        options=edge_options
    )

    driver.maximize_window()

    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    yield driver

    driver.quit()