from flask import Blueprint, jsonify, request
from app.services.covid_service import fetch_covid_data, get_date
import logging

logger = logging.getLogger(__name__)
bp = Blueprint('api', __name__)

@bp.route('', methods=["GET"])
@bp.route('/<date>', methods=["GET"])
def get_covid_data(date=None):
    """
    Endpoint to fetch COVID-19 data.
    """
    search_date = date 

    if search_date:
        search_date = get_date(int(search_date))
    else:
        search_date = get_date()

    print("\n\n", search_date, "\n\n")
    
    logger.info(f"Fetching data for date: {search_date}")
    
    try:
        data = fetch_covid_data(search_date)
        
        if not data:
            return jsonify({
                "status": "error",
                "message": f"No data found for date {search_date}.",
                "total_cases": []
            }), 404
            
        return jsonify({
            "status": "success",
            "date": search_date,
            "total_cases": data
        })

    except Exception as e:
        logger.error(f"Error processing request for date {search_date}: {e}")
        return jsonify({
            "status": "error",
            "message": "An internal error occurred."
        }), 500
