import csv
import re
import tkinter as tk
from tkinter import messagebox
import os

"""Creates the template CSV"""
def create_csv(filename, filepath, tube_20, tube_24, tare_set, gross_set):
    suffix_24 = ['011', '012', '021', '022', '031', '032', '041', '042', '051', '052', '061', '062', '071', '072']
    suffix_20 = ['013', '014', '023', '024', '033', '034', '043', '044', '053', '054', '063', '064', '073', '074']
    rack_position = ['A0', 'B0', 'C0', 'D0']
    
    # Writes CSV
    with open(filepath + "\\" + filename, 'w', newline='') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            spamwriter.writerow(['TareRack', 'TarePos', 'TgtRack', 'TgtPos'])
            
            # If statement that changes the csv if it's 24 or 20
            if tube_20 and tube_24:
                suffix = -1 # Start suffix at -1 so it gets immediatly turned to 0 the first loop
                
                # for loop for 24s
                for i in range(336):
                    if i % 24 == 0:
                        suffix += 1
                        rack_num = 0
                        
                    if i % 4 == 0:
                        rack_num += 1
                        rack_position_num = 0
                        
                    TareRack = tare_set + suffix_24[suffix]
                    TarePos = rack_position[rack_position_num] + str(rack_num)
                    TgtRack = gross_set + suffix_24[suffix]
                    TgtPos = rack_position[rack_position_num] + str(rack_num)
                    
                    rack_position_num += 1
                    
                    spamwriter.writerow([str(TareRack), TarePos, str(TgtRack), TgtPos])
        
                # for loop for 20s
                suffix = -1 # Start suffix at -1 so it gets immediatly turned to 0 the first loop
                
                for i in range(280):
                    if i % 20 == 0:
                        suffix += 1
                        rack_num = 0
                        
                    if i % 4 == 0:
                        rack_num += 1
                        rack_position_num = 0
                        
                    TareRack = tare_set + suffix_20[suffix]
                    TarePos = rack_position[rack_position_num] + str(rack_num)
                    TgtRack = gross_set + suffix_20[suffix]
                    TgtPos = rack_position[rack_position_num] + str(rack_num)
                    
                    rack_position_num += 1
                    
                    spamwriter.writerow([str(TareRack), TarePos, str(TgtRack), TgtPos])
                    
            elif tube_20:
                suffix = -1 # Start suffix at -1 so it gets immediatly turned to 0 the first loop
                
                # for loop for 24s
                for i in range(280):
                    if i % 20 == 0:
                        suffix += 1
                        rack_num = 0
                        
                    if i % 4 == 0:
                        rack_num += 1
                        rack_position_num = 0
                        
                    TareRack = tare_set + suffix_20[suffix]
                    TarePos = rack_position[rack_position_num] + str(rack_num)
                    TgtRack = gross_set + suffix_20[suffix]
                    TgtPos = rack_position[rack_position_num] + str(rack_num)
                    
                    rack_position_num += 1
                    
                    spamwriter.writerow([str(TareRack), TarePos, str(TgtRack), TgtPos])
                    
            elif tube_24:
                suffix = -1 # Start suffix at -1 so it gets immediatly turned to 0 the first loop
                
                # for loop for 24s
                for i in range(336):
                    if i % 24 == 0:
                        suffix += 1
                        rack_num = 0
                        
                    if i % 4 == 0:
                        rack_num += 1
                        rack_position_num = 0
                        
                    TareRack = tare_set + suffix_24[suffix]
                    TarePos = rack_position[rack_position_num] + str(rack_num)
                    TgtRack = gross_set + suffix_24[suffix]
                    TgtPos = rack_position[rack_position_num] + str(rack_num)
                    
                    rack_position_num += 1
                    
                    spamwriter.writerow([str(TareRack), TarePos, str(TgtRack), TgtPos])

def easter():
    res = messagebox.askquestion('You found me :)', 'Do you know what one Biomicrolab said to the other?')
    if res == 'yes':
        messagebox.showinfo("You found me :)", "Okay :) Don't tell anyone")
    elif res == 'no':
        messagebox.showinfo('You found me :)', "\"Hey don't let that tube's comment weigh on you, he was acting unnecessarily crude.\"")
    
