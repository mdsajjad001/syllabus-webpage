from flask import Flask, render_template, request, send_file
from docx import Document
from io import BytesIO
import csv

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        classname = request.form['class']
        date = request.form['date']
        day = request.form['day']
        subjects = [v for k, v in request.form.items() if k.startswith('subject') and v.strip()]
        
        # Generate DOCX
        doc = Document()
        doc.add_heading(f'{classname} Syllabus - {date} ({day})', level=1)
        for i, subject in enumerate(subjects, 1):
            doc.add_paragraph(f'{i}. {subject}', style='List Number')
        
        # Save as in-memory file
        buffer = BytesIO()
        doc.save(buffer)
        buffer.seek(0)

        # Optionally save to CSV
        with open('submissions.csv', 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([classname, date, day] + subjects)

        return send_file(buffer, as_attachment=True, download_name='syllabus.docx')

    return render_template('index.html')
