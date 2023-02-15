# import smtplib
#
# my_email = "fake@gmail.com"
# # will replace with pw given when log in
# password = "abcd1234()"
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     #makes connection encrypted and secure
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="fake@yahoo.com",
#         msg="Subject: Hello\n\n This is the body of my email")
#
#


# connection.close()


# import datetime as dt
#
# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()
#
# # when createing date obj only required year, month, day
# date_of_birth = dt.datetime(year=1995, month=12, day=15)
# print(date_of_birth)


"""send motivational quote via email on current weekday
1.use the datetime module to obtain current day of week
2.open quotes.txt file and obtain list of quotes
3. use random module to pick a random quote from list
4. use smtplib to send the email to yourself
"""

import datetime as dt
import random
import smtplib

MY_EMAIL = "fake@gmail.com"
MY_PASSWORD = "1234abcd**"

now = dt.datetime.now()
weekday = now.weekday()
# 0 = Monday
if weekday == 0:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)
    print(quote)

   with smtplib.SMTP("smtp.gmail.com") as connection:
       connection.starttls()
       connection.login(MY_EMAIL, MY_PASSWORD)
       connection.sendmail(
           from_addr=MY_EMAIL,
           to_address=MY_EMAIL,
           msg=f"Subject:Monday Motivation \n\n{quote}"
       )







