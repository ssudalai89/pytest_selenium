# 🧪 Pytest + Selenium + BDD Automation Framework

A sample Python automation framework using **Selenium**, **Pytest**, and **BDD (pytest-bdd)**.
This guide walks through complete setup instructions — from Git installation to running tests and managing environments.

---

## ⚙️ 1. Install Git

1. Download **Git for Windows** → [https://git-scm.com/downloads](https://git-scm.com/downloads)
2. During installation, select:

   ```
   Git from the command line and also from 3rd-party software
   ```
3. Verify installation:

   ```bash
   git --version
   ```

---

## 📦 2. Clone the Repository

```bash
git clone https://github.com/ssudalai89/pytest_selenium.git
cd pytest_selenium
```

---

## 🌿 3. Create a New Branch

Always create a new branch before making changes:

```bash
git checkout -b feature/selenium-setup
```

---

## 🐍 4. Set Up Python Virtual Environment

Create and activate your virtual environment:

```bash
python -m venv venv
```

If you see a PowerShell policy error while activating:

```bash
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\venv\Scripts\activate
```

Your terminal should now show `(venv)` prefix.

---

For the first time, after installing all the required packages we need to create the requirements.txt file using the below command

pip freeze > requirements.txt

## 📋 5. Install Required Packages

Install all dependencies:

```bash
pip install -r requirements.txt
```

If the file doesn’t exist yet, create one with the following content:

```
pytest
pytest-bdd
selenium
webdriver-manager
pytest-html
```

---

## 🧪 6. Running Tests

To run all tests:

```bash
pytest
```

To generate an HTML report:

```bash
pytest --html=reports/report.html --self-contained-html
```

---

## 🚫 7. Manage `.gitignore` and Virtual Environment

Never commit the `venv/` folder.
Add these entries to `.gitignore` (in project root):

```
# Virtual environment
venv/

# Python cache
__pycache__/
*.pyc

# Reports and logs
reports/
logs/
```

If you accidentally added `venv/` before:

```bash
git rm -r --cached venv
git add .gitignore
git commit -m "Removed venv from tracking and added .gitignore"
git push
```

---

## 🌳 8. Working with Branches & Pull Requests

1. Create your feature branch:

   ```bash
   git checkout -b feature/your-feature-name
   ```
2. Commit and push your changes:

   ```bash
   git add .
   git commit -m "Added Selenium + Pytest-BDD setup"
   git push origin feature/your-feature-name
   ```
3. Open GitHub → click **Compare & Pull Request** to merge changes into `main`.

---

## 🧩 9. VS Code Setup (For BDD Highlighting)

Install the following extensions:

* 🥒 **Cucumber (Gherkin) Full Support** – by *alexkrechik*
* 📏 **Gherkin Indent** – for auto-formatting
* 🧼 **Cucumber Formatter** – for clean layouts

Add this configuration in `.vscode/settings.json`:

```json
{
  "cucumberautocomplete.steps": [
    "step_definitions/*.py"
  ],
  "cucumberautocomplete.syncfeatures": "features/*feature",
  "cucumberautocomplete.strictGherkinCompletion": true,
  "cucumberautocomplete.smartSnippets": true,
  "cucumberautocomplete.gherkinDefinitionPart": "@(given|when|then|step)"
}
```

This enables:

* Syntax highlighting in `.feature` files
* Ctrl+Click navigation from steps → step definitions

---

## 🔁 10. Recreating Environment (For New Developers)

After cloning:

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
pytest
```

---

## ✅ Summary

| Step            | Command                             | Purpose                     |
| --------------- | ----------------------------------- | --------------------------- |
| Install Git     | `git --version`                     | Verify Git setup            |
| Clone repo      | `git clone ...`                     | Get project locally         |
| Create venv     | `python -m venv venv`               | Isolated Python environment |
| Install deps    | `pip install -r requirements.txt`   | Install dependencies        |
| Run tests       | `pytest`                            | Execute automation suite    |
| Generate report | `pytest --html=reports/report.html` | Get HTML report             |
| Manage branches | `git checkout -b feature/...`       | Safe development            |
| Ignore files    | `.gitignore`                        | Keep repo clean             |

---

🎯 **This setup ensures:**

* Clean, portable Python environment
* Proper Git workflow using feature branches and PRs
* Organized Selenium + Pytest-BDD framework
* Easy onboarding for new contributors

---


New-Item -ItemType File -Name conftest.py
New-Item -ItemType directory -Name step_definitions 
