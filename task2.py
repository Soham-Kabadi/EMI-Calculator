from tkinter import *
from tkinter.messagebox import *
from pyrebase import *

firebaseConfig = {
  	"apiKey": "AIzaSyDcCofjsVu4Cifi3OBcbSTGfIrrm_PKY3Q",
  	"authDomain": "emi-4a5de.firebaseapp.com",
  	"databaseURL": "https://emi-4a5de-default-rtdb.firebaseio.com",
  	"projectId": "emi-4a5de",
  	"storageBucket": "emi-4a5de.appspot.com",
  	"messagingSenderId": "89774150771",
  	"appId": "1:89774150771:web:59936428d48ed979e0c606"
}
fb = initialize_app(firebaseConfig)
db = fb.database()


def calculate_emi():
    amount = amount_entry.get().strip()
    tenure = tenure_entry.get().strip()
    rate = rate_entry.get().strip()

    if not (amount and tenure and rate):
        showerror("Error", "Please enter vaild values in  fields.")
        return

    try:
        amount = float(amount)
        tenure = int(tenure)
        rate = float(rate)
        
        if amount <= 0 or tenure <= 0 or rate <= 0:
            showerror("Error", "Please enter positive values in  fields.")
            return
        
        r = rate / 100 / 12
        n = tenure * 12
        emi = (amount * r * (pow(1 + r, n))) / (pow(1 + r, n) - 1)

        emi_label.config(text=f"EMI: {emi:.2f}")
        info = {"Amount": amount, "Tenure": tenure, "Rate": rate, "EMI": emi}
        db.child("EMI Calculator").push(info)
        showinfo("Success", "EMI calculated successfully.")

        amount_entry.delete(0, END)
        tenure_entry.delete(0, END)
        rate_entry.delete(0, END)
        amount_entry.focus()

    except ValueError:
        showerror("Error", "Please enter valid numeric values for in fields.")

root = Tk()
root.title("EMI Calculator")
root.geometry("800x500+50+50")
f = ("Times New Roman", 20, "bold")

title_label = Label(root, text="EMI Calcluator", font= f)
title_label.place(x=250, y =30)
amount_label = Label(root, text="Loan Amount (₹):",font=f)
amount_entry = Entry(root, font=f)
amount_label.place(x = 100, y=100)
amount_entry.place(x = 400, y=100)

tenure_label = Label(root, text="Loan Tenure (Yrs):", font=f)
tenure_entry = Entry(root, font=f)
tenure_label.place(x = 100, y=150)
tenure_entry.place(x = 400, y=150)

rate_label = Label(root, text="Interest Rate (%):", font=f)
rate_entry = Entry(root, font=f)
rate_label.place(x = 100, y=200)
rate_entry.place(x = 400, y=200)

calculate_button = Button(root, text="Calculate EMI", font=f, command=calculate_emi)
calculate_button.place(x=250, y =250)

emi_label = Label(root, text="", font=f)
emi_label.place(x=250, y =350) 
emi_entry = Entry(root, font=f)


root.mainloop()