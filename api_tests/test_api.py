import requests

# Test case 1: Verify GET request to the endpoint
def test_get_post():

    url = "https://jsonplaceholder.typicode.com/posts/1"
    response = requests.get(url)

    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    assert "title" in response.json(), "Response JSON does not contain 'title' field"

# Test case 2: Validate POST request
def test_create_post():

    url = "https://jsonplaceholder.typicode.com/posts"
    payload = {"title": "foo", "body": "bar", "userId": 1}
    response = requests.post(url, json=payload)

    assert response.status_code == 201, f"Expected 201, got {response.status_code}"

    response_json = response.json()

    assert response_json.get("title") == "foo", "Title does not match"
    assert response_json.get("body") == "bar", "Body does not match"
    assert response_json.get("userId") == 1, "UserId does not match"

if __name__ == "__main__":

    test_get_post()
    print("GET test passed.")

    test_create_post()
    print("POST test passed.")
