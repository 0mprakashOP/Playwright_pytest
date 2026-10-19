This is a Python language based Playwright test . 
Developed web automation framework utilizing Playwright and PyTest with Python.
• Implemented Page Object Model (POM) design pattern to maintain clean code architecture, reduce redundancy, and
enhance test maintainability.
• Leveraged PyTest fixtures, parameterized testing, and custom assertions for parallel test execution and comprehensive
test coverage, along with cross-browser execution capabilities (Chromium, Firefox).


Clone the project from GitHub:

git clone https://github.com/0mprakashOP/Playwright_pytest.git

Install Pytest and the Playwright Pytest plugin:

python -m pip install pytest pytest-playwright

Install the browser binaries required for testing:

python -m playwright install

To install only Chromium:

python -m playwright install chromium

To install only Firefox:

python -m playwright install firefox

Run all tests discovered by Pytest:

python -m pytest

This command discovers and executes tests according to Pytest's discovery rules and your project configuration.

Run all tests discovered by Pytest:

python -m pytest
python -m pytest --headed

For example, if your test file is pytest/test_login.py, run:

python -m pytest pytest/test_login.py