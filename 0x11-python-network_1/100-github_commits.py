#!/usr/bin/python3
"""
retrieves and prints 10 most recent commits from the
"rails" repository by the user "rails" using the GitHub API
"""
import requests
import sys

if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    response = requests.get(url)

    if response.status_code == 200:
        commits = response.json()
        for commit in commits[:10]:
            sha = commit['sha']
            author_name = commit['commit']['author']['name']
            print(f"{sha}: {author_name}")
