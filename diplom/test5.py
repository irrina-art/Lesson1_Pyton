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
    created_task = response.json()
    task_id = str(created_task['id'])
    view_url = f"https://ru.yougile.com//api-v2/tasks/{task_id}"
    response_get = requests.get(view_url, headers=headers)
    assert response_get.status_code == 200