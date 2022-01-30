###############################
## Practice making a GUI
###############################

import tkinter as tk
import Misc.faultinjections_example as injections
import Misc.motorcontrol_example


# def print_status():
#     lbl_value["text"] = "Motor ON"

window = tk.Tk()

window.rowconfigure(0, minsize=50, weight=1)
window.columnconfigure([0, 1, 2], minsize=50, weight=1)

lbl_value = tk.Label(master=window, text="Motor status HERE")
lbl_value.grid(row=0, column=1)

btn_increase = tk.Button(master=window, text="+", command=injections.print_status)
btn_increase.grid(row=0, column=2, sticky="nsew")

window.mainloop()
    












