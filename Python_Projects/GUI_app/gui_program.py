from tkinter import *
       

root = Tk()     # создаем корневой объект - окно
root.title("ЕГЭ Информатика")     # устанавливаем заголовок окна
root.geometry("300x250")    # устанавливаем размеры окна
label = Label(text="Выбери номер задания") # создаем текстовую метку
label.grid(row=0, column=0, columnspan=3)
 
btn01 = Button(text="№1") # command=open_no01) # создаем кнопку из пакета tkinter
btn01.grid(row=1, column=0) # позиция на сетке


root.mainloop()