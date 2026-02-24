import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    BASE_URL = "https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_daily_reports/"
    CORS_HEADERS = 'Content-Type'
    WEST_AFRICAN_COUNTRIES = [
        "Benin", "Burkina Faso", "Cape Verde", "Gambia", "Ghana", "Guinea", 
        "Guinea-Bissau", "Cote d'Ivoire", "Liberia", "Mali", "Mauritania", 
        "Niger", "Nigeria", "Senegal", "Sierra Leone", "Togo"
    ]
    DEBUG = os.getenv("DEBUG", "True").lower() == "true"
    PORT = int(os.getenv("PORT", 5000))
