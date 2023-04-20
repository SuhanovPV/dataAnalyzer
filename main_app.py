import sys

# import tkinter as tk
# from tkinter import messagebox, DISABLED, NORMAL, S
# from tkinter import filedialog as fd
# import tkinter.font as tk_font
import file_helper
import ui_const as const
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QFileDialog, QWidget
from PyQt5 import QtWidgets
from PyQt5.QtGui import QFont
from PyQt5.QtCore import pyqtSlot


# class MainApp(tk.Tk):
#     def __init__(self):
#         super().__init__()
#         self.title('Data analyzer')
#         self.geometry(f'{const.WIDTH}x{const.HEIGHT}')
#         self.file_name = None
#         self.tmp_file = None
#         self.folder = None
#         self.file_set = set()
#         font_size = tk_font.Font(size=const.FONT_SIZE)
#
#         # UI select file
#         self.lbl_open_file = tk.Label(
#             text="Файл:",
#             font=font_size
#         )
#         self.lbl_file_name = tk.Label(
#             foreground="#9ca3a2",
#             text="не выбран",
#             font=font_size
#         )
#
#         self.btn_open_file = tk.Button(
#             text="Выбрать файл",
#             command=self.open_file,
#             width=18,
#             font=font_size
#         )
#
#         self.btn_remove_duplicates = tk.Button(
#             text="Удалить дубликаты",
#             command=self.remove_duplicates,
#             width=18,
#             font=font_size
#         )
#         self.btn_remove_duplicates['state'] = DISABLED
#
#         self.btn_open_file_without_duplicates = tk.Button(
#             text="Посмотреть результат",
#             command=self.open_file_without_duplicates,
#             width=18,
#             font=font_size
#         )
#         self.btn_open_file_without_duplicates['state'] = DISABLED
#
#         # UI select folder with file to compare
#         self.lbl_select_folder = tk.Label(
#             text="Выберите файлы для сравнения:",
#             font=font_size
#         )
#
#         self.frame = tk.Frame(self)
#         tk.Label(self.frame, text='34234').pack()
#
#
#         self.btn_select_dir = tk.Button(
#             text="Выбрать файлы",
#             command=self.add_files_for_compare,
#             width=18,
#             font=font_size
#         )
#
#         # UI status bar
#         self.status_bar = tk.Label(
#             text='Пожалуйста, выберите файл, с которым хотите работать',
#             foreground="#434343"
#         )
#
#         # UI pack elements
#         self.lbl_open_file.place(x=6, y=12)
#         self.lbl_file_name.place(x=50, y=12)
#         self.btn_open_file.place(x=6, y=40)
#         self.btn_remove_duplicates.place(x=186, y=40)
#         self.btn_open_file_without_duplicates.place(x=366, y=40)
#         self.lbl_select_folder.place(x=6, y=76)
#         self.frame.place(x=6, y=104)
#
#     def open_file(self):
#         self.file_name = fd.askopenfilename(
#             initialdir=file_helper.get_init_path(),
#             filetypes=(("Еxcel files", "*.xls;*xlsx"),
#                        ("Все файлы", "*.*"))
#         )
#         if len(self.file_name) > 0:
#             self.lbl_file_name['text'] = file_helper.convert_path(self.file_name, 60)
#             self.btn_remove_duplicates['state'] = NORMAL
#
#     def remove_duplicates(self):
#         if self.file_name is None or self.file_name == '':
#             messagebox.showinfo(title="Внимание!", message="Файл не выбран.")
#             return
#         self.tmp_file = file_helper.create_file_with_unique_users(self.file_name)
#         self.btn_open_file_without_duplicates['state'] = NORMAL
#
#     def add_files_for_compare(self):
#         files = fd.askopenfilenames(
#             initialdir=file_helper.get_init_path(),
#             filetypes=(("Еxcel files", "*.xls;*xlsx"),
#                        ("Все файлы", "*.*"))
#         )
#         if type(files).__name__ == 'tuple':
#             self.file_set = file_helper.add_files_to_list(self.file_set, files)
#         print(self.file_set)
#
#     def open_file_without_duplicates(self):
#         os.startfile(self.tmp_file)
#
#


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()
        self.file_name = None

    def init_ui(self):
        font = QFont()
        font.setPointSize(const.FONT_SIZE)
        self.setGeometry(200, 200, const.WINDOW_WIDTH, const.WINDOW_HEIGHT)
        self.setWindowTitle(const.WINDOW_TITILE)

        self.lbl_file = self._set_label("Файл:", font)
        self.lbl_file.move(const.STEP, const.STEP)
        self.lbl_file_name = self._set_label("не выбран", font)
        self.lbl_file_name.setStyleSheet("QLabel {color:grey}")
        self.lbl_file_name.move(
            self._get_end_by_x(self.lbl_file) + const.STEP,
            const.STEP
        )

        self.btn_open_file = self._set_button('Выбрать файл', font, self.open_file)
        self.btn_open_file.move(
            const.STEP,
            self._get_end_by_y(self.lbl_file) + const.STEP
        )

    def _set_label(self, txt, font):
        lbl = QLabel(self, text=txt)
        lbl.setFont(font)
        lbl.adjustSize()
        return lbl

    def _set_button(self, txt, font, command):
        btn = QPushButton(self)
        btn.setText(txt)
        btn.setFont(font)
        btn.setFixedWidth(const.BUTTON_WIDTH)
        btn.setFixedHeight(const.BUTTON_HEIGHT)
        btn.clicked.connect(command)
        return btn

    #     def open_file(self):
    #         self.file_name = fd.askopenfilename(
    #             initialdir=file_helper.get_init_path(),
    #             filetypes=(("Еxcel files", "*.xls;*xlsx"),
    #                        ("Все файлы", "*.*"))
    #         )
    #         if len(self.file_name) > 0:
    #             self.lbl_file_name['text'] = file_helper.convert_path(self.file_name, 60)
    #             self.btn_remove_duplicates['state'] = NORMAL

    def _get_end_by_x(self, element: QWidget):
        return element.x() + element.width()

    def _get_end_by_y(self, element: QWidget):
        return element.y() + element.height()

    @pyqtSlot()
    def open_file(self):
        filename, filetype = QFileDialog.getOpenFileName(self,
                                                         caption="Выберите файл, с которым хотите работать",
                                                         directory=file_helper.get_init_path(),
                                                         filter="Excel (*.xls;*xlsx)"
                                                         )
        if filename:
            self.file_name = file_helper.path_to_win_format(filename)
            self.lbl_file_name.setText(self.file_name)
            self.lbl_file_name.adjustSize()


if __name__ == '__main__':
    app = QApplication(sys.argv[1:])

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
