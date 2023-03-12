import warnings
warnings.filterwarnings("ignore")
import plotly_express as px
from oauth2client.service_account import ServiceAccountCredentials
import gspread
import pandas as pd
from colorama import init
from termcolor import colored
init()

# READ the data from various gsheetts

def authenticate(cred):
    scope = ["https://www.googleapis.com/auth/spreadsheets"]
    creds = ServiceAccountCredentials.from_json_keyfile_name(cred, scope)  # ‘client_secret.json’, scope)
    gc = gspread.authorize(creds)
    # read the data contained on the sheets
    # defining my worksheet
    # tab = "Income"
    return gc


def reader(sheet,client,key):
    """Given a sheet name, this function returns the data contained therein"""
    wks = client.open_by_key(key)
    sheetnme = wks.worksheet(sheet)
    record = pd.DataFrame(sheetnme.get_all_records())
    print(
        colored(f"The read data:{sheet} has shape ----------->{record.shape}", "green")
    )
    record = record.rename(columns={"Firm ID": "firm_id"})
    try:
        record = record.fillna(0)
        record = record.drop(["Unnamed: 0"], 1)
        record = record.drop(["check"], 1)
    except:
        pass
    return record

# send the data to google sheets

def authenticater(cred):
    # use creds to create a client to interact with the Google Drive API
    scope = ['https://www.googleapis.com/auth/spreadsheets']
    creds = ServiceAccountCredentials.from_json_keyfile_name(cred, scope)
    client = gspread.authorize(creds)
    return client


def sender(df,key,sheet,cred = "credentials.json"):
    import numpy as np
    client = authenticater(cred)
    wks = client.open_by_key(key)
    #
    try:
        sh = wks.add_worksheet(title=f"{sheet}")
        sh.clear()
        sh.update([df.columns.values.tolist()] + df.values.tolist())
    except:
        sh = wks.worksheet(sheet)
        sh.clear()
        sh.update([df.columns.values.tolist()] + df.values.tolist())

def cleaner(df):
    for i in df.columns:
        df[i] = [str(i) for i in df[i]]
    return df

def sheets(key):
    # Prints out the list of all sheets in the data
    client = authenticater(cred)
    wks = client.open_by_key(key)
    sheets = wks.worksheets()   # generates a list of all sheets in the survey file
    return [sheet.title for sheet in sheets]

# tests on whether the functions worked
# test the reader function
cred  = "../Preparingvariousvariablesforgsheets/credentials.json"
url = "1qClVnVzuu7zTu6K66J4gcmPxyV6RfPxwGJ1kayX2fyI"
# wks = authenticate(cred)
# reader("Aspiration",wks,url)

# # test the sender function
# test = pd.DataFrame([23,11,234],columns = ['age'])
# print(test.head())


# # test the sending
# client = authenticater(cred)
# key = "1gV25QiySiqVtv5Q1_tzgy0TiKS3_-ZGGEeUVEiG3g0I"
# sender(test,key,"test")
# print("sent...>")