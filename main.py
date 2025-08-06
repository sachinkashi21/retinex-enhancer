from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os

from utils.retinex import enhance_image
from utils.file_utils import get_next_filename

app = Flask(__name__)
INPUT_FOLDER = 'static/input'
OUTPUT_FOLDER = 'static/output'
app.config['INPUT_FOLDER'] = INPUT_FOLDER
app.config['OUTPUT_FOLDER'] = OUTPUT_FOLDER

os.makedirs(INPUT_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def upload_image():
    if request.method == 'POST':
        if 'image' not in request.files:
            return "No file uploaded", 400
        file = request.files['image']
        if file.filename == '':
            return "No file selected", 400

        filename = get_next_filename(INPUT_FOLDER, file.filename)
        input_path = os.path.join(INPUT_FOLDER, filename)
        output_path = os.path.join(OUTPUT_FOLDER, filename)

        file.save(input_path)
        enhance_image(input_path, output_path)

        return render_template('index.html', input_file=filename, output_file=filename)

    return render_template('index.html', input_file=None, output_file=None)

@app.route('/gallery')
def gallery():
    image_pairs = []
    for filename in sorted(os.listdir(INPUT_FOLDER)):
        if os.path.isfile(os.path.join(INPUT_FOLDER, filename)) and os.path.isfile(os.path.join(OUTPUT_FOLDER, filename)):
            image_pairs.append((f"input/{filename}", f"output/{filename}"))
    return render_template('gallery.html', image_pairs=image_pairs)

if __name__ == '__main__':
    app.run(debug=True)
