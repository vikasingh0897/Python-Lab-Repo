import sqlite3
from typing import List, Tuple, Optional


class StudentDatabase:
    def __init__(self, db_name: str = ":memory:"):
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self) -> None:
        with self.conn:
            self.conn.execute("""
                CREATE TABLE IF NOT EXISTS students (
                    roll_no INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    branch TEXT NOT NULL,
                    cgpa REAL NOT NULL
                )
            """)

    def insert_student(self, roll_no: int, name: str, branch: str, cgpa: float) -> None:
        with self.conn:
            self.conn.execute(
                "INSERT INTO students (roll_no, name, branch, cgpa) VALUES (?, ?, ?, ?)",
                (roll_no, name, branch, cgpa)
            )

    def fetch_all(self) -> List[Tuple]:
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM students ORDER BY roll_no")
        return cursor.fetchall()

    def update_cgpa(self, roll_no: int, new_cgpa: float) -> None:
        with self.conn:
            self.conn.execute(
                "UPDATE students SET cgpa = ? WHERE roll_no = ?",
                (new_cgpa, roll_no)
            )

    def delete_student(self, roll_no: int) -> None:
        with self.conn:
            self.conn.execute("DELETE FROM students WHERE roll_no = ?", (roll_no,))

    def close(self) -> None:
        self.conn.close()


def main():
    db = StudentDatabase()

    print("Inserting student records...")
    db.insert_student(241504, "Vikas Singh", "CSE", 9.2)
    db.insert_student(241478, "Namish", "CSE", 8.8)
    db.insert_student(241480, "Rahul Sharma", "ECE", 8.5)

    print("\nCurrent Student Directory:")
    for row in db.fetch_all():
        print(f"  Roll: {row[0]} | Name: {row[1]:<14} | Branch: {row[2]} | CGPA: {row[3]}")

    print("\nUpdating CGPA for Roll No 241504 -> 9.5...")
    db.update_cgpa(241504, 9.5)

    print("Deleting student with Roll No 241480...")
    db.delete_student(241480)

    print("\nFinal Database Records:")
    for row in db.fetch_all():
        print(f"  Roll: {row[0]} | Name: {row[1]:<14} | Branch: {row[2]} | CGPA: {row[3]}")

    db.close()


if __name__ == "__main__":
    main()
