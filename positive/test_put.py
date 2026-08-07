import os
import requests
from dotenv import load_dotenv


load_dotenv()


def test_create_project():
    token = os.getenv("auth_secret_0c2k")
    update_data = {"title": "New"}
    id = "d0b2c270-37e4-4040-8562-0040bd097592"
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {token}"}
    response = requests.put(url=f"https://ru.yougile.com/api-v2/projects/{id}", 
                            json=update_data, headers=headers)
    print(response.text)
    assert response.status_code == 200
