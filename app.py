from flask import Flask, render_template, request, redirect, url_for, send_file
import os

app = Flask(__name__)

UPLOAD_FOLDER = os.path.join('static', 'uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True) 

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'photo' not in request.files:
        return 'No photo uploaded', 400
    photo = request.files['photo']
    if photo.filename == '':
        return 'No selected file', 400
    if photo:
        # Save photo to upload folder
        photo_path = os.path.join(app.config['UPLOAD_FOLDER'], photo.filename)
        photo.save(photo_path)
        # Redirect to page showing the link to view photo
        return redirect(url_for('view_photo', filename=photo.filename))

@app.route('/view/<filename>')
def view_photo(filename):
    photo_url = url_for('uploaded_file', filename=filename)
    return render_template('view.html', photo_url=photo_url)

@app.route('/static/uploads/<filename>')
def uploaded_file(filename):
    photo_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    mimetype = f'image/{filename.split(".")[-1]}'
    return send_file(photo_path, mimetype=mimetype)

if __name__ == '__main__':
    app.run(debug=True)
