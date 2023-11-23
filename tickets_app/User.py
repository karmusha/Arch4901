import Ticket

class User:
    tickets = [Ticket]

    def __init__(self, user_id, user_name, tickets, login, pwd_hash_code, account_id) -> None:
        self.user_id = user_id
        self.user_name = user_name
        self.tickets = tickets
        self.login = login
        self.pwd_hash_code = pwd_hash_code
        self.account_id = account_id

    def get_user_id(self):
        return self.user_id
    
    def get_name(self):
        return f'Name: {self.user_name}'
    
    def __str__(self):
        return f'Name: {self.user_name}, tickets: {self.tickets}, login: {self.login}'