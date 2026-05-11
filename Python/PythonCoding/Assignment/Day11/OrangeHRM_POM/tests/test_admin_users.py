import pytest
from pages.login_page import LoginPage
from pages.admin_page import AdminPage

@pytest.mark.parametrize("username", [
    "Admin"
])
def test_verify_users(driver, username):

    login_page = LoginPage(driver)

    login_page.login("Admin", "admin123")

    admin_page = AdminPage(driver)

    admin_page.side_menu.click_admin()

    assert admin_page.verify_user_exists(username)
