import tkinter as tk
from tkinter import ttk

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    celsius = fahrenheit_to_celsius(fahrenheit)
    return celsius_to_kelvin(celsius)

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    celsius = kelvin_to_celsius(kelvin)
    return celsius_to_fahrenheit(celsius)

def convert_temperature():
    original_unit = original_unit_combobox.get()
    temperature = float(temperature_entry.get())
    
    if original_unit == "Celsius":
        fahrenheit = celsius_to_fahrenheit(temperature)
        kelvin = celsius_to_kelvin(temperature)
        result_label.config(text=f"{temperature} degrees Celsius is equal to {fahrenheit:.2f} degrees Fahrenheit and {kelvin:.2f} Kelvin.")
    elif original_unit == "Fahrenheit":
        celsius = fahrenheit_to_celsius(temperature)
        kelvin = fahrenheit_to_kelvin(temperature)
        result_label.config(text=f"{temperature} degrees Fahrenheit is equal to {celsius:.2f} degrees Celsius and {kelvin:.2f} Kelvin.")
    else:
        celsius = kelvin_to_celsius(temperature)
        fahrenheit = kelvin_to_fahrenheit(temperature)
        result_label.config(text=f"{temperature} Kelvin is equal to {celsius:.2f} degrees Celsius and {fahrenheit:.2f} degrees Fahrenheit.")

# Create the main window
window = tk.Tk()
window.title("Temperature Conversion")

# Create and configure widgets
frame = ttk.Frame(window)
frame.grid(row=0, column=0, padx=20, pady=20)

original_unit_label = ttk.Label(frame, text="Original Unit:")
original_unit_label.grid(row=0, column=0)

original_unit_combobox = ttk.Combobox(frame, values=["Celsius", "Fahrenheit", "Kelvin"])
original_unit_combobox.grid(row=0, column=1)
original_unit_combobox.set("Celsius")

temperature_label = ttk.Label(frame, text="Temperature:")
temperature_label.grid(row=1, column=0)

temperature_entry = ttk.Entry(frame)
temperature_entry.grid(row=1, column=1)

convert_button = ttk.Button(frame, text="Convert", command=convert_temperature)
convert_button.grid(row=2, column=0, columnspan=2)

result_label = ttk.Label(frame, text="")
result_label.grid(row=3, column=0, columnspan=2)

# Start the GUI main loop
window.mainloop()
