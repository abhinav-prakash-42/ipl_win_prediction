# 🏏 IPL Win Predictor

Predict the winning probability of your favourite IPL team **based on real match situations** using machine learning.  
Built with **Python**, **Scikit-Learn**, and **Streamlit**.

---

## 📌 Features

- Predicts win probability based on:
  - Batting team & Bowling team
  - Match city
  - Target score
  - Current score
  - Overs completed
  - Wickets fallen
- Clean and interactive **Streamlit UI**
- Pretrained **Logistic Regression model**
- Real IPL historical data from `matches.csv` & `deliveries.csv`

---

## 🖼 Demo

![App Screenshot](https://via.placeholder.com/800x400?text=IPL+Win+Predictor+Screenshot)

---

## 🗂 Project Structure

.
├── app.py # Streamlit web app
├── pipe.pkl # Trained ML model
├── matches.csv # IPL match data
├── deliveries.csv # IPL ball-by-ball data
├── requirements.txt # Python dependencies
└── README.md # Project documentation

yaml
Copy
Edit

---

## ⚙️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/ipl-win-predictor.git
   cd ipl-win-predictor
Create virtual environment (optional but recommended)

bash
Copy
Edit
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
Run the app

bash
Copy
Edit
streamlit run app.py
📊 Data Preprocessing
Merged matches and deliveries datasets

Removed matches with D/L method applied

Encoded categorical variables using OneHotEncoder

Engineered features:

Runs left

Balls left

Wickets remaining

Current Run Rate (CRR)

Required Run Rate (RRR)

🧠 Model
Logistic Regression classifier

Trained using historical IPL data

Output: Probability of winning (win_prob) & losing (loss_prob)

📌 Usage
Select Batting team, Bowling team, and Match city

Enter:

Target score

Current score

Overs completed

Wickets fallen

Click "Predict Probability"

View:

Winning percentage for batting & bowling teams

Progress bars showing chances visually

📦 Requirements
Python 3.8+

pandas

numpy

scikit-learn

streamlit

matplotlib

Install with:

bash
Copy
Edit
pip install -r requirements.txt
🚀 Deployment
You can deploy this app for free on Streamlit Cloud:

bash
Copy
Edit
# Commit your code to GitHub
# Sign in to Streamlit Cloud and link your repo
# Set up the app entry point as app.py
📜 License
This project is licensed under the MIT License — you’re free to use, modify, and share it.

🙌 Acknowledgements
Kaggle IPL Dataset for the data

Streamlit for easy web app creation

Scikit-Learn for model building

yaml
Copy
Edit
