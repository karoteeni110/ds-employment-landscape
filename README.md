# ds-employment-landscape
A dashboard to show you Finland's data science employment landscape.

## Features of the deliverable (Work in progress)

Use tabs: https://docs.streamlit.io/library/api-reference/layout/st.tabs 

### Page 1, Demo

A web app with the following panes:

1. A line chart of time against the number of data science positions.

https://www.gradio.app/docs/lineplot 

    Optional feature: 
    - Choose time frame;  
    - Temperature of the job market

3. A line chart of time against the number of positions requiring English only, or English + Finnish, or Finnish only, or English + some other language.

4. The most valued technical skills for data scientists, data engineers and data analysts. 

    - TODO: Given a job description, how can we extract the technical skill related words?

    - Deliver a list of ordered keywords. And an example job description.

    - User should be able to choose from the dropdown menu: data scientists, data engineers or data analysts

    - Fixed time frame: the past 1 month.
    
5. (Optional) Salary prediction over company, title, experience level. 

### Page 2, Blog post

Sections:

- Data collection
      - How I crawled Linkedin
      - C

- Data management (Using simple CSVs)


## Web app Development & Deployment plan

- Gradio for front end?

- A cron job to scrape data every day

- AWS app runner to host the web app