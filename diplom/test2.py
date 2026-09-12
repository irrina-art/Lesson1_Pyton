import os
import requests
from dotenv import load_dotenv


load_dotenv()


def test_post_task():
    token = os.getenv("token")
    task_data = {"title": "Провести встречу"}
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {token}"}
    response = requests.post(url="https://ru.yougile.com//api-v2/tasks",
                             json=task_data, headers=headers)
    print(response.text)
    assert response.status_code == 201
    