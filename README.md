# Aristto

# Research Paper Search - Pro Edition

## Description

This is a web application for searching and managing research papers. Users can search for papers, apply filters, save papers, and view previous search results.

## Features

- Search research papers by keywords.
- Apply filters (year, citations, author).
- Save and remove papers from a saved list.
- View previous search queries and results.

## Prerequisites

- Python 3.x
- Flask
- A local server for backend (Flask-based)

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/Gauri-AB/aristto.git
   cd research-paper-search
2. **Set Up Virtual Environment
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
3. **Install Dependencies
   ```bash
    pip install -r requirements.txt
4.**Start the Flask Backend Server
```bash
  flask run

Ensure that your backend server is running on http://127.0.0.1:5000 or update the URL in the frontend code accordingly.



   ##Running the Application
   1.**Open Your Web Browser**
   
   Navigate to http://localhost:8000 to access the application.
   
   2.**Search and Manage Papers**
   
   .Enter keywords in the search bar and click "Search" to view results.
   .Use filters to refine search results.
   .Click "Save Paper" to add papers to your saved list.
   .View and remove saved papers from the "Saved Papers" section.
   .Access previous search queries and results from the "Previous Search Results" section.
   
   ##Testing
   
   **Front-End Testing**
   
   Test the front-end by interacting with the application in your browser.
   
   **Back-End Testing**
   
   Use tools like Postman or cURL to test API endpoints (e.g., /search, /save).
   
   ##Contributing
   Feel free to open issues or submit pull requests if you have improvements or bug fixes.
   
   ##License
   This project is licensed under the MIT License. See the LICENSE file for details.
