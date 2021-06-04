#! python3
import openpyxl,os,sys,shutil,time,subprocess,pyperclip,tkinter,random,docx,threading,webbrowser
from openpyxl.styles import Font
from tkinter import*
from PIL import ImageTk,Image
import requests
from lxml import etree
import lxml.html
import csv
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
cvet='#011128'
Style=("Arial", 9)
# ИНТЕРФЕЙС
# №1 ОКНО
window=Tk()
window.title('База команд МФФ')
window.geometry('1366x768')
image1 = ImageTk.PhotoImage(Image.open('oboi.jpg'))
bg_label = tkinter.Label(window, image = image1)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)
window.mainloop()
