import sys


def caesar_cipher(text: str, shift: int) -> str:
    result = []
    shift = shift % 26
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted = chr((ord(char) - base + shift) % 26 + base)
            result.append(shifted)
        else:
            result.append(char)
    return "".join(result)


def main():
    if len(sys.argv) >= 4:
        text = sys.argv[1]
        try:
            shift = int(sys.argv[2])
        except ValueError:
            print("Error: Shift key must be an integer.")
            return
        mode = sys.argv[3].strip().upper()
    else:
        text = input("Enter text: ")
        shift_str = input("Enter shift key: ").strip()
        try:
            shift = int(shift_str)
        except ValueError:
            print("Error: Shift key must be an integer.")
            return
        mode = input("Enter E to encrypt or D to decrypt: ").strip().upper()

    if mode == "D":
        shift = -shift
    elif mode != "E":
        print("Error: Invalid mode. Enter 'E' for encryption or 'D' for decryption.")
        return

    result = caesar_cipher(text, shift)
    print("Result:", result)


if __name__ == "__main__":
    main()
