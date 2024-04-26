# import tkinter
#
# window = tkinter.Tk()
#
# button = tkinter.Button(window, text="Click Me!")
# button.pack()
#
# window.mainloop()


# from tkinter import messagebox
# import tkinter
#
# button = messagebox.showwarning("Warning", "Warning.")


import tkinter

root = tkinter.Tk()

canvas1 = tkinter.Canvas(root, width=400, height=300, relief='raised')
canvas1.pack()
canvas2 = tkinter.Canvas(root)
canvas2.pack()

prompt_label = tkinter.Label(root, text='Enter distance in Kilometers: ')
prompt_label.config(font=('helvetica', 14))
canvas1.create_window(200, 25, window=prompt_label)

entry = tkinter.Entry(canvas1, width=10)

prompt_label.pack(side='left')
entry.pack(side='left')


def convert():
    kilo = float(entry.get())
    miles = kilo * 0.62
    label4 = tkinter.Label(bottom_frame, 'str(kilo) + "kilometers is equal to" + str(miles) + "miles"')
    root.create_window(200, 230, window=label4)

calc_button = tkinter.Button(bottom_frame, text='Convert', command=convert)
quit_button = tkinter.Button(bottom_frame, text='Quit', command=root.destroy)

button1 = tkinter.Button(text='Convert', command=convert)



root.mainloop()
