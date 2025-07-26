import cv2
import numpy as np
import cv2.ximgproc as xip
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
INPUT_FOLDER = 'static/input'
OUTPUT_FOLDER = 'static/output'
app.config['INPUT_FOLDER'] = INPUT_FOLDER
app.config['OUTPUT_FOLDER'] = OUTPUT_FOLDER

os.makedirs(INPUT_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# ---------------- Retinex Enhancement ----------------
def msr(img, sigma_list=[15, 80, 250]):
    img = img.astype(np.float32) + 1.0
    result = np.zeros_like(img)
    for sigma in sigma_list:
        blur = cv2.GaussianBlur(img, (0, 0), sigma)
        result += np.log(img) - np.log(blur + 1.0)
    return result / len(sigma_list)

def color_restoration(img, alpha=125.0, beta=46.0):
    sum_channels = np.sum(img, axis=2, keepdims=True)
    return beta * (np.log(alpha * img + 1.0) - np.log(sum_channels + 1.0))

def msrcr(img):
    img = img.astype(np.float32) + 1.0
    msr_result = msr(img)
    crf = color_restoration(img)
    return msr_result * crf

def apply_guided_filter(I, p, radius=8, eps=0.2**2):
    I = I.astype(np.float32)
    p = p.astype(np.float32)
    return xip.guidedFilter(guide=I, src=p, radius=radius, eps=eps, dDepth=-1)

def enhance_image(input_path, output_path):
    img = cv2.imread(input_path)
    enhanced = msrcr(img)
    guided = apply_guided_filter(img, enhanced)
    guided = cv2.normalize(guided, None, 0, 255, cv2.NORM_MINMAX)
    guided = np.clip(guided, 0, 255).astype(np.uint8)
    cv2.imwrite(output_path, guided)

# ---------------- Flask Routes ----------------
@app.route('/', methods=['GET', 'POST'])
def upload_image():
    if request.method == 'POST':
        if 'image' not in request.files:
            return "No file uploaded", 400
        file = request.files['image']
        if file.filename == '':
            return "No file selected", 400

        filename = secure_filename(file.filename)
        input_path = os.path.join(app.config['INPUT_FOLDER'], filename)
        output_path = os.path.join(app.config['OUTPUT_FOLDER'], filename)

        file.save(input_path)
        enhance_image(input_path, output_path)

        return render_template('index.html', input_file=filename, output_file=filename)

    return render_template('index.html', input_file=None, output_file=None)

if __name__ == '__main__':
    app.run(debug=True)
