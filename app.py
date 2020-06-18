from flask import Flask, jsonify, request
from libs.helper import fetch_data, getDate


app = Flask(__name__)


# yesToday = getDate()


url = "https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_daily_reports/"


@app.route('/api/v1', methods=["GET"])
@app.route('/api/v1/<date>', methods=["GET"])
def index(date=None):
    query_date = request.args.get("date")

    if date is None:
        if query_date is not None:
            d = query_date
        else:
            d = getDate()
        data = fetch_data(url, date=d)
    else:
        data = fetch_data(url, date)
    
    return jsonify({"total_cases" : data })


if __name__ == "__main__":
    app.run(debug=True)


