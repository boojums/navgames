''' Generate a new secret key. Adapted from: https://gist.github.com/ndarville/3452907'''
import os
import random

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
print(BASE_DIR)

SECRET_FILE = os.path.join(BASE_DIR, 'secret_key.txt')
SECRET_KEY = ''.join([random.SystemRandom().choice('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)') for i in range(50)])
with open(SECRET_FILE, 'w') as f:
    f.write(SECRET_KEY)