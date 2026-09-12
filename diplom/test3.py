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

    rename_url = f"https://ru.yougile.com//api-v2/tasks/{task_id}"
    update_data = {"title": "Новая встреча"}
    response = requests.put(rename_url, json=update_data, headers=headers)
    assert response.status_code == 200