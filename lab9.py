from collections import Counter
from typing import Dict, List


def clean_text(text: str) -> str:
    return "".join(char.lower() for char in text if char.isalnum())


def are_anagrams_sort(text1: str, text2: str) -> bool:
    return sorted(clean_text(text1)) == sorted(clean_text(text2))


def are_anagrams_count(text1: str, text2: str) -> bool:
    return Counter(clean_text(text1)) == Counter(clean_text(text2))


def find_anagrams(word_list: List[str], target: str) -> List[str]:
    target_clean = sorted(clean_text(target))
    return [w for w in word_list if sorted(clean_text(w)) == target_clean]


def group_anagrams(word_list: List[str]) -> List[List[str]]:
    groups: Dict[str, List[str]] = {}
    for word in word_list:
        key = "".join(sorted(clean_text(word)))
        groups.setdefault(key, []).append(word)
    return [grp for grp in groups.values() if len(grp) > 1]


def main():
    w1, w2 = "listen", "silent"
    print(f"Anagram Check ('{w1}', '{w2}'):", are_anagrams_sort(w1, w2))

    p1, p2 = "Dormitory", "Dirty Room"
    print(f"Phrase Anagram Check ('{p1}', '{p2}'):", are_anagrams_count(p1, p2))

    corpus = ["listen", "silent", "enlist", "hello", "inlets", "world"]
    print("\nMatching Anagrams for 'listen':")
    print(find_anagrams(corpus, "listen"))

    print("\nDiscovered Anagram Groups:")
    for group in group_anagrams(corpus):
        print(group)


if __name__ == "__main__":
    main()
