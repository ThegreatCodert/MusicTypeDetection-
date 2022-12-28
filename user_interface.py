from tkinter import *
import tkinter as tk
import tkinter.font as tkFont
from AI_MODULE import *
from python_speech_features import mfcc
import scipy.io.wavfile as wav
import numpy as np
from tempfile import TemporaryFile
import os
import pickle
import random 
import operator
import math
import numpy as np
from collections import defaultdict



valuex = ""

class App:
    def GButton_641_command(self):
        (rate,sig)=wav.read(GLineEdit_309.get())
        mfcc_feat=mfcc(sig,rate,winlen=0.020,appendEnergy=False)
        covariance = np.cov(np.matrix.transpose(mfcc_feat))
        mean_matrix = mfcc_feat.mean(0)
        feature=(mean_matrix,covariance,0)
        pred=nearestClass(getNeighbors(dataset ,feature , 5))
        valuex = results[pred]
        print(valuex)
        text = tk.Text(root, height=8)
        text.place(x=90,y=370,width=417,height=30)
        text.insert(1.0, valuex + " " + "is the music genre")

        
        
    def __init__(self, root):
        #setting title
        root.title("Music Type Prediction ")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GButton_641=tk.Button(root)
        GButton_641["bg"] = "#00ced1"
        ft = tkFont.Font(family='Times',size=10)
        GButton_641["font"] = ft
        GButton_641["fg"] = "#393d49"
        GButton_641["justify"] = "center"
        GButton_641["text"] = "Predict"
        GButton_641.place(x=180,y=290,width=255,height=61)
        GButton_641["command"] = self.GButton_641_command
        
        global GLineEdit_309
        global value
        GLineEdit_309=tk.Entry(root)
        GLineEdit_309["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_309["font"] = ft
        GLineEdit_309["fg"] = "#333333"
        GLineEdit_309["justify"] = "center"
        GLineEdit_309["text"] = "Entry"
        GLineEdit_309.place(x=90,y=140,width=417,height=30)

        

        

        

    
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
