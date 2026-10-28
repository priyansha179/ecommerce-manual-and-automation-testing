from playwright.sync_api import Page, expect

def test_bug_001_cart_sorting(page: Page):
    # 1. Login
    page.goto("https://www.saucedemo.com/")
    page.locator('[data-test="username"]').fill("standard_user")
    page.locator('[data-test="password"]').fill("secret_sauce")
    page.locator('[data-test="login-button"]').click()

    # 2. Add the Backpack to the cart
    page.locator('[data-test="add-to-cart-sauce-labs-backpack"]').click()

    # Verify the cart badge is 1 (Expected behavior)
    expect(page.locator('.shopping_cart_badge')).to_have_text("1")

    # 3. Change the sort order to "Name (Z to A)"
    page.locator('[data-test="product_sort_container"]').select_option("za")

    # 4. Verify the cart badge stays at 1 
    # (Because of the bug, this will FAIL! The actual count will be 2)
    expect(page.locator('.shopping_cart_badge')).to_have_text("1")