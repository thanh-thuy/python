from datetime import datetime


def santaclaus():
    today = datetime.today().strftime("%j")
    ending_day_of_current_year = int(datetime.now().date().replace(month=12, day=25).strftime("%j"))
    print("santa clause ", ending_day_of_current_year - int(today), "days left")
    return


santaclaus()
