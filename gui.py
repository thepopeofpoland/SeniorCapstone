import tkinter
from tkinter import ttk
from tkinter import scrolledtext
import home

"""the frame is what is in the window, but not the ribbon on top an bottom and design of the window surround"""


class App(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        master.title('Vacation Property Date Requests')
        self.grid(row=0, column=0)
        self.create_widgets()

    def create_widgets(self):
        self.text = scrolledtext.ScrolledText(self)
        self.text.grid(row=2, column=0)
        # make read only
        self.text.config(state=tkinter.DISABLED)

        text_label = ttk.Label(self, text="Data")
        text_label.grid(row=3, column=0)

        # below are the buttons
        self.add_family =ttk.Button(self, text="Add Family", command=self.add_data)
        self.add_family.grid(row=1, column=0)

        self.list_button = ttk.Button(self, text="List", command=self.list_data)
        self.list_button.grid(row=2, column=1)

        self.fam_mod_button = ttk.Button(self, text="Update Family", command=self.update_family)
        self.fam_mod_button.grid(row=1, column=1)

        # self.save_button = ttk.Button(self, text="Save", command=self.save())
        # self.save_button.grid(row=1, column=2)

        # below are the input text fields
        self.fam_entry = tkinter.Entry(self, width=30)
        self.fam_entry.grid(row=0, column=0)
        self.fam_entry.insert(0, "sir name, number of members")
        self.fam_entry.bind('<Return>', lambda event: self.add_data())

        self.fam_mod = tkinter.Entry(self, width=30)
        self.fam_mod.grid(row=0, column=1)
        self.fam_mod.insert(0, "Updated number of members")

    def list_data(self):
        data = home.list_data()
        # below is a "list comprehension" does the same as calling an array then appending something to the array
        text = '\n'.join(f"{key}: {values}" for key, values in data.items())

        # below re-enables the text box to let it be written to then clears it, then adds the text, then
        # re-locks the box to prevent writing.
        self.text.config(state=tkinter.NORMAL)
        self.text.delete('1.0', tkinter.END)
        self.text.insert(tkinter.INSERT, text)
        self.text.config(state=tkinter.DISABLED)

    def add_data(self):
        text = self.fam_entry.get()
        sir_name, family_members = text.split(',')
        home.add_family(sir_name, family_members)
        self.list_data()

    def update_family(self):
        text = self.fam_mod.get()
        family_members = text.split(',')
        print(family_members)
        #home.update_family(family_members)
        self.list_data()

    def clear_data(self):
        home.clear_data()

    def load_data(self):
        data = home.load()

    def save_data(self):
        home.save()

if __name__ == "__main__":
    root = tkinter.Tk()
    app = App(master=root)
    root.mainloop()
