import requests
import pytest

# Decorator to log test status
def log_test_status(func):
    def wrapper(*args, **kwargs):
        print("Test started.")
        try:
            result = func(*args, **kwargs)
            print("Test passed.")
            return result
        except Exception as e:
            print(f"Test failed: {e}")
            raise
    return wrapper

# Test case 1: Verify GET request to the endpoint
@log_test_status
def test_get_post():
    """
    Test to verify the GET request response.
    """
    url = "https://jsonplaceholder.typicode.com/posts/1"
    response = requests.get(url)

    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    assert "title" in response.json(), "Response JSON does not contain 'title' field"


# Test case 2: Validate POST request
@log_test_status
def test_create_post():
    """
    Test to verify the POST request response.
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    payload = {"title": "foo", "body": "bar", "userId": 1}
    response = requests.post(url, json=payload)

    assert response.status_code == 201, f"Expected 201, got {response.status_code}"

    response_json = response.json()

    assert response_json.get("title") == "foo", "Title does not match"
    assert response_json.get("body") == "bar", "Body does not match"
    assert response_json.get("userId") == 1, "UserId does not match"
