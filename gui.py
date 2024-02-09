import tkinter
from tkinter import ttk
from tkinter import scrolledtext
import home

"""the frame is what is in the window, but not the ribbon on top an bottom and design of the window surround"""


class App(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        master.title('Vacation Property Requests')
        self.grid(row=0, column=0)
        self.create_widgets()

    def create_widgets(self):
        self.text = scrolledtext.ScrolledText(self)
        self.text.grid(row=0, column=0)
        # make read only
        self.text.config(state=tkinter.DISABLED)

        text_label = ttk.Label(self, text="Data")
        text_label.grid(row=4, column=0)

        self.list_button = ttk.Button(self, text="List", command=self.list_data)
        self.list_button.grid(row=0, column=1)


        self.entry = tkinter.Entry(self, width=30)
        self.entry.grid(row=5, column=0)
        self.entry.insert(0,"location, weather, ice depth")
        self.entry.bind('<Return>', lambda event: self.add_data())

    def list_data(self):
        data = home.list_data()
        #below is a "list comprehension" does the same as calling an array then appending something to the array
        text = '\n'.join(f"{key}: {values}" for key, values in data.items())

        # below re-enables the text box to let it be written to then clears it, then adds the text, then
        # re-locks the box to prevent writing.
        self.text.config(state=tkinter.NORMAL)
        self.text.delete('1.0', tkinter.END)
        self.text.insert(tkinter.INSERT, text)
        self.text.config(state=tkinter.DISABLED)

    def add_data(self):
        text = self.entry.get()
        location, weather, ice_depth = text.split(',')
        home.add_entry(location, weather, ice_depth)
        self.list_data()

if __name__ == "__main__":
    root = tkinter.Tk()
    app = App(master=root)
    root.mainloop()
