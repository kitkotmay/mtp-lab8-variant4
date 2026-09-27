class StudentController:
    """Controller: связывает Model и View."""

    def __init__(self, model, view):
        self.model = model
        self.view = view

    def add_student(self, full_name, group_name, variant):
        """Передаёт данные нового студента в Model."""
        self.model.add_student(
            full_name,
            group_name,
            variant,
        )

        self.view.show_message(
            f"Студент {full_name} добавлен."
        )

    def show_students(self):
        """Получает данные из Model и передаёт их во View."""
        students = self.model.get_students()

        self.view.show_title()
        self.view.show_students(students)
