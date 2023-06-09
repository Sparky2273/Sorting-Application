from timeit import default_timer as timer
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QLabel,
    QVBoxLayout,
    QHBoxLayout,
    QWidget,
    QLineEdit,
    QPushButton,
    QFrame,
    QAction,
    QMessageBox,
    QGroupBox,
)


class Sorting(QMainWindow):
    def __init__(self):
        super().__init__()
        self.number_list = []
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Sorting")
        self.setGeometry(200, 200, 345, 495)
        self.setFixedSize(345, 495)
        self.setWindowIcon(QIcon("Sorting.ico"))
        self.setWindowFlags(
            self.windowFlags()
            & ~(Qt.WindowMinimizeButtonHint | Qt.WindowMaximizeButtonHint)
        )

        menubar = self.menuBar()
        help_menu = menubar.addMenu("Help")

        about_action = QAction("About", self)
        about_action.triggered.connect(self.about)
        help_menu.addAction(about_action)

        manual_action = QAction("Manual", self)
        manual_action.triggered.connect(self.manual)
        help_menu.addAction(manual_action)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)

        data_group_box = QGroupBox("Data")
        data_layout = QVBoxLayout()
        data_group_box.setLayout(data_layout)

        number_group_box = QGroupBox()
        number_layout = QHBoxLayout()
        number_group_box.setLayout(number_layout)

        number_label = QLabel("NUMBER:")
        self.number_entry = QLineEdit()
        number_layout.addWidget(number_label)
        number_layout.addWidget(self.number_entry)

        list_group_box = QGroupBox()
        list_layout = QHBoxLayout()
        list_group_box.setLayout(list_layout)

        list_label = QLabel("LIST:")
        self.list_entry = QLineEdit()
        self.list_entry.setReadOnly(True)
        list_layout.addWidget(list_label)
        list_layout.addWidget(self.list_entry)

        sorted_list_group_box = QGroupBox()
        sorted_list_layout = QHBoxLayout()
        sorted_list_group_box.setLayout(sorted_list_layout)

        sorted_list_label = QLabel("SORTED LIST:")
        self.sorted_list_entry = QLineEdit()
        self.sorted_list_entry.setReadOnly(True)
        sorted_list_layout.addWidget(sorted_list_label)
        sorted_list_layout.addWidget(self.sorted_list_entry)

        execution_time_group_box = QGroupBox()
        execution_time_layout = QHBoxLayout()
        execution_time_group_box.setLayout(execution_time_layout)

        execution_time_label = QLabel("EXECUTION TIME:")
        self.execution_time_entry = QLineEdit()
        self.execution_time_entry.setReadOnly(True)
        execution_time_layout.addWidget(execution_time_label)
        execution_time_layout.addWidget(self.execution_time_entry)

        data_layout.addWidget(number_group_box)
        data_layout.addWidget(list_group_box)
        data_layout.addWidget(sorted_list_group_box)
        data_layout.addWidget(execution_time_group_box)

        main_layout.addWidget(data_group_box)

        button_frame = QGroupBox("Buttons")
        button_layout = QHBoxLayout()
        button_frame.setLayout(button_layout)

        add_button = QPushButton("Add")
        add_button.clicked.connect(self.add_number)
        button_layout.addWidget(add_button)

        reset_button = QPushButton("Reset")
        reset_button.clicked.connect(self.reset)
        button_layout.addWidget(reset_button)

        close_button = QPushButton("Close")
        close_button.clicked.connect(self.close)
        button_layout.addWidget(close_button)

        main_layout.addWidget(button_frame)

        sort_button_frame = QGroupBox("Sorting Algorithms")
        sort_button_layout = QHBoxLayout()
        sort_button_frame.setLayout(sort_button_layout)

        bubble_sort_button = QPushButton("Bubble Sort")
        bubble_sort_button.clicked.connect(self.sort_bubble)
        sort_button_layout.addWidget(bubble_sort_button)

        insertion_sort_button = QPushButton("Insertion Sort")
        insertion_sort_button.clicked.connect(self.sort_insertion)
        sort_button_layout.addWidget(insertion_sort_button)

        selection_sort_button = QPushButton("Selection Sort")
        selection_sort_button.clicked.connect(self.sort_selection)
        sort_button_layout.addWidget(selection_sort_button)

        main_layout.addWidget(sort_button_frame)

    def sort_bubble(self):
        sorted_list, execution_time = self.bubble_sort(self.number_list)
        self.sort_show(sorted_list, execution_time)

    def sort_insertion(self):
        sorted_list, execution_time = self.insertion_sort(self.number_list)
        self.sort_show(sorted_list, execution_time)

    def sort_selection(self):
        sorted_list, execution_time = self.selection_sort(self.number_list)
        self.sort_show(sorted_list, execution_time)

    def sort_show(self, sorted_list, execution_time):
        self.sorted_list_entry.setText(", ".join(str(i) for i in sorted_list))
        self.execution_time_entry.setText(f"{execution_time:.6f} seconds")

    def add_number(self):
        try:
            number = int(self.number_entry.text())
            self.number_entry.clear()
            self.number_list.append(number)
            self.list_entry.clear()
            self.list_entry.setText(", ".join(str(i) for i in self.number_list))
        except ValueError:
            print("Number not entered!")
            self.number_entry.clear()

    def bubble_sort(self, array):
        start_time = timer()
        n = len(array)
        for i in range(n - 1):
            for j in range(n - 1 - i):
                if array[j] > array[j + 1]:
                    array[j], array[j + 1] = array[j + 1], array[j]
        end_time = timer()
        return array, end_time - start_time

    def insertion_sort(self, array):
        start_time = timer()
        for i in range(1, len(array)):
            key_item = array[i]
            j = i - 1
            while j >= 0 and array[j] > key_item:
                array[j + 1] = array[j]
                j -= 1
            array[j + 1] = key_item
        end_time = timer()
        return array, end_time - start_time

    def selection_sort(self, array):
        start_time = timer()
        for i in range(len(array)):
            min_index = i
            for j in range(i + 1, len(array)):
                if array[j] < array[min_index]:
                    min_index = j
            array[i], array[min_index] = array[min_index], array[i]
        end_time = timer()
        return array, end_time - start_time

    def reset(self):
        self.number_entry.clear()
        self.list_entry.clear()
        self.sorted_list_entry.clear()
        self.execution_time_entry.clear()
        self.number_list.clear()

    def about(self):
        about_text = f"Version: 1.0\nDeveloper: Sparky\nContact: Sparky#2273 on Discord or Sparky2273 on Telegram\nREPORT ANY BUG"
        QMessageBox.information(self, "About", about_text)

    def manual(self):
        self.manual_window = ManualWindow()
        self.manual_window.show()


class ManualWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sorting Application Manual")
        self.setGeometry(150, 150, 1250, 815)
        self.setFixedSize(1250, 815)
        self.setWindowFlags(
            self.windowFlags()
            & ~(Qt.WindowMinimizeButtonHint | Qt.WindowMaximizeButtonHint)
        )

        self.manual_text = """
        Manual for Sorting Application:

        1. Introduction:
        The Sorting Application is a graphical user interface (GUI) program that allows you to sort a list of numbers using different sorting algorithms. This manual will guide you on how to use the application efficiently.

        2. Installation:
        - No installation is required. The Sorting Application is an executable (`.exe`) file that can be run directly on your operating system.

        3. User Interface:
        - The Sorting Application window consists of several components:
            - Number Entry: Enter a number to add it to the list.
            - List: Displays the current list of numbers.
            - Sorted List: Displays the sorted list after applying a sorting algorithm.
            - Execution Time: Displays the time taken to perform the sorting operation.
            - Add Button: Adds the entered number to the list.
            - Reset Button: Clears all fields and resets the application.
            - Close Button: Closes the application.
            - Sorting Algorithm Buttons: Three sorting algorithms are available: Bubble Sort, Insertion Sort, and Selection Sort. Clicking on any of these buttons will perform the corresponding sorting operation.

        4. Adding Numbers:
        - Enter a number in the "Number" field.
        - Click the "Add" button to add the number to the list.
        - The entered number will be displayed in the "List" field.

        5. Sorting Algorithms:
        - Bubble Sort: Click the "Bubble Sort" button to sort the list using the bubble sort algorithm.
        - Insertion Sort: Click the "Insertion Sort" button to sort the list using the insertion sort algorithm.
        - Selection Sort: Click the "Selection Sort" button to sort the list using the selection sort algorithm.
        - After clicking any of the sorting algorithm buttons, the sorted list will be displayed in the "Sorted List" field, and the execution time will be shown in the "Execution Time" field.

        6. Resetting:
        - Click the "Reset" button to clear all fields and reset the application.
        - This action will clear the number list, the list display, the sorted list display, and the execution time display.

        7. About:
        - Click the "About" option in the "Help" menu to get information about the application.
        - A dialog box will appear showing the application version, developer name, and contact information.

        8. Exiting the Application:
        - Click the "Close" button to exit the application.

        9. Troubleshooting:
        - If you encounter any issues or errors while using the Sorting Application, please contact the developer for support. You can reach out to Sparky#2273 on Discord.

        Note: This manual provides a basic understanding of the Sorting Application's features and functionality. For further details or specific inquiries, please refer to the developer or the application documentation.
        """

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        frame = QFrame()
        frame.setFrameShape(QFrame.StyledPanel)
        frame_layout = QVBoxLayout()
        frame.setLayout(frame_layout)

        manual_label = QLabel(self.manual_text)
        manual_label.setWordWrap(True)
        frame_layout.addWidget(manual_label)

        layout.addWidget(frame)


def main():
    app = QApplication([])
    window = Sorting()
    window.show()
    app.exec_()


if __name__ == "__main__":
    main()
