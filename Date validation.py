date = input("input a date")

def format(date):
    datelen = len(date)
    if datelen != 8:
        temp  = False
    else:
        temp = True
    return temp


def split(date):
    days = int(date[0:2])
    months = int(date[3:5])
    years = int(date[6:8])


def check_days_months():





