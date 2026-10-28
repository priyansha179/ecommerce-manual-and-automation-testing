from playwright.sync_api import Page
from pages.login_page import LoginPage
from pages.cart_page import CartPage

def test_bug_001_cart_sorting(page: Page):
    # Setup Page Objects
    login_page = LoginPage(page)
    cart_page = CartPage(page)

    # 1. Login
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")

    # 2. Add the Backpack to the cart & verify count is 1
    cart_page.add_backpack_to_cart()
    cart_page.verify_cart_count("1")

    # 3. Change the sort order to "Name (Z to A)"
    cart_page.change_sort_to_za()

    # 4. Verify the cart badge stays at 1 
    # (Because of the bug, this will FAIL! The actual count will be 2)
    cart_page.verify_cart_count("1")
