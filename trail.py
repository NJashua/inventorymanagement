import requests
import json

with open(r"C:\Users\1038588\OneDrive - Blue Yonder\program files\learnpython\companydetails.json")as file:

   data = json.load(file)
   if len(data):
      print(data)
   else:
      print("null")