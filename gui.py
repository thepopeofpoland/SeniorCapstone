import tkinter
from tkinter import font, messagebox
from tkcalendar import Calendar
import datetime

from tkinter import ttk
import core


class App(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.calendar = None
        master.title('Vacation Property Date Requests')
        self.defaultFont = font.nametofont("TkDefaultFont")
        self.defaultFont.configure(family="Helvetica", size=12)
        self.grid(row=0, column=0)
        self.create_widgets()
        self.list_cal_data()

    def create_widgets(self):
        # Text field creation and
        self.family_text = tkinter.Text(self, width=30, height=15)
        self.family_text.grid(row=6, column=1, columnspan=2)
        self.family_text.config(state=tkinter.DISABLED, font=font.Font(family='Helvetica', size=12))

        self.fault_field = tkinter.Text(self, width=80, height=1)
        self.fault_field.grid(row=4, column=0, columnspan=3)
        self.fault_field.insert(tkinter.INSERT, "Fault Field")
        self.fault_field.tag_configure("center", justify="center")
        self.fault_field.tag_add("center", "1.0", "end")
        self.fault_field.config(state=tkinter.DISABLED, font=font.Font(family='Helvetica', size=12))

        # below creates the labels for the reservation window and calendar
        text_label = ttk.Label(self, text="Who has Reservations for Selected Date",
                               font=font.Font(family='Helvetica', size=12))
        text_label.grid(row=5, column=1, columnspan=2)
        calendar_label = ttk.Label(self, text="Reservation Calendar", font=font.Font(family='Helvetica', size=12))
        calendar_label.grid(row=5, column=0)

        # below are the input text fields and functions to delete the default text.
        def surname_delete_on_click(event):
            if self.family_name.get() == "Surname for Reservations":
                self.family_name.delete(0, tkinter.END)
                self.family_name.configure(foreground="black")

        def num_mem_delete_on_click(event):
            if self.fam_mod.get() == "Number of Members in Family":
                self.fam_mod.delete(0, tkinter.END)
                self.fam_mod.configure(foreground="black")

        self.family_name = tkinter.Entry(self, width=25, font=('Helvetica', 12), justify="center")
        self.family_name.grid(row=0, column=0, padx=5, pady=5)
        self.family_name.insert(0, "Surname for Reservations")

        self.family_name.bind("<FocusIn>", surname_delete_on_click)
        self.family_name.bind('<Return>', lambda event: self.add_family_data())

        self.fam_mod = tkinter.Entry(self, width=28, font=('Helvetica', 12), justify="center")
        self.fam_mod.grid(row=0, column=1, padx=5, pady=5)
        self.fam_mod.bind("<FocusIn>", num_mem_delete_on_click)
        self.fam_mod.insert(0, "Number of Members in Family")

        # Custom button styling and button creation.
        s = ttk.Style()
        s.configure('my.TButton', font=('Helvetica', 12))

        add_family = ttk.Button(self, text="Add Family", style='my.TButton', command=self.add_family_data)
        add_family.grid(row=2, column=0)

        fam_mod_button = ttk.Button(self, text="Update Family", style='my.TButton', command=self.update_family)
        fam_mod_button.grid(row=2, column=1)

        reservation_button = ttk.Button(self, text="Reserve Date", style='my.TButton', command=self.create_event)
        reservation_button.grid(row=3, column=0)

        delete_button = ttk.Button(self, text="Delete Reservation Date", style='my.TButton', command=self.remove_date)
        delete_button.grid(row=3, column=1)

        # creating the calendar
        self.reservation_calendar = Calendar(self, selectmode='day', font=('Helvetica', 18))
        self.reservation_calendar.grid(row=6, column=0, padx=5, pady=5)

        self.reservation_calendar.bind("<<CalendarSelected>>", self.display_selected_date_name)

    @staticmethod
    def get_event_names(event_date):
        """This function returns a list of all the names for the selected date on the calendar."""
        events = core.list_cal_dates()
        matching_names = []
        for event_date_str, event_name in events:
            if event_date_str == event_date.strftime('%Y-%m-%d'):
                matching_names.append(event_name)
        if matching_names:
            return ", ".join(matching_names)
        else:
            return "No Reservation Today"

    def display_selected_date_name(self, event):
        """This function uses the above get_event_names function to get names to print to a text field to show the
        names for a selected date."""
        selected_date = self.reservation_calendar.selection_get()
        event_name = self.get_event_names(selected_date)
        self.family_text.config(state=tkinter.NORMAL)
        self.family_text.delete('1.0', tkinter.END)
        self.family_text.insert(tkinter.INSERT, event_name)
        self.family_text.config(state=tkinter.DISABLED)

    def list_cal_data(self):
        """This function calls to core's list_cal_dates() to get all the dates available in the calendar,
        and then prints it to the calendar."""
        events = core.list_cal_dates()

        # Clear existing events from the calendar
        for event_id in self.reservation_calendar.get_calevents():
            self.reservation_calendar.calevent_remove(event_id)

        # Add parsed events to the calendar
        for event_date_tuple in events:
            try:
                event_date_str, event_name = event_date_tuple
                date_obj = datetime.datetime.strptime(event_date_str, "%Y-%m-%d").date()
                self.reservation_calendar.calevent_create(date_obj, event_name, 'custom')
            except (ValueError, IndexError) as e:
                print("Error parsing date:", e)

    def add_family_data(self):
        """This function calls to core's add_family_data() function to add a family to the database."""
        surname = self.family_name.get()
        family_members = int(self.fam_mod.get())
        core.add_family(surname, family_members)

    def update_family(self):
        """This function calls to core's update_family() function to update a family's number of members in the
        database."""
        family_members = self.fam_mod.get()
        name = self.family_name.get()
        core.update_family(family_members, name)

    def create_event(self):
        """This function calls to core's create_event() function to create a new event in the database. It also
        checks if there is a conflict and then gives the user the option to or not to create the reservation."""
        selected_date = self.reservation_calendar.selection_get()
        selected_date_str = selected_date.strftime('%Y-%m-%d')
        family_name = self.family_name.get()
        self.reservation_calendar.calevent_create(selected_date, family_name, tags="")
        check_date = core.conflict_check(selected_date_str)

        if check_date:
            # Ask the user if they want to proceed despite the conflicts
            user_decision = tkinter.messagebox.askyesno("Conflict Detected",
                                                        "Conflicts have been detected. Do you want to proceed with "
                                                        "the event creation?")

            if user_decision:
                # If the user chooses to proceed, add the event despite conflicts
                test = core.add_reservation(selected_date_str, family_name)
                self.fault_field.config(state=tkinter.NORMAL)
                self.fault_field.delete('1.0', tkinter.END)
                self.fault_field.insert(tkinter.INSERT, test)
                self.fault_field.tag_configure("center", justify="center")
                self.fault_field.tag_add("center", "1.0", "end")
                self.fault_field.config(state=tkinter.DISABLED)

                self.list_cal_data()

        else:
            test = core.add_reservation(selected_date_str, family_name)
            self.fault_field.config(state=tkinter.NORMAL)
            self.fault_field.delete('1.0', tkinter.END)
            self.fault_field.insert(tkinter.INSERT, test)
            self.fault_field.config(state=tkinter.DISABLED)

            self.list_cal_data()

    def remove_date(self):
        """This function removes a date from the database."""
        date = self.reservation_calendar.selection_get()
        selected_date_str = date.strftime('%Y-%m-%d')
        name = self.family_name.get()
        test = core.remove_date(selected_date_str, name)
        self.fault_field.config(state=tkinter.NORMAL)
        self.fault_field.delete('1.0', tkinter.END)
        self.fault_field.insert(tkinter.INSERT, test)
        self.fault_field.config(state=tkinter.DISABLED)

        self.list_cal_data()


if __name__ == "__main__":
    root = tkinter.Tk()
    app = App(master=root)
    root.mainloop()
