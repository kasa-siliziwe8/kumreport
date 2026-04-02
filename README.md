# KumReport – Community Waste Reporting System

**NHCI63110 Assignment | Sol Plaatje University | 2026**

KumReport is a Django-based web application that allows Kimberley residents to report missed waste bin collections and track the status of their reports. The system also supports an SMS fallback channel for users without internet access.

---

## Project Structure

```
kumreport/
├── kumreport/              # Main project config
│   ├── settings.py
│   └── urls.py
├── reports/                # App 1: Report submission
│   ├── views.py
│   ├── urls.py
│   └── templates/reports/
│       └── submission.html
├── tracker/                # App 2: Report tracking
│   ├── views.py
│   ├── urls.py
│   └── templates/tracker/
│       └── track.html
├── manage.py
└── requirements.txt
```

---

## Apps

### App 1: `reports`
Handles the report submission flow. Users can submit a missed bin collection report without registering. On submission, a unique reference number (e.g. `KMR-2026-A1B2C`) is generated and displayed.

**URL:** `/` → `reports.views.report_submission`

### App 2: `tracker`
Handles the report tracking flow. Users enter their reference number to view the current status of their report, displayed as a step-by-step progress tracker.

**URL:** `/tracker/` → `tracker.views.track_report`

---

## How to Run

```bash
# 1. Clone the repository
git clone https://github.com/kasa-siliziwe8/kumreport.git
cd kumreport

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run migrations
python manage.py migrate

# 4. Start the development server
python manage.py runserver

# 5. Open in browser
# Report page:  http://127.0.0.1:8000/
# Track page:   http://127.0.0.1:8000/tracker/
```
Password for Admin is: kumreport2026
---

## Demo Reference Numbers (for tracker testing)

| Reference Number | Status |
|---|---|
| KMR-2026-A1B2C | Assigned |
| KMR-2026-D3E4F | Resolved |

---

## Module Info
- **Course:** Human-Computer Interaction (NHCI63110)
- **Institution:** Sol Plaatje University
- **Examiner:** Mrs. K.E Mamabolo
- **Student:** kasa-siliziwe8
