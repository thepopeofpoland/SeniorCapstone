import tkinter
from tkinter import ttk
import main


class App(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        master.title('Vacation Property Date Requests')
        self.grid(row=0, column=0)
        self.create_widgets()

    def create_widgets(self):
        # creates a window to see the families in the DB
        self.text = tkinter.Text(self, width=28, height=5)
        self.text.grid(row=4, column=0)
        # make read only
        self.text.config(state=tkinter.DISABLED)

        # creates a window to see the reserved dates in the DB
        self.calendar = tkinter.Text(self, width=28, height=5)
        self.calendar.grid(row=4, column=1)
        # make read only
        self.calendar.config(state=tkinter.DISABLED)

        self.overlap_field = tkinter.Text(self, width=28, height=5)
        self.overlap_field.grid(row=4, column=2)
        self.overlap_field.config(state=tkinter.DISABLED)

        # below creates the labels for the family data window and calendar window
        text_label = ttk.Label(self, text="Family data")
        text_label.grid(row=5, column=0)
        calendar_label = ttk.Label(self, text="Reserved dates")
        calendar_label.grid(row=5, column=1)

        # below are the input text fields
        self.fam_entry = tkinter.Entry(self, width=28)
        self.fam_entry.grid(row=0, column=0, padx=5, pady=5)
        self.fam_entry.insert(0, "surname, number of members")
        self.fam_entry.bind('<Return>', lambda event: self.add_family_data())

        self.fam_mod = tkinter.Entry(self, width=28)
        self.fam_mod.grid(row=0, column=1, padx=5, pady=5)
        self.fam_mod.insert(0, "Updated number of members")

        self.reserve_date = tkinter.Entry(self, width=20)
        self.reserve_date.grid(row=0, column=2, padx=5, pady=5)
        self.reserve_date.insert(0, "Date to reserve")

        self.res_name = tkinter.Entry(self, width=20)
        self.res_name.grid(row=0, column=3, padx=5, pady=5)
        self.res_name.insert(0, "Reservation name")

        self.delete_date = tkinter.Entry(self, width=20)
        self.delete_date.grid(row=0, column=4, padx=5, pady=5)
        self.delete_date.insert(0, "date to delete")

        # input field label
        date_label = ttk.Label(self, text="Date format is mm/dd/yyy")
        date_label.grid(row=2, column=2)
        check_label = ttk.Label(self, text="Conflicting dates")
        check_label.grid(row=5, column=2)

        # below are the buttons
        self.add_family = ttk.Button(self, text="Add Family", command=self.add_family_data)
        self.add_family.grid(row=1, column=0)

        self.fam_mod_button = ttk.Button(self, text="Update Family", command=self.update_family)
        self.fam_mod_button.grid(row=1, column=1)

        self.reservation_button = ttk.Button(self, text="Reserve Date", command=self.add_date)
        self.reservation_button.grid(row=1, column=2)

        self.delete_button = ttk.Button(self, text="Delete Reservation Date", command=self.remove_date)
        self.delete_button.grid(row=1, column=4)

        self.list_button = ttk.Button(self, text="List Families", command=self.list_data)
        self.list_button.grid(row=6, column=0)

        self.list_cal_button = ttk.Button(self, text="List Dates", command=self.list_cal_data)
        self.list_cal_button.grid(row=6, column=1)

    def list_data(self):
        data = main.list_data()
        # below re-enables the text box to let it be written to then clears it, then adds the text, then
        # re-locks the box to prevent writing.
        self.text.config(state=tkinter.NORMAL)
        self.text.delete('1.0', tkinter.END)
        # below inserts into the text box
        self.text.insert(tkinter.INSERT, data)
        self.text.config(state=tkinter.DISABLED)

    def list_cal_data(self):
        data = main.list_cal_dates()
        self.calendar.config(state=tkinter.NORMAL)
        self.calendar.delete('1.0', tkinter.END)
        # below inserts into the text box
        self.calendar.insert(tkinter.INSERT, data)
        self.calendar.config(state=tkinter.DISABLED)

    def add_family_data(self):
        text = self.fam_entry.get()
        surname, family_members = text.split(',')
        main.add_family(surname, family_members)
        self.list_data()

    def add_date(self):
        date = self.reserve_date.get()
        name = self.res_name.get()
        #main.conflict_check(date)
        main.add_reservation(date, name)
        data = main.list_cal_dates()
        self.calendar.config(state=tkinter.NORMAL)
        self.calendar.delete('1.0', tkinter.END)
        self.calendar.insert(tkinter.INSERT, data)
        self.calendar.config(state=tkinter.DISABLED)

        # self.overlap_field.config(state=tkinter.NORMAL)
        # self.overlap_field.delete('1.0', tkinter.END)
        # self.overlap_field.insert(tkinter.INSERT, data)
        # self.overlap_field.config(state=tkinter.DISABLED)

    # modify the input fields to just be a name field, a number field, and a date field.
    def update_family(self):
        pass
        # integer = self.fam_mod.get()
        # # name = self.
        # main.update_family(integer)
        # self.list_data()

    def remove_date(self):
        date = self.delete_date.get()
        name = self.res_name.get()
        main.remove_date(date, name)


if __name__ == "__main__":
    root = tkinter.Tk()
    app = App(master=root)
    root.mainloop()
