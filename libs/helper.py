import csv
import requests
import datetime
from io import StringIO
from typing import List, Dict, Optional
import logging
from config import Config

logger = logging.getLogger(__name__)

def getDate(number_of_days: int = 1) -> str:
    """
    Fetch the date for the data update.
    
    :param number_of_days: Number of days to look back.
    :return: Formatted date string (MM-DD-YYYY).
    """
    now = datetime.datetime.now()
    check_time = now.replace(hour=4, minute=0, second=0, microsecond=0)
    
    if now < check_time:
        target_date = now - datetime.timedelta(days=number_of_days + 1)
    else:
        target_date = now - datetime.timedelta(days=number_of_days)
        
    return target_date.strftime('%m-%d-%Y')

def fetch_data(url: str, date: str) -> List[Dict]:
    """
    Fetch and parse COVID-19 data for a specific date.
    
    :param url: Base URL for the CSV files.
    :param date: The date string (MM-DD-YYYY).
    :return: List of dictionaries containing country data.
    """
    full_url = f"{url}{date}.csv"
    try:
        response = requests.get(full_url, timeout=10)
        response.raise_for_status()
        
        raw_data = response.content.decode("utf-8")
        decoded_data = StringIO(raw_data)
        
        reader = csv.DictReader(decoded_data)
        
        data = []
        for row in reader:
            country = row.get("Country_Region") or row.get("Country/Region")
            
            if country in Config.WEST_AFRICAN_COUNTRIES:
                data.append({
                    "id": len(data) + 1,
                    "Country": country,
                    "Confirmed": row.get("Confirmed", "0"),
                    "Deaths": row.get("Deaths", "0"),
                    "Recovered": row.get("Recovered", "0"),
                    "Active": row.get("Active", "0")
                })
        return data

    except requests.exceptions.RequestException as e:
        logger.error(f"Error fetching data from {full_url}: {e}")
        return []
    except Exception as e:
        logger.error(f"Unexpected error parsing data: {e}")
        return []
