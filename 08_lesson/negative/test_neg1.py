import os
import requests
from dotenv import load_dotenv


load_dotenv()


def test_post_project():
    token = os.getenv("auth_secret_0c2k")
    project_data = ""
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {token}"}
    response = requests.post(url="https://ru.yougile.com/api-v2/projects",
                             json=project_data, headers=headers)
    print(response.text)
    assert response.status_code == 400
