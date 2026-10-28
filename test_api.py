import requests

def test_get_post_by_id():
    # 1. Send a GET request to the API
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

    # 2. Check if the status code is 200 (Success)
    assert response.status_code == 200, f"Expected 200, but got {response.status_code}"

    # 3. Convert response to JSON
    data = response.json()

    # 4. Verify the data
    assert data["id"] == 1, "The ID returned does not match 1"
    assert "title" in data, "The response does not contain a title"
    
    print(f"\nSuccessfully fetched post! Title: {data['title']}")