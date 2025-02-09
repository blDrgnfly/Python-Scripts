import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd

def load_csv():
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if file_path:
        entry_path.delete(0, tk.END)
        entry_path.insert(0, file_path)
        global df
        df = pd.read_csv(file_path)
        messagebox.showinfo("Success", "File loaded successfully!")

def process_csv():
    if 'df' in globals():
        # Пример обработки: добавление нового столбца
        df['new_column'] = df['existing_column'] * 2  # Измените это в соответствии с вашей обработкой
        messagebox.showinfo("Success", "File processed successfully!")
    else:
        messagebox.showerror("Error", "No file loaded!")

def download_csv():
    if 'df' in globals():
        file_path = filedialog.asksaveasfilename(defaultextension=".csv",
                                                  filetypes=[("CSV files", "*.csv")])
        if file_path:
            df.to_csv(file_path, index=False)
            messagebox.showinfo("Success", "File downloaded successfully!")
    else:
        messagebox.showerror("Error", "No file to download!")

# Создание главного окна
root = tk.Tk()
root.title("CSV Processor")

# Поле для отображения пути к файлу
entry_path = tk.Entry(root, width=50)
entry_path.pack(pady=10)

# Кнопка загрузки
load_button = tk.Button(root, text="Загрузить", command=load_csv)
load_button.pack(pady=5)

# Кнопка обработки
process_button = tk.Button(root, text="Обработать", command=process_csv)
process_button.pack(pady=5)

# Кнопка скачивания
download_button = tk.Button(root, text="Скачать", command=download_csv)
download_button.pack(pady=5)

# Запуск главного цикла
root.mainloop()
