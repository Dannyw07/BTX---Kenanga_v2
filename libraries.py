import tkinter as tk
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import base64
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
import sys
import os
from socket import timeout as SocketTimeoutError
from tkinter import ttk
import time
import requests
from threading import Thread
import ttkbootstrap as tb
from tkinter import messagebox
import datetime
import subprocess
from dotenv import load_dotenv
load_dotenv()
import queue
from selenium.webdriver.support.ui import Select
import datetime
import configparser
from selenium.common.exceptions import NoSuchWindowException
from driver_utils import initialize_driver, navigate_to_initial_url, login
from emailBody import generate_email_body, image1_base64, image2_base64
from create_excel import generate_excel_file
from create_html_table import modify_html_table
from socket import timeout as SocketTimeoutError