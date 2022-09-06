import phonenumbers # installed
from phonenumbers import timezone,geocoder,carrier

number = input('Enter phone no. with +91 :- ')
phone = phonenumbers.parse(number)                # national
time = timezone.time_zones_for_number(phone)      # timezone
carr = carrier.name_for_number(phone,'en')        # company
reg = geocoder.description_for_number(phone,'en') # country

print(number)
print(phone)
print(time)
print(carr)
print(reg)
