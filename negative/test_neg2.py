import os
import requests
from dotenv import load_dotenv


load_dotenv()


def test_get_project():
    token = os.getenv("auth_secret_0c2k")
    id = "d0b2c270-37e4-4040-8562-00499d097592"
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {token}"}
    response = requests.get(
        url=f"https://ru.yougile.com/api-v2/projects/{id}", headers=headers)
    print(response.text)
    assert response.status_code == 404
