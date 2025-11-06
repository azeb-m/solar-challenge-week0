# solar-challenge-week0
# Solar Data Discovery: Week 0 Challenge  
Date: 05 Nov - 12 Nov 2025  

## Project Overview  
The challenge focuses on understanding, exploring, and analyzing solar-farm data from Benin, Sierra Leone, and Togo. The goal is to evaluate key trends and deliver insights that support regional solar installation strategy for MoonLight Energy Solutions.

## Environment Setup & Reproduction  
1. Clone the repository  
git clone https://github.com/azeb-m/solar-challenge-week0.git
cd solar-challenge-week0
2. Create & switch to the setup branch
git checkout -b setup-task
3. Create and activate a Python virtual environment
python -m venv venv
venv/Scripts/activate
4. Install dependencies
python -m pip install --upgrade pip
pip install -r requirements.txt
5. Create the GitHub Actions workflow directory & file
mkdir -p .github/workflows
touch .github/workflows/ci.yml
Then edit ci.yml with workflow content (checkout repo, setup Python, install dependencies).
6. Commit changes on setup-task branch
git add .gitignore requirements.txt .github/workflows/ci.yml
git commit -m "init: add .gitignore"
git commit -m "chore: venv setup"
git commit -m "ci: add GitHub Actions workflow"
7. Push branch and create Pull Request
git push -u origin setup-task
Then on GitHub create a Pull Request from setup-task → main and merge it.

Folder Structure
.

├── .github/
│   └── workflows/
│       └── ci.yml
├── .gitignore
├── requirements.txt
├── README.md
├── src/
├── notebooks/
│   ├── __init__.py
│   └── README.md
├── tests/
│   ├── __init__.py
└── scripts/
    ├── __init__.py
    └── README.md