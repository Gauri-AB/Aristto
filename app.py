from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Mock data for research papers
mock_papers = [
    {
        "title": "Deep Learning for AI",
        "authors": "John Doe, Jane Smith",
        "year": 2021,
        "citations": 50
    },
    {
        "title": "AI and the Future of Work",
        "authors": "Alice Brown, Bob White",
        "year": 2020,
        "citations": 100
    }
]

# List to store saved papers
saved_papers = []

# Serve index.html
@app.route('/')
def index():
    return render_template('index.html')

# API to return search results (mocked for now)
@app.route('/search', methods=['POST'])
def search_papers():
    query = request.json.get('query', '').lower()
    # Filter mock papers based on query
    results = [paper for paper in mock_papers if query in paper['title'].lower()]
    return jsonify(results)

# API to save papers
@app.route('/save', methods=['POST'])
def save_paper():
    paper = request.json
    if paper not in saved_papers:
        saved_papers.append(paper)
    return jsonify({"message": "Paper saved!"}), 200

# API to remove papers
@app.route('/remove', methods=['POST'])
def remove_paper():
    title_to_remove = request.json.get('title')
    global saved_papers
    saved_papers = [paper for paper in saved_papers if paper['title'] != title_to_remove]
    return jsonify({"message": f"Paper '{title_to_remove}' removed"}), 200

# API to fetch saved papers
@app.route('/saved', methods=['GET'])
def get_saved_papers():
    return jsonify(saved_papers), 200

if __name__ == '__main__':
    app.run(debug=True)
