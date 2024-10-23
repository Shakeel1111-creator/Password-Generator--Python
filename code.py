import random
import string

def randomPassword():
    randomSource = string.ascii_letters + string.digits + string.punctuation
    password = random.sample(randomSource, 6)
    password += random.sample(string.ascii_uppercase, 2)
    password += random.choice(string.digits)
    password += random.choice(string.punctuation)
    print(password)
    l=password
    random.shuffle(l)
    l="".join(l)
    print(password)
    return password

print ("Password is ", randomPassword())
