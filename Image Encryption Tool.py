from PIL import Image
import numpy as np
import os

def generate_key_array(shape, seed):
    """Generate a pseudo-random key array using a seed (must match for decryption)."""
    rng = np.random.default_rng(seed)
    return rng.integers(0, 256, size=shape, dtype=np.uint8)

def xor_encrypt_image(image_array, key_array):
    """Encrypt the image using XOR with key array."""
    return np.bitwise_xor(image_array, key_array)

def encrypt_image(image_path, key):
    original_image = Image.open(image_path).convert("RGB")
    image_array = np.array(original_image, dtype=np.uint8)

    print(f"🔑 Using encryption key (seed): {key}")

    key_array = generate_key_array(image_array.shape, seed=key)
    encrypted_array = xor_encrypt_image(image_array, key_array)

    encrypted_image = Image.fromarray(encrypted_array, mode="RGB")
    encrypted_image_path = "encrypted_image.png"
    encrypted_image.save(encrypted_image_path)
    print(f"✅ Encrypted image saved as: {encrypted_image_path}")

def decrypt_image(image_path, key):
    encrypted_image = Image.open(image_path).convert("RGB")
    encrypted_array = np.array(encrypted_image, dtype=np.uint8)

    print(f"🔑 Using decryption key (seed): {key}")

    key_array = generate_key_array(encrypted_array.shape, seed=key)
    decrypted_array = xor_encrypt_image(encrypted_array, key_array)

    decrypted_image = Image.fromarray(decrypted_array, mode="RGB")
    decrypted_image_path = "decrypted_image.png"
    decrypted_image.save(decrypted_image_path)
    print(f"✅ Decrypted image saved as: {decrypted_image_path}")

def compare_images(img1_path, img2_path):
    img1 = np.array(Image.open(img1_path).convert("RGB"))
    img2 = np.array(Image.open(img2_path).convert("RGB"))

    if np.array_equal(img1, img2):
        print("✅ Decryption successful! Images are identical.")
    else:
        print("❌ Images do not match. Something went wrong.")

def main():
    print("🔐 Welcome to the Sreeram's Secure Image Encryption Tool")
    while True:
        print("\nChoose an option:")
        print("  e - Encrypt an image")
        print("  d - Decrypt an image")
        print("  c - Compare original and decrypted image")
        print("  q - Quit the program")

        choice = input("Your choice: ").lower()

        if choice == 'q':
            print("👋 Exiting the program.")
            break
        elif choice not in ['e', 'd', 'c']:
            print("⚠️ Invalid input. Please type 'e', 'd', 'c', or 'q'.")
            continue

        if choice in ['e', 'd']:
            try:
                key = int(input("Enter a numeric encryption key (any positive integer): "))
                if key <= 0:
                    print("❌ Key must be a positive integer.")
                    continue
            except ValueError:
                print("❌ Invalid input. Key must be a number.")
                continue

            image_path = input("Enter the path to the image: ")
            if not os.path.isfile(image_path):
                print("❌ File not found.")
                continue

            if choice == 'e':
                encrypt_image(image_path, key)
            elif choice == 'd':
                decrypt_image(image_path, key)

        elif choice == 'c':
            img1 = input("Enter path to original image: ")
            img2 = input("Enter path to decrypted image: ")
            if not os.path.isfile(img1) or not os.path.isfile(img2):
                print("❌ One or both files not found.")
                continue
            compare_images(img1, img2)

if __name__ == "__main__":
    main()
