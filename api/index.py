from flask import Flask, render_template, url_for, send_from_directory
import sys
import os

# Add parent directory to path so we can import config
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import PROFILE, PROJECTS, NOTEBOOKS, PAPERS, ACHIEVEMENTS, ACHIEVEMENT_DESCRIPTION, CERTIFICATIONS

app = Flask(__name__, 
           static_folder='../static',    
           template_folder='../templates' 
)

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

if __name__ == '__main__':
    app.run()
    
# File download route
@app.route('/download/<filename>')
def download_file(filename):
    """
    Serve static files for download from the 'static' directory.
    """
    return send_from_directory('static/files', filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)