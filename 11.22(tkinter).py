# import tkinter
#
# root = tkinter.Tk()
#
# top_frame = tkinter.Frame(root)
# bottom_frame = tkinter.Frame(root)
#
# label1 = tkinter.Label(top_frame, text="Winken")
# label2 = tkinter.Label(top_frame, text="Blinken")
# label3 = tkinter.Label(top_frame, text="Nod")
#
# label1.pack(side='top')
# label2.pack(side='top')
# label3.pack(side='top')
#
# label4 = tkinter.Label(bottom_frame, text="Winken")
# label5 = tkinter.Label(bottom_frame, text="Blinken")
# label6 = tkinter.Label(bottom_frame, text="Nod")
#
# label4.pack(side='left')
# label5.pack(side='left')
# label6.pack(side='left')
#
# top_frame.pack(ipady=10)
# bottom_frame.pack(pady=10, padx=10)
#
# tkinter.mainloop()

import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("To-Do List Application")

# Add widgets here (labels, entry widgets, buttons, etc.)
main_window = tk.Tk()
label = tk.Label(text="Hello")

# Run the main loop
window.mainloop()

