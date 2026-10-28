# E-Commerce QA Portfolio

A hands-on Quality Assurance portfolio demonstrating manual testing, defect reporting, 
and test automation against a public e-commerce demo application.

**Author:** Priyansha
**Tools:** Python, Pytest, Playwright, Git/GitHub

---

##  Project Overview

This repository showcases a complete QA testing lifecycle, from manual exploratory 
testing to automated regression testing. 

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
| `test_login.py` | Playwright automated test script (Python) |

---

##  Manual Testing

- **Test Cases:** [`test-cases.md`](test-cases.md) (Executed login flows, validated error messages).
- **Bug Reports:** [`bug-reports/`](bug-reports/) (Documented a cart state bug).

---

## 🤖 Test Automation

Automated using **Python**, **Pytest**, and **Microsoft Playwright**.

### What is automated:
1. **Login flow** (`test_login.py`): Validates successful login and navigation.

### How to run the tests locally:
```bash
# Install dependencies
pip install -r requirements.txt
playwright install

# Run tests
pytest
