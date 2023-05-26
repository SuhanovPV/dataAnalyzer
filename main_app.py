import sys

import file_helper
import ui_const
import ui_const as const
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QFileDialog, QWidget, QMessageBox, QLineEdit
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QGroupBox, QScrollArea, QSizePolicy
from PyQt5.QtGui import QFont, QFontMetrics
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        # self.file_name = None
        # self.file_dict = dict()
        # self.file_list_cnt = 0
        self.init_ui()

    def init_ui(self):
        self.create_central_widget()
        self.setGeometry(200, 200, const.WINDOW_WIDTH, const.WINDOW_HEIGHT)
        self.setWindowTitle(const.TEXT_WINDOW_TITILE)
        self.setCentralWidget(self.create_central_widget())

    def create_central_widget(self):
        central_widget = QWidget()
        common_layout = QVBoxLayout()
        common_layout.addWidget(self.create_widget_select_file())
        central_widget.setLayout(common_layout)
        return central_widget

    def create_widget_select_file(self):
        widget = QWidget()
        layout = QHBoxLayout()
        text = QLineEdit()
        text.setObjectName('common_file_line_edit')
        btn = self._set_button(txt=const.TEXT_SELECT_MAIN_FILE, command=self.open_common_file)
        layout.addWidget(text)
        layout.addWidget(btn)
        widget.setLayout(layout)
        return widget

    def set_font(self):
        font = QFont()
        font.setPointSize(const.FONT_SIZE)
        return font

    def _set_button(self, txt, command, width=const.BUTTON_WIDTH, height=const.BUTTON_HEIGHT):
        btn = QPushButton(self)
        btn.setText(txt)
        btn.setFont(self.set_font())
        btn.setStyleSheet('color: rgb(60, 57, 56);')
        # btn.setFixedWidth(width)
        # btn.setFixedHeight(height)
        btn.setGeometry(width=width, height=height)
        btn.clicked.connect(command)
        return btn


#     # TODO Вынести создание отдельных групп в отдельные функции
#     def create_central_widget(self):
#         central_widget = QWidget()
#         common_layout = QVBoxLayout()
#
#         # OPEN FILE LAYOUT
#         self.gbox_open_file = QGroupBox('Выберите файл, с которым хотите работать')
#         layout_work_with_file = QVBoxLayout()
#         layout_select_file = QHBoxLayout()
#         self.lbl_file_name = self._set_label('Файл: не выбран')
#         self.btn_open_file = self._set_button(txt='Выбрать файл', command=self.open_common_file)
#         layout_select_file.addWidget(self.lbl_file_name)
#         layout_select_file.addWidget(self.btn_open_file)
#
#         layout_btn_work_with_file = QHBoxLayout()
#         self.btn_remove_duplicates = self._set_button('Удалить дубликаты', self.remove_duplicates)
#         self.btn_remove_duplicates.setDisabled(True)
#         self.btn_open_file_without_duplicates = self._set_button("Открыть результат",
#                                                                  self.open_file_without_duplicates)
#         self.btn_open_file_without_duplicates.setDisabled(True)
#         layout_btn_work_with_file.addWidget(self.btn_remove_duplicates, alignment=Qt.AlignRight)
#         layout_btn_work_with_file.addWidget(self.btn_open_file_without_duplicates)
#         layout_work_with_file.addLayout(layout_select_file)
#         layout_work_with_file.addLayout(layout_btn_work_with_file)
#         layout_work_with_file.setStretch(0, 0)
#         self.gbox_open_file.setLayout(layout_work_with_file)
#
#         # FILE LIST LAYOUT
#         self.gbox_add_files_to_compare = QGroupBox('Файлы для сравнения')
#
#         layout_for_add_files = QVBoxLayout()
#
#         layout_for_btn_add_files = QHBoxLayout()
#         btn_add_file_to_compare = self._set_button('Добавить файл', self.add_files_to_compare)
#         btn_clear_filelist = self._set_button('Удалить все', self.clear_all_files)
#         layout_for_btn_add_files.addWidget(btn_add_file_to_compare, alignment=Qt.AlignRight)
#         layout_for_btn_add_files.addWidget(btn_clear_filelist)
#         self.layout_filelist = QVBoxLayout()
#         layout_for_add_files.addLayout(layout_for_btn_add_files)
#         layout_for_add_files.addLayout(self.layout_filelist)
#         layout_for_add_files.addStretch(0)
#         self.gbox_add_files_to_compare.setLayout(layout_for_add_files)
#         self.gbox_add_files_to_compare.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Preferred)
#
#         common_layout.addWidget(self.gbox_open_file, alignment=Qt.AlignTop)
#         common_layout.addWidget(self.gbox_add_files_to_compare)
#         central_widget.setLayout(common_layout)
#         return central_widget
#
#
#     def _set_label(self, txt):
#         lbl = QLabel(self, text=txt)
#         lbl.setFont(self.set_font())
#         lbl.setStyleSheet('color: rgb(60, 57, 56);')
#         lbl.adjustSize()
#         return lbl
#

