from datetime import datetime, timedelta
import pandas as pd

from pathlib import Path
import re

from ftlangdetect import detect

def load_aggregated_data():
    this_path = Path(__file__)
    data_dir_path = Path(this_path.parent.parent.absolute(), "data")
    
    start_date = datetime(2023, 10, 29)
    end_date = datetime(2023, 11, 4)

    date = start_date
    dfs = []
    while date <= end_date:
        csv_path = Path(data_dir_path, f"crawled_jobs_{date.strftime('%Y-%m-%d')}.csv")

        new_daily_data = pd.read_csv(csv_path)
        new_daily_data.loc[:,"crawl_date"] = date
        dfs.append(new_daily_data)

        date += timedelta(days=1)

    df = pd.concat(dfs, axis=0, ignore_index=True)
    return df

def _standardize_job_url(url):
    return re.match(string=url, pattern="https://www.linkedin.com/jobs/view/\d+").group(0)
    
def standardize_job_urls(df):
    df.loc[:,"linkedin_url"] = df.loc[:, "linkedin_url"].map(_standardize_job_url)
    return df

def preprocess_agg_df(df):
    steps = []

    def is_remote(df):
        df["is_remote"] = df.apply(lambda _row: _row["job_type_1"] == "Remote" 
                                or _row["job_type_2"] == "Remote"
                                , axis=1)
        return df
    
    def is_on_site(df):
        df["is_on_site"] = df.apply(lambda _row: _row["job_type_1"] == "On-site" 
                                    or _row["job_type_2"] == "On-site" 
                                    , axis=1)
        return df

    def is_hybrid(df):
        df["is_hybrid"] = df.apply(lambda _row: _row["job_type_1"] == "Hybrid" 
                                    or _row["job_type_2"] == "Hybrid" 
                                    , axis=1)
        return df
                        

    def is_fulltime(df):
        df["is_fulltime"] = df.apply(lambda _row: _row["job_type_1"] == "Full-time"
                                    or _row["job_type_2"] == "Full-time",
                                    axis=1)
        return df
    
    def drop_useless_columns(df):
        _show_columns = [x for x in df.columns 
                        if (x not in [
                            "applicant_count", "benefits","company_linkedin_url", "location", "posted_date", "job_type_1", "job_type_2"
                            ])]
        return df.loc[:,_show_columns]
    
    def add_jd_langs(df):
        # Add "jd_langs" column
        def get_jd_langs(jd):
            langs = set()
            for line in jd.split("\n"):
                # Remove empty line,
                # the prilogue "About the job",
                # the epilogue "See more".
                clean_line = line.strip().lower()
                if not clean_line or \
                len(clean_line.split()) <= 4:
                    continue

                detected_lang =  detect(clean_line)["lang"]
                langs.add(detected_lang)
            return langs

        df["jd_langs"] = df.job_description.map(get_jd_langs)
        
        # Remove the wrong detections
        idx_lang_anomalies = df.jd_langs.isin(df.jd_langs.value_counts().index[4:])
        df.loc[idx_lang_anomalies, ["jd_langs"]] = df.loc[idx_lang_anomalies, ["jd_langs"]].apply(lambda _: {"en"}, axis=1)

        return df

    steps.append(standardize_job_urls)
    steps.append(is_remote)
    steps.append(is_on_site)
    steps.append(is_hybrid)
    steps.append(is_fulltime)
    steps.append(drop_useless_columns)
    steps.append(add_jd_langs)

    for step in steps:
        df = df.pipe(step)
        print(step, "done")
    
    return df 

if __name__ == "__main__":
    data = load_aggregated_data()
    preprocessed_data = preprocess_agg_df(data)
    print(preprocessed_data)