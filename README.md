Great — here’s a **detailed and original README** tailored to your own work while matching the professionalism and clarity you admire. You can paste this into your `README.md` file and customize further if needed:

---

# 🔍 TERM DEPOSIT SUBSCRIPTION PREDICTION

**Azubi Africa - Talent Mobility Program Assessment**
*By Barbara Asiamah*

---

## 📌 PROJECT OVERVIEW

This project was developed as part of the **Azubi Africa Talent Mobility Program**. The objective is to build a predictive machine learning solution that determines whether a client will subscribe to a **term deposit product** based on information gathered during direct marketing campaigns by a bank.

The final product includes a deployed **interactive Streamlit app** that allows users to input various client attributes and receive a real-time prediction on the likelihood of subscription.

---

## 🧠 PROBLEM STATEMENT

The marketing team of a financial institution wants to optimize their campaigns by targeting clients who are most likely to subscribe to a term deposit. With thousands of clients contacted across various campaigns, it’s essential to use past data to guide future marketing efforts.

As a data analyst, my task was to:

* Explore the dataset and uncover useful trends.
* Build a model that predicts whether a client will subscribe to the term deposit (`y = yes` or `no`).
* Deploy the model through a web interface for easy usability by non-technical users.

---

## 🗂 PROJECT STRUCTURE

| Task No. | Task Name                      | Description                                                          |
| -------- | ------------------------------ | -------------------------------------------------------------------- |
| TMP\_1   | Client Term Deposit Prediction | Build and deploy an ML model to predict client subscription behavior |

---

## ✅ TASK BREAKDOWN

### 1. Exploratory Data Analysis (EDA)

I started with a comprehensive review of the dataset, which included:

* Identifying **missing values** (e.g., `unknown` entries in categorical features),
* Analyzing **distribution of categorical and numeric variables**,
* Assessing **correlations** and **target imbalance**,
* Investigating trends in subscription behavior.

### 2. Feature Engineering

* Encoded categorical variables using **one-hot encoding**,
* Created additional features like `campaign_diff`,
* Evaluated **feature importance** using Random Forest.

### 3. Model Development

* Trained multiple models including:

  * **Random Forest** (final model),
  * Logistic Regression,
  * XGBoost.
* Random Forest was selected for its overall balance in accuracy and interpretability.

### 4. Model Evaluation

* Evaluated with **Accuracy, Precision, Recall, and F1-Score**,
* Handled **class imbalance** using SMOTE and threshold adjustments,
* Final model reached \~88% accuracy with a reasonable balance of precision and recall.

### 5. Deployment

* The model was deployed using **Streamlit**, offering a clean, interactive interface for predictions.

---

## 📁 DATA OVERVIEW

The data used for this project originates from direct marketing efforts conducted via phone calls. More than one contact per client is possible.

### 📊 Feature Sample

| Variable       | Description                                      | Type        |
| -------------- | ------------------------------------------------ | ----------- |
| age            | Age of the client                                | Numeric     |
| job            | Type of job                                      | Categorical |
| marital        | Marital status                                   | Categorical |
| education      | Education level                                  | Categorical |
| default        | Has credit in default?                           | Binary      |
| housing        | Has a house loan?                                | Binary      |
| loan           | Has a personal loan?                             | Binary      |
| contact        | Contact communication type                       | Categorical |
| month          | Last contact month                               | Categorical |
| day\_of\_week  | Day of week of last contact                      | Categorical |
| duration       | Last contact duration (seconds)                  | Numeric     |
| campaign       | Number of contacts in current campaign           | Numeric     |
| pdays          | Days since last contact from a previous campaign | Numeric     |
| previous       | Number of contacts before this campaign          | Numeric     |
| poutcome       | Outcome of the previous campaign                 | Categorical |
| emp.var.rate   | Employment variation rate                        | Numeric     |
| cons.price.idx | Consumer price index                             | Numeric     |
| cons.conf.idx  | Consumer confidence index                        | Numeric     |
| euribor3m      | 3-month Euribor rate                             | Numeric     |
| nr.employed    | Number of employees                              | Numeric     |
| y              | Target: Has the client subscribed?               | Binary      |

---

## ⚙️ TECH STACK

* **Python 3.10+**
* **Streamlit** (Web App)
* **Pandas, Scikit-learn, Joblib**
* **Jupyter/Colab** for development and analysis
* **Hugging Face Hub** (for hosting large model artifacts)

---

## 🚀 DEPLOYMENT

🔗 **Live App**: [Click to Use the App](https://barbara-azubitmp.streamlit.app/)

To run locally:

```bash
# Clone repository
git clone https://github.com/barbara99/Azubi_tmp.git
cd Azubi_tmp

# Create virtual environment
python -m venv venv
source venv/bin/activate   # or venv\Scripts\activate on Windows

# Install requirements
pip install -r requirements.txt

# Run Streamlit app
streamlit run app.py
```

---

## 🔍 EVALUATION METRICS

| Metric    | Score                   |
| --------- | ----------------------- |
| Accuracy  | 88%                     |
| Precision | Moderate                |
| Recall    | Lower on positive class |
| F1 Score  | Balanced across models  |

Special care was taken to address **class imbalance**, particularly since subscriptions (`y = yes`) were relatively rare in the dataset.

---

## 💡 KEY INSIGHTS

* Clients contacted during **certain months** like March or September had higher conversion rates.
* **Contact method** (e.g., cellular vs telephone) had an effect on subscription likelihood.
* Features such as `age`, `euribor3m`, and `campaign` were among the **top predictors**.

---

## 📸 APP PREVIEW

![Streamlit UI](screenshots/sample_ui.png)
*A user-friendly form to simulate new client entries and predict outcomes.*

---

## ✉️ AUTHOR

| Name            | Country | Email                                                           |
| --------------- | ------- | --------------------------------------------------------------- |
| Barbara Asiamah | Ghana   | [barbaraasiamah99@gmail.com](mailto:barbaraasiamah99@gmail.com) |

---

## 📚 RESOURCES

* [Streamlit Docs](https://docs.streamlit.io/)
* [SMOTE for Imbalanced Classification](https://imbalanced-learn.org/)
* [Scikit-learn User Guide](https://scikit-learn.org/stable/)
* [Feature Engineering for ML](https://www.kaggle.com/learn/feature-engineering)
