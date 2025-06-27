
# 🤖 Flask AI Chatbot & File Analyzer

This project is a Flask-based web application that combines a conversational chatbot with file analysis capabilities. It uses pre-trained models to generate text responses, classify images, and summarize content from PDFs and text files.

---

## 📌 Features

✅ Chat with AI using Microsoft's **DialoGPT**  
✅ Classify images using Google's **ViT (Vision Transformer)**  
✅ Summarize content from `.pdf` and `.txt` files using Facebook's **BART**  
✅ Displays current system time  
✅ Handles various file types and gives intelligent responses  
✅ Provides time-based greetings (Good morning/afternoon/evening)

---

## 🛠️ Tech Stack

- **Backend**: Flask
- **NLP & Vision Models**: Hugging Face Transformers
  - `microsoft/DialoGPT-large`
  - `google/vit-base-patch16-224`
  - `facebook/bart-large-cnn`
- **Text Extraction**: `pdfminer.six`
- **Image Processing**: PIL (Pillow)

---

## 🗂️ File Support

| File Type | Action |
|-----------|--------|
| `.png`, `.jpg`, `.jpeg`, `.webp` | Image classification |
| `.pdf` | Text extraction and summarization |
| `.txt` | Text summarization |
| Others | Unsupported |

---

## 📁 Project Structure

```
📦project-root/
├── app.py                   # Main Flask application
├── templates/
│   └── index.html           # Frontend HTML page
├── uploads/                 # Folder to store uploaded files
├── static/                  # Optional: for styles or JS
└── README.md                # This file
```

---

## 🚀 Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/flask-ai-chatbot.git
cd flask-ai-chatbot
```

### 2. Install Dependencies

Ensure Python 3.8+ is installed. Then run:

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install flask transformers pillow pdfminer.six
```

### 3. Run the Application

```bash
python app.py
```

### 4. Open in Browser

Navigate to:

```
http://127.0.0.1:5000/
```

---

## 💬 Chat Commands

- **Ask anything**:
  - "Tell me a joke"
  - "What is AI?"
- **Get current time**:
  - "What's the time now?"

---

## 📤 Upload Instructions

- Upload an **image file** (`.png`, `.jpg`, etc.) → Returns top prediction label.
- Upload a **PDF or TXT file** → Returns summarized content.
- Unsupported formats return an error message.

---

## 🔐 Security Tips

> ⚠️ This app is for **educational/demo use only**. For production:
- Add file size/type validation.
- Use environment variables for secrets.
- Sanitize inputs and manage user sessions.

---

## 📌 Sample requirements.txt

```txt
flask
transformers
pdfminer.six
Pillow
```

---

## 🧠 Model References

- [DialoGPT (Microsoft)](https://huggingface.co/microsoft/DialoGPT-large)
- [ViT Image Classifier (Google)](https://huggingface.co/google/vit-base-patch16-224)
- [BART Summarizer (Facebook)](https://huggingface.co/facebook/bart-large-cnn)

---

## 👨‍💻 Author

**Tushar Maurya**  
Email: [mauryatushar115@gmail.com](mailto:mauryatushar115@gmail.com)  
LinkedIn: [linkedin.com/in/tushar-maurya-aa7548297](https://www.linkedin.com/in/tushar-maurya-aa7548297)

---

## 📄 License

This project is licensed under the **MIT License**.

Feel free to fork, enhance, and share!
