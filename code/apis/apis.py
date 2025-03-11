# As a Data Engineer, working with APIs is essential
# We need the 'requests' library to send HTTP requests

import requests

# Step 1: Sending a GET request to retrieve data from an API
url = "https://jsonplaceholder.typicode.com/posts/1"
response = requests.get(url)

# Checking if the request was successful (HTTP status code 200)
print("\nGET Request - Fetching Data\n" + "-" * 40)
print(f"Response Status: {response.status_code} (200 means success)")

# Displaying the JSON response (formatted data from the API)
print("JSON Response:")
print(response.json())

# If needed, we can also display the raw content
print("\nRaw Content:")
print(response.content)
print("-" * 40 + "\n")

# Step 2: Sending a POST request to create a new user
post_url = "https://reqres.in/api/users"
data = {"name": "Fabricio", "job": "Developer"}

response2 = requests.post(post_url, json=data)

# Checking if the request was successful (HTTP status code 201 - Created)
if response2.status_code == 201:
    json_response = response2.json()  # Convert response to a dictionary

    # Extracting only relevant values (using .get() to avoid missing keys)
    name = json_response.get("name", "N/A")
    job = json_response.get("job", "N/A")
    user_id = json_response.get("id", "N/A")
    created_at = json_response.get("createdAt", "N/A")

    # Displaying the extracted values in a structured format
    print("\nPOST Request - Sending Data\n" + "-" * 40)
    print(f"Name: {name}")
    print(f"Job: {job}")
    print(f"User ID: {user_id}")
    print(f"Created At: {created_at}")
    print("-" * 40 + "\n")

else:
    # Printing an error message if the request failed
    print(f"\nPOST Request Failed! HTTP Status Code: {response2.status_code}\n")
