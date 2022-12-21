from datetime import datetime
from datetime import timedelta

def date_in_future(uday):

    today = datetime.now()
    try:
        future = today
        future = future + timedelta(days=int(uday))
    finally:
        return future.strftime("%d-%m-%Y %H:%M:%S");

print("This programm see future")
print("If you write non-integers programm do erorr")
usr = input("Input days: ")
print(date_in_future(usr))

