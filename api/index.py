from flask import Flask, render_template
import sys
import os

# Add parent directory to path so we can import config
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import PROFILE, PROJECTS, NOTEBOOKS, PAPERS, ACHIEVEMENTS, ACHIEVEMENT_DESCRIPTION

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
                         achievement_description=ACHIEVEMENT_DESCRIPTION)

if __name__ == '__main__':
    app.run()