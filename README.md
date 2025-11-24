🧪 Playwright Test Automation Project (Python)
This project demonstrates the implementation of robust and maintainable end-to-end (E2E) tests using
the Playwright library with Python and the Pytest framework.
🎯 Design Pattern Used: Page Object Model (POM)
The code structure follows the Page Object Model (POM) pattern to ensure the separation of test logic
from the user interface locators. This enhances code reusability and simplifies maintenance (if a
selector changes, it only needs to be updated in the corresponding Page Object).
pages/ Folder (Model/Controller): Contains the LoginPage class, which encapsulates page
elements and actions ( login() , Maps() - Note: Changed 'Maps' to a general action name,
assuming it's an action, but keeping the original if it was intentional).
tests/ Folder (View): Contains the test scenarios defined as Pytest functions.
⚙️Setup and Execution
Follow these steps to run the tests on your machine:
1. Prerequisites
You need to have Python 3.8+ installed, along with the main browsers (Chromium, Firefox, WebKit).
2. Environment Installation
# Create a virtual environment (optional but recommended)
python -m venv venv
# Activate the virtual environment (use activate.bat for CMD on Windows)
.\venv\Scripts\activate.bat
# Install Python dependencies
pip install -r requirements.txt
# Install Playwright browser binaries
playwright install
3. Test Execution
Run the following command from the project's root directory.
To view execution in slow motion (recommended for review):
pytest tests/test_login.py --headed --slowmo 1000
11/24/25, 5:01 PM Google Gemini
https://gemini.google.com/app/bc406be0ebd3f087 1/2
For fast execution (headless by default):
pytest tests/test_login.py
🖼️Artifacts and Evidence
The project is configured to generate evidence of the execution:
Screenshot: The successful login test saves a screenshot in the artefactos/ folder.
Terminal Output: The final result of 2 passed confirms that both login scenarios (success and
failure) were validated correctly.
11/24/25, 5:01 PM Google Gemini
https://gemini.google.com/app/bc406be0ebd3f087 2/2
