from typing import Any, Dict


def calculate_statistics(*grades: float, **student_info: Any) -> Dict[str, Any]:
    if not grades:
        return {}

    minimum = min(grades)
    maximum = max(grades)
    average = sum(grades) / len(grades)

    distribution = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}
    for grade in grades:
        if grade >= 90:
            distribution["A"] += 1
        elif grade >= 80:
            distribution["B"] += 1
        elif grade >= 70:
            distribution["C"] += 1
        elif grade >= 60:
            distribution["D"] += 1
        else:
            distribution["F"] += 1

    return {
        "info": student_info,
        "count": len(grades),
        "min": minimum,
        "max": maximum,
        "average": round(average, 2),
        "distribution": distribution
    }


def main():
    stats = calculate_statistics(
        85, 92, 78, 64, 55, 90,
        Subject="Python Programming",
        Semester=5,
        Instructor="Mr. Anant R. Bara"
    )

    print("Student & Course Information:")
    for key, val in stats["info"].items():
        print(f"  {key}: {val}")

    print(f"\nTotal Evaluations : {stats['count']}")
    print(f"Minimum Score     : {stats['min']}")
    print(f"Maximum Score     : {stats['max']}")
    print(f"Average Score     : {stats['average']}")
    print(f"Grade Distribution: {stats['distribution']}")


if __name__ == "__main__":
    main()
