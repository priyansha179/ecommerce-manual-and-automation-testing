from playwright.sync_api import Page, expect
from pages.login_page import LoginPage

def test_tc001_valid_login(page: Page):
    # Create an instance of the page object
    login_page = LoginPage(page)
    
    # Use the page object methods
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")

    # Verify
    expect(login_page.page_title).to_have_text("Products")