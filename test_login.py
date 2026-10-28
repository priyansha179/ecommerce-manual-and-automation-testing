from playwright.sync_api import Page, expect

def test_tc001_valid_login(page: Page):
    # 1. Go to the website
    page.goto("https://www.saucedemo.com/")

    # 2. Enter username and password
    page.locator('[data-test="username"]').fill("standard_user")
    page.locator('[data-test="password"]').fill("secret_sauce")

    # 3. Click Login
    page.locator('[data-test="login-button"]').click()

    # 4. Verify we are on the Products page
    expect(page.locator(".title")).to_have_text("Products")