from playwright.sync_api import Page, expect

class CartPage:
    def __init__(self, page: Page):
        self.page = page
        self.backpack_button = page.locator('[data-test="add-to-cart-sauce-labs-backpack"]')
        self.cart_badge = page.locator('.shopping_cart_badge')
        self.sort_dropdown = page.locator('[data-test="product_sort_container"]')

    def add_backpack_to_cart(self):
        self.backpack_button.click()

    def change_sort_to_za(self):
        self.sort_dropdown.select_option("za")

    def verify_cart_count(self, expected_count):
        expect(self.cart_badge).to_have_text(expected_count)
