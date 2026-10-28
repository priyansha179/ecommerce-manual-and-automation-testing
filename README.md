# E-Commerce QA Portfolio

A hands-on Quality Assurance portfolio demonstrating manual testing, defect reporting, UI automation, and API testing against a public e-commerce demo application.

**Author:** Priyansha
**Tools:** Python, Pytest, Playwright, Requests, Git/GitHub

---

##  Project Overview

This repository showcases a complete QA testing lifecycle, from manual exploratory testing to automated regression testing. 

**Application under test:** [SauceDemo](https://www.saucedemo.com) (A public demo e-commerce site).

**Core User Flows Tested:**
- Login & Authentication (Valid, Invalid, Locked-out users)
- Product Listing & Sorting
- Shopping Cart Management

---

##  Repository Structure

| Folder/File | Description |
|--------|-------------|
| `bug-reports/` | Defect reports |
| `test-cases.md` | Manual test cases |
| `test_login.py` | Playwright UI automated test (Login) |
| `test_cart_bug.py` | Playwright UI automated test (Cart Bug) |
| `test_api.py` | API automated test (GET request validation) |

---

##  Manual Testing

- **Test Cases:** [`test-cases.md`](test-cases.md) (Executed login flows, validated error messages).
- **Bug Reports:** [`bug-reports/`](bug-reports/) (Documented a cart state bug).

---

##  Test Automation

Automated using **Python**, **Pytest**, **Microsoft Playwright** (UI), and **Requests** (API).

### What is automated:
1. **UI Login flow** (`test_login.py`): Validates successful login and navigation.
2. **UI Cart Bug** (`test_cart_bug.py`): Attempts to catch a known sorting bug on the site.
3. **API Testing** (`test_api.py`): Sends a GET request to a public API and validates the JSON response and status code.

### How to run the tests locally:
```bash
# Install dependencies
pip install -r requirements.txt
playwright install

# Run all tests
pytest

# Run just the API test with print output
pytest test_api.py -s
