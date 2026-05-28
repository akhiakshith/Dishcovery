# 🍽️ Dishcovery — Smart Food Recommendation System

A premium, interactive Flask application that delivers personalized recipe recommendations based on input ingredients. Upgraded with an ultra-minimalist, high-end Gen Z dark obsidian theme and neon emerald green accents.

---

## ⚡ Key Features

- **Ingredient-Based Search:** Input a comma-separated list of ingredients to find matching recipes.
- **Smart Recommendations:** Connects to an external Machine Learning recommendation API endpoint to compute recipe suggestions.
- **Recipe Cards:** Displays translated recipe names, preparation times, cuisine tags, and ingredient details.
- **Direct Access:** Integrated "View Recipe" links to quickly open the complete cooking instructions.
- **Modern Aesthetic:** Features glassmorphism inputs, responsive layouts, custom scrollbars, and premium typography.

---

## 🛠️ Tech Stack & Architecture

- **Backend:** Python, Flask, requests
- **Frontend:** HTML5, CSS3, Bootstrap 5 (heavily customized style blocks), Google Fonts (`Outfit` & `Space Grotesk`)
- **API Endpoint:** `https://food-recommendation-system-u1td.onrender.com/recommend`

```
Dishcovery/
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── vercel.json         # Deployment configuration for Vercel
├── README.md           # Project documentation
└── templates/          # Render templates
    └── index.html      # Heavy-styled, dark mode frontend
```

---

## 🚀 Getting Started

### 1. Clone & Install Dependencies
First, install the Python package dependencies:
```bash
pip install -r requirements.txt
```

### 2. Run the Flask App
Start the local development server:
```bash
python app.py
```
Open `http://127.0.0.1:5000` in your web browser.

---

## 🔌 API Integration

The app communicates with a backend model API by sending a JSON payload:

```json
{
  "ingredients": ["tomato", "basil", "pasta"],
  "top_n": 5
}
```

The endpoint processes the ingredients and returns detailed recipe suggestions, which are dynamically rendered into card layouts on the frontend.
