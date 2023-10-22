# ds-employment-landscape
A dashboard to show you Finland's data science employment landscape.

## Features of the deliverable (Work in progress)

A web app with the following panes:

1. A line chart of time against the number of data science positions.

    Optional feature: 
    - Choose time frame;  
    - Temperature of the job market

2. A line chart of time against the number of positions requiring English only, or English + Finnish, or Finnish only, or English + some other language.

3. The most valued technical skills for data scientists, data engineers and data analysts. 

    - TODO: Given a job description, how can we extract the technical skill related words?

    - Deliver a list of ordered keywords. And an example job description.

    - User should be able to choose from the dropdown menu: data scientists, data engineers or data analysts

    - Fixed time frame: the past 1 month.
    
4. (Optional) Salary prediction over company, title, experience level. 

## Machine learning problems

1. 

## Web app Development & Deployment plan

- Gradio for front end?

- A cron job to scrape data every day

- AWS app runner