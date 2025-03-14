#! pip install nuitka
#* python -m nuitka --windows-disable-console --windows-icon-from-ico=rezis.ico --enable-plugin=tk-inter rezistor.py
import tkinter as tk
from tkinter import ttk, messagebox

global cod_col, cod_tol

cod_col = []
cod_tol = ''

mycolors = ['black', 'coral4', 'red', 'DarkOrange', 'yellow', 'green', 'blue', 'purple1', 'grey', 'white']
tolercol = ['silver', 'gold2', 'brown', 'green', 'violet']
tolerance = ['±10 %', '±5 %', '± 1%','±0.5%', '±0.1%']

def set_sel_color(selcolor='white'):
    col = str(selcolor)
    #print(mycolors.index(col), col)
    cod_col.append(mycolors.index(col))
    lable_rez.configure(text=f'{cod_col}')


def oncol_click(event):
    set_sel_color(selcolor=event.widget.cget('background'))


def set_sel_color_tol(selcolor='white'):
    global cod_tol
    col = str(selcolor)
    codd = tolercol.index(col)
    cod_tol = tolerance[codd]
    #print(tolercol.index(col), col, cod_tol)
    lable_rez.configure(text=f'{cod_col} {cod_tol}')

def oncolt_click(event):
    set_sel_color_tol(selcolor=event.widget.cget('background'))

def on_start():
    global cod_col, cod_tol

    if len(cod_col) < 3:
        messagebox.showwarning(title='Внимание', message='Выбрано меньше 3-х цветов\nТребуется выбрать 2 или 3 цвета номинала\nи цвет множителя\nДопуск смотрим в ряду ниже')
    if len(cod_col) > 4:
        messagebox.showwarning(title='Внимание', message='Выбрано больше 4-х цветов\nТребуется выбрать 2 или 3 цвета номинала\nи цвет множителя\nДопуск смотрим в ряду ниже')
    if len(cod_col) == 3:
        rezik = int((cod_col[0] * 10 + cod_col[1]) * (10 ** cod_col[2]))
        krezik = rezik / 1000
        lable_rez.configure(text=f'{rezik} Ω or {krezik} kΩ {cod_tol}')
    if len(cod_col) == 4:
        rezik = int((cod_col[0] * 100 + cod_col[1] * 10 + cod_col[2]) * (10 ** cod_col[3]))
        krezik = rezik / 1000
        lable_rez.configure(text=f'{rezik} Ω or {krezik} kΩ {cod_tol}')
    cod_col = []
    cod_tol = ''


win = tk.Tk()
win.title('Resistor with Color Bands')
photos = tk.PhotoImage(file='rezis.png')
win.iconphoto(False, photos)
w_width = 400
w_height = 400
s_width = win.winfo_screenwidth()
s_height = win.winfo_screenheight()
x = (s_width / 2) - (w_width / 2)
y = (s_height / 2) - (w_height / 2)
win.geometry(f"{w_width}x{w_height}+{int(x)}+{int(y)}")

dataframe = ttk.Frame(win)
button_on = ttk.Button(dataframe, text='Определить', command=on_start)
button_on.grid(row=0, column=0, padx=5, pady=2, sticky='nw')
lable_rez = ttk.Label(dataframe, text=' 0,00 kΩ ')
lable_rez.grid(row=0, column=1, columnspan=2, padx=15, pady=2, sticky='news')
button_off = ttk.Button(dataframe, text='Выход', command=win.destroy)
button_off.grid(row=0, column=3, padx=5, pady=2, sticky='ne')
dataframe.pack(padx=10, pady=5)

colorframe = ttk.Frame(win, height=15)
nominal = ttk.Label(colorframe, text='Выбор номинала и множителя', justify='center', foreground='blue')
nominal.grid(row=0, column=2, columnspan=6, padx=1, pady=2, sticky='wens')
icolor = 0
icol = 0
for icolor in mycolors:
    colpick = ttk.Label(colorframe, width=3, padding=3, relief=tk.RIDGE, background=icolor)
    colpick.grid(row=1, column=icol,padx=1, pady=1, sticky='wens')
    colpick.bind('<Button-1>', oncol_click)
    icol += 1
colorframe.pack(padx=10, pady=5)

tolerframe = ttk.Frame(win, height=10)
dopusk = ttk.Label(tolerframe, text='Допуск, отклонение от номинала, ± %', justify='center', foreground='blue')
dopusk.grid(row=0, column=0, columnspan=5, padx=1, pady=2, sticky='we')
icolor = 0
icol = 0
for icolor in tolercol:
    colpickt = ttk.Label(tolerframe, text=f'{tolerance[icol]}', justify='center', width=6, padding=1, relief=tk.RIDGE, background=icolor)
    colpickt.grid(row=1, column=icol, padx=1, pady=1, sticky='wens')
    colpickt.bind('<Button-1>', oncolt_click)
    icol += 1
tolerframe.pack(padx=10, pady=5)

imgframe = ttk.Frame(win)
img_rez = tk.PhotoImage(file="photo.png")
imglabel = ttk.Label(imgframe, image=img_rez, justify='center')
imglabel.grid(row=0, column=0, sticky='news')
imgframe.pack(padx=5, pady=10)


win.mainloop()