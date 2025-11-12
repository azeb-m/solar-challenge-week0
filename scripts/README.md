# Solar Data Streamlit Dashboard
Link: https://solar-challenge-week0-cd9g3hza4bunhqxewy64ki.streamlit.app/
Overview

This Streamlit dashboard visualizes and compares solar irradiance metrics (GHI, DNI, and DHI) across Benin, Sierra Leone, and Togo.
It enables users to interactively explore, filter, and analyze solar energy potential across countries and time periods.

Development Process

I created a new branch named dashboard-dev for developing the Streamlit dashboard.

I set up the project folder structure with an app/ directory containing main.py and utils.py for the dashboard code.

I activated the virtual environment and installed the required libraries using:

pip install streamlit pandas matplotlib seaborn


I developed the main Streamlit script (main.py) to visualize solar irradiance metrics (GHI, DNI, DHI) for Benin, Sierra Leone, and Togo.

I implemented interactive widgets to allow users to select countries and metrics dynamically.

I added boxplots and summary tables to compare solar data across countries.

I wrote a helper function in utils.py to load and process the cleaned CSV files from the data/ folder.

I tested the app locally using streamlit run app/main.py to ensure the dashboard worked correctly.



Features

Country Selection Widgets – Dynamically filter which countries’ data to visualize.

Date Range Filtering – Focus analysis on specific time periods.

Interactive Boxplots – Compare solar metrics (GHI, DNI, DHI) between countries.

Summary Tables – View mean, median, and standard deviation of each metric by country.

Multi-Page Navigation – Organized tabs for Home, Visualization, and Summary views.

Cached Data Loading – Optimized performance using Streamlit caching.


Run the App

To launch the dashboard locally:

streamlit run app/main.py

How to Use

Open the sidebar to:

Select which countries to display

Filter the dataset by date range

Use the top tabs to navigate:

 Home – Overview and usage guide

 Visualization – Boxplots comparing solar metrics

 Summary – Statistical summary table by country
