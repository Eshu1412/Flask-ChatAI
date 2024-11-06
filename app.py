from flask import Flask, request, render_template, jsonify
from transformers import pipeline, AutoModelForCausalLM, AutoTokenizer
from PIL import Image
import os
import webbrowser
import threading
from werkzeug.utils import secure_filename
from pdfminer.high_level import extract_text
from datetime import datetime
"""def open_webrowser():
    webbrowser.open_new("http://127.0.0.1:5500/")"""
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Initialize DialoGPT model and tokenizer
tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-large")
chat_model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-large")
image_model = pipeline("image-classification", model="google/vit-base-patch16-224")
text_model = pipeline("summarization", model="facebook/bart-large-cnn")

def get_greeting():
    current_hour = datetime.now().hour
    if 5 <= current_hour < 12:
        return "Good morning!"
    elif 12 <= current_hour < 18:
        return "Good afternoon!"
    elif 18 <= current_hour < 22:
        return "Good evening!"

def get_current_time():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/chat', methods=['POST'])
def chat():
    if 'file' in request.files:
        file = request.files['file']
        if file:
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            if filename.lower().endswith(('.png', '.jpg', '.jpeg', 'webp')):
                try:
                    img = Image.open(file_path)
                    results = image_model(img)
                    top_prediction = results[0]['label']
                    response = f"This image looks like: {top_prediction}."
                    return jsonify({'response': response})
                except Exception as e:
                    return jsonify({'response': f"Error processing image: {str(e)}"}), 500

            elif filename.lower().endswith('.pdf'):
                try:
                    text = extract_text(file_path)
                    summary = text_model(text, max_length=150, min_length=40, do_sample=False)[0]['summary_text']
                    response = f"Here's a summary of the PDF: {summary}"
                    return jsonify({'response': response})
                except Exception as e:
                    return jsonify({'response': f"Error processing PDF: {str(e)}"}), 500

            elif filename.lower().endswith('.txt'):
                try:
                    text = file.read().decode('utf-8')
                    summary = text_model(text, max_length=150, min_length=40, do_sample=False)[0]['summary_text']
                    response = f"Here's a summary of the text file: {summary}"
                    return jsonify({'response': response})
                except Exception as e:
                    return jsonify({'response': f"Error processing text file: {str(e)}"}), 500

            else:
                return jsonify({'response': "Unsupported file format."}), 400

    # Handle text-based chat
    elif 'message' in request.form:
        user_input = request.form['message'].strip().lower()
        
        # Check for time request
        if "time" in user_input:
            current_time = get_current_time()
            return jsonify({'response': f"The current time is: {current_time}"})

        try:
            inputs = tokenizer.encode(user_input + tokenizer.eos_token, return_tensors='pt')
            chat_response_ids = chat_model.generate(inputs, max_length=100, pad_token_id=tokenizer.eos_token_id)
            chat_response = tokenizer.decode(chat_response_ids[:, inputs.shape[-1]:][0], skip_special_tokens=True)
            return jsonify({'response': chat_response})
        except Exception as e:
            return jsonify({'response': f"Error generating response: {str(e)}"}), 500

    return jsonify({'response': 'Please enter a valid message or file.'}), 400

if __name__ == '__main__':
    """threading.Timer(1, open_webrowser).start()"""
    app.run(debug=True)  # Port should be an integer, no quotes
