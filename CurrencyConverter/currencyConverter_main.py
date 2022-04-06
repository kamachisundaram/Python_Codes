import os,requests,io
from bs4 import BeautifulSoup
import tkinter as tk
os.system('cls')
import json
import platform    # For getting the operating system name
import subprocess  # For executing a shell command
from tkinter.messagebox import showinfo

def ping(host):
    """
    Returns True if host (str) responds to a ping request.
    Remember that a host may not respond to a ping (ICMP) request even if the host name is valid.
    """

    # Option for the number of packets as a function of
    param = '-n' if platform.system().lower()=='windows' else '-c'

    # Building the command. Ex: "ping -c 1 google.com"
    command = ['ping', param, '1', host]

    return subprocess.call(command) == 0

def ConvertCurrency(amount,src,destination):
    URL='https://www.xe.com/currencyconverter/convert/?Amount='+str(amount)+'&From='+str(src)+'&To='+str(destination)
    page=requests.get(URL)
    soup=BeautifulSoup(page.content,"html.parser")
    results=soup.find(id="__next")
    job_elements=results.find(class_="result__BigRate-sc-1bsijpp-1 iGrAod")
    print(job_elements.text)

def RunPingTest():
    """ callback when the login button clicked
    """
    d=ping('www.xe.com')
    if d:
        print('Ping Success')
    else:
        exit()

def VerifyValidCurrency(currency):
    with open("availableCurrency.json", "r") as read_file:
        data = json.load(read_file)
    if currency not in list(data['en'].keys()):
        print('Please enter a valid currency')
        exit()



def GetUserInput():

    srcCurrency=str(input('Enter the src currency\n'))
    DestinationCurrency=str(input('Enter the destination currency\n'))
    Amount=int(input('Enter the Amount\n'))
    RunPingTest()
    VerifyValidCurrency(srcCurrency)
    VerifyValidCurrency(DestinationCurrency)
    ConvertCurrency(Amount,srcCurrency,DestinationCurrency)
GetUserInput()