import tkinter as tk

class YourGUIApplication(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Your GUI Application")
        self.pack()

        self.label = tk.Label(self, text="Click Me")
        self.label.pack()

        self.button = tk.Button(self, text="Click", command=self.on_button_click)
        self.button.pack()

    def on_button_click(self):
        print("Button clicked!")

if __name__ == "__main__":
    root = tk.Tk()
    app = YourGUIApplication(master=root)
    root.mainloop()