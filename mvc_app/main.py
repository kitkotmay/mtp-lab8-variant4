from mvc_app.controller import StudentController
from mvc_app.model import StudentModel
from mvc_app.view import StudentView


def main():
    """Запускает демонстрацию MVC-приложения."""
    model = StudentModel()
    view = StudentView()
    controller = StudentController(model, view)

    controller.add_student(
        "Ковалевич Александра Андреевна",
        "221141р",
        4,
    )

    controller.add_student(
        "Иванов Иван Иванович",
        "221141р",
        2,
    )

    print()
    controller.show_students()


if __name__ == "__main__":
    main()
