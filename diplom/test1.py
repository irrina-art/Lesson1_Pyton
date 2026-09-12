import os
import requests
from dotenv import load_dotenv


load_dotenv()


def test_post_project():
    token = os.getenv("token")
    project_data = {"title": "Мой проект"}
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {token}"}
    response = requests.post(url="https://ru.yougile.com/api-v2/projects",
                             json=project_data, headers=headers)
    assert response.status_code == 201