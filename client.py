import tkinter as tk
import socket

def convert_currency():
    base_currency = base_currency_var.get()
    amount = amount_entry.get()
    target_currency = target_currency_var.get()
    
    data = f"{base_currency},{amount},{target_currency}"
    client.send(data.encode())
    
    converted_amount = client.recv(1024).decode()
    result_label.config(text=f"Converted amount: {converted_amount}")


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "127.0.0.1"  
port = 12345  
client.connect((host, port))


window = tk.Tk()
window.title("Currency Converter")


base_currency_label = tk.Label(window, text="Base Currency:")
base_currency_label.pack()
base_currency_var = tk.StringVar()
base_currency_entry = tk.Entry(window, textvariable=base_currency_var)
base_currency_entry.pack()

amount_label = tk.Label(window, text="Amount:")
amount_label.pack()
amount_entry = tk.Entry(window)
amount_entry.pack()

target_currency_label = tk.Label(window, text="Target Currency:")
target_currency_label.pack()
target_currency_var = tk.StringVar()
target_currency_entry = tk.Entry(window, textvariable=target_currency_var)
target_currency_entry.pack()

convert_button = tk.Button(window, text="Convert", command=convert_currency)
convert_button.pack()

result_label = tk.Label(window, text="")
result_label.pack()

window.mainloop()