import phonenumbers as p
from phonenumbers import carrier,timezone,geocoder

#getting users phone number
num = input('Enter your phone number with a country code:- ')

#getting users phone numbers location, timezone and the carrier
phone = p.parse(num)
np = carrier.name_for_number(phone, 'en')
loc = geocoder.description_for_number(phone, 'en')
timez = timezone.time_zones_for_number(phone)

#prints users carrier name,location and timezone 
if np =='Telewings':
    print('Airtel')
    print(loc)
    print(timez)
else: 
    print(np)
    print(loc)
    print(timez)




