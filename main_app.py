import tkinter as tk
from tkinter import ttk
from tkinter import END
from tkinter import filedialog as fd
import helper


class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Data analyzer')
        self.geometry('450x300')
        self.file_name = ''

        for c in range(5):
            self.columnconfigure(index=c, weight=1)
        for r in range(5):
            self.rowconfigure(index=r, weight=1)

        # UI выбора файла для
        self.lbl_open_file = tk.Label(
            text="Файл"
        )
        self.entry = ttk.Entry(width=40, foreground="#9ca3a2")
        self.entry.insert(0, "Выберите файл")

        self.btn_open_file = tk.Button(
            text="Выбрать файл",
            command=self.open_file
        )
        self.lbl_open_file.grid(row=0, column=0, pady=1)
        self.entry.grid(row=0, column=1, pady=1)
        self.btn_open_file.grid(row=0, column=3, pady=1)

    def open_file(self):
        self.file_name = fd.askopenfilename(
            initialdir=r"C:\Users\Pavel.Sukhanov\Desktop",
            filetypes=(("Еxcel files", "*.xls;*xlsx"),
                       ("Все файлы", "*.*"))
        )
        self.entry.delete(0, END)
        print(helper.convert_path_to_win_format(self.file_name))
        self.entry.insert(0, helper.convert_path(self.file_name, self.entry['width']))


if __name__ == '__main__':
    app = MainApp()
    app.mainloop()
