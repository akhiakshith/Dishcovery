from flask import Flask, render_template, request, jsonify
import requests
import json

app = Flask(__name__)

# Your ML model API endpoint
API_ENDPOINT = "https://food-recommendation-system-u1td.onrender.com/recommend"

@app.route('/', methods=['GET', 'POST'])
def index():
    recommendations = []
    ingredients = []
    
    if request.method == 'POST':
        # Get ingredients from form
        ingredients_input = request.form.get('ingredients', '')
        ingredients = [ing.strip() for ing in ingredients_input.split(',') if ing.strip()]
        top_n = int(request.form.get('top_n', 5))
        
        if ingredients:
            # Prepare the payload
            payload = {
                "ingredients": ingredients,
                "top_n": top_n
            }
            
            try:
                # Make API request to your ML model
                response = requests.post(API_ENDPOINT, json=payload)
                
                if response.status_code == 200:
                    data = response.json()
                    recommendations = data.get('recommendations', [])
                else:
                    return render_template('index.html', 
                                          error=f"Error: API returned status code {response.status_code}",
                                          ingredients=','.join(ingredients))
            except Exception as e:
                return render_template('index.html', 
                                      error=f"Error connecting to API: {str(e)}",
                                      ingredients=','.join(ingredients))
    
    return render_template('index.html', 
                          recommendations=recommendations, 
                          ingredients=','.join(ingredients))

# For Vercel WSGI
app = app

