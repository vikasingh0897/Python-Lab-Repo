import os
import sys


def show_directory(path: str) -> None:
    try:
        items = os.listdir(path)
        print(f"\nContents of: {os.path.abspath(path)}")
        for item in sorted(items):
            full_path = os.path.join(path, item)
            if os.path.isdir(full_path):
                print(f"[DIR]  {item}")
            else:
                print(f"[FILE] {item}")
    except FileNotFoundError:
        print("Directory not found.")
    except PermissionError:
        print("Permission denied.")


def create_workspace(name: str) -> None:
    try:
        os.makedirs(name, exist_ok=True)
        print(f"Workspace created: {os.path.abspath(name)}")
    except OSError as e:
        print("Could not create workspace:", e)


def list_extensions(path: str, extension: str) -> None:
    try:
        print(f"\nFiles with extension '{extension}':")
        matched = [i for i in os.listdir(path) if i.endswith(extension)]
        if matched:
            for item in sorted(matched):
                print(f"[FILE] {item}")
        else:
            print(f"No files ending with {extension} found.")
    except FileNotFoundError:
        print("Directory not found.")


def read_or_create_log(filename: str) -> None:
    try:
        if os.path.exists(filename):
            with open(filename, "r", encoding="utf-8") as file:
                print("\nLog contents:")
                print(file.read().strip())
        else:
            with open(filename, "w", encoding="utf-8") as file:
                file.write("Utility system initialization log entry.\n")
            print(f"Created new log: {os.path.abspath(filename)}")
    except PermissionError:
        print("Permission denied while accessing log.")
    except OSError as e:
        print("File error:", e)


def main():
    print("===== File Management Utility =====")
    path = sys.argv[1] if len(sys.argv) > 1 else os.getcwd()
    print("Current path:", os.path.abspath(path))

    show_directory(path)
    workspace = os.path.join(path, "workspace")
    create_workspace(workspace)
    list_extensions(path, ".py")
    log_file = os.path.join(workspace, "utility.log")
    read_or_create_log(log_file)


if __name__ == "__main__":
    main()
