from pydoc import locate
from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox, Image
from timezonefinder import TimezoneFinder
from datetime import *
import requests
import pytz
from PIL import Image, ImageTk

# Create the root window
root = Tk()
root.title("Weather App")
root.geometry("890x470+300+300")
root.configure(bg="#57adff")
root.resizable(False, False)

import requests
from datetime import datetime
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
import pytz

def getweather():
    city = textfield.get()
    geolocator = Nominatim(user_agent="weather_app")
    try:
        location = geolocator.geocode(city)
    except Exception as e:
        print(f"Geocoding error: {e}")
        return

    if location:
        try:
            obj = TimezoneFinder()
            result = obj.timezone_at(lng=location.longitude, lat=location.latitude)
            if result:
                timezone.config(text=result)
                long_lat.config(text=f"({round(location.latitude, 4)}ºN, {round(location.longitude, 4)}ºE)")

                # Get current time in the found timezone
                home_timezone = pytz.timezone(result)
                local_time = datetime.now(home_timezone)
                current_time = local_time.strftime("%I:%M %p")
                clock.config(text=current_time)

                # Call Weatherbit API using latitude and longitude
                lat = location.latitude
                lon = location.longitude
                weatherbit_api = f"https://api.weatherbit.io/v2.0/forecast/hourly?lat={lat}&lon={lon}&key=e171355b6854414783a29bbf95e6b468&hours=240"
                data=json_data = requests.get(weatherbit_api).json()
                # Get weather data for the first hour (current weather)
                first_hour = json_data['data'][0]
                temp = first_hour['temp']
                weather_description = first_hour['weather']['description']
                wind_speed = first_hour['wind_spd']
                humidity = first_hour['rh']
                pressure = first_hour['pres']

                t.config(text=f"{temp}°C")
                h.config(text=f"{humidity}%")
                p.config(text=f"{pressure} hPa")
                w.config(text=f"{wind_speed} m/s")
                d.config(text=weather_description)



                day1_icon = data['data'][0]['weather']['icon']
                day1_temp_day = max([data['data'][i]['temp'] for i in range(0, 24)])  # Max temperature in the first 24 hours (Day 1)
                day1_temp_night = min([data['data'][i]['temp'] for i in range(0, 24)])  # Min temperature in the first 24 hours (Night 1)


                image1 = Image.open(f"icon/{day1_icon}.png")
                resized_image = image1.resize((70,70))
                photo1 = ImageTk.PhotoImage(resized_image)
                firstimage.config(image=photo1)
                firstimage.image = photo1
                day1temp.config(text=f"Day:{day1_temp_day}\n Night:{day1_temp_night}")
                # For Day 2 (hours 24 to 48)

                day2_icon = data['data'][24]['weather']['icon']
                day2_temp_day = max([data['data'][i]['temp'] for i in range(24, 48)])  # Max temperature in the next 24 hours (Day 2)
                day2_temp_night = min([data['data'][i]['temp'] for i in range(24, 48)])  # Min temperature in the next 24 hours (Night 2)

                image2 = Image.open(f"icon/{day2_icon}.png")
                resized_image = image2.resize((40,40))
                print(resized_image)
                photo2 = ImageTk.PhotoImage(resized_image)
                secondimage.config(image=photo2)
                secondimage.image = photo2

                day2temp.config(text=f"Day:{day2_temp_day}\n Night:{day2_temp_night}")#it is correct
                # For Day 3 (hours 48 to 72)

                day3_icon = data['data'][48]['weather']['icon']
                day3_temp_day = max([data['data'][i]['temp'] for i in range(48, 72)])  # Max temperature in the next 24 hours (Day 3)
                day3_temp_night = min([data['data'][i]['temp'] for i in range(48, 72)])  # Min temperature in the next 24 hours (Night 3)

                image3 = Image.open(f"icon/{day3_icon}.png")
                resized_image = image3.resize((40,40))
                photo3 = ImageTk.PhotoImage(resized_image)
                thirdimage.config(image=photo3)
                thirdimage.image = photo3
                day3temp.config(text=f"Day:{day3_temp_day}\n Night:{day3_temp_night}")
                # For Day 4 (hours 72 to 96)

                day4_icon = data['data'][72]['weather']['icon']
                day4_temp_day = max([data['data'][i]['temp'] for i in range(72, 96)])  # Max temperature in the next 24 hours (Day 4)
                day4_temp_night = min([data['data'][i]['temp'] for i in range(72, 96)])  # Min temperature in the next 24 hours (Night 4)
                image4 = Image.open(f"icon/{day4_icon}.png")
                resized_image = image4.resize((40,40))
                photo4 = ImageTk.PhotoImage(resized_image)
                fourthimage.config(image=photo4)
                fourthimage.image = photo4
                day4temp.config(text=f"Day:{day4_temp_day}\n Night:{day4_temp_night}")

                # For Day 5 (hours 96 to 120)

                day5_icon = data['data'][96]['weather']['icon']
                day5_temp_day = max([data['data'][i]['temp'] for i in range(96, 120)])  # Max temperature in the next 24 hours (Day 5)
                day5_temp_night = min([data['data'][i]['temp'] for i in range(96, 120)])  # Min temperature in the next 24 hours (Night 5)
                image5 = Image.open(f"icon/{day5_icon}.png")
                resized_image = image5.resize((40,40))
                photo5 = ImageTk.PhotoImage(resized_image)
                fifthimage.config(image=photo5)
                fifthimage.image = photo5
                day5temp.config(text=f"Day:{day5_temp_day}\n Night:{day5_temp_night}")
                # For Day 6 (hours 120 to 144)

                day6_icon = data['data'][120]['weather']['icon']
                day6_temp_day = max([data['data'][i]['temp'] for i in range(120, 144)])  # Max temperature in the next 24 hours (Day 6)
                day6_temp_night = min([data['data'][i]['temp'] for i in range(120, 144)])  # Min temperature in the next 24 hours (Night 6)
                image6 = Image.open(f"icon/{day6_icon}.png")
                resized_image = image6.resize((40,40))
                photo6 = ImageTk.PhotoImage(resized_image)
                sixthimage.config(image=photo6)
                sixthimage.image = photo6
                day6temp.config(text=f"Day:{day6_temp_day}\n Night:{day6_temp_night}")

                # For Day 7 (hours 144 to 168)
                day7_icon = data['data'][144]['weather']['icon']
                day7_temp_day = max([data['data'][i]['temp'] for i in range(144, 168)])
                day7_temp_night = min([data['data'][i]['temp'] for i in range(144, 168)])


                image7 = Image.open(f"icon/{day7_icon}.png")
                resized_image = image7.resize((40,40))
                photo7 = ImageTk.PhotoImage(resized_image)
                seventhimage.config(image=photo7)
                seventhimage.image = photo7
                day7temp.config(text=f"Day:{day7_temp_day}\n Night:{day7_temp_night}")


