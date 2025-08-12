
![App Screenshot](https://drive.google.com/uc?export=view&id=1iIE0BAOb7c7qKuiqZMQUeBk-1vdqSXjf)


## Table of Contents

* [Features](#features)
* [Project Structure](#project-structure)
* [Installation](#installation)
* [Usage](#usage)
* [Data Preprocessing](#data-preprocessing)
* [Model](#model)
* [Deployment](#deployment)
* [Requirements](#requirements)
* [License](#license)
* [Acknowledgements](#acknowledgements)

---

## Features

* Predicts win probability using:

  * Batting team & Bowling team
  * Match city
  * Target score
  * Current score
  * Overs completed
  * Wickets fallen
* Clean and interactive **Streamlit** UI
* Pretrained **Logistic Regression** model (serialized as `pipe.pkl`)
* Uses historical IPL data from `matches.csv` & `deliveries.csv`

---

## Project Structure

```
.
├── app.py              # Streamlit web app
├── pipe.pkl            # Trained ML pipeline (Logistic Regression)
├── matches.csv         # IPL match data
├── deliveries.csv      # IPL ball-by-ball data
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
```

---

## Installation

1. **Clone the repository**

```bash
git clone https://github.com/your-username/ipl-win-predictor.git
cd ipl-win-predictor
```

2. (Optional but recommended) Create and activate a virtual environment

```bash
# macOS / Linux
python -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Run the app

```bash
streamlit run app.py
```

---

## Usage

1. Open the Streamlit app in your browser (Streamlit will show the local URL after `streamlit run`).
2. Select the **Batting team**, **Bowling team**, and **Match city** from dropdowns.
3. Enter the match details:

   * Target score
   * Current score
   * Overs completed
   * Wickets fallen
4. Click **Predict Probability** to see:

   * Winning percentage for batting & bowling teams
   * Progress bars visualising win chances

---

## Data Preprocessing

* Merged `matches.csv` and `deliveries.csv` for feature engineering.
* Removed matches where Duckworth–Lewis (D/L) method was applied.
* Encoded categorical variables with `OneHotEncoder`.
* Engineered features:

  * **Runs left**
  * **Balls left**
  * **Wickets remaining**
  * **Current Run Rate (CRR)**
  * **Required Run Rate (RRR)**

---

## Model

* **Model type:** Logistic Regression (scikit-learn pipeline)
* **Labels:** Win / Loss for the batting team
* **Outputs:** `win_prob` and `loss_prob` (probabilities)
* The trained pipeline is saved as `pipe.pkl` and is loaded by `app.py`.

---

## Deployment

You can deploy this app for free on **Streamlit Cloud**:

1. Commit your code to a GitHub repository.
2. Sign in to Streamlit Cloud and connect the repo.
3. Set the app entry point to `app.py` and specify any required secrets (if used).

---

## Requirements

* Python 3.8+
* pandas
* numpy
* scikit-learn
* streamlit
* matplotlib

Install via:

```bash
pip install -r requirements.txt
```

---

## License

This project is licensed under the **MIT License** — feel free to use, modify, and share.

---

## Acknowledgements

* Kaggle IPL Dataset (for historical matches and deliveries)
* Streamlit (for the web UI)
* scikit-learn (for model building)

---

## Contact

If you have questions, suggestions or improvements, open an issue or submit a pull request on the repository.

