import requests

class ApiHelper:
    def __init__(self, base_url):
        self.base_url = base_url

    def create_user(self, data):
        return requests.post(f"{self.base_url}/api/users", json=data)

    def get_user(self, user_id):
        return requests.get(f"{self.base_url}/api/users/{user_id}")

    def update_user(self, user_id, data):
        return requests.put(f"{self.base_url}/api/users/{user_id}", json=data)

    def delete_user(self, user_id):
        return requests.delete(f"{self.base_url}/api/users/{user_id}")
