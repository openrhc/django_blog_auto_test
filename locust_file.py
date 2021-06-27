# demo.py
import os
from locust import HttpUser, TaskSet, task


class WebsiteTasks(TaskSet):
    def on_start(self):
        self.host = "http://centos:80/"
        self.h = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36",
            "Content-Type": "application/javascript",
        }

    @task(2)
    def index(self):
        self.client.get("")

    @task(1)
    def about(self):
        self.client.get("?cat_id=1")

    @task(3)
    def login(self):
        data = {
            "mobile": "18196789181", "password": " 12345678", "remember": "on"
        }
        r = self.client.get(self.host + "login", data=data, headers=self.h)
        assert r.status_code == 200

    @task(4)
    def details(self):
        self.client.get('detail/?id=6')

class WebsiteUser(HttpUser):
    # task_set = WebsiteTasks
    tasks = [WebsiteTasks]
    task_create = WebsiteTasks
    host = "http://centos:80/"
    min_wait = 1000
    max_wait = 5000


if __name__ == '__main__':
    os.system(r'locust  -f  locust_file.py')
