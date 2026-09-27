class StudentView:
    """View: отвечает за отображение данных."""

    @staticmethod
    def show_title():
        """Выводит заголовок."""
        print("Список студентов")
        print("-" * 60)

    @staticmethod
    def show_students(students):
        """Выводит список студентов."""
        if not students:
            print("Список студентов пуст.")
            return

        for number, student in enumerate(students, start=1):
            print(
                f"{number}. {student['full_name']} | "
                f"группа: {student['group']} | "
                f"вариант: {student['variant']}"
            )

    @staticmethod
    def show_message(message):
        """Выводит сообщение."""
        print(message)
