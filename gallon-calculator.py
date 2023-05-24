from tkinter import *   #COMPETENCY(Utilize basic and advanced Graphical User Interface (GUI) Components.)
from tkinter import messagebox
from tkinter import ttk




tanks_saved = {}  # COMPETENCY(array processing), by using a dictionary for storing tank gallon amount and its dimensions
current_tank_info = None
current_tank_gallons = None
gallon_capacity = None
current_length = None
current_height = None
current_width = None
number_tanks_saved = 0



root= Tk()

style = ttk.Style(root)
style.theme_use("xpnative")




# function that calculates total gallons given user entries
def calculate_gallons():

    #  COMPETENCY(error handling) if statement, checks that all entries are filled out & that all entries are numbers over 0  
    if len(length_entry.get()) == 0 or len(height_entry.get()) == 0 or len(width_entry.get()) == 0:  #COMPETENCY(use of methods)
        messagebox.showwarning("Warning", "Fill out all entries")
    else:
        try:
            current_length = float(length_entry.get())
            current_height = float(height_entry.get())
            current_width = float(width_entry.get())
        except:
            messagebox.showwarning("Warning", "Make sure all entries are numbers")
        if isinstance(current_length, float) and isinstance(current_height, float) and isinstance(current_width, float) and current_length > 0 and current_height > 0 and current_width > 0:
            global gallon_capacity 
            gallon_capacity = (current_length * current_height * current_width) / 231 

            if gallon_capacity < 1: #COMPETENCY(string and character manipulation) nested if statement, if value is < 1 gallon, answer is in float data type
                gallon_label.config(text = f"{gallon_capacity:.2f} gallons")
                gallon_capacity = float(f'{gallon_capacity:.2f}')

            else:    #COMPETENCY(string and character manipulation) nested if statement, if value > 1 gallon, answer is rounded to integer data type
                gallon_label.config(text = f"{round(gallon_capacity)} gallons") # #COMPETENCY(use of methods) to modify label
                gallon_capacity = round(gallon_capacity)

        else: # displays warning to user, shows entry requirements 
            messagebox.showwarning("Warning", "Make sure all entries are numbers greater than 0 ")

        # Once erros are taken cared of, current tank info is made available with global variable where user can choose to save     
    global current_tank_info
    current_tank_info = f"{current_length} x {current_height} x {current_width}"    

   


# this functions runs when user clicks button which saves current tank info by appending to dictionary and displays it
def save_tank_info():
    global number_tanks_saved
    number_tanks_saved += 1   # COMPETENCY(array processing), by using a dictionary for storing tank gallon amount and its dimensions
    tanks_saved[f'Tank #{number_tanks_saved}'] = f"{gallon_capacity} gal : {current_tank_info}" 
    tanks_saved_label.config(text = tanks_saved, wraplength=200) #COMPETENCY(use of methods) use of methods to modify label




length_label = ttk.Label(root, text='Enter tank length')
length_label.grid(row = 0, column= 0)
height_label = ttk.Label(root, text='Enter tank height')
height_label.grid(row = 1, column= 0)
width_label = ttk.Label(root, text='Enter tank depth')
width_label.grid(row = 2, column= 0)
gallon_label = ttk.Label(root, text = f"{gallon_capacity} gallons")
gallon_label.grid(row = 3, column = 0)
tanks_saved_label = ttk.Label(root, text= '')
tanks_saved_label.grid(row = 5, column = 0, columnspan = 3)


length_entry = ttk.Entry(root)   
length_entry.grid(row = 0, column= 1)
height_entry = ttk.Entry(root)               
height_entry.grid(row = 1, column= 1)
width_entry = ttk.Entry(root)               
width_entry.grid(row = 2, column= 1)


#button that calls calculate_gallons function when pressed
calculate_gallons_btn = ttk.Button(root,
                 text='Calculate Gallons',
                 command= calculate_gallons)
calculate_gallons_btn.grid(row = 3, column= 1)

#button that calls save_tank function when pressed
save_tank_btn = ttk.Button(root,
                 text ='Save Tank Dimensions',
                 command = save_tank_info)
save_tank_btn.grid(row = 4, column= 1)


root.mainloop()