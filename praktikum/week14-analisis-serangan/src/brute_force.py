import hashlib
import itertools
import string

# Password asli (disimulasikan)
password_asli = "abc"

# Hash MD5 dari password
hash_target = hashlib.md5(password_asli.encode()).hexdigest()
print("Target hash:", hash_target)

# Karakter yang dicoba (sangat sederhana)
chars = string.ascii_lowercase

# Brute force maksimal 3 karakter
for length in range(1, 4):
    for guess in itertools.product(chars, repeat=length):
        percobaan = ''.join(guess)
        hash_percobaan = hashlib.md5(percobaan.encode()).hexdigest()
        
        if hash_percobaan == hash_target:
            print("Password ditemukan:", percobaan)
            exit()
