import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QMenuBar, QMenu, QFileDialog, QListWidget, QLineEdit, QPushButton, QMessageBox
from PyQt6.QtGui import QAction, QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("TODO List")
        self.setGeometry(100, 100, 550, 320)
        self.setFixedSize(550, 320)

        # Загрузка иконки из файла
        icon = QIcon("icon.ico")

        # Установка иконки для главного окна
        self.setWindowIcon(icon)

        self.create_menu()
        self.create_widgets()

    def create_menu(self):
        menubar = self.menuBar()

        developer_action = QAction("Разработчик: Tailogs", self)
        menubar.addAction(developer_action)

    def create_widgets(self):
        label = QLabel("Список задач", self)
        label.setGeometry(150, 35, 150, 20)

        self.listbox = QListWidget(self)
        self.listbox.setGeometry(10, 60, 350, 200)

        label2 = QLabel("Добавить задачу", self)
        label2.setGeometry(405, 35, 150, 20)

        self.entry = QLineEdit(self)
        self.entry.setGeometry(371, 60, 160, 20)
        self.entry.returnPressed.connect(self.add_task)

        add_button = QPushButton("Добавить задачу", self)
        add_button.setGeometry(370, 90, 160, 30)
        add_button.clicked.connect(self.add_task)

        delete_button = QPushButton("Удалить", self)
        delete_button.setGeometry(370, 130, 160, 30)
        delete_button.clicked.connect(self.delete_task)

        clear_button = QPushButton("Очистить всё", self)
        clear_button.setGeometry(10, 270, 350, 30)
        clear_button.clicked.connect(self.clear_tasks)

        open_button = QPushButton("Открыть файл", self)
        open_button.setGeometry(370, 170, 160, 30)
        open_button.clicked.connect(self.open_file)

        export_button = QPushButton("Экспорт файла", self)
        export_button.setGeometry(370, 210, 160, 30)
        export_button.clicked.connect(self.export_file)

    def add_task(self):
        task = self.entry.text()
        if task != "":
            self.listbox.addItem(task)
            self.entry.clear()
        else:
            QMessageBox.warning(self, "Пустая задача", "Пожалуйста, введите задачу!")

    def delete_task(self):
        selected_item = self.listbox.currentItem()
        if selected_item:
            self.listbox.takeItem(self.listbox.row(selected_item))

    def clear_tasks(self):
        self.listbox.clear()

    def open_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Открыть файл", "", "Text Files (*.txt)")
        if file_path:
            with open(file_path, 'r') as file:
                tasks = file.readlines()
                for task in tasks:
                    self.listbox.addItem(task.strip())

    def export_file(self):
        file_path, _ = QFileDialog.getSaveFileName(self, "Экспорт файла", "", "Text Files (*.txt)")
        if file_path:
            with open(file_path, 'w') as file:
                tasks = [self.listbox.item(i).text() for i in range(self.listbox.count())]
                file.write("\n".join(tasks))


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
