from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime, timedelta

app = Flask(__name__)
CORS(app)

@app.route('/api/cycle', methods=['POST'])
def calculate_cycle():
    data = request.get_json()

    try:
        last_period_str = data.get('lastPeriod')
        if not last_period_str:
            return jsonify({"error": "Missing lastPeriod field"}), 400

        # Convert ISO string to datetime object
        last_period = datetime.strptime(last_period_str, '%Y-%m-%d')
        cycle_length = int(data.get('cycleLength', 28))
        period_length = int(data.get('periodLength', 5))

        today = datetime.today()
        days_since = (today - last_period).days
        days_into_cycle = days_since % cycle_length
        days_left = cycle_length - days_into_cycle

        highlighted_days = [
            (last_period + timedelta(days=i)).day for i in range(period_length)
        ]

        ovulation_day = last_period + timedelta(days=cycle_length - 14)
        ovulation_days = [(ovulation_day + timedelta(days=i)).day for i in range(-1, 2)]

        return jsonify({
            'highlightedDays': highlighted_days,
            'ovulationDays': ovulation_days,
            'daysLeft': days_left
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500

import os

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Render will provide PORT env var
    app.run(host='0.0.0.0', port=port)
