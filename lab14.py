import os
import pickle
import shelve
from typing import List


class Student:
    def __init__(self, name: str, age: int, marks: List[int]):
        self.name = name
        self.age = age
        self.marks = marks

    def display(self) -> None:
        print(f"Name : {self.name}")
        print(f"Age  : {self.age}")
        print(f"Marks: {self.marks}")

    def average(self) -> float:
        return sum(self.marks) / len(self.marks) if self.marks else 0.0


def main():
    s1 = Student("Rahul", 21, [85, 90, 78])
    print("Original Object:")
    s1.display()

    # 1. Pickle serialization
    pickle_file = "student.pkl"
    with open(pickle_file, "wb") as f:
        pickle.dump(s1, f)
    print("\nObject serialized using pickle.")

    with open(pickle_file, "rb") as f:
        restored_student: Student = pickle.load(f)
    print("Object restored from pickle:")
    restored_student.display()
    print("Computed Average:", round(restored_student.average(), 2))

    # 2. Shelve persistence
    db_file = "student_db"
    with shelve.open(db_file) as db:
        db["student_1"] = s1
        db["student_2"] = Student("Priya", 20, [92, 88, 95])
    print("\nMultiple objects stored in shelve database.")

    with shelve.open(db_file) as db:
        print("Restored from shelve:")
        for key in db:
            obj: Student = db[key]
            print(f"- [{key}] {obj.name}, Age: {obj.age}, Avg: {obj.average():.2f}")


if __name__ == "__main__":
    main()
