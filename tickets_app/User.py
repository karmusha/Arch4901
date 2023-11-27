import Ticket
from ctypes.wintypes import LONG


class User:
    user_id: LONG
    user_name: str
    tickets: [Ticket]
    login: str
    pwd_hash_code: LONG
    account_id: LONG

    def __init__(self, user_id, user_name, tickets, login, pwd_hash_code, account_id) -> None:
        self.user_id = user_id
        self.user_name = user_name
        self.tickets = tickets
        self.login = login
        self.pwd_hash_code = pwd_hash_code
        self.account_id = account_id

    def get_user_id(self):
        return self.user_id
    
    def get_user_name(self):
        return self.user_name
    
    def get_user_tickets(self):
        return self.tickets
    
    def get_login(self):
        return self.login
    
    def get_account_id(self):
        return self.account_id
    
    def __str__(self):
        return f'Name: {self.user_name}, tickets: {self.tickets}, login: {self.login}'