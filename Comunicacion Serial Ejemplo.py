import serial
import tkinter as tk

# Set up serial communication
ser = serial.Serial('COM5', 9600) # Replace 'COM3' with the port name of your microcontroller
ser.flushInput()

# Create GUI window
window = tk.Tk()
window.title("Serial Communication")
window.geometry("300x200")

# Create label for displaying received character
label = tk.Label(window, text="La letra correspondiente es: ")
label.pack(pady=10)

# Create label for displaying received character
char_label = tk.Label(window, text="")
char_label.pack()

# Function to update label with received character
def update_label():
    if ser.in_waiting > 0:
        received_char = ser.read().decode('ascii')
        char_label.config(text=received_char)

    window.after(100, update_label)

update_label()

window.mainloop()
