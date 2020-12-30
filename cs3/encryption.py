from cryptography.fernet import Fernet


# Generating the key and writing it to a file
def genwrite_key():
    key = Fernet.generate_key()
    with open("pass.key", "wb") as key_file:
        key_file.write(key)


def call_key():
    return open("pass.key", "rb").read()


def encrypt_data(slogan):
    genwrite_key()
    key = call_key()
    # slogan = "hello world".encode()
    a = Fernet(key)
    coded_slogan = a.encrypt(slogan)
    # print("print encrypted message :%s" %(coded_slogan))
    return coded_slogan

def decrypt_data(coded_slogan):
    key = call_key()
    b = Fernet(key)
    decoded_slogan = b.decrypt(coded_slogan)
    print(decoded_slogan)


message = "hello world"
encoded_message = message.encode()
enc=encrypt_data(encoded_message)
print(enc)
dec=decrypt_data(enc)

