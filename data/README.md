# Job Posting Data

## Kaggle data (Jobs in the U.S.)

Data downloaded from Kaggle. The source and download time (dd-mm-yyyy):

```
name,source,job_source,download_time,share_ok_license
kaggle-linkedin_Job_data,https://www.kaggle.com/datasets/shashankshukla123123/linkedin-job-data/data,linkedin,07-03-2023,yes
kaggle-linkedin-job-2023,https://www.kaggle.com/datasets/arshkon/linkedin-job-postings,linkedin,07-03-2023,yes
""
```

## Crawled data (Jobs in Helsinki region)

Filenames: `crawled_jobs_{date}.csv`

Linkedin job postings data collected from 2023-10-28 till now. The result of running `../notebooks/01-collect-data.ipynb` every day. 

The crawling task can be automated using an AWS EC2 instance with VNC connection, to pass the security check from Linkedin. See https://github.com/joeyism/linkedin_scraper/issues/177 