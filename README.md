# Image Encryption Tool (Pixel Manipulation)

## Overview

This project provides a Python script (`image_encrypt.py`) that demonstrates a basic image encryption and decryption technique by manipulating the pixel values of an image.  The script uses the Pillow library to access and modify pixel data, applying a simple XOR operation to encrypt and decrypt the image.

## Features

* Encrypts an image by performing a bitwise XOR operation on the Red, Green, and Blue (RGB) values of each pixel.
* Decrypts an image that has been previously encrypted using this script and the same key.
* Supports common image formats handled by the Pillow library (e.g., PNG, JPG, etc.).
* Command-line interface for ease of use.

## How It Works

The script uses the Pillow library to open the image and access its pixel data.  For each pixel in the image, the red, green, and blue color components are extracted.  A bitwise XOR operation is then performed on each of these components with a user-provided integer key.  This process effectively alters the pixel's color, rendering the image unrecognizable.  Decryption reverses this process by performing the same XOR operation with the same key, restoring the original pixel values.

## Prerequisites

* **Python 3**
* **Pillow** library.  Install it using:
    ```bash
    pip install Pillow
    ```

## Usage

1.  **Download the script:** Download `image_encrypt.py` and save it to your desired directory.
2.  **Open a terminal:** Navigate to the directory where you saved the script.
3.  **Run the script:**
    ```bash
    python image_encrypt.py
    ```
4.  **Follow the prompts:**
    * The script will ask you to choose between encryption ('e'), decryption ('d'), or quitting ('q').
    * Enter the corresponding letter and press Enter.
    * Enter the path to the image file.
    * Enter an integer encryption key.  **Important:** Remember this key, as you'll need it for decryption.
    * The script will then process the image and save the result as a new file (either `*_pixel_encrypted.*` or `*_pixel_decrypted.*`).

## Important Notes

* **Security:** This is a *very basic* encryption method for demonstration purposes.  It is **not secure** for protecting sensitive information.  A simple XOR cipher is vulnerable to various attacks.
* **Lossless:** The encryption/decryption process is lossless.  Using the same key for decryption will perfectly restore the original image.
* **Key Importance:** The security of this script relies entirely on the secrecy of the encryption key.
* **File Handling:** The script creates new image files for the encrypted and decrypted output, preserving the original file format.

## Code

Here's the code of the `image_encrypt.py` script:

```python
from PIL import Image
import os

def encrypt_image_pixels(image_path, key):
    """
    Encrypts the pixel data of an image using a simple XOR cipher on RGB values.
    Developed by yuvaprasath.

    Args:
        image_path (str): The path to the image file.
        key (int): An integer key for the XOR operation.

    Returns:
        Image.Image: The encrypted PIL Image object, or None on error.
    """
    try:
        img = Image.open(image_path).convert("RGB")
        pixels = img.load()
        width, height = img.size
        for x in range(width):
            for y in range(height):
                r, g, b = pixels[x, y]
                new_r = r ^ key
                new_g = g ^ key
                new_b = b ^ key
                pixels[x, y] = (new_r, new_g, new_b)
        return img
    except FileNotFoundError:
        print(f"Error: Image file not found at {image_path}")
        return None
    except Exception as e:
        print(f"Error loading image: {e}")
        return None

def decrypt_image_pixels(encrypted_image, key):
    """
    Decrypts an image that was encrypted using the encrypt_image_pixels function.
    Developed by yuvaprasath.

    Args:
        encrypted_image (Image.Image): The encrypted PIL Image object.
        key (int): The integer key used for the XOR operation during encryption.

    Returns:
        Image.Image: The decrypted PIL Image object.
    """
    pixels = encrypted_image.load()
    width, height = encrypted_image.size
    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            new_r = r ^ key
            new_g = g ^ key
            new_b = b ^ key
            pixels[x, y] = (new_r, new_g, new_b)
    return encrypted_image

def get_output_path_pixel(input_path, action):
    """
    Generates a suitable output path for pixel-manipulated images.
    Developed by yuvaprasath.

    Args:
        input_path (str): The input file path.
        action (str): "encrypt" or "decrypt".

    Returns:
        str: The generated output file path.
    """
    base_name, ext = os.path.splitext(input_path)
    if action == "encrypt":
        return base_name + "_pixel_encrypted" + ext
    elif action == "decrypt":
        return base_name + "_pixel_decrypted" + ext
    return None

def main():
    """
    Main function to run the image pixel manipulation encryption/decryption program.
    Developed by yuvaprasath.
    """
    print("Image Pixel Manipulation Encryption/Decryption Tool")
    print("Developed by yuvaprasath.\n")
    while True:
        action = input("Do you want to (e)ncrypt or (d)ecrypt an image (pixels)? (q) to quit: ").lower()
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
            image_path = input("Enter the path to the image file: ")
            encrypted_image = encrypt_image_pixels(image_path, key)
            if encrypted_image:
                output_path = get_output_path_pixel(image_path, "encrypt")
                try:
                    encrypted_image.save(output_path)
                    print(f"Pixel-encrypted image saved to {output_path}")
                except Exception as e:
                    print(f"Error saving encrypted image: {e}")
        elif action == 'd':
            image_path = input("Enter the path to the encrypted image file: ")
            try:
                encrypted_image = Image.open(image_path)
                decrypted_image = decrypt_image_pixels(encrypted_image, key)
                output_path = get_output_path_pixel(image_path, "decrypt")
                try:
                    decrypted_image.save(output_path)
                    print(f"Pixel-decrypted image saved to {output_path}")
                except Exception as e:
                    print(f"Error saving decrypted image: {e}")
            except FileNotFoundError:
                print(f"Error: Encrypted image file not found at {image_path}")
            except Exception as e:
                print(f"Error loading encrypted image: {e}")

if __name__ == "__main__":
    main()
