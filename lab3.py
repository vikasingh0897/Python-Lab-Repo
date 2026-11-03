import csv
import os
from typing import List


def inspect_csv(filename: str) -> None:
    if not os.path.exists(filename):
        print(f"Error: File '{filename}' does not exist.")
        return

    delimiter = "\t" if filename.endswith(".tsv") else ","
    with open(filename, "r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file, delimiter=delimiter)
        header = next(reader, None)
        if not header:
            print("The file is empty.")
            return

        rows = list(reader)
        row_count = len(rows)
        col_count = len(header)

        print("\n--- CSV File Information ---")
        print(f"Rows: {row_count}")
        print(f"Columns: {col_count}")

        print("\nColumn Names:")
        print(header)

        types = []
        for i in range(col_count):
            is_int = True
            is_float = True
            for r in rows:
                val = r[i].strip() if i < len(r) else ""
                try:
                    int(val)
                except ValueError:
                    is_int = False
                try:
                    float(val)
                except ValueError:
                    is_float = False
            if is_int:
                types.append("int64")
            elif is_float:
                types.append("float64")
            else:
                types.append("object")

        print("\nData Types:")
        for col, dt in zip(header, types):
            print(f"{col:<15} {dt}")

        print("\nFirst 5 Rows:")
        for row in rows[:5]:
            print(row)


def create_sample_csv(filename: str = "students.csv") -> str:
    data = [
        ["Name", "Age", "Marks"],
        ["Rahul", "20", "85"],
        ["Amit", "21", "90"],
        ["Priya", "19", "95"],
        ["Neha", "22", "88"]
    ]
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(data)
    print(f"Sample file '{filename}' generated.")
    return filename


def main():
    fname = input("Enter CSV/TSV file name (or press Enter for default): ").strip()
    if not fname:
        fname = create_sample_csv("students.csv")
    inspect_csv(fname)


if __name__ == "__main__":
    main()
