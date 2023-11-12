# 1-Week Snapshot: Uncovering Helsinki's Data Science Job Market 

This blog aims at giving the audience a general picture of Helsinki's data science job market using the result from Linkedin job search.

For more detailed data collection processes and analysis, see the Github repo: https://github.com/karoteeni110/ds-employment-landscape/tree/main/notebooks 

## Data Collection 

My exploration of Helsinki's data science job market starts by collecting the data. The data sources I have considered:

- Kaggle: Initially considered, but excluded due to the absence of European job data.
- Web Scraping: Chosen as the primary data source for its breadth and depth. Although it is against the user agreement to scrape Linkedin webpage.

Given the ethical concers from the user agreement, I limited the data collecation to one-week's amount. This yields 

### Stage #1: Web Scraping

In this phase, I leveraged the `linkedin_scraper` tool (See [here](https://github.com/joeyism/linkedin_scraper/tree/master)) for data crawling. The mechenism of the tool is that it initiates a `selenium` web driver, log in with an account, fetch the source page, and finally parse the page to get information. 

Unfortunately, the tool is not well maintained: A lot of features are not synced with the dependencies; Linkedin authentication requires a life check; Parsing does not fit Linkedin pages' layout and so on. The errors need to be fixed manually. See my debugging process from the [notebook](https://github.com/karoteeni110/ds-employment-landscape/blob/main/notebooks/00-debug-scraper.ipynb).

After debugging, the scraper works as smoothly as a browser.

[picture]

By using the keyword "data," I cast a wide net for job listings to ensure high recall. Subsequently, during data cleaning, I meticulously filtered out non-data-related job postings.

### Stage #2: Data Engineering and Automation 

To enhance efficiency and scalability, I automated the web scraping process using Amazon EC2 VPC: It has a remote desktop, which allows me to log in from the graphic interface to pass the life check.  

## Exploratory Data Analysis (EDA)

See the full analysis [here](https://github.com/karoteeni110/ds-employment-landscape/blob/main/notebooks/02-EDA.ipynb). Briefly, the questions and the observations are:

### #1 How much data is there?

- We have collected the data of consecutive days from 2023-10-28 to 2023-11-04, and a non-consecutive day of 2023-10-22. Including the statistics of all the days to the plotting demo can result in a gap, so I would skip the non-consecutive one.

- New data will come to the plotting demo later. A continuous pipeline would be needed to validate and deploy the new batches.

### #2: What does every day's job postings look like?

- `required_skills` is a list of skills delimited by commas, but is stored as a single string. It would require tokenizing.
- `applicant_count` and `benefit` columns are not informative and should be dropped.
- `company_linkedin_url` and `posted_date` not useful for answering the research questions (Q1 or Q2), and should be dropped.
- `location` contains non-relevant infomation, such as company name and applicants. It should also be dropped.

### #3 Are there duplicate postings in the day's crawl?

Usually not. In any case, deduplication should be part of the preprocessing pipeline.

### #4 Descriptive statistics

- Across the one week's data collection, there are 2593 postings but only 699 unique jobs in the market (or at least open ones in Linkedin). 

- `job_title`s are variable -- there are 545 unique titles out of 2593 postings.

- The skills named by recruiter are similarly variable as job titles.

- Most jobs employ hybrid working mode.

- Most jobs are full-time -- leaving only ~100 positions for contractors, interns and part-timers.

- A lot of `required_skills` specified by the recruiters are general and not informative -- Words like "problem-solving" or "data analytics" means nothing. More advanced keyword extraction is needed -- to extract specific skills such as "team work", "Presentations", "English", "Python" or "Spark".

### #5 How many jobs require Finnish? English? Swedish? Or both Fin & Eng?

- Around 10% of the jobs contains Finnish. This is a big chunk.

- For the purpose of extracting skill keywords or of classifying jobs -- Either I should use a multilingual language model to handle them, or I should translate Finnish.

### #6 Job Classification - Data scientist, engineer or analyst (or None of those)?

- Naively following the job titles cannot accurately classify the jobs. There are inconsistencies between the titles and the postings, or some titles are not explicitly stating which group the job belongs to: Some of the jobs are real data engineer positions, but some are not. For example 'Peroxides Process Engineer - Europe 1' and 'Manager, Process Engineering'. 

- To classify the jobs, we can use the former to train a machine learning model, or use them as the test set for unsupervised algorithms. And the rest unknowns should take the classification's label. 

## Data Cleaning 

Data cleaning is done by a pipeline of the following steps:

1. Standardize job URLs. Job searches from `linkedin_scraper` have gone through multiple redirections, which causes the URLs to contain unnecessary parameters. The job URLs can be shortened by stripping the parameters. It also makes scraping faster.

2. Transform job types (remote, full-time jobs etc) from strings to boolean. This step is for the plotting demo: This way the users can choose data views by filtering job types.

3. Drop useless columns. This is for better readability of the data frame demo.

4. Detect job languages. Again for better readability of the demo; and the job posting language is an implicit skill requirement.

The data cleaning pipeline (For the full code, see [utils.py](https://github.com/karoteeni110/ds-employment-landscape/blob/main/notebooks/utils.py)):

```python
def preprocess_agg_df(df):
    steps = []

    # ...

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
```

## Data Modeling

One of the trendiest topic in data science community is the career prospects of different roles: data scientist, data engineer, and data analyst. The division of the roles is a domain-specific phenomenon. Given the division, it is worth classifying the job postings into the groups and analyze the divided market in detail. Naturally, these problems are fit to be solved by machine learning methods:

- Job Posting Classification: A classification problem. Useful features can be job titles and job descriptions; Language models can embed and extract features from job description documents. With a proper classification method (such as Random Forest) the jobs can be assigned to groups. 

- Skills Extraction: A (token-level) classification problem. Leveraging a question-answering model, I can extract key skill information from job descriptions, providing nuanced insights into the skill requirements for each role.

Unfortunately given the limited time, I haven't finished the data modeling: Data collection and cleaning took almost all my time. But The exploration will come soon.