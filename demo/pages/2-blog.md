# 1-Week Snapshot: Uncovering Helsinki's Data Science Job Market 

## Data Collection 

Candidates:
- Kaggle 

Not used because of lack of Europe data

- Web scrapings

### Stage #1: Manual Web Scraping

Linkedin_scraper

keyword: data. Try to be general for high recall; Filter non data related job later.

### Stage #2: Data Engineering and Automation 

#### Automating Web Scraping with Amazon EC2 VPC

#### Data Management: From CSVs to SQLite

## EDA 

### Question 1: Describing the market: How many data jobs are there? How volatile the job market is?

### Question 2: Real data science jobs VS. Irrelevant results

### Question 3: What languages are used in the job postings?

## Data Cleaning 

### Remove irrelevant jobs

### Translate Non-English Job Postings

## Data Modelling

What skills do data scientist, engineer, and analyst jobs require?

To know that, we need to:

1. Classify the job postings into data scientist-, engineer-, and analyst- groups;

2. Extract the skill keywords from the job postings;

3. Show the distribution of each skills across the kinds of jobs.

### Modelling #1: Job Posting Classification

Embedding + Unsupervised clustering.

### Modelling #2: Skills Extraction

Question answering model 