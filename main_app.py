import tkinter as tk
from tkinter import ttk, END, messagebox, DISABLED, NORMAL
from tkinter import filedialog as fd
import helper


class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Data analyzer')
        self.geometry('450x300')
        self.file_name = None

        for c in range(5):
            self.columnconfigure(index=c, weight=1)
        for r in range(15):
            self.rowconfigure(index=r, weight=1)

        # UI select file
        self.lbl_open_file = tk.Label(
            text="Файл"
        )
        self.entry = ttk.Entry(width=40, foreground="#9ca3a2")
        self.entry.insert(0, "Выберите файл")

        self.btn_open_file = tk.Button(
            text="Выбрать файл",
            command=self.open_file
        )

        # UI remove duplicates
        self.btn_remove_duplicates = tk.Button(
            text="Удалить дубли",
            command=self.remove_duplicates
        )
        self.btn_remove_duplicates['state'] = DISABLED

        self.lbl_open_file.grid(row=0, column=0)
        self.entry.grid(row=0, column=1)
        self.btn_open_file.grid(row=0, column=3)
        self.btn_remove_duplicates.grid(row=1, column=3)

    def open_file(self):
        self.file_name = fd.askopenfilename(
            initialdir=r"C:\Users\Pavel.Sukhanov\Desktop",
            filetypes=(("Еxcel files", "*.xls;*xlsx"),
                       ("Все файлы", "*.*"))
        )
        if len(self.file_name) > 0:
            self.entry.delete(0, END)
            self.entry.insert(0, helper.convert_path(self.file_name, self.entry['width']))
            self.btn_remove_duplicates['state'] = NORMAL

    def remove_duplicates(self):
        if self.file_name is None or self.file_name == '':
            messagebox.showinfo(title="Внимание!", message="Файл не выбран.")
            return
        helper.create_file_with_unique_users(self.file_name)


if __name__ == '__main__':
    app = MainApp()
    app.mainloop()