# Display forecast for the next 7 days
                first = datetime.now()
                day1.config(text=first.strftime("%A"))
                second = first + timedelta(days=1)
                day2.config(text=second.strftime("%A"))
                third = first + timedelta(days=2)
                day3.config(text=third.strftime("%A"))
                fourth = first + timedelta(days=3)
                day4.config(text=fourth.strftime("%A"))
                fifth = first + timedelta(days=4)
                day5.config(text=fifth.strftime("%A"))
                sixth = first + timedelta(days=5)
                day6.config(text=sixth.strftime("%A"))
                seventh = first + timedelta(days=6)
                day7.config(text=seventh.strftime("%A"))

            else:
                timezone.config(text="Timezone not found")
                long_lat.config(text="")
                clock.config(text="")
        except Exception as e:
            print(f"Error occurred: {e}")
    else:
        timezone.config(text="Location not found")
        long_lat.config(text="")
        clock.config(text="")

#icons
image_icon=PhotoImage(file="images/cloudy.png")
root.iconphoto(False,image_icon)

image = Image.open("images/rectangle.png")
resized_image = image.resize((200,150))
round_box = ImageTk.PhotoImage(resized_image)
Label(root, image=round_box, bg="#57adff").place(x=30, y=110)

label1 = Label(root, text="Temperature", font=('Helvetica', 11), fg="white", bg="#000000")
label1.place(x=50, y=120)
label1 = Label(root, text="Humidity", font=('Helvetica', 11), fg="white", bg="#000000")
label1.place(x=50, y=145)
label1 = Label(root, text="Pressure", font=('Helvetica', 11), fg="white", bg="#000000")
label1.place(x=50, y=170)
label1 = Label(root, text="Wind speed", font=('Helvetica', 11), fg="white", bg="#000000")
label1.place(x=50, y=195)
label1 = Label(root, text="Description", font=('Helvetica', 11), fg="white", bg="#000000")
label1.place(x=50, y=220)


search_image = Image.open("images/search_bar.png").resize((500,70))  # Provide dimensions as a tuple
search_photo = ImageTk.PhotoImage(search_image)
myimage = Label(root, image=search_photo, bg="#57adff")
myimage.place(x=260, y=120)

# Text field for input (Fixing missing parentheses and parameters)
textfield = tk.Entry(root, justify='center', width=15, font=('poppins', 25, 'bold'),
                     bg="#203243", border=0, fg="white")
textfield.place(x=395, y=135)
textfield.focus()
#
# Search Icon Button (Resized)
search_icon = Image.open("images/search.png").resize((50, 50))  # Resize the search icon
search_photo_icon = ImageTk.PhotoImage(search_icon)
myimage_icon = Button(root, image=search_photo_icon, borderwidth=0, cursor="hand2", bg="#203243",command=getweather)
myimage_icon.place(x=680, y=130)

# Bottom box frame
frame = Frame(root, width=900, height=180, bg="#212120")
frame.pack(side=BOTTOM)

# Load and resize bottom box images
# First box image (resized)
box = Image.open("images/rectangle.png").resize((200, 125))  # Resize to 50x50
firstbox = ImageTk.PhotoImage(box)

