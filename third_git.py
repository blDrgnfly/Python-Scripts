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

        global df
        df = pd.read_csv(file_path, encoding='utf-8')
        messagebox.showinfo("Success", "File loaded successfully!")

def process_csv():
    global df  # Объявляем, что используем глобальную переменную df
    cols = ['id',
            'p_num',
            'time',
            'bg-5:55',
            'bg-5:50',
            'bg-5:45',
            'bg-5:40',
            'bg-5:35',
            'bg-5:30',
            'bg-5:25',
            'bg-5:20',
            'bg-5:15',
            'bg-5:10',
            'bg-5:05',
            'bg-5:00',
            'bg-4:55',
            'bg-4:50',
            'bg-4:45',
            'bg-4:40',
            'bg-4:35',
            'bg-4:30',
            'bg-4:25',
            'bg-4:20',
            'bg-4:15',
            'bg-4:10',
            'bg-4:05',
            'bg-4:00',
            'bg-3:55',
            'bg-3:50',
            'bg-3:45',
            'bg-3:40',
            'bg-3:35',
            'bg-3:30',
            'bg-3:25',
            'bg-3:20',
            'bg-3:15',
            'bg-3:10',
            'bg-3:05',
            'bg-3:00',
            'bg-2:55',
            'bg-2:50',
            'bg-2:45',
            'bg-2:40',
            'bg-2:35',
            'bg-2:30',
            'bg-2:25',
            'bg-2:20',
            'bg-2:15',
            'bg-2:10',
            'bg-2:05',
            'bg-2:00',
            'bg-1:55',
            'bg-1:50',
            'bg-1:45',
            'bg-1:40',
            'bg-1:35',
            'bg-1:30',
            'bg-1:25',
            'bg-1:20',
            'bg-1:15',
            'bg-1:10',
            'bg-1:05',
            'bg-1:00',
            'bg-0:55',
            'bg-0:50',
            'bg-0:45',
            'bg-0:40',
            'bg-0:35',
            'bg-0:30',
            'bg-0:25',
            'bg-0:20',
            'bg-0:15',
            'bg-0:10',
            'bg-0:05',
            'bg-0:00',
            'insulin-5:55',
            'insulin-5:50',
            'insulin-5:45',
            'insulin-5:40',
            'insulin-5:35',
            'insulin-5:30',
            'insulin-5:25',
            'insulin-5:20',
            'insulin-5:15',
            'insulin-5:10',
            'insulin-5:05',
            'insulin-5:00',
            'insulin-4:55',
            'insulin-4:50',
            'insulin-4:45',
            'insulin-4:40',
            'insulin-4:35',
            'insulin-4:30',
            'insulin-4:25',
            'insulin-4:20',
            'insulin-4:15',
            'insulin-4:10',
            'insulin-4:05',
            'insulin-4:00',
            'insulin-3:55',
            'insulin-3:50',
            'insulin-3:45',
            'insulin-3:40',
            'insulin-3:35',
            'insulin-3:30',
            'insulin-3:25',
            'insulin-3:20',
            'insulin-3:15',
            'insulin-3:10',
            'insulin-3:05',
            'insulin-3:00',
            'insulin-2:55',
            'insulin-2:50',
            'insulin-2:45',
            'insulin-2:40',
            'insulin-2:35',
            'insulin-2:30',
            'insulin-2:25',
            'insulin-2:20',
            'insulin-2:15',
            'insulin-2:10',
            'insulin-2:05',
            'insulin-2:00',
            'insulin-1:55',
            'insulin-1:50',
            'insulin-1:45',
            'insulin-1:40',
            'insulin-1:35',
            'insulin-1:30',
            'insulin-1:25',
            'insulin-1:20',
            'insulin-1:15',
            'insulin-1:10',
            'insulin-1:05',
            'insulin-1:00',
            'insulin-0:55',
            'insulin-0:50',
            'insulin-0:45',
            'insulin-0:40',
            'insulin-0:35',
            'insulin-0:30',
            'insulin-0:25',
            'insulin-0:20',
            'insulin-0:15',
            'insulin-0:10',
            'insulin-0:05',
            'insulin-0:00',
            'carbs-5:55',
            'carbs-5:50',
            'carbs-5:45',
            'carbs-5:40',
            'carbs-5:35',
            'carbs-5:30',
            'carbs-5:25',
            'carbs-5:20',
            'carbs-5:15',
            'carbs-5:10',
            'carbs-5:05',
            'carbs-5:00',
            'carbs-4:55',
            'carbs-4:50',
            'carbs-4:45',
            'carbs-4:40',
            'carbs-4:35',
            'carbs-4:30',
            'carbs-4:25',
            'carbs-4:20',
            'carbs-4:15',
            'carbs-4:10',
            'carbs-4:05',
            'carbs-4:00',
            'carbs-3:55',
            'carbs-3:50',
            'carbs-3:45',
            'carbs-3:40',
            'carbs-3:35',
            'carbs-3:30',
            'carbs-3:25',
            'carbs-3:20',
            'carbs-3:15',
            'carbs-3:10',
            'carbs-3:05',
            'carbs-3:00',
            'carbs-2:55',
            'carbs-2:50',
            'carbs-2:45',
            'carbs-2:40',
            'carbs-2:35',
            'carbs-2:30',
            'carbs-2:25',
            'carbs-2:20',
            'carbs-2:15',
            'carbs-2:10',
            'carbs-2:05',
            'carbs-2:00',
            'carbs-1:55',
            'carbs-1:50',
            'carbs-1:45',
            'carbs-1:40',
            'carbs-1:35',
            'carbs-1:30',
            'carbs-1:25',
            'carbs-1:20',
            'carbs-1:15',
            'carbs-1:10',
            'carbs-1:05',
            'carbs-1:00',
            'carbs-0:55',
            'carbs-0:50',
            'carbs-0:45',
            'carbs-0:40',
            'carbs-0:35',
            'carbs-0:30',
            'carbs-0:25',
            'carbs-0:20',
            'carbs-0:15',
            'carbs-0:10',
            'carbs-0:05',
            'carbs-0:00',
            'hr-5:55',
            'hr-5:50',
            'hr-5:45',
            'hr-5:40',
            'hr-5:35',
            'hr-5:30',
            'hr-5:25',
            'hr-5:20',
            'hr-5:15',
            'hr-5:10',
            'hr-5:05',
            'hr-5:00',
            'hr-4:55',
            'hr-4:50',
            'hr-4:45',
            'hr-4:40',
            'hr-4:35',
            'hr-4:30',
            'hr-4:25',
            'hr-4:20',
            'hr-4:15',
            'hr-4:10',
            'hr-4:05',
            'hr-4:00',
            'hr-3:55',
            'hr-3:50',
            'hr-3:45',
            'hr-3:40',
            'hr-3:35',
            'hr-3:30',
            'hr-3:25',
            'hr-3:20',
            'hr-3:15',
            'hr-3:10',
            'hr-3:05',
            'hr-3:00',
            'hr-2:55',
            'hr-2:50',
            'hr-2:45',
            'hr-2:40',
            'hr-2:35',
            'hr-2:30',
            'hr-2:25',
            'hr-2:20',
            'hr-2:15',
            'hr-2:10',
            'hr-2:05',
            'hr-2:00',
            'hr-1:55',
            'hr-1:50',
            'hr-1:45',
            'hr-1:40',
            'hr-1:35',
            'hr-1:30',
            'hr-1:25',
            'hr-1:20',
            'hr-1:15',
            'hr-1:10',
            'hr-1:05',
            'hr-1:00',
            'hr-0:55',
            'hr-0:50',
            'hr-0:45',
            'hr-0:40',
            'hr-0:35',
            'hr-0:30',
            'hr-0:25',
            'hr-0:20',
            'hr-0:15',
            'hr-0:10',
            'hr-0:05',
            'hr-0:00',
            'steps-5:55',
            'steps-5:50',
            'steps-5:45',
            'steps-5:40',
            'steps-5:35',
            'steps-5:30',
            'steps-5:25',
            'steps-5:20',
            'steps-5:15',
            'steps-5:10',
            'steps-5:05',
            'steps-5:00',
            'steps-4:55',
            'steps-4:50',
            'steps-4:45',
            'steps-4:40',
            'steps-4:35',
            'steps-4:30',
            'steps-4:25',
            'steps-4:20',
            'steps-4:15',
            'steps-4:10',
            'steps-4:05',
            'steps-4:00',
            'steps-3:55',
            'steps-3:50',
            'steps-3:45',
            'steps-3:40',
            'steps-3:35',
            'steps-3:30',
            'steps-3:25',
            'steps-3:20',
            'steps-3:15',
            'steps-3:10',
            'steps-3:05',
            'steps-3:00',
            'steps-2:55',
            'steps-2:50',
            'steps-2:45',
            'steps-2:40',
            'steps-2:35',
            'steps-2:30',
            'steps-2:25',
            'steps-2:20',
            'steps-2:15',
            'steps-2:10',
            'steps-2:05',
            'steps-2:00',
            'steps-1:55',
            'steps-1:50',
            'steps-1:45',
            'steps-1:40',
            'steps-1:35',
            'steps-1:30',
            'steps-1:25',
            'steps-1:20',
            'steps-1:15',
            'steps-1:10',
            'steps-1:05',
            'steps-1:00',
            'steps-0:55',
            'steps-0:50',
            'steps-0:45',
            'steps-0:40',
            'steps-0:35',
            'steps-0:30',
            'steps-0:25',
            'steps-0:20',
            'steps-0:15',
            'steps-0:10',
            'steps-0:05',
            'steps-0:00',
            'cals-5:55',
            'cals-5:50',
            'cals-5:45',
            'cals-5:40',
            'cals-5:35',
            'cals-5:30',
            'cals-5:25',
            'cals-5:20',
            'cals-5:15',
            'cals-5:10',
            'cals-5:05',
            'cals-5:00',
            'cals-4:55',
            'cals-4:50',
            'cals-4:45',
            'cals-4:40',
            'cals-4:35',
            'cals-4:30',
            'cals-4:25',
            'cals-4:20',
            'cals-4:15',
            'cals-4:10',
            'cals-4:05',
            'cals-4:00',
            'cals-3:55',
            'cals-3:50',
            'cals-3:45',
            'cals-3:40',
            'cals-3:35',
            'cals-3:30',
            'cals-3:25',
            'cals-3:20',
            'cals-3:15',
            'cals-3:10',
            'cals-3:05',
            'cals-3:00',
            'cals-2:55',
            'cals-2:50',
            'cals-2:45',
            'cals-2:40',
            'cals-2:35',
            'cals-2:30',
            'cals-2:25',
            'cals-2:20',
            'cals-2:15',
            'cals-2:10',
            'cals-2:05',
            'cals-2:00',
            'cals-1:55',
            'cals-1:50',
            'cals-1:45',
            'cals-1:40',
            'cals-1:35',
            'cals-1:30',
            'cals-1:25',
            'cals-1:20',
            'cals-1:15',
            'cals-1:10',
            'cals-1:05',
            'cals-1:00',
            'cals-0:55',
            'cals-0:50',
            'cals-0:45',
            'cals-0:40',
            'cals-0:35',
            'cals-0:30',
            'cals-0:25',
            'cals-0:20',
            'cals-0:15',
            'cals-0:10',
            'cals-0:05',
            'cals-0:00',
            'activity-5:55',
            'activity-5:50',
            'activity-5:45',
            'activity-5:40',
            'activity-5:35',
            'activity-5:30',
            'activity-5:25',
            'activity-5:20',
            'activity-5:15',
            'activity-5:10',
            'activity-5:05',
            'activity-5:00',
            'activity-4:55',
            'activity-4:50',
            'activity-4:45',
            'activity-4:40',
            'activity-4:35',
            'activity-4:30',
            'activity-4:25',
            'activity-4:20',
            'activity-4:15',
            'activity-4:10',
            'activity-4:05',
            'activity-4:00',
            'activity-3:55',
            'activity-3:50',
            'activity-3:45',
            'activity-3:40',
            'activity-3:35',
            'activity-3:30',
            'activity-3:25',
            'activity-3:20',
            'activity-3:15',
            'activity-3:10',
            'activity-3:05',
            'activity-3:00',
            'activity-2:55',
            'activity-2:50',
            'activity-2:45',
            'activity-2:40',
            'activity-2:35',
            'activity-2:30',
            'activity-2:25',
            'activity-2:20',
            'activity-2:15',
            'activity-2:10',
            'activity-2:05',
            'activity-2:00',
            'activity-1:55',
            'activity-1:50',
            'activity-1:45',
            'activity-1:40',
            'activity-1:35',
            'activity-1:30',
            'activity-1:25',
            'activity-1:20',
            'activity-1:15',
            'activity-1:10',
            'activity-1:05',
            'activity-1:00',
            'activity-0:55',
            'activity-0:50',
            'activity-0:45',
            'activity-0:40',
            'activity-0:35',
            'activity-0:30',
            'activity-0:25',
            'activity-0:20',
            'activity-0:15',
            'activity-0:10',
            'activity-0:05',
            'activity-0:00',
            'bg+1:00']

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
        #df['datetime'] = pd.to_datetime(df['datetime'], format='%Y-%m-%d %H:%M', errors='coerce') #игнорировать ошибки - на NaT
        # Преобразование обратно в str чтобы удалить дубликаты
        df['datetime'] = df['datetime'].dt.strftime('%Y-%m-%d %H:%M')
        df = df.drop_duplicates(subset=['datetime'])
        
        # Преобразование в datetime
        df['datetime'] = pd.to_datetime(df['datetime'], format='%Y-%m-%d %H:%M')   
             
        # Генерация списка значений от 5:55 до 0:00 - 72 нужных нам столбца
        start_time = timedelta(hours=5, minutes=55)
        name_cols_dt = [start_time - timedelta(minutes=5 * i) for i in range(72)]  # 72 столбца
        # Переводим в строки и сразу обрезаем до первых 4 символов
        name_cols = [str(td)[:4] for td in name_cols_dt]
        #name_cols = name_cols[::-1]
        first_row = df['datetime'].iloc[0::3]
        #создаём массив-кондуктор, для сравнения
        df_conductor = pd.DataFrame(columns=name_cols)
        #заполняем первый столбец массива
        df_conductor['0:00'] = first_row
        #последний столбец массива
        # Сброс индексов, чтобы они были последовательными
        df_conductor = df_conductor.reset_index(drop=True)
        bgafter1hours = df_conductor['0:00']+timedelta(hours=1)
        #заполняем все остальные элементы массива
        for i in range(len(df_conductor)-1):
            for j in range(72):
                df_conductor.iloc[i,j] = (df_conductor.at[i, '0:00']-name_cols_dt[j]).strftime('%Y-%m-%d %H:%M:%S')
                
        #заполняем последний столбец массива
        df_conductor['bg+1:00'] = bgafter1hours
        # Преобразование обратно в строку чтобы корректно сравнивать
        df_conductor['0:00'] = df_conductor['0:00'].dt.strftime('%Y-%m-%d %H:%M:%S')
        df_conductor['bg+1:00'] = df_conductor['bg+1:00'].dt.strftime('%Y-%m-%d %H:%M:%S')
        df['datetime'] = df['datetime'].dt.strftime('%Y-%m-%d %H:%M:%S')
        #создаем остальные массивы, которые будет нужно заполнить если сравнение пройдет успешно
        name_cols.append('bg+1:00')
        df_bg = pd.DataFrame(np.nan, index = range(0, first_row.shape[0], 1), columns=name_cols)
        df_carbohydrates = pd.DataFrame(np.nan, index = range(0, first_row.shape[0], 1), columns=name_cols)
        df_insulin = pd.DataFrame(np.nan, index = range(0, first_row.shape[0], 1), columns=name_cols)
        df_acv = pd.DataFrame(np.nan, index = range(0, first_row.shape[0], 1), columns=name_cols)

        # Создаем словарь для быстрого поиска
        datetime_to_values = df.set_index('datetime')[['bg', 'carbohydrates', 'insulin', 'acv']].to_dict(orient='index')
        # Итерируем по индексам и столбцам df_conductor
        for i in df_conductor.index:
            for  j in df_conductor.columns:
                what_find = df_conductor.at[i, j]
                if what_find in datetime_to_values:
                    df_bg.at[i,j] = datetime_to_values[what_find]['bg']
                    df_carbohydrates.at[i,j] = datetime_to_values[what_find]['carbohydrates']
                    df_insulin.at[i,j] = datetime_to_values[what_find]['insulin']
                    df_acv.at[i,j] = datetime_to_values[what_find]['acv']
                    
        cols_bg = cols[2:74]
        
        cols_bg.append('bg+1:00')

        cols_insulin = cols[74:146]
        cols_insulin.append('bg+1:00')

        cols_carbohydrates = cols[146:218]
        cols_carbohydrates.append('bg+1:00')

        cols_acv = cols[434:506]
        #cols_acv = cols_acv.tolist()
        cols_acv.append('bg+1:00')

        cols_cals = cols[362:434]
        #cols_cals = cols_cals.tolist()
        cols_cals.append('bg+1:00')
        # переименовываем столбцы чтобы были как в колаб
        df_bg.columns = cols_bg
        #  переименовываем столбцы чтобы были как в колаб
        df_carbohydrates.columns = cols_carbohydrates
        # переименовываем столбцы чтобы были как в колаб
        df_insulin.columns = cols_insulin
        # переименовываем столбцы чтобы были как в колаб
        df_acv.columns = cols_acv
        # переименовываем столбцы чтобы были как в колаб
        df_cals = df_carbohydrates*48
        df_cals.columns = cols_cals
        #удалим лишний 73 столбец который получился в каждом из подмассивов
        df_acv = df_acv.drop(columns='bg+1:00')
        df_cals = df_cals.drop(columns='bg+1:00')
        df_insulin = df_insulin.drop(columns='bg+1:00')
        df_carbohydrates = df_carbohydrates.drop(columns='bg+1:00')
        
        df_kaggle = pd.DataFrame(np.nan, index=first_row.index, columns=cols)
        df_kaggle['time'] = first_row
        df_kaggle['p_num'] = 'p_15'
        df_kaggle.update(df_bg)
        df_kaggle.update(df_acv)
        df_kaggle.update(df_cals)
        df_kaggle.update(df_insulin)
        df_kaggle.update(df_carbohydrates)
        
        df_kaggle = df_kaggle.iloc[:-4]
        df_kaggle = df_kaggle.replace(0, np.nan).replace(0.0, np.nan)
        df_kaggle = df_kaggle.dropna(subset=['bg+1:00'])
        
        del df
        df = df_kaggle
        messagebox.showinfo("Success", "Файл успешно обработан!!")
    else:
        messagebox.showerror("Error", "Не получилось обработать файл!")

def download_csv():
    if 'df' in globals():
        file_path = filedialog.asksaveasfilename(defaultextension=".csv",
                                                  filetypes=[("CSV files", "*.csv")])
        if file_path:
            df.to_csv(file_path, index=False)
            messagebox.showinfo("Success", "Файл успешно загружен!")
    else:
        messagebox.showerror("Error", "Не получилось загрузить файл!")

# Создание главного окна
root = tk.Tk()
root.title("преобразование файла с измерительного прибора в файл обучения")

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
