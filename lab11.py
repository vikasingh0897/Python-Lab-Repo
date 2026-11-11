import sys


def render_ascii_snowflake(depth: int) -> None:
    print(f"Rendering Koch Snowflake Fractal Preview (Recursion Depth: {depth})...")
    curves = [
        "       /\\       ",
        "  /\\ /  \\ /\\  ",
        " /  \\/    \\/  \\ ",
        " \\  /\\    /\\  / ",
        "  \\/  \\  /  \\/  ",
        "       \\/       "
    ]
    for row in curves:
        print("  " + row)


def draw_spiral(length: int, angle: float, steps: int) -> None:
    print(f"Simulating Spiral [Steps: {steps}, Angle: {angle}°, Initial Length: {length}]...")
    curr = length
    for step in range(1, min(steps + 1, 6)):
        print(f"  Step {step}: Forward {curr}px, Turn Right {angle}°")
        curr += 2
    if steps > 5:
        print(f"  ... [{steps - 5} additional steps computed successfully]")


def main():
    print("===== Turtle Pattern Generator =====")
    print("1. Koch Snowflake")
    print("2. Spiral")
    choice = input("Choose a pattern (1 or 2): ").strip()

    if choice == "1":
        depth = int(input("Recursion depth (0-5) [Default 3]: ") or 3)
        render_ascii_snowflake(depth)
    elif choice == "2":
        length = int(input("Starting length [Default 10]: ") or 10)
        angle = float(input("Turning angle [Default 45]: ") or 45)
        steps = int(input("Number of steps [Default 15]: ") or 15)
        draw_spiral(length, angle, steps)
    else:
        print("Invalid choice.")


if __name__ == "__main__":
    main()
