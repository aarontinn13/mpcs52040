import itertools
import string
import hashlib

def bruteforce_password(hashed_password, max_length):
    chars = string.printable
    attempts = 0
    prefix = 'a'

    for password_length in range(1, max_length+1):
        for guess in itertools.product(prefix, chars, repeat=password_length):

            attempts += 1
            guess = ''.join(guess)
            print(guess)
            if hashlib.md5(guess.encode()).hexdigest() == hashed_password:
                return {'password' : guess, 'attempts' : attempts}
    return None


password = 'at'         # this is the password to crack
length = len(password)  # this is the length of the password

password = hashlib.md5(password.encode()).hexdigest()
#print(bruteforce_password(password, length))

for i in string.printable:
    print(i)