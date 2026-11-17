import re
from typing import Dict, List


def validate_email(email: str) -> bool:
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return bool(re.match(pattern, email.strip()))


def extract_phone_numbers(text: str) -> List[str]:
    pattern = r"(?:\+?\d{1,3}[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}"
    return re.findall(pattern, text)


def extract_urls(text: str) -> List[str]:
    pattern = r"https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+[/\w .?=%&-]*"
    return re.findall(pattern, text)


def parse_log_entry(log_line: str) -> Dict[str, str]:
    pattern = r"\[(?P<timestamp>.*?)\]\s+(?P<level>[A-Z]+)\s+(?P<ip>\d{1,3}(?:\.\d{1,3}){3})\s+-\s+(?P<message>.*)"
    match = re.match(pattern, log_line)
    return match.groupdict() if match else {}


def main():
    sample_text = """
    Contact support at support@cuh.ac.in or emergency@cuh.gov.
    Office line: +91-98765-43210 or alternate (123) 456-7890.
    Portal docs available at https://cuh.ac.in/portal and https://github.com/vikasingh0897.
    """

    print("--- 1. Email Address Validation ---")
    emails = ["student@cuh.ac.in", "invalid-email@", "vikas@domain.com"]
    for e in emails:
        print(f"'{e}' -> Valid: {validate_email(e)}")

    print("\n--- 2. Phone Numbers Extracted ---")
    phones = extract_phone_numbers(sample_text)
    for p in phones:
        print(f"  Phone: {p}")

    print("\n--- 3. URLs Extracted ---")
    urls = extract_urls(sample_text)
    for u in urls:
        print(f"  URL: {u}")

    print("\n--- 4. Log Entry Tokenization ---")
    raw_log = "[2026-11-22 14:30:15] INFO 192.168.1.105 - Student authentication verified successfully"
    parsed = parse_log_entry(raw_log)
    for key, val in parsed.items():
        print(f"  {key:<10}: {val}")


if __name__ == "__main__":
    main()
