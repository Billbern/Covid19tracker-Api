import csv
import requests
import datetime
from io import StringIO


countries = ["Benin", "Burkina Faso", "Cape Verde", "Gambia", "Ghana", "Guinea", "Guinea-Bissau", "Cote d'Ivoire", "Liberia", "Mali", "Mauritania", "Niger", "Nigeria", "Senegal", "Sierra Leone","Togo"]



def getDate(number_of_days=1):
    """
        Fetch the data of the last update from the number of days given.
        
        :param number_of_days defaults to 1 but can take any number of days
    """
    check_today = datetime.datetime.now().replace(hour=4,minute=0,second=0,microsecond=0)
    today = datetime.datetime.today()
    if today < check_today:
        yesterday = today - datetime.timedelta(days=number_of_days+1)
    else:
        yesterday = today - datetime.timedelta(days=number_of_days)
    return yesterday.strftime('%m-%d-%Y')



def fetch_data(url, date=None):
    data = []
    raw_data = requests.get(url+date+".csv").content.decode("ascii")
    decoded_data = StringIO(raw_data)
    actual_data = csv.reader(decoded_data)
    
    for items in actual_data:
        if items[3] in countries:
            data.append({"id": len(data)+1,"Country" : items[3], "Confirmed" : items[7], "Deaths": items[8], "Recovered": items[9], "Active": items[10]})
    return data
