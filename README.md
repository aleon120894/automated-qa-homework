# Automated QA Homework Assignment

## Overview
This repository contains automated test scripts for API and UI testing as per the assignment requirements.

### API Tests
- **Test 1:** Verify GET request to `https://jsonplaceholder.typicode.com/posts/1` returns 200 status code and contains a `title` field.
- **Test 2:** Validate POST request to `https://jsonplaceholder.typicode.com/posts` successfully creates a new resource with status code 201.

### UI Tests
- Open `http://example.com` and verify the page title is "Example Domain".

## Setup Instructions

### Prerequisites
- Python 3.x installed
- Google Chrome and ChromeDriver

### Tests running

- UI tests running:
```sh 
   cd ui_tests
   pytest ui_yest.py
```

- API tests running:
```shell
   cd api_tests
   pytest test_api.py
```
