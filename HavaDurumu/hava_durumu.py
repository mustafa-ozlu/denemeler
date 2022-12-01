''' written by B.SasiVatsal on 22nd Jan,2022 '''

# importing all the required libraries
from tkinter import *
import tkinter,requests
from tkinter.font import BOLD
from urllib import response
from tkinter import BOTH
from PIL import ImageTk, Image
from io import BytesIO
from cv2 import FONT_HERSHEY_COMPLEX

''' defining the global varibales that are to be used throught the development '''
sky_blue = "#171010"
green_color = "#EC0101"
output_color = "red"
input_color = "#3D0000"
# defining font style and size, can be changed later
large_font = ('SimSun', 20)
small_font = ('Simsun', 15)

# creating an object of TK class
root = tkinter.Tk()
# making a title for the app
root.title("Havva Durumu")
# adding icon to the app
#root.iconbitmap(r'\weather.ico')
# defining dimensions of the appp
root.geometry('500x500')
# making the app non-reszable to avoid scaling issues
root.resizable(0,0)

'''==========='''
''' FUNCTIONS '''
'''==========='''

def get_current_weather():
    city_name = response['name']
    city_lat = str(response['coord']['lat'])
    city_lon = str(response['coord']['lon'])
    main_weather = response['weather'][0]['main']
    description = response['weather'][0]['description']
    tempc = response['main']['temp']
    temp = str(tempc)
    feels_like = str(response['main']['feels_like'])
    temp_min = str(response['main']['temp_min'])
    temp_max = str(response['main']['temp_max'])
    humidity = str(response['main']['humidity'])

    # updating the gui using label.config() method
    
    test_canvas.itemconfig(city_info_label,text=city_name + " (" + city_lat + ", " + city_lon + ")")
    test_canvas.itemconfig(weather_label,text="Hava Durumu:  \t"  + description)
    test_canvas.itemconfig(temp_label,text='Sıcaklık:  \t' + temp + " °C")
    test_canvas.itemconfig(feels_label,text="Hissedilen:  \t" + feels_like + " °C")
    test_canvas.itemconfig(temp_min_label,text="Min Sıcaklık:\t" + temp_min + " °C")
    test_canvas.itemconfig(temp_max_label,text="Max Sıcaklık:\t" + temp_max + " °C")
    test_canvas.itemconfig(humidity_label,text="Nem:  \t\t%" + humidity)

''' adding icons depending on climate condition for more user interactivity '''

def get_current_climate_icon():
    global icon
    # getting the icon from API response
    iconss = response['weather'][0]['icon']
    # requesting weather icon from the same api
    url = 'http://openweathermap.org/img/wn/{icon}.png'.format(icon=iconss)
    # after receving the desired icon we have to download it in order to display
    # its can be implemented by giving argument stream=TRUE 
    icon_response = requests.get(url, stream=True)
    img_data = icon_response.content  
    '''The ImageTk module contains support to create and modify 
        Tkinter BitmapImage and PhotoImage objects from PIL images'''
    icon = ImageTk.PhotoImage(Image.open(BytesIO(img_data)))
    #Update label
    test_canvas.create_image(212.5,73,image=icon)


# main function form which everything is operated
def submit_search():
    global response
    url = ' http://api.openweathermap.org/data/2.5/weather'
    api_key = 'YOUR_OPENWEATHERMAP_APIKEY'
    #  get: () -> str, to convert it into the string
    queryy = {"q":cityy_name.get(),'units':'metric','appid':api_key ,'lang':'tr'}
    # calling the api using request method in request module
    response = requests.request("GET",url,params=queryy)
    response = response.json()

    get_current_weather()
    get_current_climate_icon()


# making frames using Frame() method in tkinter
up_frame = tkinter.Frame(root, bg=sky_blue, height=350)
down_frame = tkinter.Frame(root,  bg=green_color)
# pack() is method is used to simply pack the attributes we defined in frame()
up_frame.pack(fill=BOTH, expand=True)
down_frame.pack( expand=True)

output_frame = tkinter.LabelFrame(up_frame,bg=output_color, width=425, height=350)
test_canvas = tkinter.Canvas(output_frame,width=425, height=350,bg=output_color, highlightthickness=False)
imgg = PhotoImage(file="bg.png")
test_canvas.create_image(2.5,227.5,image=imgg)

city_info_label = test_canvas.create_text(210,40,text="Şehir",fill="#FF0000",font=(FONT_HERSHEY_COMPLEX,20,'bold'))
weather_label = test_canvas.create_text(212.5,100,text="Hava Durumu: ",fill=output_color,font=(FONT_HERSHEY_COMPLEX,15,'bold'))
temp_label = test_canvas.create_text(212.5,130,text='Sıcaklık: ',fill=output_color,font=(FONT_HERSHEY_COMPLEX,15,'bold'))
feels_label = test_canvas.create_text(212.5,160,text="Hissedilen: ",fill=output_color,font=(FONT_HERSHEY_COMPLEX,15,'bold'))
temp_max_label = test_canvas.create_text(212.5,190,text="Min Sıcaklık: ",fill=output_color,font=(FONT_HERSHEY_COMPLEX,15,'bold'))
temp_min_label = test_canvas.create_text(212.5,220,text="Max Sıcaklık: ",fill=output_color,font=(FONT_HERSHEY_COMPLEX,15,'bold'))
humidity_label = test_canvas.create_text(212.5,250,text="Nem: ",fill=output_color,font=(FONT_HERSHEY_COMPLEX,15,'bold'))

input_frame = tkinter.LabelFrame(down_frame, bg=input_color, width=425)
output_frame.pack(pady=20)

output_frame.pack_propagate(0)
# u know pad is used for passing y for y-side and x for x-side
input_frame.pack(pady=0)
# packing all teh attributes defined in the create_textl() method together
test_canvas.pack()

''' This section contains text field to take user input '''
# The Entry Widget is a Tkinter Widget used to Enter 
# or display a single line of text. 
heading = tkinter.Label(input_frame,text="Şehir İsmi girin:",font=('Arial', 15,BOLD), bg=input_color,fg=output_color)
cityy_name = tkinter.Entry(input_frame,justify='center', width=33, font=('SimSun', 17))
cityy_name.focus()
# submit button using button() in tkinetr
submit_button = tkinter.Button(input_frame, text='Arama', font=('SimSun', 17,BOLD), bg=input_color,fg=output_color, command=submit_search)
cityy_name.grid(row=1, column=0, padx=(5,0), pady=(0,5))
submit_button.grid(row=1, column=1, padx=5,pady=(0,5))
heading.grid(row=0, column=0,pady=(5,5))


# mainloop() is reason for app to run
root.mainloop()
