class UserDB:
    def __init__(self):
        self._users = []

    def add_user(self, user):
        if not isinstance(user, dict):
            raise ValueError('Passed user is not a dict')

        if not user.get('name'):
            raise ValueError('"name" field is mandatory')

        if not isinstance(user['name'], str):
            raise ValueError('Name should be a string')

        if 'age' in user and not isinstance(user['age'], int):
            raise ValueError('Age should be an int')

        self._users.append(user)

    def list_users(self):
        return self._users.copy()

    def sort_users(self, sort_by='name', reverse=False):
        if sort_by not in ['name', 'age']:
            raise ValueError(f'Cannot sort by {sort_by}')

        self._users.sort(key=lambda user: user.get(sort_by, float('inf')), reverse=False)

    def delete_user(self, name):
        to_delete = None

        for user in self._users:
            if user['name'] == name:
                to_delete = user
                break

        if not to_delete:
            raise ValueError(f'User with name {to_delete} does not exist')

    def report(self):
        age_sum = 0
        for user in self._users:
            age_sum += user.get('age', 0)

        return {
            'total_users': len(self._users),
            'mean_age': age_sum / len(self._users)
        }
