from flask import Flask, render_template, url_for, send_from_directory
from config import PROFILE, PROJECTS, NOTEBOOKS, PAPERS, ACHIEVEMENTS, ACHIEVEMENT_DESCRIPTION, CERTIFICATIONS

app = Flask(__name__)

# Context processor for dynamic year
@app.context_processor
def utility_processor():
    def get_year():
        from datetime import datetime
        return datetime.now().year
    return dict(get_year=get_year)

# Home route
@app.route('/')
def home():
    return render_template('index.html', 
                           profile=PROFILE, 
                           projects=PROJECTS, 
                           notebooks=NOTEBOOKS, 
                           papers=PAPERS,
                           achievements=ACHIEVEMENTS,
                           achievement_description=ACHIEVEMENT_DESCRIPTION,
                           certifications=CERTIFICATIONS)

# File download route
@app.route('/download/<filename>')
def download_file(filename):
    """
    Serve static files for download from the 'static' directory.
    """
    return send_from_directory('static/files', filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
