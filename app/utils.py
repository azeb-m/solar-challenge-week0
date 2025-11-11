import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
import os
import gdown

@st.cache_data
def load_data_with_fallback(file_path, gdrive_folder_url):
    """Load CSV from local path; if missing, download from Google Drive folder."""
    if not os.path.exists(file_path):
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        gdown.download_folder(gdrive_folder_url, output=os.path.dirname(file_path), quiet=False)
    df = pd.read_csv(file_path, parse_dates=['Timestamp'])
    return df
@st.cache_data
def load_data(file_path):
    """Load cleaned CSV file into a pandas DataFrame."""
    df = pd.read_csv(file_path, parse_dates=['Timestamp'])
    return df

def plot_boxplot(df, metric):
    """Generate a boxplot for the selected metric."""
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.boxplot(x='country', y=metric, data=df, palette='viridis', ax=ax)
    ax.set_title(f'{metric} Distribution by Country', fontsize=14)
    ax.set_xlabel('Country')
    ax.set_ylabel(f'{metric} (W/m²)')
    return fig

def top_countries_table(df, metric):
    """Return a summary table sorted by average metric."""
    summary = df.groupby('country')[metric].agg(['mean', 'median', 'std']).reset_index()
    summary = summary.sort_values(by='mean', ascending=False)
    summary.columns = ['Country', 'Mean', 'Median', 'Standard Deviation']
    return summary
