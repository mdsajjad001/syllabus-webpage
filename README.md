# Syllabus Webpage

A Flask web application for **Noori Abraari School** that lets staff fill out a class syllabus form and instantly download a formatted `.docx` document populated from a Word template.

---

## Features

- Web form for selecting a class (LKG–V) and an assessment type (Formative / Summative)
- Dynamically renders per-subject fields (date, day, syllabus portion) based on the selected class
- Auto-fills the day of the week from a chosen date
- Populates a pre-formatted `.docx` template with the submitted data
- Serves the generated document as a downloadable file
- Confirmation page with client-side file cleanup after download

---

## Project Structure

```
syllabus-webpage/
├── app.py                    # Flask application & document generation logic
├── syllabus-template.docx    # Word template with placeholders
├── requirements.txt          # Python dependencies
├── render.yaml               # Render.com deployment environment variables
├── templates/
│   ├── form.html             # Syllabus entry form
│   └── confirm.html          # Download confirmation page
└── static/
    ├── style.css
    ├── style1.css
    ├── print-style.css
    └── generated_docs/       # Temporary output directory for generated files
```

---

## Prerequisites

- Python 3.9+
- pip

---

## Local Setup

1. **Clone the repository**
   ```bash
   git clone <repo-url>
   cd syllabus-webpage
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # macOS / Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the development server**
   ```bash
   python app.py
   ```
   The app will be available at `http://127.0.0.1:5000`.

---

## Usage

1. Open the app in a browser.
2. Select an **Assessment Title** and a **Class** from the dropdowns.
3. Subject-specific fields appear automatically — enter the exam date and syllabus portion for each subject.
4. Click **Generate Document**.
5. The app fills `syllabus-template.docx` with the submitted data and prompts a download.

### Template Placeholders

The Word template uses the following placeholders, which are replaced at runtime:

| Placeholder    | Replaced with              |
|----------------|----------------------------|
| `{assessment}` | Assessment title (uppercased) |
| `{class}`      | Class name                 |
| `(month)`      | Month of the latest exam date |
| `(year)`       | Year of the latest exam date  |

The first table in the template is filled with rows of: **Date · Day · Subject · Syllabus Portion**, sorted by date.

---

## Deployment

The project includes a [`render.yaml`](render.yaml) for deployment on [Render](https://render.com). Set the following environment variables in your Render service dashboard:

| Variable                  | Description                        |
|---------------------------|------------------------------------|
| `FLASK_SECRET_KEY`        | Flask session secret key           |
| `GOOGLE_OAUTH_CLIENT_ID`  | Google OAuth client ID (reserved)  |
| `GOOGLE_OAUTH_CLIENT_SECRET` | Google OAuth client secret (reserved) |

The app is served in production via **Gunicorn** (included in `requirements.txt`).

---

## Dependencies

| Package            | Version   | Purpose                              |
|--------------------|-----------|--------------------------------------|
| Flask              | 3.0.0     | Web framework                        |
| python-docx        | 1.1.0     | Read/write `.docx` files             |
| gunicorn           | 21.2.0    | Production WSGI server               |
| Flask-Login        | 0.6.3     | User session management (reserved)   |
| Flask-Dance        | 7.1.0     | Google OAuth integration (reserved)  |
| docx2pdf           | 0.1.8     | PDF conversion (reserved)            |
| python-dateutil    | ≥2.8.0    | Flexible date parsing                |
