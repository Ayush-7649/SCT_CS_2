# image_encryption.py
from PIL import Image
import numpy as np

class ImageEncryptor:
    def __init__(self, key: int):
        self.key = key  # encryption key

    def encrypt(self, input_path: str, output_path: str):
        # Load image
        img = Image.open(input_path)
        arr = np.array(img)

        # Pixel manipulation (XOR with key)
        encrypted_arr = arr ^ self.key

        # Swap rows (simple pixel shuffle)
        encrypted_arr = np.flipud(encrypted_arr)

        # Save encrypted image
        encrypted_img = Image.fromarray(encrypted_arr)
        encrypted_img.save(output_path)
        print(f"✅ Image encrypted and saved as {output_path}")

    def decrypt(self, input_path: str, output_path: str):
        # Load encrypted image
        img = Image.open(input_path)
        arr = np.array(img)

        # Reverse row swap
        decrypted_arr = np.flipud(arr)

        # Reverse XOR with key
        decrypted_arr = decrypted_arr ^ self.key

        # Save decrypted image
        decrypted_img = Image.fromarray(decrypted_arr)
        decrypted_img.save(output_path)
        print(f" Image decrypted and saved as {output_path}")


# ---------------- Main Program ----------------
if __name__ == "__main__":
    print("===== Simple Image Encryption Tool =====")
    print("1. Encrypt Image")
    print("2. Decrypt Image")
    choice = int(input("Enter your choice (1 or 2): "))

    path = input("Enter image file name (with extension, e.g., photo.png): ")
    key = int(input("Enter numeric key for encryption/decryption (e.g., 123): "))

    encryptor = ImageEncryptor(key)

    if choice == 1:
        encryptor.encrypt(path, "encrypted.png")
    elif choice == 2:
        encryptor.decrypt(path, "decrypted.png")
    else:
        print(" Invalid choice")
