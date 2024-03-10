
from cryptography.fernet import Fernet

import pyperclip
key = Fernet.generate_key()
fernet = Fernet(key)

def encrypt(message):
    encMessage = fernet.encrypt(message.encode())
    return encMessage

def decrypt(encMessage):
    decMessage = fernet.decrypt(encMessage)
    message_1=decMessage.decode()
    #pyperclip.copy(str(decMessage)[2:-1])
    return message_1
'''
import pickle
import pandas as pd

try:
    with open("C:/Users/shail/projects/pswd_pest/Password_Encryption_Sys/Final Code/storage.csv", 'rb') as file:
        data = pickle.load(file)
        df = pd.DataFrame(self.data)
        print(self.df)
except FileNotFoundError:
    print("No passwords stored yet.")

'''