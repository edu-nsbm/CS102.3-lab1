from dataclasses import dataclass


@dataclass
class Student:
    student_id: int
    age: int
    gpa: float
    student_name: str
    grade: str
    is_scholarship_holder: bool


def get_student_data() -> Student:
    student_id: int = 40256
    age: int = 19
    gpa: float = 4.0
    student_name: str = "De Zoysa K D"
    grade: str = "A"
    is_scholarship_holder: bool = False

    data_class: Student = Student(
        student_id,
        age,
        gpa,
        student_name,
        grade,
        is_scholarship_holder,
    )

    return data_class


def print_student_data() -> None:
    student_data: Student = get_student_data()

    print(f"Student ID: {student_data.student_id}")
    print(f"Student Age: {student_data.age}")
    print(f"Student GPA: {student_data.gpa}")
    print(f"Student name: {student_data.student_name}")
    print(f"Student Grade: {student_data.grade}")
    print(f"Is Student Scholarship Holder: {student_data.is_scholarship_holder}")


def main() -> None:
    print_student_data()


if __name__ == "__main__":
    main()
