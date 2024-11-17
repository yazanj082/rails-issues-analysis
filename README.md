
## Project Overview

This project solves the following tasks:

1. **Collect the last 500 issues from the Rails GitHub repository**: Using the GitHub API, the data is collected and stored in CSV format. This includes issues’ metadata like the number of comments, labels, creation date, and issue description.

2. **Data Analysis**:
   - **How do the number of issues evolve over time?** Analyze trends in issue creation over the years.
   - **Periods with a surge in issues**: Investigate if there are periods where more issues are reported.
   - **Reporter activity**: Identify if any users report more issues than others.
   - **Popular Categories**: Determine the most common labels for issues and visualize label distribution.
   - **Custom Question**: The Correlation between popularity and of label and number of comments.

3. **Classification of Issues**:
   - Use machine learning models from HuggingFace to classify issues based on their descriptions.
   - Train and evaluate a classification model to predict labels automatically for new issues.

## Methodology

### Data Collection

- **data_collect.py**: This Python script is responsible for collecting issues data from the Rails GitHub repository using the GitHub API.
- The data includes details such as issue descriptions, creation dates, labels, and the number of comments.
- The data is then saved into CSV files for further analysis.

### Data Analysis

- **data_analysis.ipynb**: This Jupyter notebook performs exploratory data analysis (EDA) and visualizations.
  - Trends over time in the number of issues are analyzed using line plots and bar charts.
  - The correlation between label popularity and the number of comments is studied.
  - The distribution of issue reports per author is visualized.
  - Popular categories (labels) are identified and visualized.

### Issue Classification

- **rails-issues-classification.ipynb**: This notebook utilizes HuggingFace’s models to automatically classify issues into pre-defined categories based on their descriptions.
  - A model is fine-tuned on the collected issues, and its performance is evaluated using standard metrics such as accuracy and F1 score.
  - The model is then used to classify the issues and visualize label distributions.

### Results & Analysis

- Visualizations such as box plots, scatter plots, and bar charts provide insights into the data.
- The performance of the classification model is reported, including accuracy metrics and a detailed explanation of the methodology used to train the model.

  ### Project Structure

  │
  ├───data
  │       rails_issues.csv              # Full dataset of collected issues
  │       rails_issues_partial.csv      # A partial dataset (subset of the full dataset)
  │
  ├───plots
  │       Box plot Issues Count per Label.png      # Visualization of issue count per label
  │       Correlation Between Label Popularity and Number of Comments.png  # Visual correlation between label popularity and comments
  │       Count of Author Issues.png    # Visualization of issues reported by authors
  │       Count of Labels in Issues.png # Visualization of label distribution across issues
  │       Count_of_Issues_Per_Year.png # Visualization of issues per year
  │       Issues Statistics.png         # Summary statistics of issues
  │       Number of Issues Over Time.png  # Visualization of issue counts over time
  │
  └───scripts
          data_analysis.ipynb           # Jupyter notebook for data analysis and exploration
          data_collect.py               # Python script to collect Rails issues from GitHub
          rails-issues-classification.ipynb  # Jupyter notebook for training and testing classification model
  


