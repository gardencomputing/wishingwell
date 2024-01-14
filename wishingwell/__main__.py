#__main__.py

"""
GUIDE FOR USING WISHING WELL


"""



"""

import dependencies

"""

#Wishing Well admin variables:

from time import *


#web scraping dependencies

from bs4 import BeautifulSoup
import requests
from requests.exceptions import RequestException
from reports.reports import *
from lxml import html


#GUI design dependencies:

from tkinter import *


#Device OS dependencies

import os


"""

Define admin variables

"""


scrape_session_memory = []

directory = os.getcwd()

t = time()



"""

Define application functions

"""


def display_message(x):
    try:
        status_message.delete(0,END)
        x_convert=str(x)
        status_message.insert(0,f"{x_convert}")
        
    except:
        status_message.insert(0,"Error: status message unavailable.")


def robots():
    try:
        #retrieving input data from tkinter widget
        url = str(base_url_entry.get())
        url_digest = url.split("/")

        #requesting data from specified website
        session = requests.Session()
        site = session.get(f"{url}robots.txt",timeout=10)

        #https request data
        status_code = site.status_code
        status_reason = site.reason

        #analyzing site data via BeautifulSoup
        data = site.text
        convert = BeautifulSoup(data, features='lxml')
        search = convert.find_all
        result = str(search)
        
        try:
            #generate scraping session .txt report
            robots_report(time(),status_code,status_reason,result)
            display_message(f"Success:  {url} robots.txt report created in current directory.")
            
        except:
            display_message(f"Error:  could not generate {url} robots.txt report.")
            
        try:
            #close existing https request session
            session.close()
            
        except:
            display_message(f"Web session error:  exiting program.")
            quit()
    
    except requests.ConnectionError as e:
        display_message(f"Connection Error:  {url} robots.txt not found.")

    except requests.Timeout as e:
        display_message(f"Timeout Error:  {url} robots.txt not found.")

    except requests.RequestException as e:
        display_message(f"Unspecified Error:  {url} robots.txt not found.")


def scrape_page():
    try:
        #retrieving input data from tkinter widgets
        url = str(webpage_entry.get())
        scrape_html = str(html_entry.get())
        scrape_class = str(class_entry.get())

        #requesting data from specified website
        session = requests.Session()
        site = session.get(f"{url}",timeout=60)

        #https request data
        status_code = site.status_code
        status_reason = site.reason

        #analyzing site data via BeautifulSoup
        data = site.text
        convert = BeautifulSoup(data, features='lxml')
        search = convert.find_all(f"{scrape_html}",class_=f"{scrape_class}")
        result = list(search)
        for item in enumerate(result):
            scrape_session_memory.append(item)

        try:
            #generate scraping session .txt report
            scrape_report(f"{time()}",status_code,status_reason,str_mem)
            display_message(f"Success:  {url} html + class report created in directory.")

        except:
            display_message(f"Error:  could not generate {url} scrape report.")
        
        try:
            session.close()
            scrape_session_memory.clear()
            
        except:
            display_message(f"Memory error:  please exit program.")
        
    except requests.ConnectionError as e:
        display_message(f"Connection Error:  {url} not found.")

    except requests.Timeout as e:
        display_message(f"Timeout Error:  {url} not found.")

    except requests.RequestException as e:
        display_message(f"Unspecified Error:  {url} not found.")


#File menu variable:  "close"
def close():
    quit()


#File menu variable:  "reset"
def reset():
    try:
        robots_txt_entry.delete(0,END)
        robots_txt_entry.insert(0,"")
        webpage_entry.delete(0,END)
        webpage_entry.insert(0,"")
        html_entry.delete(0,END)
        html_entry.insert(0,"")
        class_entry.delete(0,END)
        class_entry.insert(0,"")
        status_message.delete(0,END)
        status_message.insert(0,"")
    except:
        display_message("Error:  could not clear widget contents.")


"""

Tkinter GUI template widgets

This section contains the variables for the GUI widgets.


"""


#Tkinter root window GUI variables
root = Tk()
root.wm_title("Wishing Well   |   web scraper")
root.geometry("600x250")
root.resizable(False,False)


#set directory GUI variables
set_cwd_entry = Entry(root)
set_cwd_entry.place(x=100,y=20,width=475)
set_cwd_entry.insert(0,f"{directory}")
set_cwd_label = Label(root,text="directory",fg="Blue")
set_cwd_label.place(x=20,y=20)


#check website GUI variables
base_url_entry = Entry(root)
base_url_entry.place(x=100,y=60,width=475)
base_url_entry.insert(0,"https://example.com/")

base_url_label = Label(root,text="base URL",fg="Blue")
base_url_label.place(x=20,y=60)


#scrape webpage GUI variables
webpage_entry = Entry(root)
webpage_entry.place(x=100,y=100,width=475)
webpage_entry.insert(0,"https://example.com/specific-page/within-website")

webpage_label = Label(root,text="target page",fg="Blue")
webpage_label.place(x=20,y=100)


#HTML entry GUI variables
html_entry = Entry(root)
html_entry.place(x=100,y=140,width=60)

html_label = Label(root,text="HTML",fg="Blue")
html_label.place(x=20,y=140)


#HTML class entry GUI variables
class_entry = Entry(root)
class_entry.place(x=220,y=140,width=120)

class_label = Label(root,text="Class",fg="Blue")
class_label.place(x=170,y=140)


#Application status update messages GUI variables
status_message = Entry(root)
status_message.place(x=20,y=205,width=540)

status_message_label = Label(root,text="Status Updates",fg="Black")
status_message_label.place(x=20,y=225)


#menu bar GUI variables
menu = Menu(root)
root.config(menu=menu)


#file menu GUI variables
file_menu = Menu(menu)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Close", command=close)
file_menu.add_command(label="Reset",command=reset)


#base url menu GUI variables
base_url_menu = Menu(menu)
menu.add_cascade(label="base URL", menu=base_url_menu)
base_url_menu.add_command(label="robots.txt",command=robots)


#target webpage menu GUI variables
target_page_menu = Menu(menu)
menu.add_cascade(label="target page", menu=target_page_menu)
target_page_menu.add_command(label="HTML and class",command=scrape_page)



"""


__main__ program entry point


"""


if __name__ == "__main__":
    root.mainloop()