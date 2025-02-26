from flask import Flask, render_template, request, send_from_directory, redirect, url_for
import os

# Initialize the Flask app
app = Flask(__name__)

# Define the upload folder and configure the app
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Route for the home page
@app.route('/')
def index():
    # List all files in the upload folder
    filenames = os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template('index.html', filenames=filenames)

# Route for handling file uploads
@app.route('/upload', methods=['POST'])
def upload_file():
    # Check if a file is included in the request
    if 'file' not in request.files:
        return "No file part"

    file = request.files['file']

    # Check if a file is selected
    if file.filename == '':
        return "No selected file"

    # Save the file to the upload folder
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
    return redirect(url_for('index'))

# Route for downloading files
@app.route('/download/<filename>')
def download_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)