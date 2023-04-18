import os
import tkinter as tk
from tkinter import messagebox, DISABLED, NORMAL
from tkinter import filedialog as fd
import tkinter.font as tk_font
import file_helper
import ui_const as const


class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Data analyzer')
        self.geometry(f'{const.WIDTH}x{const.HEIGHT}')
        self.file_name = None
        self.tmp_file = None
        self.folder = None
        font_size = tk_font.Font(size=const.FONT_SIZE)

        # UI select file
        self.lbl_open_file = tk.Label(
            text="Файл:",
            font=font_size
        )
        self.lbl_file_name = tk.Label(
            foreground="#9ca3a2",
            text="не выбран",
            font=font_size
        )

        self.btn_open_file = tk.Button(
            text="Выбрать файл",
            command=self.open_file,
            width=18,
            font=font_size
        )

        # UI remove duplicates
        self.btn_remove_duplicates = tk.Button(
            text="Удалить дубликаты",
            command=self.remove_duplicates,
            width=18,
            font=font_size
        )
        self.btn_remove_duplicates['state'] = DISABLED

        self.btn_open_file_without_duplicates = tk.Button(
            text="Посмотреть результат",
            command=self.open_file_without_duplicates,
            width=18,
            font=font_size
        )
        self.btn_open_file_without_duplicates['state'] = DISABLED

        # UI select folder with file to compare
        self.lbl_select_folder = tk.Label(
            text="Директория:",
            font=font_size
        )
        self.lbl_dir = tk.Label(
            foreground="#9ca3a2",
            text="не выбрана",
            font=font_size
        )

        self.btn_select_dir = tk.Button(
            text="Выбрать папку",
            command=self.open_folder,
            width=18,
            font=font_size
        )

        # UI status bar
        self.status_bar = tk.Label(
            text='Пожалуйста, выберите файл, с которым хотите работать',
            foreground="#434343"
        )

        # UI pack elements

        self.lbl_open_file.place(x=6, y=12)
        self.lbl_file_name.place(x=50, y=12)
        self.btn_open_file.place(x=6, y=40)
        self.btn_remove_duplicates.place(x=186, y=40)
        self.btn_open_file_without_duplicates.place(x=366, y=40)
        self.lbl_select_folder.place(x=6, y=76)
        self.lbl_dir.place(x=94, y=76)
        self.btn_select_dir.place(x=6, y=104)

        '''
        self.ent_file.grid(row=1, column=0)
        self.btn_open_file.grid(row=1, column=2)

        self.btn_remove_duplicates.grid(row=1, column=3)

        self.lbl_select_folder.grid(row=2, column=0)
        self.ent_dir.grid(row=2, column=1)
        self.btn_select_folder.grid(row=2, column=3)
        '''

    def open_file(self):
        self.file_name = fd.askopenfilename(
            initialdir=file_helper.get_init_path(),
            filetypes=(("Еxcel files", "*.xls;*xlsx"),
                       ("Все файлы", "*.*"))
        )
        if len(self.file_name) > 0:
            self.lbl_file_name['text'] = file_helper.convert_path(self.file_name, 60)
            self.btn_remove_duplicates['state'] = NORMAL

    def remove_duplicates(self):
        if self.file_name is None or self.file_name == '':
            messagebox.showinfo(title="Внимание!", message="Файл не выбран.")
            return
        self.tmp_file = file_helper.create_file_with_unique_users(self.file_name)
        self.btn_open_file_without_duplicates['state'] = NORMAL

    def open_folder(self):
        self.folder = fd.askdirectory(
            initialdir=file_helper.get_init_path()
        )

    def open_file_without_duplicates(self):
        os.startfile(self.tmp_file)


if __name__ == '__main__':
    app = MainApp()
    app.mainloop()
