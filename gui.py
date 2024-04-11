import tkinter
from tkcalendar import Calendar

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
        self.family_name = tkinter.Entry(self, width=28)
        self.family_name.grid(row=0, column=0, padx=5, pady=5)
        self.family_name.insert(0, "Surname")
        self.family_name.bind('<Return>', lambda event: self.add_family_data())

        self.fam_mod = tkinter.Entry(self, width=28)
        self.fam_mod.grid(row=0, column=1, padx=5, pady=5)
        self.fam_mod.insert(0, "Number of members")

        self.reserve_date = tkinter.Entry(self, width=20)
        self.reserve_date.grid(row=0, column=2, padx=5, pady=5)
        self.reserve_date.insert(0, "Date to reserve")

        self.delete_date = tkinter.Entry(self, width=20)
        self.delete_date.grid(row=0, column=4, padx=5, pady=5)
        self.delete_date.insert(0, "Date to delete")

        # input field label
        date_label = ttk.Label(self, text="Date format is yyyy-mm-dd")
        date_label.grid(row=2, column=2)
        check_label = ttk.Label(self, text="Conflicting dates")
        check_label.grid(row=5, column=2)

        # below are the buttons
        add_family = ttk.Button(self, text="Add Family", command=self.add_family_data)
        add_family.grid(row=1, column=0)

        self.fam_mod_button = ttk.Button(self, text="Update Family", command=self.update_family)
        self.fam_mod_button.grid(row=1, column=1)

        reservation_button = ttk.Button(self, text="Reserve Date", command=self.add_date)
        reservation_button.grid(row=1, column=2)

        delete_button = ttk.Button(self, text="Delete Reservation Date", command=self.remove_date)
        delete_button.grid(row=1, column=4)

        list_button = ttk.Button(self, text="List Families", command=self.list_data)
        list_button.grid(row=6, column=0)

        list_cal_button = ttk.Button(self, text="List Dates", command=self.list_cal_data)
        list_cal_button.grid(row=6, column=1)

    def list_data(self):
        data = main.list_data()
        self.text.config(state=tkinter.NORMAL)
        self.text.delete('1.0', tkinter.END)
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
        surname = self.family_name.get()
        family_members = self.fam_mod.get()
        main.add_family(surname, family_members)
        self.list_data()

    def add_date(self):
        date = self.reserve_date.get()
        name = self.family_name.get()
        check_date = main.conflict_check(date)

        if check_date:
            test = main.find_conflicts(date)

            self.overlap_field.config(state=tkinter.NORMAL)
            self.overlap_field.delete('1.0', tkinter.END)
            self.overlap_field.insert(tkinter.INSERT, test)
            self.overlap_field.config(state=tkinter.DISABLED)

        else:
            main.add_reservation(date, name)
            data = main.list_cal_dates()

            self.calendar.config(state=tkinter.NORMAL)
            self.calendar.delete('1.0', tkinter.END)
            self.calendar.insert(tkinter.INSERT, data)
            self.calendar.config(state=tkinter.DISABLED)

    def update_family(self):
        family_members = self.fam_mod.get()
        family_members = int(family_members)
        name = self.family_name.get()
        print(name)
        main.update_family(family_members, name)
        self.list_data()
        data = main.list_data()
        self.text.config(state=tkinter.NORMAL)
        self.text.delete('1.0', tkinter.END)
        self.text.insert(tkinter.INSERT, data)
        self.text.config(state=tkinter.DISABLED)

    def remove_date(self):
        date = self.delete_date.get()
        name = self.family_name.get()
        main.remove_date(date, name)
        data = main.list_cal_dates()
        self.calendar.config(state=tkinter.NORMAL)
        self.calendar.delete('1.0', tkinter.END)
        self.calendar.insert(tkinter.INSERT, data)
        self.calendar.config(state=tkinter.DISABLED)


if __name__ == "__main__":
    root = tkinter.Tk()
    app = App(master=root)
    root.mainloop()
