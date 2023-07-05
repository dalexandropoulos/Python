import hashlib


def find_char(text, char):
    count = 0
    for c in text:
        if c == char:
            count += 1
    return count






text = "Sample text no "

for salt in range(20):
    data = text + str(salt)
    # SHA-512 hash
    hash_sha512 = hashlib.sha512(data.encode()).hexdigest()
    # print("SHA-512 hash:", hash_sha512, find_char(hash_sha512,"0"))
    print(data, find_char(hash_sha512,"0"))
    
