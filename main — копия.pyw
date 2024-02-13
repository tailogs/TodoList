import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QMenuBar, QMenu, QFileDialog, QListWidget, QLineEdit, QPushButton, QMessageBox
from PyQt6.QtGui import QAction

WHITE = "#FFFFFF"
LIGHT_GRAY = "#666666"
GRAY = "#555555"
DARK_GRAY = "#444444"
DARK_DARK_GRAY = "#222222"
BLACK = "#000000"

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("TODO List")
        self.setGeometry(100, 100, 350, 280)
        self.setFixedSize(350, 280)
        self.setStyleSheet("background-color: #222222;")

        self.create_menu()
        self.create_widgets()

    def create_menu(self):
        menubar = self.menuBar()

        theme_menu = QMenu("Тема", self)
        menubar.addMenu(theme_menu)

        dark_theme_action = QAction("Темная", self)
        dark_theme_action.triggered.connect(lambda: self.change_theme(DARK_DARK_GRAY))
        theme_menu.addAction(dark_theme_action)

        light_theme_action = QAction("Светлая", self)
        light_theme_action.triggered.connect(lambda: self.change_theme(WHITE))
        theme_menu.addAction(light_theme_action)

        exit_action = QAction("Выход", self)
        exit_action.triggered.connect(self.close)
        menubar.addAction(exit_action)

        developer_action = QAction("Разработчик: Tailogs", self)
        menubar.addAction(developer_action)

    def create_widgets(self):
        label = QLabel("Список задач:", self)
        label.setStyleSheet(f"color: {WHITE}; background-color: {DARK_DARK_GRAY}; font: bold 14px Arial;")
        label.setGeometry(10, 10, 150, 20)

        self.listbox = QListWidget(self)
        self.listbox.setStyleSheet(f"background-color: ; color: {WHITE}; selection-background-color: {LIGHT_GRAY}; selection-color: {WHITE}; font: 12px Arial; border: 0px;")
        self.listbox.setGeometry(10, 40, 150, 200)

        label2 = QLabel("Добавить задачу:", self)
        label2.setStyleSheet(f"color: {WHITE}; background-color: {DARK_DARK_GRAY}; font: bold 12px Arial;")
        label2.setGeometry(170, 10, 150, 20)

        self.entry = QLineEdit(self)
        self.entry.setStyleSheet(f"background-color: {DARK_GRAY}; color: {WHITE}; selection-background-color: {LIGHT_GRAY}; selection-color: {WHITE};")
        self.entry.setGeometry(170, 40, 150, 20)
        self.entry.returnPressed.connect(self.add_task)

        add_button = QPushButton("Добавить задачу", self)
        add_button.setStyleSheet(f"background-color: {DARK_GRAY}; color: {WHITE}; selection-background-color: {LIGHT_GRAY}; selection-color: {WHITE}; font: 10px Arial;")
        add_button.setGeometry(170, 70, 150, 20)
        add_button.clicked.connect(self.add_task)

        delete_button = QPushButton("Удалить", self)
        delete_button.setStyleSheet(f"background-color: {DARK_GRAY}; ; color: {WHITE}; selection-background-color: {LIGHT_GRAY}; selection-color: {WHITE}; font: 10px Arial;")
        delete_button.setGeometry(170, 100, 150, 20)
        delete_button.clicked.connect(self.delete_task)

        clear_button = QPushButton("Очистить всё", self)
        clear_button.setStyleSheet(f"background-color: {DARK_GRAY}; ; color: {WHITE}; selection-background-color: {LIGHT_GRAY}; selection-color: {WHITE}; font: 10px Arial;")
        clear_button.setGeometry(10, 250, 150, 20)
        clear_button.clicked.connect(self.clear_tasks)

        open_button = QPushButton("Открыть файл", self)
        open_button.setStyleSheet(f"background-color: {DARK_GRAY}; ; color: {WHITE}; selection-background-color: {LIGHT_GRAY}; selection-color: {WHITE}; font: 10px Arial;")
        open_button.setGeometry(170, 130, 150, 20)
        open_button.clicked.connect(self.open_file)

        export_button = QPushButton("Экспорт файла", self)
        export_button.setStyleSheet(f"background-color: {DARK_GRAY}; ; color: {WHITE}; selection-background-color: {LIGHT_GRAY}; selection-color: {WHITE}; font: 10px Arial;")
        export_button.setGeometry(170, 160, 150, 20)
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

    def change_theme(self, theme):
        self.setStyleSheet(f"background-color: {theme};")
        self.listbox.setStyleSheet(f"background-color: {DARK_GRAY}; color: {WHITE}; selection-background-color: {LIGHT_GRAY}; selection-color: {WHITE}; font: 12px Arial; border: 0px;")
        self.entry.setStyleSheet(f"background-color: {DARK_GRAY}; color: {WHITE}; selection-background-color: {LIGHT_GRAY}; selection-color: {WHITE};")

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
