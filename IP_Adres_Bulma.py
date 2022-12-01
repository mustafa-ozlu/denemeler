from ipaddress import ip_address
import geocoder as geo
import requests
import webbrowser

r = requests.get(r'http://jsonip.com')
# r = requests.get(r'https://ifconfig.co/json')
ip= r.json()['ip']
print('IP Adresin\t: {}'.format(ip))


ip=geo.ip(ip)
print("Şehir\t\t: ",ip.city)
print("Enlem Boylam\t: ",ip.latlng)
lat=str(ip.latlng[0])
long=str(ip.latlng[1])

harita=("https://maps.google.com/maps?q="+lat+","+long+"&ll="+lat+","+long+"&z=9")
print("Web tarayıcınızda "+harita+" sayfası açılacaktır.")
webbrowser.open(harita,new=0)
