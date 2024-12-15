from flask import Flask, render_template, url_for
from config import PROFILE, PROJECTS, NOTEBOOKS, PAPERS

app = Flask(__name__)

@app.context_processor
def utility_processor():
    def get_year():
        from datetime import datetime
        return datetime.now().year
    return dict(get_year=get_year)

@app.route('/')
def home():
    return render_template('index.html', 
                         profile=PROFILE, 
                         projects=PROJECTS, 
                         notebooks=NOTEBOOKS, 
                         papers=PAPERS)


if __name__ == '__main__':
    app.run(debug=True)