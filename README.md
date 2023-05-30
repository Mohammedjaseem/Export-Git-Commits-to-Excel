# Export-Git-Commits-to-Excel

   To retrieve all the commits made in your repository and export them to an Excel file, you can use the GitHub API along with programming languages such as Python. Here's an example using the GitHub API and the Python programming language:

1. Install the required libraries:

   Install the requests library by running pip install requests in your command prompt or terminal.
   Install the pandas library by running pip install pandas in your command prompt or terminal.
   
         pip install requests
         pip install pandas
   

2.  Generate a personal access token (PAT) from GitHub:

    Go to your GitHub account settings and navigate to "Developer settings" -> "Personal access tokens."
    Click on "Generate new token" and provide a description for your token.
    Select the necessary permissions (e.g., repo) for accessing your repository.
    Click on "Generate token" and make sure to copy the generated token.

3. Use the  Python code in the file "Commit Excel Generator.py" to retrieve the commits and save them in an Excel file

Note : Make sure to replace 'YOUR_PERSONAL_ACCESS_TOKEN', 'YOUR_REPO_OWNER', and 'YOUR_REPO_NAME' with your actual personal access token, repository owner, and repository name, respectively.

After running the code, it will retrieve all the commits from your repository and save them in an Excel file named commit_details.xlsx.
