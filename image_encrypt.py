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
