import tkinter as tk
from tkinter import ttk

# Function to create the pop-up window
def create_popup(message):
    popup = tk.Tk()  # Create the pop-up window directly as the main window
    popup.title("Report")  # Set the title of the pop-up window
    
    # Create a frame to contain the Text widget and the Close button
    frame = ttk.Frame(popup,width=800, height=300, padding=(10, 10, 10, 10))
    frame.grid(row=0, column=0, sticky="nsew")

    # Add a Text widget to display the message (with copy-paste support)
    text_widget = tk.Text(frame, wrap='word', height=20, width=100)
    text_widget.insert(tk.END, message)  # Insert the message into the Text widget
    text_widget.config(state='disabled')  # Make it read-only
    text_widget.grid(row=0, column=0, sticky="nsew")  # Make the text widget sticky

    # Add a button to close the window
    close_button = ttk.Button(frame, text="Close", command=popup.destroy)
    close_button.grid(row=1, column=0, pady=5)

    # Configure the frame and popup to resize with the window
    popup.grid_rowconfigure(0, weight=1)  # Make row 0 (Text widget) expandable
    popup.grid_columnconfigure(0, weight=1)  # Make column 0 expandable
    frame.grid_rowconfigure(0, weight=1)  # Allow text widget to expand within the frame
    frame.grid_columnconfigure(0, weight=1)

    popup.mainloop()  # Start the Tkinter event loop to keep the window open

# Example message to display in the pop-up
message =''
for i in range(5):
    message+=r'file "C:\Users\k1-on\Pictures\Camera Roll\WIN_20240323_22_08_26_Pro.jpg" did NOT resize' + str(i)+'\n' 

# Call the function to display the message as soon as the program starts
create_popup(message)
