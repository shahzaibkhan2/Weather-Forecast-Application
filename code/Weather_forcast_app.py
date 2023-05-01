# IMPORTING MODULES
from tkinter import *
from tkinter import ttk
import requests


# FUNCTION TO GET CITY NAME AND WEATHER CONDITIONS FROM THE DATA COLLECTED FROM API
def get_city():
    city = city_name.get()
    data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=871e9f8eef799701bdc978ec1979ea1d").json()
    weather1_label.config(text=data["weather"][0]["main"])
    description1_label.config(text=data["weather"][0]["description"])
    temperature1_label.config(text=str(data["main"]["temp"] - 273.15))
    pressure1_label.config(text=data["main"]["pressure"])

# TKINTER MAIN ROOT AND ITS FEATURES
root = Tk()

root.title('Accurate Weather Forcast')
root.geometry("950x650")
root.config(bg="lightblue")

# LABELS
name_label = Label(root,text="Accurate Weather Forcast",font=("Arial",30,"bold"))
name_label.place(x=25,y=50,height=50,width=900)

city_name = StringVar()
list_names = ["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]
combo = ttk.Combobox(root,text="Accurate Weather Forcast",font=("Arial",15),values=list_names,textvariable=city_name)
combo.place(x=300,y=120,height=35,width=300)

# LABELS FOR THE PARAMETERS
weather_label = Label(root,text="Weather Climate :",font=("Arial",20,"bold"),bg="lightblue")
weather_label.place(x=2,y=300,height=50,width=250)

weather1_label = Label(root,text="",font=("Arial",20),bg="lightblue")
weather1_label.place(x=250,y=300,height=50,width=450)

description_label = Label(root,text="Weather Description :",font=("Arial",20,"bold"),bg="lightblue")
description_label.place(x=3,y=380,height=50,width=300)
description1_label = Label(root,text="",font=("Arial",20),bg="lightblue")
description1_label.place(x=300,y=380,height=50,width=450)

temperature_label = Label(root,text="Weather Temperature :",font=("Arial",20,"bold"),bg="lightblue")
temperature_label.place(x=1,y=460,height=50,width=310)
temperature1_label = Label(root,text="",font=("Arial",20),bg="lightblue")
temperature1_label.place(x=360,y=460,height=50,width=390)

pressure_label = Label(root,text="Weather Pressure :",font=("Arial",20,"bold"),bg="lightblue")
pressure_label.place(x=0,y=540,height=50,width=260)
pressure1_label = Label(root,text="",font=("Arial",20),bg="lightblue")
pressure1_label.place(x=370,y=540,height=50,width=200)

find_button = Button(root,text="Find",font=("Arial",20,"bold"),command=get_city)
find_button.place(x=380,y=210,height=50,width=150)

# MAIN LOOP TO OPEN APPLICATION
root.mainloop()
