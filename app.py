from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from dotenv import load_dotenv
import os
import certifi

# Load environment variables
load_dotenv()

app = Flask(__name__)

# # MongoDB connection
# MONGO_URI = os.getenv('MONGO_URI')
# client = MongoClient(MONGO_URI, tlsCAFile=certifi.where())
# db = client['test']  # Use your actual DB name
# collection = db['submissions']

# MongoDB connection
MONGO_URI = "mongodb+srv://ronakmalpani28:gl9Ajzt9jinpx0xG@cluster.lovmmhz.mongodb.net/?retryWrites=true&w=majority&appName=cluster"
client = MongoClient(MONGO_URI, tlsCAFile=certifi.where())
db = client['test']  # replace with your DB name
collection = db['form_entries']

@app.route('/', methods=['GET', 'POST'])
def form():
    error = None
    if request.method == 'POST':
        try:
            form_data = dict(request.form)
            collection.insert_one(form_data)
            return redirect(url_for('success'))
        except Exception as e:
            error = f"Error submitting data: {str(e)}"
    return render_template('form.html', error=error)

@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)
