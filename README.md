# PYTHON CRUD API Test Automation

This project provides a test automation framework for CRUD operations on REST APIs, specifically using [Reqres](https://reqres.in/) as a sample API for testing. The tests are written in Python, using the Pytest framework, and generate an HTML report upon execution.

## Project Structure

```plaintext
crud_api_tests/
├── reports/                 # Generated HTML reports
├── tests/                   # Contains test cases
│   ├── __init__.py
│   └── test_api_crud.py     # CRUD test cases for the API
├── utils/                   # Helper functions for API requests
│   ├── __init__.py
│   └── api_helper.py
├── config.py                # Configuration file for API settings
├── requirements.txt         # Project dependencies
├── pytest.ini               # Pytest configuration file
└── README.md                # Project documentation
```

## Prerequisites

- Python 3 installed on your machine
- [Requests](https://pypi.org/project/requests/), [Pytest](https://pypi.org/project/pytest/), and [Pytest HTML](https://pypi.org/project/pytest-html/) packages

## Setup Guide

Follow these steps to set up and run the tests.

### Step 1: Clone the Repository

```bash
git clone <repository-url>
cd crud_api_tests
```

### Step 2: Create and Activate a Virtual Environment

It’s recommended to use a virtual environment for dependency management.

```bash
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
# For Windows use: venv\Scripts\activate
```

### Step 3: Install Dependencies

Install the necessary Python packages by running:

```bash
pip install -r requirements.txt
```

### Step 4: Project Configuration

The API base URL is defined in `config.py`. Update this file if you are targeting a different API.

```python
# config.py
BASE_URL = "https://reqres.in"
```

### Step 5: Running the Tests

To run the tests and generate an HTML report, execute the following command:

```bash
pytest
```

Alternatively, you can specify a custom location for the report:

```bash
pytest --html=reports/custom_report.html --self-contained-html
```

### Step 6: Viewing the HTML Report

After running the tests, open the generated report in the `reports` folder. You can view it in a web browser to see details on test execution and results.

## Test Cases

The tests cover basic CRUD operations (Create, Read, Update, Delete) on the sample API.

- **Create User**: Tests creating a new user with a POST request.
- **Get User**: Tests retrieving an existing user with a GET request.
- **Update User**: Tests updating user details with a PUT request.
- **Delete User**: Tests deleting a user with a DELETE request.

## Additional Notes

- **Virtual Environment**: Remember to activate the virtual environment each time you work on the project.
- **Deactivating Environment**: When you are finished, deactivate the virtual environment with `deactivate`.

## Dependencies

All project dependencies are listed in `requirements.txt`:

```plaintext
requests
pytest
pytest-html
```

## License

This project is for educational and testing purposes.
