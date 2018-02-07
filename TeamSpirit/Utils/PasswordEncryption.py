from passlib.hash import pbkdf2_sha512
from app import *

class PasswordEncryption(object):
    def __init__(self):
        self.salt = 'password_salt'

    def encrypt_password(self, password):
        
        hashed_password = pbkdf2_sha512.using(rounds=8000, salt_size=10).hash(password)  
        return hashed_password

    def validate_password(self, password, true_password):
        if pbkdf2_sha512.verify(password, true_password):
            return True
        else:
            return False