"""Checks if the file already exists"""
def file_exists(tare_set, gross_set, tube_20, tube_24):
    # Making the filename
    if tube_20 and tube_24:
        filename = "gross_tare_" + gross_set + "_" + tare_set + ".csv"
    elif tube_20:
        filename = "gross_tare_" + gross_set + "_" + tare_set + "_20.csv"
    elif tube_24:
        filename = "gross_tare_" + gross_set + "_" + tare_set + "_24.csv"
        
    # Checking if the file is in the folder
    filepath = "C:\\Fractionation"
    for file in os.listdir(filepath):
        if file == filename:
            return True, filename, filepath
        
    # If the file has not been created
    return False, filename, filepath
    

"""App actions"""
# Funcions to make the buttons work
def press_okay():    
    # Getting variables
    tare_set = entry_tare.get()
    gross_set = entry_gross.get()
    tube_20 = var20.get()
    tube_24 = var24.get()
    
    # Regex matching to see if input is accurate
    tare_confirm = re.search('\d{8}', tare_set)
    gross_confirm = re.search('\d{8}', gross_set)
    
    # If statement that controls how to react
    if len(tare_set) != 8 or tare_confirm is None:
        messagebox.showerror("Error", "Enter legitiment tare set")
    elif len(gross_set) != 8 or gross_confirm is None:
        messagebox.showerror("Error", "Enter legitiment gross set")
    elif tube_20 == 0 and tube_24 == 0:
        messagebox.showerror("Error", "Select number of tubes")
    else:
        # Determines if the file exists or not and what to do about it
        isfile, filename, filepath = file_exists(tare_set, gross_set, tube_20, tube_24)
        if isfile:
            # TODO: ask the user if they want to proceed anyways
            messagebox.showerror("Error", "File " + filename + " already exists")
        else:
            create_csv(filename, filepath, tube_20, tube_24, tare_set, gross_set)
            messagebox.showinfo("Success", "Success!")
            window.destroy() # Closes the app


if __name__ == '__main__':
    """Creating app Layout"""
    # Initializing the window
    window = tk.Tk()
    window.title('Gross and Tare Assistant')

    # Labeling the app
    frame_app = tk.Frame(master=window, borderwidth=10)
    easter_button = tk.Button(master=frame_app, text="WELCOME!", relief=tk.FLAT, command=easter)
    label_app = tk.Label(master=frame_app, text="What would you like to weigh today?")
#     label2_app = tk.Label(master=frame_app, text="What would you like to weigh today?")
    easter_button.pack(side=tk.LEFT)
    label_app.pack(side=tk.LEFT)
#     label2_app.pack()
    frame_app.pack()

    # Tare set input
    frame_tare = tk.Frame(master=window, borderwidth=5)
    label_tare = tk.Label(master=frame_tare, text="Tare Set:") # Adds text
    entry_tare = tk.Entry(master=frame_tare) # Adds entry box
    label_tare.pack(side=tk.LEFT) # .pack populates the window
    entry_tare.pack(fill=tk.X)
    frame_tare.pack(fill=tk.X)

    # Gross set input
    frame_gross = tk.Frame(master=window, borderwidth=5)
    label_gross = tk.Label(master=frame_gross, text="Gross Set:") # Adds text
    entry_gross = tk.Entry(master=frame_gross) # Adds entry box
    label_gross.pack(side=tk.LEFT) # .pack populates the window
    entry_gross.pack(fill=tk.X)
    frame_gross.pack(fill=tk.X)

    # Checkboxes
    frame_checkbox = tk.Frame(master=window, borderwidth=5)
    label_checkbox = tk.Label(master=frame_checkbox, text="Number of tubes:")
    var20 = tk.IntVar() # variale for the 20 box
    var24 = tk.IntVar() # variabel for the 24 box
    box20 = tk.Checkbutton(master=frame_checkbox, text="20", variable=var20)
    box24 = tk.Checkbutton(master=frame_checkbox, text="24", variable=var24)
    label_checkbox.pack(side=tk.LEFT)
    box20.pack(side=tk.LEFT)
    box24.pack()
    frame_checkbox.pack()

    # Okay Button
    frame_ok = tk.Frame(master=window, borderwidth=10)
    button_ok = tk.Button(master=frame_ok, text="Ok", relief=tk.RAISED, command=press_okay)
    button_ok.pack()
    frame_ok.pack()

    window.mainloop() # Start the app