#
#     def open_file(self, title: str):
#         file = None
#         filename, filetype = QFileDialog.getOpenFileName(self,
#                                                          caption=title,
#                                                          directory=file_helper.get_init_path(),
#                                                          filter="Excel (*.xls;*xlsx;*.csv)"
#                                                          )
#         if filename:
#             file = file_helper.path_to_win_format(filename)
#         return file
#
#     def add_file_to_file_list(self, file: str):
#         self.file_dict[self.file_list_cnt] = file
#         self.file_list_cnt += 1
#
#     def add_file_to_layout(self, file: str):
#         widget = QWidget()
#         layout = QHBoxLayout()
#         lbl = self._set_label(txt=file)
#         btn = self._set_button(txt='X', command=self.remove_file)
#         layout.addWidget(lbl)
#         layout.addWidget(btn)
#         widget.setLayout(layout)
#         self.layout_filelist.addWidget(widget)
#
    @pyqtSlot()
    def open_common_file(self):
        pass
#         filename = self.open_file(ui_const.OPEN_COMMON_FILE_TILTLE)
#         if filename:
#             self.lbl_file_name.setText('Файл: ' + file_helper.get_file_name(self.file_name))
#             self.lbl_file_name.setToolTip(f'<b>файл:</b><br><i>{self.file_name}</i>')
#             self.btn_remove_duplicates.setDisabled(False)
#
#     @pyqtSlot()
#     def remove_duplicates(self):
#         if self.file_name is None or self.file_name == '':
#             self.show_warning_messagebox("Необходимо выбрать файл с котормы будете работать!")
#             return
#         self.tmp_file = file_helper.create_file_with_unique_users(self.file_name)
#         self.btn_open_file_without_duplicates.setEnabled(True)
#
#     @pyqtSlot()
#     def open_file_without_duplicates(self):
#         file_helper.open_file_in_excel(self.tmp_file)
#
#     @pyqtSlot()
#     def add_files_to_compare(self):
#         file = self.open_file(ui_const.OPEN_FILE_FOR_COMPARE)
#         if file:
#             self.add_file_to_file_list(file)
#             self.add_file_to_layout(file)
#         print(self.file_dict)
#
#     @pyqtSlot()
#     def clear_all_files(self):
#         pass
#
#     @pyqtSlot()
#     def remove_file(self):
#         parent = self.sender().parent()
#         parent.setParent(None)
#
if __name__ == '__main__':
    app = QApplication(sys.argv[1:])

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())


# self.gbox_add_files_to_compare = QGroupBox('Файлы для сравнения')
#         layout = QVBoxLayout()
#         for x in range(30):
#             lbl = QLabel()
#             lbl.setText(f'{x}'*10)
#             layout.addWidget(lbl)
#         self.gbox_add_files_to_compare.setLayout(layout)
#         self.gbox_add_files_to_compare.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Preferred)
#
#         scroll = QScrollArea()
#         scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
#         scroll.setWidgetResizable(True)
#         scroll.setWidget(self.gbox_add_files_to_compare)
#
#         common_layout.addWidget(self.gbox_open_file, alignment=Qt.AlignTop)
#         common_layout.addWidget(scroll)
#         central_widget.setLayout(common_layout)
#         return central_widget