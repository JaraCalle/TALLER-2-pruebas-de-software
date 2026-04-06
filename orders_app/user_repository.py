import requests
"""
class JsonPlaceholderUserRepository:
    def get_user_email(self, user_id):
        print(user_id)
        response = requests.get(
            f'https://jsonplaceholder.typicode.com/users/{user_id}', timeout=5
        )
        response.raise_for_status()
        return response.json()['email']
"""

class JsonPlaceholderUserRepository:
    def get_user_email(self, user_id):
        raise ConnectionError("User service unavailable")


class FakeUserRepository:
    def get_user_email(self, user_id):
        return f"{user_id}_test_mail@{user_id*123}mail.com"
