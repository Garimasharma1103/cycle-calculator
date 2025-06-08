# 🩺 Cycle Calculator API

A simple Flask-based API for estimating key menstrual cycle dates such as period days and ovulation days, based on user-provided data. Useful for health apps, tracking tools, or personal use.

---

## 🚀 Features

* Calculates current cycle status based on the last period date
* Estimates:

  * **Days remaining** until next period
  * **Period days**
  * **Ovulation window**
* Accepts customizable cycle and period lengths
* CORS-enabled for frontend integrations

---

## 🛠️ Tech Stack

* Python 3
* Flask
* Flask-CORS

---

## 📦 Installation

```bash
git clone https://github.com/Garimasharma1103/cycle-calculator.git
cd cycle-calculator
pip install -r requirements.txt
python app.py
```

---

## 🧪 API Usage

### Endpoint

```
POST /api/cycle
```

### Request Body (JSON)

```json
{
  "lastPeriod": "2025-06-01",
  "cycleLength": 28,        // Optional (default: 28)
  "periodLength": 5         // Optional (default: 5)
}
```

### Response (JSON)

```json
{
  "highlightedDays": [1, 2, 3, 4, 5],      // Period days
  "ovulationDays": [14, 15, 16],          // Estimated ovulation window
  "daysLeft": 21                          // Days until next cycle
}
```

---

## 🧠 How It Works

* `highlightedDays`: Calculates the days of the period from the `lastPeriod` date.
* `ovulationDays`: Estimated as 14 days before the next cycle, plus one day before and after.
* `daysLeft`: Number of days until the next expected period start.

---

## 🌐 Deployment

The app is ready for deployment on platforms like **Render**, **Heroku**, etc.

> It respects the `PORT` environment variable for cloud deployment compatibility.

---

## 🔒 Notes

* All date inputs must be in `YYYY-MM-DD` format.
* No persistent storage — calculations are stateless and per request.

---

## 📄 License

[MIT License](LICENSE)

---

## ✍️ Author

[Garima Sharma](https://github.com/Garimasharma1103)