# Second box image (resized)
second_box_img = Image.open("images/day.png").resize((90,125))
secondbox = ImageTk.PhotoImage(second_box_img)

# Place the bottom boxes correctly
Label(frame, image=firstbox, bg="#212120").place(x=30, y=20)  # First box placed
Label(frame, image=secondbox, bg="#212120").place(x=270, y=20)
Label(frame, image=secondbox, bg="#212120").place(x=370, y=20)
Label(frame, image=secondbox, bg="#212120").place(x=470, y=20)
Label(frame, image=secondbox, bg="#212120").place(x=570, y=20)
Label(frame, image=secondbox, bg="#212120").place(x=670, y=20)
Label(frame, image=secondbox, bg="#212120").place(x=770, y=20)



# Clock (displays the current time)
clock = Label(root, font=("Helvetica", 30, 'bold'), fg="white", bg="#57adff")
clock.place(x=30, y=20)

# Timezone label
timezone = Label(root, font=("Helvetica", 20), fg="white", bg="#57adff")
timezone.place(x=700, y=20)

# Latitude and Longitude label
long_lat = Label(root, font=("Helvetica", 10), fg="white", bg="#57adff")
long_lat.place(x=700, y=50)

#
# # Temperature, Humidity, Pressure, Wind Speed, and Description labels
t = Label(root, font=("Helvetica", 11), fg="white", bg="#000000")
t.place(x=140, y=120)
h = Label(root, font=("Helvetica", 11), fg="white", bg="#000000")
h.place(x=140, y=145)
p = Label(root, font=("Helvetica", 11), fg="white", bg="#000000")
p.place(x=140, y=170)
w = Label(root, font=("Helvetica", 11), fg="white", bg="#000000")
w.place(x=140, y=195)
d = Label(root, font=("Helvetica", 11), fg="white", bg="#000000")
d.place(x=140, y=220)

firstframe = Frame(frame, width=200, height=125, bg="#000000")
firstframe.place(x=30, y=20)
day1 = Label(firstframe, font="arial 16", fg="white", bg="#000000")
day1.place(x=100, y=5)
firstimage = Label(firstframe, bg="#000000")
firstimage.place(x=20, y=30)

day1temp=Label(firstframe,font="Verdana 12",bg="#000000",fg="#000fff")
day1temp.place(x=100,y=60)

secondframe = Frame(frame, width=90, height=125, bg="#000000")
secondframe.place(x=270, y=20)
day2 = Label(secondframe, font="arial 14", fg="white", bg="#000000")
day2.place(x=10, y=5)

secondimage = Label(secondframe, bg="#000000")
secondimage.place(x=30, y=35)

day2temp=Label(secondframe,font="Verdana 10",bg="#000000",fg="#fff")
day2temp.place(x=10,y=80)

threeframe = Frame(frame, width=90, height=125, bg="#000000")
threeframe.place(x=370, y=20)
day3 = Label(threeframe, font="arial 14", fg="white", bg="#000000")
day3.place(x=10, y=5)
thirdimage = Label(threeframe, bg="#000000")
thirdimage.place(x=30, y=35)

day3temp=Label(threeframe,font="Verdana 10",bg="#000000",fg="#fff")
day3temp.place(x=10,y=80)

fourframe = Frame(frame, width=90, height=125, bg="#000000")
fourframe.place(x=470, y=20)
day4 = Label(fourframe, font="arial 14", fg="white", bg="#000000")
day4.place(x=10, y=5)
fourthimage = Label(fourframe, bg="#000000")
fourthimage.place(x=30, y=35)

day4temp=Label(fourframe,font="Verdana 10",bg="#000000",fg="#fff")
day4temp.place(x=10,y=80)

fiveframe = Frame(frame, width=90, height=125, bg="#000000")
fiveframe.place(x=570, y=20)
day5 = Label(fiveframe, font="arial 14", fg="white", bg="#000000")
day5.place(x=10, y=5)
fifthimage = Label(fiveframe, bg="#000000")
fifthimage.place(x=30, y=35)

day5temp=Label(fiveframe,font="Verdana 10",bg="#000000",fg="#fff")
day5temp.place(x=10,y=80)

sixframe = Frame(frame, width=90, height=125, bg="#000000")
sixframe.place(x=670, y=20)
day6 = Label(sixframe, font="arial 14", fg="white", bg="#000000")
day6.place(x=10, y=5)
sixthimage = Label(sixframe, bg="#000000")
sixthimage.place(x=30, y=35)

day6temp=Label(sixframe,font="Verdana 10",bg="#000000",fg="#fff")
day6temp.place(x=10,y=80)

sevenframe = Frame(frame, width=90, height=125, bg="#000000")
sevenframe.place(x=770, y=20)
day7 = Label(sevenframe, font="arial 14", fg="white", bg="#000000")
day7.place(x=10, y=5)
seventhimage = Label(sevenframe, bg="#000000")
seventhimage.place(x=30, y=35)

day7temp=Label(sevenframe,font="Verdana 10",bg="#000000",fg="#fff")
day7temp.place(x=10,y=80)
root.mainloop()
