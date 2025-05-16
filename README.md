# Simple Image Encryption Tool (Binary Data Manipulation)

## Overview

This project contains a Python script (`image_encrypt.py`) that demonstrates a basic image encryption and decryption technique by manipulating the binary data of the image file. The script reads an image file, performs a bitwise XOR operation on its bytes with a user-provided key, and saves the resulting encrypted or decrypted data.

**Author:** yuvaprasath

## Features

* Encrypts an image file by XORing its binary data with a key.
* Decrypts an image file that was previously encrypted with the same key using this tool.
* Simple command-line interface.
* Operates on the raw binary data, making the encrypted image unreadable by standard image viewers.

## Prerequisites

* **Python 3** installed on your system.

## Usage

1.  **Save the script:** Save the provided Python code as `image_encrypt.py` in your project directory.

2.  **Open your terminal or command prompt.** Navigate to the directory where you saved the script.

3.  **Run the script:** Execute the script using the Python interpreter:
    ```bash
    python image_encrypt.py
    ```

4.  **Follow the prompts:**
    * The script will ask if you want to encrypt ('e') or decrypt ('d') an image, or quit ('q').
    * Enter the corresponding letter and press Enter.
    * You will be prompted to enter the path to the image file you want to process.
    * Enter an integer encryption key. **Remember this key!** You will need the same key to decrypt the image.
    * For encryption, the encrypted data will be saved with an `_encrypted` suffix, keeping the original file extension.
    * For decryption, enter the path to the encrypted file, the same key used for encryption, and the decrypted image will be saved with a `_decrypted` suffix, keeping the original file extension.

## Important Notes

* **Security:** This is a very basic encryption method using a simple XOR operation on the file's binary data. It is **not secure** for protecting sensitive images. A determined individual could likely break this encryption relatively easily. This tool is primarily for educational purposes to demonstrate binary data manipulation for a simple form of "encryption."
* **Key Importance:** The same key **must** be used for both encryption and decryption.
* **File Format Alteration:** Encrypting the image using this method alters its binary data, making it an invalid image file format that cannot be opened by standard image viewers. Decryption with the correct key should restore the original binary data, making it a valid image file again.

## Code (`image_encrypt.py`)

```python
import os

def encrypt_image(image_path, key):
    """
    Encrypts an image file by applying XOR operation to its binary data.
    This code was developed by yuvaprasath.

    Args:
        image_path (str): The path to the image file.
        key (int): An integer key for the XOR operation.

    Returns:
        bytes: The encrypted byte data of the image, or None on error.
    """
    try:
        with open(image_path, 'rb') as image_file:
            image_data = image_file.read()
    except FileNotFoundError:
        print(f"Error: Image file not found at {image_path}")
        return None
    except Exception as e:
        print(f"Error reading image file: {e}")
        return None

    encrypted_data = bytearray()
    for byte in image_data:
        encrypted_byte = byte ^ key
        encrypted_data.append(encrypted_byte)
    return bytes(encrypted_data)

def decrypt_image(encrypted_data, key):
    """
    Decrypts image data that was encrypted using the encrypt_image function.
    This code was developed by yuvaprasath.

    Args:
        encrypted_data (bytes): The encrypted byte data of the image.
        key (int): The integer key used for the XOR operation during encryption.

    Returns:
        bytes: The decrypted byte data of the image.
    """
    decrypted_data = bytearray()
    for byte in encrypted_data:
        decrypted_byte = byte ^ key
        decrypted_data.append(decrypted_byte)
    return bytes(decrypted_data)

def get_output_path(input_path, action):
    """
    Generates a suitable output path for the encrypted/decrypted image.
    This code was developed by yuvaprasath.

    Args:
        input_path (str): The input file path.
        action (str): "encrypt" or "decrypt".

    Returns:
        str: The generated output file path.
    """
    base_name, ext = os.path.splitext(input_path)
    if action == "encrypt":
        return base_name + "_encrypted" + ext
    elif action == "decrypt":
        return base_name + "_decrypted" + ext
    return None

def main():
    """
    Main function to run the image encryption/decryption program.
    This program encrypts and decrypts image files by manipulating their binary data.
    This code was developed by yuvaprasath.
    """
    print("Novel Approach to Image Encryption using Pixel Manipulation in Python")
    print("Leveraging cryptographic algorithms, individual pixel values undergo")
    print("substitution (XOR), making the image unreadable.")
    print("This code was developed by yuvaprasath.\n")
    print("Let's start with Image Encryption:\n")

    while True:
        action = input("Do you want to (e)ncrypt or (d)ecrypt an image? (q) to quit: ").lower()
        if action == 'q':
            break
        elif action not in ['e', 'd']:
            print("Invalid action. Please enter 'e' for encrypt, 'd' for decrypt, or 'q' to quit.")
            continue

        try:
            key = int(input("Enter the encryption key (an integer): "))
        except ValueError:
            print("Invalid key. Please enter an integer.")
            continue

        if action == 'e':
            image_path = input("Enter the path of the image for encryption: ")
            encrypted_data = encrypt_image(image_path, key)
            if encrypted_data:
                output_path = get_output_path(image_path, "encrypt")
                try:
                    with open(output_path, 'wb') as outfile:
                        outfile.write(encrypted_data)
                    print(f"Encryption successful! Encrypted image saved as: {output_path}\n")
                    print("As the binary data of the image has been altered, you will be unable to open the image directly.")
                except Exception as e:
                    print(f"Error saving encrypted image: {e}")
        elif action == 'd':
            print("\nNow let's move to Decrypting the Image:\n")
            encrypted_path = input("Enter the path of the encrypted image: ")
            try:
                with open(encrypted_path, 'rb') as infile:
                    encrypted_data = infile.read()
                decrypted_data = decrypt_image(encrypted_data, key)
                output_path = get_output_path(encrypted_path, "decrypt")
                try:
                    with open(output_path, 'wb') as outfile:
                        outfile.write(decrypted_data)
                    print(f"Decryption successful! Decrypted image saved as: {output_path}\n")
                    print("The image should now be in its original readable form.")
                except Exception as e:
                    print(f"Error saving decrypted image: {e}")
            except FileNotFoundError:
                print(f"Error: Encrypted image file not found at {encrypted_path}")
            except Exception as e:
                print(f"Error reading encrypted image file: {e}")

if __name__ == "__main__":
    main()
