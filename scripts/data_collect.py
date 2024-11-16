import requests
import pandas as pd
import time

# GitHub API settings
REPO = "rails/rails"
BASE_URL = f"https://api.github.com/repos/{REPO}/issues"
TOKEN = ""
HEADERS = {"Authorization": f"token {TOKEN}"} if TOKEN else {}

# Parameters
ISSUES_PER_PAGE = 100
TOTAL_ISSUES = 17700
PAGES = (TOTAL_ISSUES // ISSUES_PER_PAGE) + 1

# Data collection
issues_data = []
rate_limit_exceeded = False

for page in range(1, PAGES + 1):
    print(f"Fetching page {page} of {PAGES}...")
    params = {"state": "all", "per_page": ISSUES_PER_PAGE, "page": page}
    response = requests.get(BASE_URL, headers=HEADERS, params=params)

    # Handle rate limiting
    if response.status_code == 403:
        print("Rate limit reached. Waiting for 60 seconds before retrying...")
        time.sleep(60)
        continue
    elif response.status_code != 200:
        print(f"Error: {response.status_code} - {response.text}")
        break

    issues = response.json()

    # Stop if no more issues are found (in case of fewer than expected issues)
    if not issues:
        print("No more issues found. Stopping.")
        break

    # Extract issue details
    for issue in issues:
        if "pull_request" in issue:  # Skip pull requests, only collect issues
            continue
        issue_data = {
            "id": issue.get("id"),
            "number": issue.get("number"),
            "title": issue.get("title"),
            "description": issue.get("body"),
            "labels": [label["name"] for label in issue.get("labels", [])],
            "comments": issue.get("comments"),
            "author": issue.get("user", {}).get("login"),
            "created_at": issue.get("created_at"),
            "state": issue.get("state"),
        }
        issues_data.append(issue_data)

    # Save data every 10 pages to avoid data loss
    if page % 10 == 0:
        df = pd.DataFrame(issues_data)
        df.to_csv("data/rails_issues_partial.csv", index=False)
        print(f"Saved partial data up to page {page}.")

    # Respect the API rate limit
    time.sleep(1)

# Final save
df = pd.DataFrame(issues_data)
df.to_csv("data/rails_issues.csv", index=False)
print("Data collection complete. Saved to 'rails_issues.csv'.")