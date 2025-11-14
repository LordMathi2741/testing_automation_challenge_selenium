# Automation Challenge

## Overview
This repository is a month-long automated testing challenge focused on end-to-end UI tests using Selenium WebDriver with Python. The purpose is to learn and demonstrate reliable, maintainable browser automation and test design through practical exercises and scenarios located in `test` and `142`.

## Goals
- Practice Selenium WebDriver and browser automation.
- Design maintainable tests using the Page Object Model.
- Produce deterministic, reproducible tests and simple reports.
- Improve test organization and collaboration workflows.

## Tech Stack
- Python 3.8+
- Selenium WebDriver
- pytest
- Optional: `pytest-html`, `webdriver-manager`
- Browser drivers: ChromeDriver / GeckoDriver

## Requirements

### System
- macOS (development environment)
- Google Chrome or Firefox installed
- Corresponding driver accessible via `PATH` (e.g., `chromedriver`, `geckodriver`)

### Python dependencies
Install from `requirements.txt`. Example packages:
- `selenium==4.10.0`
- `pytest>=7.0`
- `pytest-html` (optional)
- `webdriver-manager` (optional)

## Installation
1. Create and activate a virtual environment:
   - `python -m venv venv`
   - `source venv/bin/activate`
2. Install dependencies:
   - `pip install -r requirements.txt`

## Project structure (relevant)
- `test/` \- main pytest suites and test cases for the challenge.
- `142/` \- additional scenario(s), test data or specialized scripts related to challenge item 142.
- `pages/` \- Page Object Model classes (if present).
- `fixtures/` \- pytest fixtures for browser setup/teardown.
- `reports/` \- generated test reports and artifacts.
- `requirements.txt` \- Python dependencies.

Update the description of `142/` if its purpose differs (data, artifacts, or tests).

## Running tests
- Run all tests in `test/`:
  - `pytest test`
- Run tests in `142/` (if they are pytest files):
  - `pytest 142`
- Generate an HTML report:
  - `pytest --html=reports/report.html --self-contained-html`

## Configuration
- Select browser via environment variable or pytest option:
  - `BROWSER=chrome pytest`
- Configure `BASE_URL`, timeouts and other constants via a central config file or fixtures.

## Best practices
- Use Page Object Model to encapsulate locators and actions.
- Prefer explicit waits (`WebDriverWait`) over fixed sleeps.
- Keep tests small, idempotent and isolated.
- Use fixtures for setup/teardown and test data.

## Troubleshooting
- Ensure driver version matches browser; consider `webdriver-manager` to manage drivers automatically.
- On macOS, grant execute permission if needed:
  - `chmod +x /path/to/chromedriver`
