import sys

import file_helper
import ui_const as const
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QFileDialog, QWidget, QMessageBox
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QGroupBox
from PyQt5.QtGui import QFont, QFontMetrics
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtCore import Qt
from PyQt5 import QtCore


# TODO разобраться с расположением элементов, см. пример:
# class MainApp(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         main_widget = QWidget()
#         self.ok_btn = QPushButton("ОК")
#         self.cancel_btn = QPushButton("Cancel")
#         self.ok_btn.clicked.connect(self.test)
#         self.ok_btn.setObjectName("OKK")
#
#         self.hbox = QHBoxLayout()
#         self.hbox.addStretch(1)
#         self.hbox.addWidget(self.ok_btn)
#         self.hbox.addWidget(self.cancel_btn)
#
#         self.vbox = QVBoxLayout()
#         self.vbox.addStretch(1)
#         self.vbox.addLayout(self.hbox)
#
#         main_widget.setLayout(self.vbox)
#         self.setCentralWidget(main_widget)
#
#         self.setGeometry(300, 300, 300, 150)
#         self.show()
#
#     def test(self):
#         print(self.centralWidget().findChild(QPushButton, name="OKK").setText('lol'))
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     main = MainApp()
#     sys.exit(app.exec_())


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.file_name = None
        self.init_ui()

    # TODO https://ru.stackoverflow.com/questions/1417424/Позиционирование-элементов-в-pyqt
    def set_font(self):
        font = QFont()
        font.setPointSize(const.FONT_SIZE)
        return font

    def create_central_widget(self):
        central_widget = QWidget()
        common_layout = QVBoxLayout()

        self.gbox_open_file = QGroupBox('Выберите файл, с которым хотите работать')
        select_file_layout = QHBoxLayout()
        self.lbl_file_name = self._set_label('Файл не выбран')
        # self.btn_open_file = self._set_button(txt='Выбрать файл', command=self.open_file)
        self.btn_open_file = self._set_button(txt='Выбрать файл', command=self.test)
        select_file_layout.addWidget(self.lbl_file_name, alignment=Qt.AlignLeft)
        select_file_layout.addWidget(self.btn_open_file, alignment=Qt.AlignRight)
        self.gbox_open_file.setLayout(select_file_layout)

        # common_layout.addLayout(select_file_layout)
        common_layout.addWidget(self.gbox_open_file, alignment=Qt.AlignTop)
        central_widget.setLayout(common_layout)
        return central_widget

    def init_ui(self):
        self.create_central_widget()
        self.setGeometry(200, 200, const.WINDOW_WIDTH, const.WINDOW_HEIGHT)
        self.setWindowTitle(const.WINDOW_TITILE)
        self.setCentralWidget(self.create_central_widget())

    #     self.lbl_file = self._set_label("Файл:", font)
    #     self.lbl_file.move(const.STEP, const.STEP)
    #     self.lbl_file_name = self._set_label("не выбран", font)
    #     self.lbl_file_name.setStyleSheet("QLabel {color:grey}")
    #     self.lbl_file_name.move(
    #         self._get_end_by_x(self.lbl_file) + const.STEP,
    #         const.STEP
    #     )
    #
    #     self.btn_open_file = self._set_button('Выбрать файл', font, self.open_file)
    #     self.btn_open_file.move(
    #         const.STEP,
    #         self._get_end_by_y(self.lbl_file) + const.STEP
    #     )
    #
    #     self.btn_remove_duplicates = self._set_button('Удалить дубликаты', font, self.remove_duplicates)
    #     self.btn_remove_duplicates.setEnabled(False)
    #     self.btn_remove_duplicates.move(
    #         self._get_end_by_x(self.btn_open_file) + const.STEP,
    #         self._get_end_by_y(self.lbl_file) + const.STEP
    #     )
    #
    #     self.btn_open_file_without_duplicates = self._set_button("Посмотреть результат", font,
    #                                                              self.open_file_without_duplicates)
    #     self.btn_open_file_without_duplicates.setEnabled(False)
    #     self.btn_open_file_without_duplicates.move(
    #         self._get_end_by_x(self.btn_remove_duplicates) + const.STEP,
    #         self._get_end_by_y(self.lbl_file) + const.STEP
    #     )
    #
    #     self.btn_add_files_to_compare = self._set_button("Выбрать файлы", font, self.add_files_to_compare)
    #
    def _set_label(self, txt):
        lbl = QLabel(self, text=txt)
        lbl.setFont(self.set_font())
        lbl.adjustSize()
        return lbl

    def _set_button(self, txt, command):
        btn = QPushButton(self)
        btn.setText(txt)
        btn.setFont(self.set_font())
        btn.setFixedWidth(const.BUTTON_WIDTH)
        btn.setFixedHeight(const.BUTTON_HEIGHT)
        btn.clicked.connect(command)
        return btn

    #
    # def _get_end_by_x(self, element: QWidget):
    #     return element.x() + element.width()
    #
    # def _get_end_by_y(self, element: QWidget):
    #     return element.y() + element.height()

    #     def show_warning_messagebox(self, txt):
    #         msg = QMessageBox()
    #         msg.setIcon(QMessageBox.Warning)
    #         msg.setText(txt)
    #         msg.setWindowTitle("Внимание!")
    #         retval = msg.exec_()
    #
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
            # self.lbl_file_name.adjustSize()

    def _set_lbl_width(self):
        self.lbl_file_name.setFixedWidth(self._get_allowed_lbl_width(self.lbl_file_name))

    def _get_allowed_lbl_width(self, lbl: QLabel):
        btn = lbl.parent().findChild(QPushButton)
        width = btn.x() - lbl.x() - 10
        return width

    def _get_text_length(self, text):
        metriks = QFontMetrics(self.set_font())
        return metriks.width(text)

    def test(self):
        self.lbl_file_name.setFixedWidth(self._get_allowed_lbl_width(self.lbl_file_name))
        txt = self.lbl_file_name.text() + 'W'
        text_width = self._get_text_length(txt)
        lbl_width = self._get_allowed_lbl_width(self.lbl_file_name)
        print(text_width < lbl_width)
        self.lbl_file_name.setText(txt)


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
#         pass

if __name__ == '__main__':
    app = QApplication(sys.argv[1:])

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
