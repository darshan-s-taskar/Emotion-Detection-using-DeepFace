# Emotion Detection using DeepFace

This project performs real-time emotion detection using a webcam by leveraging the **DeepFace** library and **OpenCV**. It detects human faces and predicts emotions such as *happy, sad, angry, neutral*, etc., using a pre-trained deep learning model.

---

## 📌 System Requirements

- **Operating System:** Windows 10 / Windows 11  
- **Python Version:** Python 3.10.11 (recommended)  
- **Camera:** Webcam (built-in or external)  
- **RAM:** 8 GB or higher recommended  

⚠️ *Newer Python versions (e.g., Python 3.14) are not compatible with TensorFlow and DeepFace.*

---

## 📦 Dependencies Used

| Library | Purpose |
|------|-------|
| **TensorFlow (2.10.1)** | Deep learning backend |
| **DeepFace** | Facial emotion analysis |
| **OpenCV** | Video capture and face detection |
| **NumPy (1.23.5)** | Numerical operations |
| **Numba (0.56.4)** | Performance optimization |
| **Matplotlib** | Visualization |
| **Pandas** | Data handling |
| **Haarcascade XML** | Face detection (bundled with OpenCV) |

---

## 🛠️ Installation Steps

### 1️⃣ Install Python 3.10.11

Download and install **Python 3.10.11 (64-bit)** from the official website:

https://www.python.org/ftp/python/3.10.11/python-3.10.11-amd64.exe


---

### 2️⃣ Clone the Repository

https://github.com/darshan-s-taskar/Emotion-Detection-using-DeepFace.git


---

### 3️⃣ Create and Activate Virtual Environment

Create a virtual environment using Python 3.10.11:

```bash
py -3.10 -m venv venv

```

Activate the virtual environment:

```bash
venv\Scripts\activate

```

### 4️⃣ Upgrade pip

Upgrade pip to the latest version inside the virtual environment:

```bash
python -m pip install --upgrade pip

```

### 5️⃣ Install Project Dependencies

Install all the required libraries using the following commands:

```bash
pip install numpy==1.23.5
pip install tensorflow==2.10.1
pip install opencv-python
pip install deepface
pip install numba==0.56.4
pip install matplotlib pandas

```
## ▶️ How to Run the Project

Make sure the virtual environment is activated:

```bash
venv\Scripts\activate

```

Run the Python script:

```bash
python deepF.py

```













