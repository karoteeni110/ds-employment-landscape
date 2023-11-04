# 1-Week Snapshot: Uncovering Helsinki's Data Science Job Market 

## Data Collection 

Sources of Data:

Kaggle: Initially considered, but excluded due to the lack of European job data.

Web Scraping: Used as the primary data source.

### Stage #1: Manual Web Scraping

Employed the Linkedin_scraper tool.

Used the keyword "data" to cast a wide net for job listings, ensuring high recall.

Later filtered non-data-related job postings during data cleaning.

### Stage #2: Data Engineering and Automation 

Automated the web scraping process using Amazon EC2 VPC for efficiency and scalability.

Managed data by converting it from CSV format to SQLite for analysis.

## Exploratory Data Analysis (EDA)

### Question 1: Describing the market

- Investigated the number of data-related job postings in Helsinki.

- Examined the volatility of the job market to understand its dynamics.

### Question 2: Real data science jobs VS. Irrelevant results

Explored the distinction between authentic data science job postings and unrelated or misleading listings.

### Question 3: Language Usage in Job Postings

Analyzed the languages used in job descriptions to identify trends and preferences.

## Data Cleaning 

### Remove irrelevant jobs

Filtered out irrelevant job postings to ensure data accuracy.

### Translate Non-English Job Postings

Addressed language diversity by translating non-English job postings for a comprehensive analysis.

## Data Modeling

Identifying Required Skills for Data Roles

To understand the skills required for data scientist, data engineer, and data analyst positions:

- Classified job postings into these specific categories.
- Extracted relevant skill keywords from job descriptions.
- Visualized the distribution of skills across different job types.

### Modelling #1: Job Posting Classification

Utilized embedding and unsupervised clustering techniques to categorize job postings into data scientist, data engineer, and data analyst groups.

### Modelling #2: Skills Extraction

Employed a question-answering model to extract key skill information from job descriptions, providing a deeper understanding of the skill requirements for each role.