import streamlit as st
import pandas as pd
import altair as alt

from pathlib import Path
import os
from datetime import datetime, timedelta
import time

DATA_JOB_TYPES = ["Data Scientist", "Data Engineer", "Data Analyst"]
SHOW_COLUMNS = ["job_title", "company", "job_type_1", "job_type_2"]

st.set_page_config(page_title="Plotting Demo", page_icon="📊")

st.markdown("# Graph: Daily Data Science Job Postings")
st.markdown("""
Catch a glimpse of data science job postings on LinkedIn with this demo."""
)

st.info("""Data is gathered daily by scraping LinkedIn job search pages (keyword 'data', location 'Uusimaa, Helsinki'). 
        
Please note: the numbers presented here may vary by 1 to 10 from the actual counts due to occasional scraping errors."""
)


@st.cache_data
def get_daily_data(csv_path):
    # Check if data exists
    if not Path(csv_path).exists():
        raise FileNotFoundError(csv_path)
    
    # Get Number of job postings
    daily_data = pd.read_csv(csv_path).loc[:,SHOW_COLUMNS]
    y = len(daily_data)


    # Date -- Parse it from filename
    fname = os.path.basename(csv_path)
    x = fname[-14:-4]
    plot_data = pd.DataFrame({
        "date": [x],
        "n_positions": [y]
    })

    # Get dataframe
    daily_data.loc[:, "snapshot_date"] = x
    # Randomly assign the type of positions
    # TODO: don't use this
    import random
    daily_data.loc[:, "job_group"] = random.choices(DATA_JOB_TYPES, k=y)
    
    return plot_data, daily_data


# === progress bar

progress_bar = st.sidebar.progress(0)
status_text = st.sidebar.empty()
last_rows, df = get_daily_data(csv_path="../data/crawled_jobs_2023-10-28.csv")

chart = st.line_chart(last_rows, x="date", y="n_positions")

# === Main
start_date = datetime(2023, 10, 29)
end_date = datetime(2023, 11, 4)

date = start_date

while date <= end_date:
    csv_path = f"../data/crawled_jobs_{date.strftime('%Y-%m-%d')}.csv"

    new_rows, new_daily_data = get_daily_data(csv_path=csv_path)
    chart.add_rows(new_rows)
    df = pd.concat((df, new_daily_data), axis=0)

    # Update data loading progress
    _progress = (date - start_date).days / (end_date - start_date).days
    status_text.text("%i%% Complete" % _progress)
    progress_bar.progress(_progress)

    time.sleep(0.1)

    date += timedelta(days=1)

progress_bar.empty()

st.button("Re-run")