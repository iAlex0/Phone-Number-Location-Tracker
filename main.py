import phonenumbers
from phonenumbers import geocoder, carrier, timezone
from termcolor import colored

while True:
    number = input("\n" + colored("Ensure you include the country code (e.g. +1 for US)", "yellow") + "\n\nPlease enter a phone number (or 'q' to quit):\nNumber: ")
    if number.lower() == 'q':
        break
    
    # Remove whitespace and dashes from number
    number = number.replace(' ', '').replace('-', '')
    
    try:
        phone_number = phonenumbers.parse("+" + number)
        if not phonenumbers.is_valid_number(phone_number):
            print(colored("Invalid phone number. Please try again.", "red"))
            continue
        
        if phonenumbers.carrier._is_mobile(phone_number):
            print(colored(f"Carrier: {carrier.name_for_number(phone_number, 'en')}", "green"))
        else:
            print(colored("No carrier information available.", "yellow"))
        
        print(colored(f"Result: {geocoder.description_for_number(phone_number, 'en')}", "green"))
        
        time_zone = timezone.time_zones_for_number(phone_number)
        if len(time_zone) > 0:
            print(colored(f"Timezone: {time_zone[0]}", "green"))
        else:
            print(colored("No timezone information available.", "yellow"))
            
        print("\n-----------------------------\n")
    except phonenumbers.phonenumberutil.NumberParseException:
        print(colored("Invalid phone number. Please try again.", "red"))

print("\nGoodbye!")
