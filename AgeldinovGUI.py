# подключаем библиотеки
import PySimpleGUI as sg
import random
import pandas as pd
import convertation
import buffer_calculation
import  PK_calculation
import points_coordinates

# Основная функция
def main():
        # что будет внутри окна конвертации
        convert_layout = [
                [sg.Text('Эта вкладка для конвертации размерности на основе выбранных единиц измерения.', font='Helvetica 20')],
                # затем делаем текст
                [sg.Text('Выберете исходную единицу измерения массы', font='Helvetica 20')],
                [sg.OptionMenu(values=('Пикограммы', 'Нанограммы', 'Микрограммы', 'Милиграммы'), default_value='Пикограммы',  k='-UNIT OPTION START-'),],
                [sg.Text('Выберете конечную  единицу измерения массы', font='Helvetica 20')],
                [sg.OptionMenu(values=('Пикограммы', 'Нанограммы', 'Микрограммы', 'Милиграммы'), default_value='Пикограммы',  k='-UNIT OPTION END-'),],
                [sg.Text('Введите исходное количество', font='Helvetica 20')],
                [sg.Input(key='-AMOUNT-')],
                [sg.Button('Рассчитать', enable_events=True, key='-CAlCULATE 1-', font='Helvetica 20')],
                [sg.Text('Здесь будет отображен результат', key='-RESULTS 1-', font='Helvetica 20')]
                 ]
        # что будет внутри окна расчетов буфера
        buffer_layout = [
                [sg.Text('Эта вкладка для расчета требуемой массы вещества на основе указанного объема, концентрации и названия вещества', font='Helvetica 20')],
                # затем делаем текст
                [sg.Text('Введите формулу вещества', font='Helvetica 20')],
                [sg.Input(key='-FORMULA IN-')],
                [sg.Text('Введите концентрацию в молях', font='Helvetica 20')],
                [sg.Input(key='-CONCENTRATION IN-')],
                [sg.Text('Введите объем в литрах', font='Helvetica 20')],
                [sg.Input(key='-VOLUME IN-')],
                [sg.Button('Рассчитать', enable_events=True, key='-CAlCULATE 2-', font='Helvetica 20')],
                [sg.Text('Здесь будет отображен результат', key='-RESULTS 2-', font='Helvetica 20')]
                 ]
        PK_layout = [
                [sg.Text('В данном окне вы сможете расчитать фармакокинетику и фармакодинамику', font='Helvetica 20'),
                    sg.Button('Шпаргалка', enable_events=True, key='-FUNCTION5-', font='Helvetica 16')],  
                    [sg.Text('Укажите используемые величины', font='Helvetica 20')],
                    [sg.Text('Единица времени:', font='Helvetica 20'),
                     sg.OptionMenu(values=('Секунды', 'Минуты', 'Часы', 'Дни'), default_value='Минуты',  k='-OPTION MENU 3-')],
                    [sg.Text('Количество временных точек:', font='Helvetica 20'),
                     sg.Input(key='-TimePoints IN-')],
                    [sg.Text('Единица концентрации:', font='Helvetica 20'),
                     sg.OptionMenu(values=('пкг/мл', 'нг/мл', 'мкг/мл', 'мг/мл'), default_value='нг/мл',  k='-OPTION MENU 4-')],
                    [sg.Text('Значение дозы:', font='Helvetica 20'),
                     sg.Input(key='-Dose IN-')],
                    [sg.Text('Единица дозы:', font='Helvetica 20'),
                     sg.OptionMenu(values=('пкг', 'нг', 'мкг', 'мг'), default_value='нг',  k='-OPTION MENU 4-')],
                    [sg.Text('Файл с данными:', font='Helvetica 20'),
                     sg.Button('Выбрать файл', enable_events=True, key='-FUNCTION3-', font='Helvetica 16')],
                    [sg.Button('Посчитать', enable_events=True, key='-FUNCTION4-', font='Helvetica 20')],
                    [sg.Text('Здесь появится результат', key='-text20-', font='Helvetica 20')]    

#                [sg.Text('Результаты:  ', font='Helvetica 20')],
#                [sg.Text('Lambda Z:', font='Helvetica 20')],
#                [sg.Text('t 1/2:', font='Helvetica 20')],
#                [sg.Text('T Max:', font='Helvetica 20')],
#                [sg.Text('C Max:', font='Helvetica 20')],
#                [sg.Text('C O:', font='Helvetica 20')],
#                [sg.Text('C last obs/ C Max:', font='Helvetica 20')],
#                [sg.Text('AUC 0-t:', font='Helvetica 20')],
#                [sg.Text('AUC 0-inf_obs:', font='Helvetica 20')],
#                [sg.Text('AUC 0-t/0-inf_obs:', font='Helvetica 20')],
#               [sg.Text('AUMC 0-inf_obs:', font='Helvetica 20')],
#                [sg.Text('MRT 0-inf_obs:', font='Helvetica 20')],
#                [sg.Text('Vz_obs:', font='Helvetica 20')],
#                [sg.Text('Cl_obs:', font='Helvetica 20')],
#                [sg.Text('Vss_obs:', font='Helvetica 20')]
        ]
        coordinates_layout = [
                [sg.Text('В данном окне вы сможете вычислить координаты точки(ек) на рисунке', font='Helvetica 20')],
                    [sg.Text('Укажите диапазон осей на рисунке', font='Helvetica 20')],
                    [sg.Text('Начальное значение по оси Y:', font='Helvetica 20'),
                     sg.Input(default_text='0', key='-Y START IN-'),
                     sg.Text('Конечное значение по оси Y:', font='Helvetica 20'),
                     sg.Input(key='-Y END IN-')],
                    [sg.Text('Начальное значение по оси X:', font='Helvetica 20'),
                     sg.Input(default_text='0', key='-X START IN-'),
                     sg.Text('Конечное значение по оси X:', font='Helvetica 20'),
                     sg.Input(key='-X END IN-')],

                    [sg.Text('Файл с данными:', font='Helvetica 20'),
                     sg.Button('Выбрать файл', enable_events=True, key='-OPEN PICTURE-', font='Helvetica 16')],
                    [sg.Text('Здесь появится результат', key='-RESULT 3-', font='Helvetica 20')]  
                    ]
        # что будет внутри окна следующего окна
        next_layout = []
        # Разметка вкладок
        layout =[[sg.TabGroup([[  sg.Tab('Массовой конвертер', convert_layout),
                                  sg.Tab('Буферный калькулятор', buffer_layout),
                                  sg.Tab('Фармакокинетика (В разработке)', PK_layout),
                                  sg.Tab('Координаты (В разработке)', coordinates_layout),
                                  sg.Tab('В разработке', next_layout)]], key='-TAB GROUP-', expand_x=True, expand_y=True),
               ]]

        # рисуем окно, название и вкладки
        window = sg.Window('Ageldinov', layout)
        # запускаем основной бесконечный цикл
        while True:
                # получаем события, произошедшие в окне
                event, values = window.read()
                # если нажали на крестик
                if event in (sg.WIN_CLOSED, 'Exit'):
                        # выходим из цикла
                        break
                # если нажали на кнопку конвертации
                if event == '-CAlCULATE 1-':
                    if str(values['-AMOUNT-']) == '':
                        sg.popup("Ошибка ввода данных")
                    else:
                        # запускаем связанную функцию
                        convertation.update(values, window)
                # если нажали на кнопку буферов
                elif event == '-CAlCULATE 2-':
                    if str(values['-FORMULA IN-']) == '' or str(values['-CONCENTRATION IN-']) == '' or str(values['-VOLUME IN-']) == '':
                        sg.popup("Ошибка ввода данных")
                    else:
                        # запускаем связанную функцию
                        buffer_calculation.buff(values, window)
                elif event == '-FUNCTION3-':
                    folder_or_file = sg.popup_get_file('Выберите файд с данными', keep_on_top=True)
                    if str(folder_or_file) == '':
                        sg.popup("Вы выбрали: " + str(folder_or_file), keep_on_top=True)
                elif event == '-FUNCTION5-':
                        sg.popup('D = Доза \nt = Интервал дозирования \nCL = Клиренс \nVd = Объем распределения \nke = Константа скорости элюминации \nka = Константа скорости абсорбции \nF = Абсорбировшаяся фракция (Биодоступность) \nK0 = Скорость инфузии \nT = Продолжительность инфузии \nC = Концентрация в плазме', font='Helvetica 14')
                elif event == '-FUNCTION4-':
                      # запускаем связанную функцию
                    PK_calculation.PK_cal(values)
                elif event == '-OPEN PICTURE-':
                    if str(values['-X END IN-']) == '' or str(values['-Y END IN-']) == '':
                        sg.popup("Ошибка ввода данных")
                    else:
                        picture = sg.popup_get_file('Выберите изображение с данными', keep_on_top=True)
                        if str(picture) != '':
                            points_coordinates.coordinates(values,window,picture)

        # закрываем окно и освобождаем используемые ресурсы

        window.close()

# На случай дополнений и запуск основной функции
if __name__ == '__main__':
        main()
        convertation
        buffer_calculation
        points_coordinates