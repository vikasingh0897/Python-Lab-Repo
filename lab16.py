import os
import traceback
from typing import List


class FileProcessorError(Exception):
    """Base exception for file processing errors."""
    pass


class InvalidFileFormatError(FileProcessorError):
    """Raised when file extension or format is unsupported."""
    pass


class InvalidDataError(FileProcessorError):
    """Raised when file records cannot be parsed into numbers."""
    pass


def process_file(filename: str) -> None:
    file = None
    try:
        if not filename.endswith(".txt"):
            raise InvalidFileFormatError("Only .txt files are supported.")

        file = open(filename, "r", encoding="utf-8")
        lines = file.readlines()
        if not lines:
            raise InvalidDataError("The file is empty.")

        numbers: List[int] = []
        for line in lines:
            val = line.strip()
            if val:
                try:
                    numbers.append(int(val))
                except ValueError:
                    raise InvalidDataError(f"Non-integer value encountered: '{val}'")

    except FileNotFoundError:
        print("Error: Target file does not exist.")
    except InvalidFileFormatError as e:
        print("Format Error:", e)
    except InvalidDataError as e:
        print("Data Error:", e)
        with open("error.log", "a", encoding="utf-8") as log:
            traceback.print_exc(file=log)
    except Exception as e:
        print("Unexpected Error:", e)
    else:
        print("File processed successfully.")
        print("Extracted numbers:", numbers)
        print("Sum of numbers   :", sum(numbers))
    finally:
        if file is not None:
            file.close()
        print("File resource cleanup completed.")


def main():
    sample_path = "numbers.txt"
    with open(sample_path, "w", encoding="utf-8") as f:
        f.write("10\n20\n30\n40\n50\n")

    process_file(sample_path)


if __name__ == "__main__":
    main()
