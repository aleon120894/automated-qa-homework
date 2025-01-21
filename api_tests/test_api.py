import requests
import pytest

# Test case 1: Verify GET request to the endpoint
@pytest.fixture
def test_get_post():
    url = "https://jsonplaceholder.typicode.com/posts/1"
    response = requests.get(url)

    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    assert "title" in response.json(), "Response JSON does not contain 'title' field"


# Test case 2: Validate POST request
@pytest.fixture
def test_create_post():
    url = "https://jsonplaceholder.typicode.com/posts"
    payload = {"title": "foo", "body": "bar", "userId": 1}
    response = requests.post(url, json=payload)

    assert response.status_code == 201, f"Expected 201, got {response.status_code}"

    response_json = response.json()

    assert response_json.get("title") == "foo", "Title does not match"
    assert response_json.get("body") == "bar", "Body does not match"
    assert response_json.get("userId") == 1, "UserId does not match"


# Log test status (Fixture)
@pytest.fixture(autouse=True)
def log_test_status(request):
    """
    Fixture to log the test name and status (pass/fail) to a file or console.
    """
    yield  # Run the test

    # Get the test name and status
    test_name = request.node.name
    outcome = request.node.rep_call.outcome

    # Log the result to the console
    print(f"Test: {test_name} - Status: {outcome}")


# To run the tests, use pytest
