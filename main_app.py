import tkinter as tk
from tkinter import ttk, END, messagebox, DISABLED, NORMAL, SW, CENTER, BOTTOM, NW, TOP, W, N
from tkinter import filedialog as fd
import file_helper


class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Data analyzer')
        self.geometry('450x300')
        self.file_name = None

        # UI select file
        self.lbl_open_file = tk.Label(
            text="Файл:"
        )
        self.ent_file = ttk.Entry(foreground="#9ca3a2")
        self.ent_file.insert(0, "Файл не выбран")

        self.btn_open_file = tk.Button(
            text="Выбрать файл",
            command=self.open_file
        )

        # UI remove duplicates
        self.btn_remove_duplicates = tk.Button(
            text="Удалить дубликаты",
            command=self.remove_duplicates
        )
        self.btn_remove_duplicates['state'] = DISABLED

        # UI select folder with file to compare
        self.lbl_select_folder = tk.Label(
            text="Выберите папку"
        )
        self.ent_dir = ttk.Entry(foreground="#9ca3a2")
        self.ent_dir.insert(0, "Выберите папку с файлами для сравнения")
        self.btn_select_folder = tk.Button(
            text="Выберите папку",
            command=self.open_folder
        )

        # UI status bar
        self.status_bar = tk.Label(
            text='Пожалуйста, выберите файл, с которым хотите работать',
            foreground="#434343"
        )

        # UI pack elements

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
            self.ent_file.delete(0, END)
            self.ent_file.insert(0, file_helper.convert_path(self.file_name, self.ent_file['width']))
            self.btn_remove_duplicates['state'] = NORMAL

    def remove_duplicates(self):
        if self.file_name is None or self.file_name == '':
            messagebox.showinfo(title="Внимание!", message="Файл не выбран.")
            return
        file_helper.create_file_with_unique_users(self.file_name)

    def open_folder(self):
        pass


if __name__ == '__main__':
    app = MainApp()
    app.mainloop()
