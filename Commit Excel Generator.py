import requests
import pandas as pd

# Set your personal access token and repository details
token = 'YOUR_PERSONAL_ACCESS_TOKEN'
owner = 'YOUR_REPO_OWNER'
repo = 'YOUR_REPO_NAME'

# Define the API endpoint
url = f'https://api.github.com/repos/{owner}/{repo}/commits'

# Set the request headers
headers = {
    'Authorization': f'Token {token}',
    'Accept': 'application/vnd.github.v3+json'
}

# Create an empty list to store all commits
all_commits = []

# Send a GET request to retrieve commits page by page
page = 1
while True:
    # Add pagination information to the API endpoint
    page_url = f'{url}?page={page}&per_page=100'
    
    # Send the GET request to retrieve a page of commits
    response = requests.get(page_url, headers=headers)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Extract the commit data from the response
        commits = response.json()
        
        # Check if the current page has any commits
        if len(commits) == 0:
            break  # Exit the loop if there are no more commits
        
        # Iterate through each commit
        for commit in commits:
            sha = commit['sha']
            author = commit['commit']['author']['name']
            message = commit['commit']['message']
            date = commit['commit']['author']['date']
            
            # Add the commit details to the list
            all_commits.append({'SHA': sha, 'Author': author, 'Message': message, 'Date': date})
        
        page += 1
    else:
        print(f'Request failed with status code {response.status_code}')
        break

# Create a pandas DataFrame from the commit details
df = pd.DataFrame(all_commits)

# Save the DataFrame to an Excel file
df.to_excel('commit_details.xlsx', index=False)

print('Commit details saved to commit_details.xlsx')
