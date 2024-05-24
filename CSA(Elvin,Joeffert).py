import tkinter as tk
from tkinter import ttk, messagebox

class ConferenceScheduler(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("PARES NI DIWATA CONFERENCE SCHEDULING APPLICATION ")
        self.geometry("600x400")
        self.configure(bg="pink")

        self.create_widgets()

    def create_widgets(self):
        # Title Label
        title_label = tk.Label(self, text="DIWATA PARES CONFERENCE SCHEDULING APPLICATION", font=("Helvetica", 16, "bold"), bg="pink", fg="#00008b")
        title_label.pack(pady=10)

        # Form Frame
        form_frame = tk.Frame(self, bg="#f0f8ff")
        form_frame.pack(pady=20)

        # Conference Name
        name_label = tk.Label(form_frame, text="Conference Name:", font=("Helvetica", 12), bg="pink")
        name_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")
        self.name_entry = tk.Entry(form_frame, font=("Helvetica", 12), width=30)
        self.name_entry.grid(row=0, column=1, padx=10, pady=5)

        # Date
        date_label = tk.Label(form_frame, text="Date (YYYY-MM-DD):", font=("Helvetica", 12), bg="pink")
        date_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.date_entry = tk.Entry(form_frame, font=("Helvetica", 12), width=30)
        self.date_entry.grid(row=1, column=1, padx=10, pady=5)

        # Time
        time_label = tk.Label(form_frame, text="Time (HH:MM):", font=("Helvetica", 12), bg="pink")
        time_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.time_entry = tk.Entry(form_frame, font=("Helvetica", 12), width=30)
        self.time_entry.grid(row=2, column=1, padx=10, pady=5)

        # Location
        location_label = tk.Label(form_frame, text="Location:", font=("Helvetica", 12), bg="pink")
        location_label.grid(row=3, column=0, padx=10, pady=5, sticky="e")
        self.location_entry = tk.Entry(form_frame, font=("Helvetica", 12), width=30)
        self.location_entry.grid(row=3, column=1, padx=10, pady=5)

        # Add Button
        add_button = ttk.Button(form_frame, text="Add Conference", command=self.add_conference)
        add_button.grid(row=4, columnspan=2, pady=10)

        # Listbox Frame
        listbox_frame = tk.Frame(self, bg="pink")
        listbox_frame.pack(pady=10)

        # Conferences Listbox
        self.conferences_listbox = tk.Listbox(listbox_frame, font=("Helvetica", 12), width=50, height=10)
        self.conferences_listbox.pack(side="left", padx=10)

        # Scrollbar for Listbox
        scrollbar = tk.Scrollbar(listbox_frame, orient="vertical")
        scrollbar.config(command=self.conferences_listbox.yview)
        self.conferences_listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y")

    def add_conference(self):
        name = self.name_entry.get()
        date = self.date_entry.get()
        time = self.time_entry.get()
        location = self.location_entry.get()

        if name and date and time and location:
            conference_info = f"{date} {time} - {name} @ {location}"
            self.conferences_listbox.insert(tk.END, conference_info)
            self.clear_entries()
        else:
            messagebox.showwarning("Input Error", "All fields must be filled out")

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.date_entry.delete(0, tk.END)
        self.time_entry.delete(0, tk.END)
        self.location_entry.delete(0, tk.END)

if __name__ == "__main__":
    app = ConferenceScheduler()
    app.mainloop()
