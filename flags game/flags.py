# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 12:01:13 2022

@author: aldis
"""
import bs4 as bs
import urllib.request
import time
import csv
from PIL import Image
from io import BytesIO
import requests


file = open("flags.csv", "r")
reader = csv.reader(file)
l = []
for row in reader:
    link = row[1]
    name = row[0]
    l.append(name)

    




file.close()