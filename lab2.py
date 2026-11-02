import string
from typing import Dict, List, Tuple


def analyze_text(text: str) -> Tuple[int, Dict[str, int], List[str]]:
    cleaned = text.lower().translate(str.maketrans("", "", string.punctuation))
    words = cleaned.split()
    total_words = len(words)

    frequency: Dict[str, int] = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1

    palindromes: List[str] = []
    for word in words:
        if len(word) > 1 and word == word[::-1] and word not in palindromes:
            palindromes.append(word)

    return total_words, frequency, palindromes


def main():
    print("Enter your text.")
    print("Type END on a new line to finish:\n")
    lines = []
    while True:
        line = input()
        if line.strip() == "END":
            break
        lines.append(line)

    text = "\n".join(lines)
    total_words, frequency, palindromes = analyze_text(text)

    print("\n--- Text Analysis Report ---")
    print("Total words:", total_words)

    print("\nWord Frequency:")
    for word, count in sorted(frequency.items(), key=lambda item: (-item[1], item[0])):
        print(f"{word} : {count}")

    print("\nPalindromes:")
    if palindromes:
        print(", ".join(palindromes))
    else:
        print("No palindromes found.")


if __name__ == "__main__":
    main()
