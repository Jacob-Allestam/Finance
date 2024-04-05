import tkinter as tk
from tkinter import ttk
from scipy.stats import norm
import numpy as np
from scipy.optimize import brentq

def black_scholes(S, K, T, r, sigma, option_type):
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    if option_type == "Call":
        option_price = S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    elif option_type == "Put":
        option_price = K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
    return option_price

def implied_volatility(S, K, T, r, option_price, option_type):
    if option_type == "Call":
        obj_func = lambda sigma: black_scholes(S, K, T, r, sigma, option_type) - option_price
    elif option_type == "Put":
        obj_func = lambda sigma: black_scholes(S, K, T, r, sigma, option_type) - option_price
    implied_vol = brentq(obj_func, 0.001, 10)
    return implied_vol

def calculate_option_price():
    S = float(entry_S.get())
    K = float(entry_K.get())
    T = float(entry_T.get())
    r = float(entry_r.get())
    option_price = float(entry_option_price.get())
    option_type = combo_option_type.get()

    if option_type == "Implied Volatility":
        implied_vol = implied_volatility(S, K, T, r, option_price, "Call") # Use Call option for implied volatility calculation
        label_result.config(text=f"Implied Volatility: {implied_vol:.4f}")
    else:
        sigma = float(entry_sigma.get())
        option_price = black_scholes(S, K, T, r, sigma, option_type)
        label_result.config(text=f"{option_type} Price: {option_price:.2f}")

# Create the main window
root = tk.Tk()
root.title("Option Pricing")

# Create input labels and entry boxes
label_S = tk.Label(root, text="Stock Price (S):")
label_S.grid(row=0, column=0, padx=5, pady=5)
entry_S = tk.Entry(root)
entry_S.grid(row=0, column=1, padx=5, pady=5)

label_K = tk.Label(root, text="Strike Price (K):")
label_K.grid(row=1, column=0, padx=5, pady=5)
entry_K = tk.Entry(root)
entry_K.grid(row=1, column=1, padx=5, pady=5)

label_T = tk.Label(root, text="Time to Expiration (T):")
label_T.grid(row=2, column=0, padx=5, pady=5)
entry_T = tk.Entry(root)
entry_T.grid(row=2, column=1, padx=5, pady=5)

label_r = tk.Label(root, text="Risk-Free Rate (r):")
label_r.grid(row=3, column=0, padx=5, pady=5)
entry_r = tk.Entry(root)
entry_r.grid(row=3, column=1, padx=5, pady=5)

label_sigma = tk.Label(root, text="Volatility (sigma):")
label_sigma.grid(row=4, column=0, padx=5, pady=5)
entry_sigma = tk.Entry(root)
entry_sigma.grid(row=4, column=1, padx=5, pady=5)

label_option_type = tk.Label(root, text="Option Type:")
label_option_type.grid(row=5, column=0, padx=5, pady=5)
combo_option_type = ttk.Combobox(root, values=["Call", "Put", "Implied Volatility"])
combo_option_type.current(0)
combo_option_type.grid(row=5, column=1, padx=5, pady=5)

label_option_price = tk.Label(root, text="Option Price:")
label_option_price.grid(row=6, column=0, padx=5, pady=5)
entry_option_price = tk.Entry(root)
entry_option_price.grid(row=6, column=1, padx=5, pady=5)

button_calculate = tk.Button(root, text="Calculate", command=calculate_option_price)
button_calculate.grid(row=7, column=0, columnspan=2, padx=5, pady=5)

label_result = tk.Label(root, text="")
label_result.grid(row=8, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()
