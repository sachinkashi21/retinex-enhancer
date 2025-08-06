# 🔆 Retinex Image Enhancement Web App

This project is a simple Flask-based web application that enhances color images using **Retinex Theory** and a **Guided Filter**, based on the paper:

> "Color Image Enhancement Based on Retinex Theory with Guided Filter"  
> Shi Tang, Mingjie Dong, Jinlei Ma, Zhiqiang Zhou, Changqing Li  
> Beijing Institute of Technology, Beijing 100081, China

---

## 📸 Features

- Upload any image via a browser
- Enhances image using MSRCR (Multi-Scale Retinex with Color Restoration)
- Applies Guided Filter to preserve edges
- Displays original and enhanced image side-by-side
- Stores inputs and outputs separately for easy reference

---

## 🗂️ Project Structure

```
retinex-enhancer/
│
├── main.py                   # Main Flask app with routing
├── utils/                    # 🔧 All helper logic (modularized)
│   ├── __init__.py
│   ├── retinex.py            # Image enhancement logic
│   └── file_utils.py         # Filename handling, etc.
│
├── static/
│   ├── input/                # Uploaded original images
│   └── output/               # Enhanced output images
│
├── templates/
│   ├── index.html            # Upload form + image display
│   └── gallery.html          # View all uploaded-enhanced image pairs
│
├── venv/                     # Your virtual environment (ignored in Git)
├── .gitignore
├── readme.md
└── requirements.txt
```

---

## ⚙️ Setup Instructions

### 1. ✅ Clone or Download This Repo

```bash
git clone https://github.com/sachinkashi21/retinex-enhancer.git
cd retinex-enhancer
```

---

### 2. 🐍 Create & Activate Virtual Environment

```bash
python -m venv venv
```

#### On Windows:
```bash
venv\Scripts\activate
```

#### On macOS/Linux:
```bash
source venv/bin/activate
```

---

### 3. 📦 Install Dependencies

```bash
pip install -r requirements.txt
```

If you don’t have `requirements.txt`, manually install:

```bash
pip install flask opencv-python opencv-contrib-python numpy
```

---

### 4. 🚀 Run the App

```bash
python app.py
```

Then open your browser and go to:  
http://127.0.0.1:5000

---

## 🧪 How to Use

1. Upload an image using the form.  
2. It will be saved under `static/input/`.  
3. The enhanced version will be saved under `static/output/` with the same name.  
4. Both images will be shown on the result page.

## 🧠 Reference

Original Paper:  
"Color Image Enhancement Based on Retinex Theory with Guided Filter"  
[IEEE Xplore / ResearchGate / Paper Link] *(Add actual link if available)*

---

## 💬 Credits

Developed by: **Narendra Sachin Shivamrutv Shriganesh**  
Based on research work from Beijing Institute of Technology.

---

## 📜 License

This project is for educational purposes only. No commercial use allowed without permission from the original paper authors.