import csv
import pandas

data=pandas.read_csv("C:\\Users\\renzz\\Documents\\RENZZO\\LINKS FIELD\VARIOS\\IOTAC.csv", delimiter=';',usecols=["ICCID"])
inverted_data=data[::-1]
inverted_data.to_csv("C:\\Users\\renzz\\Downloads\\Filtered.csv",index=False)
