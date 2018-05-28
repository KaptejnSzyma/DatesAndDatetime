import datetime
import pytz

countries = {1: "Asia/Baku",
             2: "Europe/Warsaw",
             3: "Africa/Johannesburg",
             4: "America/Punta_Arenas",
             5: "Australia/Melbourne"}
for i in countries:
    print("{}: {}".format(i, countries[i]))

while True:
    a = int(input("\nChoose one of the timezones above or type '0' to quit: "))

    if a == 0:
        break

    if a in countries.keys():
        tz_to_display = pytz.timezone(countries[a])
        chosen_time = datetime.datetime.now(tz=tz_to_display)

        print("\nChosen timezone: {}, current time: {}".format(countries[a], chosen_time.strftime("%x %X")))
        print("Local time: {}".format(datetime.datetime.now().strftime("%X")))
        print("UTC Time: {}".format(datetime.datetime.utcnow().strftime("%X")))

