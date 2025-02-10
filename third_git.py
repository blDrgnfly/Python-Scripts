import tkinter as tk
from tkinter import filedialog, messagebox
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
from datetime import datetime, timedelta
#import chardet
# Глобальная переменная для хранения данных
df = None


def load_csv():
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if file_path:
        entry_path.delete(0, tk.END)
        entry_path.insert(0, file_path)
        #определить кодировку
        #with open(file_path, 'rb') as f:
        #    result = chardet.detect(f.read(10000))
        #    print(result)
        global df
        df = pd.read_csv(file_path, encoding='utf-8')
        messagebox.showinfo("Success", "File loaded successfully!")

def process_csv():
    global df  # Объявляем, что используем глобальную переменную df
    if df is not None:
        #порог гипогликемии
        min_the_target_range = 4
        #сразу заменяем записанный вручную на автоматически измеренный (когда записывают вручную столбец bg остается пустым)
        df['bg'] = df['bg'].fillna(df['bg_true'])
        #удаляем скопированное
        df = df.drop(columns=['bg_true']) #это тоже
        #строка -9999.0 ниже тоже бесполезна и без записей
        df = df[df['ток'] != -9999.0]
        #удаляем столбцы которые хоть и бывают заполнены - не несут информацию 
        df = df.drop(columns=['калибровка']) 
        df = df.drop(columns=['ток']) #это тоже
        df = df.drop(columns=['исходный тип'])#исходный тип	тоже
        df = df.drop(columns=['sensor_text'])# sensor_text тоже
        #этот "тип" дублируется
        df = df.drop(columns=['type_kkal']) 
        # Оставляем только строки, где 'событие' == NaN т.к. только в пустых заполнено bg, insulin, ccal, activ
        df = df[df['событие'].isna()]
        #после очистки dataframe столбец можно удалить, т.к. теперь остались только информативные строки
        df = df.drop(columns=['событие'])
        # Удаляем строки, где с 3 по 11 столбцы (2:) - то что (bg, insulin, ccal, activ) - все значения NaN
        df = df.dropna(subset=df.columns[2:], how='all')
        #столбцы, которые удаляю ниже могут быть информативными - но ни у кого из 15 пациентов нет больше 2х записей (не подойдет для обучения)
        df = df.drop(columns=['исключено'])
        df = df.drop(columns=['примечание'])
        df = df.drop(columns=['dream_stop'])
        df = df.drop(columns=['dream_start'])
        df = df.drop(columns=['лекарство'])
        #посчитаем интервалы между записями
            # Преобразуем первый столбец в формат datetime
        df['datetime'] = pd.to_datetime(df['datetime'])
        df['diff'] = df.iloc[:, 0].diff().dt.total_seconds().fillna(0).astype(int)
        
        condition = df['Источник'] == 'Протокол'        
        # Индексы строк, удовлетворяющих условию
        indices = df[condition].index
        for idx in indices:
            if (idx > 0) and (idx < len(df) - 1):
                if (df['diff'].loc[idx])<160:
                    df.loc[idx-1,:] = df.loc[idx,:]
                else:
                    df.loc[idx+1,:] = df.loc[idx,:]
        #
        #после копирования можно удалить
        df = df.drop(columns=['Источник'])
        
        #в dataframe 2 столбца  инсулина, перенесем запись с одного в другой и удалим второй 
        for index in df.index:
            if df['insulin_type'].loc[index] == 'Тип инсулина длительного действия':
                if pd.isna(df['insulin'].loc[index]):
                    df.at[index, 'insulin'] = -30
            else:
                df.at[index, 'insulin'] = -1 * df['insulin'].loc[index]
        df = df.drop(columns=['insulin_type'])
        # Добавляем новый столбец с условиями
        df['acv'] = np.where(df['activity'] == 'Интенсивный уровень физической активности', 3,
                            np.where(df['activity'] == 'Средний уровень физической активности', 2,
                            np.where(df['activity'] == 'Неизвестный уровень физической активности', 1,
                            0)))
        df = df.drop(columns=['activity'])
        # Условие: значение в столбце 'A' < 306 (5 минут и несколько секунд т.к. у 11го пациента автоматическое измерение 299-305 мс)
        condition = df['diff'] < 306
        # Индексы строк, удовлетворяющих условию
        indices = df[condition].index
        # Копирование значений, которые будут удалены
        for idx in indices:
            if (idx > 0) and (idx < len(df)-1):
                df.loc[idx-1,:] = df.loc[idx,:]
        df = df.drop(columns='diff')
        #df['datetime'] = pd.to_datetime(df['datetime'], format='%Y-%m-%-d %H:%M', errors='coerce')
        # Преобразование обратно
        df['datetime'] = df['datetime'].dt.strftime('%Y-%m-%d %H:%M')

        df = df.drop_duplicates(subset=['datetime'])
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
