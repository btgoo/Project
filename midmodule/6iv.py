import tkinter as tk


class GUIApplication:
    def __init__(self, master):
        self.master = master
        master.title("Simple GUI Application")

        self.label = tk.Label(master, text="Hello, tkinter!")
        self.label.pack()

        self.button = tk.Button(master, text="Enter your name and click me", command=self.on_button_click)
        self.button.pack()

        self.entry = tk.Entry()
        self.entry.pack()

    def on_button_click(self):
        self.label.config(text="Hello, " + self.entry.get() + "!")

if __name__ == "__main__":
    root = tk.Tk()
    app = GUIApplication(root)
    root.mainloop()