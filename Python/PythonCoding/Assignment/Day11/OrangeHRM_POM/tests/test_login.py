from pages.login_page import LoginPage


def test_login(driver):

    login_page = LoginPage(driver)

    dashboard_page = login_page.login("Admin", "admin123")

    assert dashboard_page.get_dashboard_heading() == "Dashboard"
