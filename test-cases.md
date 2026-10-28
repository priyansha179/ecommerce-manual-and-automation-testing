# Test Cases - Login Feature

Application:** SauceDemo
**Module:** Login / Authentication

---

### TC-001: Login with valid credentials
**Steps:**
1. Go to saucedemo.com
2. Enter username: standard_user
3. Enter password: secret_sauce
4. Click "Login"

**Expected Result:** User is successfully logged in and redirected to the Products page.
Actual Result:User successfully logged in and redirected to the Products page.
Status:PASS

---

### TC-002: Login with locked-out user
**Steps:**
1. Enter username: locked_out_user
2. Enter password: secret_sauce
3. Click "Login"

**Expected Result:** An error message appears: "Sorry, this user has been locked out."
Actual Result:Sorry, this user has been locked out. 
Status:PASS
