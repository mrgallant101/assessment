import pandas
import smtplib
import datetime as dt

MY_EMAIL = "ojochenemesani@gmail.com"
MY_PASSWORD = "simonsani"

now = dt.datetime.now()
year = now.year
month = now.month
day = now.day

data = pandas.read_csv("users_info.csv")
all_emails = data.email.to_list()

if month == 10 and day == 1:
    for email in all_emails:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=email,
                                msg=f"Subject:Happy Independence Day\n\nHappy independence to all Nigerians across the "
                                    f"world. God bless nigeria")
