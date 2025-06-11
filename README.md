# 📱 Mobile Banking App Reviews Analysis

This project analyzes user reviews from the Google Play Store for three major mobile banking apps using Natural Language Processing (NLP). It also stores the processed data in an Oracle XE relational database and provides insights through data visualization.

---

## 🚀 Project Objectives

- Scrape and preprocess mobile banking app reviews.
- Perform sentiment and thematic analysis using NLP.
- Store cleaned data in an Oracle XE database.
- Derive insights and create visualizations to inform app improvements.
- Use Git for version control and maintain reproducibility through scripts and dumps.

---

## 🛠 Tech Stack

- **Languages**: Python, SQL
- **Libraries**: pandas, BeautifulSoup, google-play-scraper, transformers (DistilBERT), spaCy, seaborn, matplotlib
- **Database**: Oracle XE 21c
- **Tools**: cx_Oracle, Data Pump (`expdp`)
- **Version Control**: Git & GitHub

## 📦 Setup Instructions

### 🔹 1. Clone Repository
```bash
git clone https://github.com/arsema-mz/mobile-banking-reviews.git
cd mobile-banking-reviews
````

### 🔹 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 🔹 3. Setup Oracle XE

* Download and install [Oracle XE 21c](https://www.oracle.com/database/technologies/xe-downloads.html)
* Use SQL\*Plus or SQL Developer to create user and schema:

```sql
CREATE USER bank_reviews_user IDENTIFIED BY Mandekid1234oracle;
GRANT CONNECT, RESOURCE TO bank_reviews_user;
```

### 🔹 4. Create Tables

Run SQL scripts to create required tables:

```sql
-- Banks Table
CREATE TABLE Banks (
    bank_id NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    bank_name VARCHAR2(100) NOT NULL,
    country VARCHAR2(50)
);

-- Reviews Table
CREATE TABLE Reviews (
    review_id NUMBER PRIMARY KEY,
    bank_id NUMBER REFERENCES Banks(bank_id),
    review_text CLOB,
    rating NUMBER
);
```

### 🔹 5. Insert Processed Data into Oracle

```bash
python scripts/insert_reviews.py
```

Make sure `combined_analysis_results.csv` exists in `data/`.

---

## 🧠 Analysis Details

### ✔ Sentiment Analysis

* Model: `distilbert-base-uncased-finetuned-sst-2-english`
* Output: Positive, Negative, Neutral labels and sentiment scores

### ✔ Thematic Analysis

* Method: TF-IDF keyword extraction + manual clustering into themes
* Themes include: **App Performance**, **Login Issues**, **Feature Requests**, **Customer Service**

---

## 🗃 Oracle Export

Dump file for reproducibility:

* [`BANK_REVIEWS_USER.DMP`](oracle_exports/BANK_REVIEWS_USER.DMP)
* [`bank_reviews_user_export.log`](oracle_exports/bank_reviews_user_export.log)

## 📊 Sample Visualizations

* Sentiment distribution by bank
* Word clouds for top complaint themes
* Bar plots for common keywords and review scores

*(See `outputs/` folder)*

---

## ✅ Project KPIs

| KPI                         | Target   | Achieved |
| --------------------------- | -------- | -------- |
| Reviews Scraped             | ≥ 1,200  | ✅ 1,200  |
| Sentiment Analysis Coverage | ≥ 90%    | ✅ 100%   |
| Themes Identified per Bank  | ≥ 3      | ✅ 5      |
| Oracle DB Inserted Rows     | ≥ 1,000  | ✅ 1,200  |
| Data Dump Exported          | Required | ✅ Yes    |

---

## 📌 Recommendations

* Improve login reliability and transaction speed.
* Enhance UI consistency across updates.
* Prioritize customer support responsiveness.
