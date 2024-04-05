import tkinter as tk
from tkinter import ttk
import numpy as np
from scipy.stats import norm

def black_scholes_with_dividend(S, K, T, r, sigma, q, option_type):
    d1 = (np.log(S / K) + (r - q + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    if option_type == "Call":
        option_price = S * np.exp(-q * T) * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    elif option_type == "Put":
        option_price = K * np.exp(-r * T) * norm.cdf(-d2) - S * np.exp(-q * T) * norm.cdf(-d1)
    return option_price

def update_option_prices(event=None):
    S = float(entry_S.get())
    K = float(entry_K.get())
    T = float(entry_T.get())
    r = float(entry_r.get())
    sigma = float(entry_sigma.get())
    q = float(entry_q.get())

    call_price = black_scholes_with_dividend(S, K, T, r, sigma, q, "Call")
    put_price = black_scholes_with_dividend(S, K, T, r, sigma, q, "Put")

    label_call_result.config(text=f"Call Price: {call_price:.2f}")
    label_put_result.config(text=f"Put Price: {put_price:.2f}")

# Create the main window
root = tk.Tk()
root.title("Option Pricing with Dividend")

# Create text fields for input parameters with pre-filled values
S_default = 100
K_default = 100
T_default = 1
r_default = 0.05
sigma_default = 0.2
q_default = 0.02

label_S = ttk.Label(root, text="Stock Price (S):")
label_S.grid(row=0, column=0, padx=5, pady=5)
entry_S = ttk.Entry(root)
entry_S.grid(row=0, column=1, padx=5, pady=5)
entry_S.insert(0, S_default)
entry_S.bind('<KeyRelease>', update_option_prices)

label_K = ttk.Label(root, text="Strike Price (K):")
label_K.grid(row=1, column=0, padx=5, pady=5)
entry_K = ttk.Entry(root)
entry_K.grid(row=1, column=1, padx=5, pady=5)
entry_K.insert(0, K_default)
entry_K.bind('<KeyRelease>', update_option_prices)

label_T = ttk.Label(root, text="Time to Expiration (T):")
label_T.grid(row=2, column=0, padx=5, pady=5)
entry_T = ttk.Entry(root)
entry_T.grid(row=2, column=1, padx=5, pady=5)
entry_T.insert(0, T_default)
entry_T.bind('<KeyRelease>', update_option_prices)

label_r = ttk.Label(root, text="Risk-Free Rate (r):")
label_r.grid(row=3, column=0, padx=5, pady=5)
entry_r = ttk.Entry(root)
entry_r.grid(row=3, column=1, padx=5, pady=5)
entry_r.insert(0, r_default)
entry_r.bind('<KeyRelease>', update_option_prices)

label_sigma = ttk.Label(root, text="Volatility (sigma):")
label_sigma.grid(row=4, column=0, padx=5, pady=5)
entry_sigma = ttk.Entry(root)
entry_sigma.grid(row=4, column=1, padx=5, pady=5)
entry_sigma.insert(0, sigma_default)
entry_sigma.bind('<KeyRelease>', update_option_prices)

label_q = ttk.Label(root, text="Dividend Yield (q):")
label_q.grid(row=5, column=0, padx=5, pady=5)
entry_q = ttk.Entry(root)
entry_q.grid(row=5, column=1, padx=5, pady=5)
entry_q.insert(0, q_default)
entry_q.bind('<KeyRelease>', update_option_prices)

# Create labels to display results
label_call_result = ttk.Label(root, text="Call Price: ")
label_call_result.grid(row=6, column=0, padx=5, pady=5)
label_put_result = ttk.Label(root, text="Put Price: ")
label_put_result.grid(row=6, column=1, padx=5, pady=5)

# Run the GUI
root.mainloop()
