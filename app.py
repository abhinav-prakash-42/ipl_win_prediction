import streamlit as st
import pickle
import pandas as pd

# ----------------------------
# Data
# ----------------------------
teams = [
    'Sunrisers Hyderabad', 'Mumbai Indians', 'Royal Challengers Bangalore',
    'Kolkata Knight Riders', 'Kings XI Punjab', 'Chennai Super Kings',
    'Rajasthan Royals', 'Delhi Capitals'
]

cities = [
    'Hyderabad', 'Bangalore', 'Mumbai', 'Indore', 'Kolkata', 'Delhi',
    'Chandigarh', 'Jaipur', 'Chennai', 'Cape Town', 'Port Elizabeth',
    'Durban', 'Centurion', 'East London', 'Johannesburg', 'Kimberley',
    'Bloemfontein', 'Ahmedabad', 'Cuttack', 'Nagpur', 'Dharamsala',
    'Visakhapatnam', 'Pune', 'Raipur', 'Ranchi', 'Abu Dhabi',
    'Sharjah', 'Mohali', 'Bengaluru'
]

# ----------------------------
# Load Model
# ----------------------------
pipe = pickle.load(open('pipe.pkl', 'rb'))

# ----------------------------
# App Layout
# ----------------------------
st.set_page_config(page_title="IPL Win Predictor", page_icon="🏏", layout="wide")
st.markdown("<h1 style='text-align: center; color: #FF4B4B;'>🏏 IPL Win Predictor</h1>", unsafe_allow_html=True)
st.write("### Predict the winning probability of your favourite IPL team based on the match situation.")

# ----------------------------
# Inputs
# ----------------------------
st.markdown("#### 🏟 Match Details")
col1, col2 = st.columns(2)
with col1:
    batting_team = st.selectbox('Batting Team', sorted(teams))
with col2:
    bowling_teams = [team for team in teams if team != batting_team]
    bowling_team = st.selectbox('Bowling Team', sorted(bowling_teams))

selected_city = st.selectbox('Host City', sorted(cities))
target = st.number_input('Target Score', min_value=1)

st.markdown("#### 📊 Current Match Stats")
col3, col4, col5 = st.columns(3)
with col3:
    score = st.number_input('Current Score', min_value=0, max_value=target)
with col4:
    overs_input = st.text_input('Overs Completed (e.g., 5.4 means 5 overs and 4 balls)', '0.0')
with col5:
    wickets = st.number_input('Wickets Fallen', min_value=0, max_value=10)

# ----------------------------
# Helper: Convert overs like 5.4 (5 overs and 4 balls) to total balls completed
# ----------------------------
def overs_to_balls(overs_str):
    try:
        if '.' in overs_str:
            overs, balls = overs_str.split('.')
            overs = int(overs)
            balls = int(balls)
            if balls >= 6:
                raise ValueError("Balls part of overs cannot be 6 or more")
            total_balls = overs * 6 + balls
        else:
            total_balls = int(float(overs_str)) * 6
        return total_balls
    except Exception:
        return None

# ----------------------------
# Prediction
# ----------------------------
if st.button('🔮 Predict Probability'):
    total_balls_completed = overs_to_balls(overs_input)
    if total_balls_completed is None or total_balls_completed < 0 or total_balls_completed > 120:
        st.error("Please enter overs correctly. Balls part must be between 0 and 5.")
    elif total_balls_completed == 0:
        st.error("Overs completed cannot be zero.")
    elif score > target:
        st.error("Current score cannot be greater than the target.")
    elif wickets > 10:
        st.error("Wickets fallen cannot be more than 10.")
    else:
        runs_left = target - score
        balls_left = 120 - total_balls_completed
        remaining_wickets = 10 - wickets
        crr = score / (total_balls_completed / 6) if total_balls_completed > 0 else 0
        rrr = (runs_left * 6) / balls_left if balls_left > 0 else 0

        input_df = pd.DataFrame({
            'batting_team': [batting_team],
            'bowling_team': [bowling_team],
            'city': [selected_city],
            'runs_left': [runs_left],
            'balls_left': [balls_left],
            'wickets': [remaining_wickets],
            'total_runs_x': [target],
            'crr': [crr],
            'rrr': [rrr]
        })

        try:
            result = pipe.predict_proba(input_df)
            loss_prob = result[0][0]
            win_prob = result[0][1]

            st.markdown("---")
            st.subheader("📈 Winning Probability")
            colA, colB = st.columns(2)
            with colA:
                st.metric(label=batting_team, value=f"{round(win_prob * 100)}%")
                st.progress(int(win_prob * 100))
            with colB:
                st.metric(label=bowling_team, value=f"{round(loss_prob * 100)}%")
                st.progress(int(loss_prob * 100))
        except Exception as e:
            st.error(f"Prediction error: {e}")
