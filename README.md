# E-Commerce QA Automation Portfolio

Welcome to my QA portfolio! This project demonstrates my skills in manual testing, bug reporting, UI automation, and API testing using an e-commerce demo application (SauceDemo).


**Tech Stack:** Python, Pytest, Playwright, Requests, Git/GitHub

---

##  Project Overview

The goal of this project was to practice the complete QA testing lifecycle. I started by manually testing the website to find bugs, and then I built a professional automation framework to verify those features automatically.

**What is tested in this repo:**
- **Login Flow:** Valid and invalid user logins.
- **Cart Bug:** A specific bug where sorting items changes the cart count incorrectly.
- **API Backend:** Verifying that the server returns the correct data.

---

##  Project Structure

Here is how the project is organized:

| Folder/File | What it does |
|-------------|--------------|
| `manual-testing/` | Contains manual test cases (`test-cases.md`) and a bug report (`bug-reports/`). |
| `pages/` | **Page Object Model:** Contains the locators and actions for the website (`login_page.py`, `cart_page.py`). |
| `test_login.py` | UI test: Validates a successful login. |
| `test_cart_bug.py` | UI test: Automates a bug where the cart count changes when sorting items. *(Note: This test intentionally fails because it catches a real bug on the site!)* |
| `test_login_data_driven.py` | Data-driven test: Tests 4 different login error scenarios at once. |
| `test_api.py` | API test: Validates a backend server response. |


##  How to Run the Tests

If you want to run these tests on your own computer, follow these simple steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/priyansha179/ecommerce-manual-and-automation-testing.git
