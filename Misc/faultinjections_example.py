################################################
## Functions to simulate fault injections
################################################

import tkinter as tk

def print_status():
    lbl_value["text"] = "Motor ON"

def short1():
    print("Shorting 1")

def short2():
    print("Shorting 2")

def short3():
    print("Shorting 3")

def shortA():
    print("Shorting A")

def shortB():
    print("Shorting B")

def shortC():
    print("Shorting C")


lbl_value = tk.Label(master=window, text="Motor status HERE")

