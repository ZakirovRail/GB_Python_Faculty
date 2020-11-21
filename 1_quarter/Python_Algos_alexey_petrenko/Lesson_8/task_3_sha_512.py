import hashlib

s = input('Enter your password: ')
hash_s = hashlib.sha512(s.encode('utf-8')).hexdigest()
print(hashlib.sha512(s.encode('utf-8')).hexdigest())


