# LeetCode Profile Scraper

A Python-based tool to scrape public profile data from [LeetCode](https://leetcode.com), store it in a PostgreSQL database, and export it as a CSV file — all from a single command.

---

## 🚀 Features

- 🔍 Scrapes LeetCode public profile stats:
  - Username
  - Global ranking
  - Total solved problems (Easy, Medium, Hard)
- 🐘 Stores the data in a PostgreSQL database
- 📁 Exports the data into a CSV file
- 🖥️ Command-line interface via `main.py`

---

## 📁 Project Structure
### leetcode-scraper/
    ├── db.py 
    ├── generate_csv.py
    ├── main.py 
    ├── scrape.py 
    ├── requirements.txt 
    ├── .env 
    ├── .gitignore 
    └── README.md


## Steps to start

```bash

git clone https://github.com/devlpr-nitish/leetcode-scraper.git

cd leetcode-scraper

python3 -m venv venv

source venv/bin/activate  # on mac/Linux

venv\Scripts\activate     # On Windows

pip install -r requirements.txt

# run the main file
python main.py

