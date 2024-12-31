
# config.py

from datetime import datetime

def sort_achievements(achievements):
    return sorted(achievements, key=lambda x: datetime.strptime(x['date'], '%Y-%m'), reverse=True)

PROFILE = {
    'name': 'Nicko Laygo',
    'title': 'Deep Learning Engineer & Computer Science Student',
    'bio': '''A passionate Computer Science student at FAITH Colleges aiming to specialize in deep learning and computer vision, 
    My experience ranges from building AI-powered applications and robust backend systems to competing in programming competitions. 
    Through projects like leaf classification systems and web applications,
    I demonstrate my commitment to creating innovative solutions across multiple domains.''',
    'email': 'nickolaygo8@gmail.com',
    'github': 'https://github.com/cromcruach52',
    'linkedin': 'https://www.linkedin.com/in/nicko-laygo-6a6548342/',
    'researchgate': 'https://www.researchgate.net/profile/Nicko-Laygo',
    'education': 'FAITH Colleges',
    'skills': {
        'programming': ['Python', 'C', 'C++', 'C#', 'Java', 'SQL'],
        'tools': ['Git', 'Jupyter Notebook', 'PowerBI', 'Microsoft Office', 'Adobe Photoshop'],
        'databases': ['MySQL', 'PostgreSQL', 'SQLite'],
        'soft_skills': ['Planning', 'Communication', 'Teamwork and collaboration']
    }
}

PROJECTS = [
    {
        'title': 'Snapfolia',
        'description': 'A leaf classifier web application using YOLOv8, developed as a joint project of FAITH CS 2024 batch. The application provides accurate leaf classification using deep learning technology.',
        'role': 'Deep Learning Engineer',
        'technologies': ['YOLOv8', 'Deep Learning', 'Computer Vision', 'Web Development'],
        'github_link': 'https://github.com/CHlNlTO/snapfolia',
        'live_link': 'https://trees.firstasia.edu.ph/',
        'logo': '/static/images/snapfolia-icon.png',
        'site_image': '/static/images/snapfolia-site.png'
    },
    {
        'title': 'Brewguard',
        'description': 'A Streamlit-based web application for detecting coffee leaf types and diseases. Users can select different models, adjust detection settings, and access detailed information about various coffee leaves and diseases.',
        'role': 'Deep Learning Engineer',
        'technologies': ['Streamlit', 'Deep Learning', 'Computer Vision', 'Python'],
        'github_link': 'https://github.com/FTsune/kape',
        'live_link': 'https://brewguard.streamlit.app',
        'logo': '/static/images/brewguard-logo.png',
        'site_image': '/static/images/brewguard-site.png'
    },
    {
        'title': 'Seasonal Anime Voting System',
        'description': 'A Django-based web application featuring CRUD functionality for voting questions, choices, and seasons using SQLite3. Includes admin dashboard with voting charts and filtering capabilities.',
        'role': 'Backend Developer',
        'technologies': ['Django', 'SQLite3', 'Python', 'Web Development'],
        'github_link': 'https://github.com/cromcruach52/Seasonal-Anime-Voting-System-Django',
        'live_link': '',
        'logo': '/static/images/anime-logo.png',
        'site_image': '/static/images/anime-site.png'
    },
    {
        'title': 'YouTube Content Strategy Analyzer',
        'description': 'An NLP-based tool that provides insights into title optimization, timing, and overall engagement potential for YouTube content upload.',
        'role': 'Deep Learning Engineer',
        'technologies': ['NLP', 'Python', 'Machine Learning', 'Data Analysis'],
        'github_link': 'https://github.com/cromcruach52/NLP-for-Youtube-Content-Strategy-Analysis',
        'live_link': '',
        'site_image' : '/static/images/youtube-site.png'
    }
]

NOTEBOOKS = [
    {
        'title': 'Brewguard Development Notebooks',
        'description': 'Collection of Jupyter notebooks documenting the development process and model training for the Brewguard coffee leaf disease detection system.',
        'link': 'https://github.com/cromcruach52/Coffee-Disease-OD-Notebooks',
        'date': '2024',
        'tags': ['Computer Vision', 'Deep Learning', 'Object Detection']
    },
    {
        'title': 'Snapfolia Leaf Detection Notebooks',
        'description': 'Research and development notebooks for the Snapfolia project, covering leaf detection and classification model training and optimization.',
        'link': 'https://github.com/cromcruach52/Snapfolia-Leaf-Detection-and-Classification',
        'date': '2024',
        'tags': ['YOLOv8', 'Computer Vision', 'Classification']
    }
]

# Since papers would be on ResearchGate, we can modify the papers section to be more of a research section
PAPERS = [
    {
        'title': 'Research Publications and Projects',
        'description': 'View my complete research portfolio and publications.',
        'platform': 'ResearchGate',
        'link': 'https://www.researchgate.net/profile/Nicko-Laygo',
        'year': '2024'
    }
]

ACHIEVEMENT_DESCRIPTION = "I regularly participate in programming competitions representing FAITH Colleges, aiming to grow both technically and professionally through these experiences."

ACHIEVEMENTS = sort_achievements([
    {
        'date': '2024-12',
        'title': 'CodeChum National Programming Challenge Grand Finals',
        'description': 'Participant'
    },
    {
        'date': '2024-12',
        'title': 'CodeChum National Programming Challenge 2024 Group Stage 3',
        'description': '3rd Place'
    },
    {
        'date': '2024-10',
        'title': 'DICT Philippine Startup Challenge 9 - Regional Pitching Competition',
        'description': 'Top 15 Finalist'
    },
    {
        'date': '2024-05',
        'title': 'CompTIA IT+ Certified',
        'description': None
    },
    {
        'date': '2024-04',
        'title': 'ISITE National IT Skills Competition',
        'description': '5th Place'
    },
    {
        'date': '2023-05',
        'title': 'ISITE National IT Skills Competition',
        'description': '8th Place'
    },
    {
        'date': '2023-03',
        'title': 'ISITE X StackLeague Programming Challenge',
        'description': 'Participant'
    }
])