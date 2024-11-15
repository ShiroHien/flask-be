# Requirements
- Python 3
- Flask

# Local Run
Create a virtual env (mandatory): https://docs.python-guide.org/dev/virtualenvs/#virtualenvironments-ref

Install Flask:
   pip install -r requirements.txt

Run the Application:
   flask run
   The app will be running at http://127.0.0.1:5000.

Test the API:
   - Drag or Choose photos from FE page
   - The photo will be stored in static/uploads folder


# Docker Run

Build the Docker Image:
   docker build -t flask-photo-upload .

Run the Docker Container:
   docker run -p 5000:5000 flask-photo-upload
   This will make the application accessible on http://localhost:5000.

Test the API in Docker:
   - Drag or Choose photos from FE page
   - The photo will be stored in static/uploads folder
