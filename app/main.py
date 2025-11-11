import streamlit as st
import pandas as pd
from utils import load_data_with_fallback, plot_boxplot, top_countries_table

# --- PAGE CONFIG ---
st.set_page_config(page_title="Solar Data Dashboard", layout="wide")

# --- PAGE TITLE ---
st.title("Solar Data Comparison Dashboard")
st.markdown("Analyze solar irradiance metrics (GHI, DNI, DHI) across Benin, Sierra Leone, and Togo.")

# --- SIDEBAR: FILES + FILTERS ---
st.sidebar.header("🔹 Data Source & Filters")

uploaded_files = {
    "Benin": "data/benin_clean.csv",
    "SierraLeone": "data/sieraleone_clean.csv",
    "Togo": "data/togo_clean.csv"
}

gdrive_folder_url = "https://drive.google.com/drive/folders/17Ez5_aMAjVc1uX4e8XXbccwKXf6jkSBc?usp=sharing"

# --- LOAD DATASETS ---
dfs = []
for country, path in uploaded_files.items():
    df = load_data_with_fallback(path, gdrive_folder_url)  # use fallback function
    df['country'] = country
    dfs.append(df)

df_all = pd.concat(dfs, ignore_index=True)


# --- Country Selection (Checkboxes) ---
st.sidebar.subheader("Select Countries")
selected_countries = []
for country in uploaded_files.keys():
    if st.sidebar.checkbox(country, value=True):
        selected_countries.append(country)

if not selected_countries:
    st.warning("⚠️ Please select at least one country to view data.")
    st.stop()

df_filtered = df_all[df_all['country'].isin(selected_countries)]

# --- Date Range Filter ---
if 'Timestamp' in df_filtered.columns:
    st.sidebar.subheader("Select Date Range")
    min_date = df_filtered['Timestamp'].min()
    max_date = df_filtered['Timestamp'].max()

    date_range = st.sidebar.date_input("Filter by Date", [min_date, max_date])
    if isinstance(date_range, list) and len(date_range) == 2:
        start_date, end_date = date_range
        df_filtered = df_filtered[(df_filtered['Timestamp'] >= pd.to_datetime(start_date)) &
                                  (df_filtered['Timestamp'] <= pd.to_datetime(end_date))]

# --- Navigation Tabs ---
tabs = st.tabs(["🏠 Home", "📊 Visualization", "📈 Summary"])

with tabs[0]:
    st.subheader("Welcome 👋")
    st.markdown("""
    This interactive dashboard allows you to explore solar irradiance data across different countries.
    Use the sidebar filters to:
    - Select one or more countries  
    - Filter data by date range  
    - Switch between different solar metrics (GHI, DNI, DHI)  
    """)

with tabs[1]:
    st.subheader("📊 Solar Metric Visualization")
    metric = st.selectbox("Select a metric to analyze:", ["GHI", "DNI", "DHI"])
    fig = plot_boxplot(df_filtered, metric)
    st.pyplot(fig)
    st.caption("Use filters on the left to customize your view.")

with tabs[2]:
    st.subheader("📈 Summary Statistics by Country")
    metric_summary = st.selectbox("Choose a metric for summary:", ["GHI", "DNI", "DHI"])
    summary_table = top_countries_table(df_filtered, metric_summary)
    st.dataframe(summary_table, use_container_width=True)
    st.caption("Countries are ranked by their average irradiance values.")
