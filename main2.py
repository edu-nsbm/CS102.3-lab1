def print_student_data() -> None:
    student_id: int = 40256
    age: int = 19
    gpa: float = 4.0
    student_name: str = "De Zoysa K D"
    grade: str = "A"
    is_scholarship_holder: bool = False

    print(f"Student ID: {student_id}")
    print(f"Student Age: {age}")
    print(f"Student GPA: {gpa}")
    print(f"Student name: {student_name}")
    print(f"Student Grade: {grade}")
    print(f"Is Student Scholarship Holder: {is_scholarship_holder}")


def main() -> None:
    print_student_data()


if __name__ == "__main__":
    main()
