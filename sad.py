import requests

headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json',
    # 'X-CSRFTOKEN': 'Sx7lGg9u4QqWRqnzPuGqZGQBtoYathbpbQGhcWoHBTAAZOdJzplWIYt5PLVyECwB',
}

json_data = {
    'username': 'ipilot7',
    'password': '123',
    'device_id': 'string',
}

response = requests.post('https://bizombor.onrender.com/login/manager/', headers=headers, json=json_data)
print(response.json())