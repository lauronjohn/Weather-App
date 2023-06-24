import tkinter as tk
import requests
import time
import os


def getWeather(canvas):
    city = textfield.get()
    geoapi = "https://api.openweathermap.org/data/2.5/weather?q="+ city +"&appid="+str(os.getenv("API_KEY"))
    geojson_data = requests.get(geoapi).json()
    condition = geojson_data['weather'][0]['main']
    #print(condition)
    temp = int(geojson_data['main']['temp'] - 273.15)
    min_temp = int(geojson_data['main']['temp_min'] - 273.15)
    max_temp = int(geojson_data['main']['temp_max'] - 273.15)
    pressure = geojson_data['main']['pressure']
    humdity = geojson_data['main']['humidity']
    sunset = time.strftime("%I:%M:%S", time.gmtime(geojson_data['sys']['sunset'] - 21600))
    sunrise = time.strftime("%I:%M:%S", time.gmtime(geojson_data['sys']['sunrise'] - 21600))

    final_info = condition + "\n" + str(temp) + "°C" 
    final_data = "\n" + "Max Temp: " + str(max_temp) + "\n" + "Min Temp: " + str(min_temp) + "\n" + "Pressure: " + str(pressure) + "\n" + "Humdity: " + str(humdity) + "\n" + "Sunrise Time: " + str(sunrise) + "\n" + "Sunset Time: " + str(sunset)
    label1.config(text = final_info)
    label2.config(text = final_data)

canvas = tk.Tk()
canvas.geometry("600x500")
canvas.title("Lauron's Weather App")

f = ("poppins", 15, "bold")
t = ("poppins", 35, "bold")

textfield = tk.Entry(canvas, font = t)
textfield.pack(pady = 20)
textfield.focus()
textfield.bind('<Return>', getWeather)

label1 = tk.Label(canvas, font= t)
label1.pack()
label2 = tk.Label(canvas, font= f)
label2.pack()

canvas.mainloop()