"""
@author: Madison Howard
@date: 2020-08-13
@purpose: create 3 seperate plots (T,P,H) of all data vs time
to-do:
    1) explain to MIH
    2) let MIH explain back
    3) create code docs
    4) create code usage example
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import csv, os, sys
import matplotlib
import matplotlib.dates as md
import dateutil
import glob

#object to store time,temp,pressure,humidity information
class ThermoData:

    def __init__(self, txtFile):
        self.txtFile = txtFile
        self.txtInfo = self.extractInfo()
        self.temp = self.txtInfo['temperature'].values
        self.pressure = self.txtInfo['pressure'].values
        self.humidity = self.txtInfo['humidity'].values
        self.date_string = self.getFormattedDateString()
        self.times = [dateutil.parser.parse(s) for s in self.date_string]
        self.date = self.date_string[0].split(" ")[0]
        self.start_time = self.date_string[0].split(" ")[1]
        self.end_time = self.date_string[-1].split(" ")[1]
        self.pi_name = "Pi_" + self.txtFile.split(".")[0].split("(")[1][0]

    def getFormattedDateString(self):
        raw_string = self.txtInfo['time'].values
        new_string = [i.replace("-"," ") for i in raw_string]
        new_string = [i.replace("/","-") for i in new_string]
        return new_string

    def extractInfo(self):
        data = pd.read_csv(self.txtFile, delimiter=' ', names=['time','temperature','pressure','humidity'])
        return data

#function to create the needed plots
def plotSingleGraph(pis, therm_var):
    fig, ax = plt.subplots()
    for pi in pis:
        if therm_var == "temperature":
            time, values = pi.times, pi.temp
            ax.plot_date(time, values, marker='.', linestyle='-', label=pi.pi_name)
            plt.xlabel("Time Stamp (Day Hour:Minute)")
            plt.ylabel("Temperature (°F)")
            plt.title("Date: {}".format(pi.date))
        elif therm_var == "humidity":
            time, values = pi.times, pi.humidity
            ax.plot_date(time, values, marker='.', linestyle='-', label=pi.pi_name)
            plt.xlabel("Time Stamp (Day Hour:Minute)")
            plt.ylabel("Relative Percentage Humidity (%)")
            plt.title("Date: {}".format(pi.date))
        elif therm_var == "pressure":
            time, values = pi.times, pi.pressure
            ax.plot_date(time, values, marker='.', linestyle='-', label=pi.pi_name)
            plt.xlabel("Time Stamp (Day Hour:Minute)")
            plt.ylabel("Pressure (kPa)")
            plt.title("Date: {}".format(pi.date))
    fig.autofmt_xdate()
    plt.legend()
    plt.grid()
    plt.minorticks_on()
    plt.grid(which='minor', linestyle=':')
    plt.show()


def printRunTimes(pis):
    for pi in pis:
        print("Start Time for Pi_{} is {}".format(pi.pi_name, pi.start_time))
        print("End Time for Pi_{} is {}\n".format(pi.pi_name, pi.end_time))

def getDataFromAllPi():
    pi_array = []
    txt_files = glob.glob("*.txt")
    for file in txt_files:
        pi_array.append(ThermoData(str(file)))
    return pi_array

def plotDataFromAllPi():
    all_pi = getDataFromAllPi()
    printRunTimes(all_pi)
    plotSingleGraph(all_pi, "temperature")
    plotSingleGraph(all_pi, "pressure")
    plotSingleGraph(all_pi, "humidity")

#main function
if __name__ == "__main__":
    pi_A = ThermoData("DataLog(A).txt")
    pi_B = ThermoData("DataLog(B).txt")
    pi_C = ThermoData("DataLog(C).txt")
    all_pi = [pi_A,pi_B,pi_C]
    printRunTimes(all_pi)
    plotSingleGraph(all_pi, "temperature")
    plotSingleGraph(all_pi, "pressure")
    plotSingleGraph(all_pi, "humidity")
  #  plotDataFromAllPi()
