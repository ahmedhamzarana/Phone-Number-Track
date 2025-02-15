import phonenumbers
from phonenumbers import timezone, geocoder, carrier

number = input("Enter your phone number: ")

phone = phonenumbers.parse(number)

time = timezone.time_zones_for_number(phone)

reg = geocoder.description_for_number(phone, "en")

country_code = phone.country_code

country_name = geocoder.country_name_for_number(phone, "en")

national_number = str(phone.national_number)

service_provider = carrier.name_for_number(phone, "en")

print(f"National Number: {national_number}")
print(f"Country Code: {country_code}")
print(f"Location: {reg}")
print(f"Time Zone: {time}")
print(f"Service Provider: {service_provider}")
print(f"Country Name: {country_name}")
