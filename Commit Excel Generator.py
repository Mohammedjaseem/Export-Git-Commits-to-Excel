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

# Send the GET request to retrieve all commits
response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    # Extract the commit data from the response
    commits = response.json()
    
    # Create a list to store the commit details
    commit_details = []
    
    # Iterate through each commit
    for commit in commits:
        sha = commit['sha']
        author = commit['commit']['author']['name']
        message = commit['commit']['message']
        
        # Add the commit details to the list
        commit_details.append({'SHA': sha, 'Author': author, 'Message': message})
    
    # Create a pandas DataFrame from the commit details
    df = pd.DataFrame(commit_details)
    
    # Save the DataFrame to an Excel file
    df.to_excel('commit_details.xlsx', index=False)
    
    print('Commit details saved to commit_details.xlsx')
else:
    print(f'Request failed with status code {response.status_code}')
