class StudentModel:
    """Model: хранит данные студентов."""

    def __init__(self):
        self.students = []

    def add_student(self, full_name, group_name, variant):
        """Добавляет студента."""
        student = {
            "full_name": full_name,
            "group": group_name,
            "variant": variant,
        }
        self.students.append(student)

    def get_students(self):
        """Возвращает список студентов."""
        return self.students
