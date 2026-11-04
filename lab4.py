from collections import deque
from typing import Callable, Deque, Tuple


class TaskScheduler:
    def __init__(self):
        self.tasks: Deque[Tuple[str, Callable[[int], bool]]] = deque()

    def add_task(self, name: str, condition: Callable[[int], bool]) -> None:
        self.tasks.append((name, condition))
        print(f"Task '{name}' added.")

    def run_tasks(self, value: int) -> None:
        print("\nChecking tasks...")
        remaining: Deque[Tuple[str, Callable[[int], bool]]] = deque()
        while self.tasks:
            name, condition = self.tasks.popleft()
            if condition(value):
                print(f"✓ Executing: {name}")
            else:
                print(f"⏳ Condition not met: {name}")
                remaining.append((name, condition))
        self.tasks = remaining

    def show_pending(self) -> None:
        print("\nPending tasks:")
        if not self.tasks:
            print("- None")
        else:
            for name, _ in self.tasks:
                print(f"- {name}")


def main():
    scheduler = TaskScheduler()
    while True:
        print("\n===== Task Scheduler =====")
        print("1. Add task")
        print("2. Run tasks")
        print("3. Show pending tasks")
        print("4. Exit")

        choice = input("Enter your choice: ").strip()
        if choice == "1":
            name = input("Enter task name: ").strip()
            threshold = int(input("Run task when value >=: ").strip())
            scheduler.add_task(name, lambda val, th=threshold: val >= th)
        elif choice == "2":
            val = int(input("Enter current value: ").strip())
            scheduler.run_tasks(val)
        elif choice == "3":
            scheduler.show_pending()
        elif choice == "4":
            print("Exiting Task Scheduler...")
            break
        else:
            print("Invalid choice. Enter 1-4.")


if __name__ == "__main__":
    main()
