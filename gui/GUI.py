import tkinter
from tkinter import *
import canvas
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import numpy
import numpy as np
import pandas as pd
import sqlite3
import datetime

## get bioimpedance value from the database
def BioimpValue():
    conn = sqlite3.connect('data.sqlite')
    c = conn.cursor()
    c.execute("SELECT value FROM sensors_data WHERE type = 'BioZ'")
    records=c.fetchall()
    value = []
    for record in records:
        strB=str(record)
        rep1=strB.replace('(', '')
        rep2=rep1.replace(')', '')
        rep3=rep2.replace(',', '')
        rep4=rep3.replace("'", '')
        getValue=float(rep4)
        value.append(getValue)
    return value

## get bioimpedance time from the database
def BioimpTime():
    conn = sqlite3.connect('data.sqlite')
    c = conn.cursor()
    c.execute("SELECT timestamp FROM sensors_data WHERE type = 'BioZ'")
    dates=c.fetchall()
    datesValues = []
    for date in dates:
        getDates = datetime.datetime.strptime(str(date), "('%Y-%m-%d %H:%M:%S.%f',)")
        datesValues.append(getDates)
    time = []
    for t in datesValues:
        tt = float(t.second+t.microsecond*0.000001)
        time.append(tt)
    return time

## get electrocardiogram value from the database
def ECGValue():
    conn = sqlite3.connect('data.sqlite')
    c = conn.cursor()
    c.execute("SELECT value FROM sensors_data WHERE type = 'ECG'")
    records=c.fetchall()
    value = []
    for record in records:
        strB=str(record)
        rep1=strB.replace('(', '')
        rep2=rep1.replace(')', '')
        rep3=rep2.replace(',', '')
        rep4=rep3.replace("'", '')
        getValue=float(rep4)
        value.append(getValue)
    return value

## get electrocardiogram time from the database
def ECGTime():
    conn = sqlite3.connect('data.sqlite')
    c = conn.cursor()
    c.execute("SELECT timestamp FROM sensors_data WHERE type = 'ECG'")
    dates=c.fetchall()
    datesValues = []
    for date in dates:
        getDates = datetime.datetime.strptime(str(date), "('%Y-%m-%d %H:%M:%S.%f',)")
        datesValues.append(getDates)
    time = []
    for t in datesValues:
        tt = float(t.second+t.microsecond*0.000001)
        time.append(tt)
    return time

## get pulse value from the database
def PulseValue():
    conn = sqlite3.connect('data.sqlite')
    c = conn.cursor()
    c.execute("SELECT value FROM sensors_data WHERE type = 'P'")
    records=c.fetchall()
    value = []
    for record in records:
        strB=str(record)
        rep1=strB.replace('(', '')
        rep2=rep1.replace(')', '')
        rep3=rep2.replace(',', '')
        rep4=rep3.replace("'", '')
        getValue=float(rep4)
        value.append(getValue)
    return value

## get pulse time from the database
def PulseTime():
    conn = sqlite3.connect('data.sqlite')
    c = conn.cursor()
    c.execute("SELECT timestamp FROM sensors_data WHERE type = 'P'")
    dates=c.fetchall()
    datesValues = []
    for date in dates:
        getDates = datetime.datetime.strptime(str(date), "('%Y-%m-%d %H:%M:%S.%f',)")
        datesValues.append(getDates)
    time = []
    for t in datesValues:
        tt = float(t.second+t.microsecond*0.000001)
        time.append(tt)
    return time

## get oxygen saturation value from the database
def OxSatValue():
    conn = sqlite3.connect('data.sqlite')
    c = conn.cursor()
    c.execute("SELECT value FROM sensors_data WHERE type = 'SpO2'")
    records=c.fetchall()
    value = []
    for record in records:
        strB=str(record)
        rep1=strB.replace('(', '')
        rep2=rep1.replace(')', '')
        rep3=rep2.replace(',', '')
        rep4=rep3.replace("'", '')
        getValue=float(rep4)
        value.append(getValue)
    return value

## get oxygen saturation time from the database
def OxSatTime():
    conn = sqlite3.connect('data.sqlite')
    c = conn.cursor()
    c.execute("SELECT timestamp FROM sensors_data WHERE type = 'SpO2'")
    dates=c.fetchall()
    datesValues = []
    for date in dates:
        getDates = datetime.datetime.strptime(str(date), "('%Y-%m-%d %H:%M:%S.%f',)")
        datesValues.append(getDates)
    time = []
    for t in datesValues:
        tt = float(t.second+t.microsecond*0.000001)
        time.append(tt)
    return time

## display bioimpedance data on a graph
gui1 = tkinter.Tk()
gui1.title("Bioimpedance")
gui1.geometry("400x400+70+200")
fig1 = Figure(figsize=(5, 4), dpi=100)
x1 = BioimpTime()
y1 = BioimpValue()
fig1.add_subplot(111).plot(x1, y1)
canvas1 = FigureCanvasTkAgg(fig1, master=gui1)
canvas1.draw()
canvas1.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
toolbar1 = NavigationToolbar2Tk(canvas1, gui1)
toolbar1.update()
canvas1.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

## display electrocardiogram data on a graph
gui2=tkinter.Tk()
gui2.title("Electrocardiogram")
gui2.geometry("400x400+520+200")
fig2 = Figure(figsize=(5, 4), dpi=100)
x2 = ECGTime()
y2 = ECGValue()
fig2.add_subplot(111).plot(x2, y2)
canvas2 = FigureCanvasTkAgg(fig2, master=gui2)
canvas2.draw()
canvas2.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
toolbar2 = NavigationToolbar2Tk(canvas2, gui2)
toolbar2.update()
canvas2.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

## display pulse data on a graph
gui3=tkinter.Tk()
gui3.title("Pulse")
gui3.geometry("400x400+970+200")
fig3 = Figure(figsize=(5, 4), dpi=100)
x3 = PulseTime()
y3 = PulseValue()
fig3.add_subplot(111).plot(x3, y3)
canvas3 = FigureCanvasTkAgg(fig3, master=gui3)
canvas3.draw()
canvas3.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
toolbar3 = NavigationToolbar2Tk(canvas3, gui3)
toolbar3.update()
canvas3.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

## display oxygen saturation data on a graph
gui4=tkinter.Tk()
gui4.title("Oxygen Saturation")
gui4.geometry("400x400+1420+200")
fig4 = Figure(figsize=(5, 4), dpi=100)
x4 = OxSatTime()
y4 = OxSatValue()
fig4.add_subplot(111).plot(x4, y4)
canvas4 = FigureCanvasTkAgg(fig4, master=gui4)
canvas4.draw()
canvas4.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
toolbar4 = NavigationToolbar2Tk(canvas4, gui4)
toolbar4.update()
canvas4.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

tkinter.mainloop()