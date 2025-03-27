import requests
import json
import argparse

def create_pull_request(username, token, repo_owner, repo_name, head, base, title, body=None):
    """
    Create a pull request on GitHub using the provided parameters.
    
    :param username: GitHub username
    :param token: GitHub personal access token
    :param repo_owner: The owner of the repository
    :param repo_name: The name of the repository
    :param head: The branch where changes are implemented (source branch)
    :param base: The branch you want to merge the changes into (target branch)
    :param title: The title of the pull request
    :param body: The body/description of the pull request (optional)
    :return: Response from the GitHub API
    """
    
    # GitHub API URL for creating pull requests
    url = f'https://api.github.com/repos/{repo_owner}/{repo_name}/pulls'

    # Construct the payload for the pull request
    pr_data = {
        "title": title,
        "head": head,  # Source branch
        "base": base,  # Target branch
        "body": body or ""  # Optional description of the PR
    }

    # Send the POST request to create the pull request
    response = requests.post(
        url,
        headers={
            "Authorization": f"token {token}",
            "Accept": "application/vnd.github.v3+json"
        },
        data=json.dumps(pr_data)
    )

    # Check for a successful response
    if response.status_code == 201:
        print("Pull request created successfully!")
        print(f"PR URL: {response.json()['html_url']}")
    else:
        print(f"Failed to create pull request. Status code: {response.status_code}")
        print(f"Error: {response.json()}")

def main():
    # Set up argument parsing
    parser = argparse.ArgumentParser(description="Create a GitHub pull request from a specified branch.")
    
    # Add arguments for the command-line options
    parser.add_argument('--username', required=True, help="Your GitHub username")
    parser.add_argument('--token', required=True, help="Your GitHub personal access token")
    parser.add_argument('--repo-owner', required=True, help="The owner of the GitHub repository")
    parser.add_argument('--repo-name', required=True, help="The name of the GitHub repository")
    parser.add_argument('--head', required=True, help="The source branch (head) for the pull request")
    parser.add_argument('--base', required=True, help="The target branch (base) for the pull request")
    parser.add_argument('--title', required=True, help="The title of the pull request")
    parser.add_argument('--body', help="Optional description of the pull request")

    # Parse the arguments from the command line
    args = parser.parse_args()

    # Create the pull request
    create_pull_request(
        args.username,
        args.token,
        args.repo_owner,
        args.repo_name,
        args.head,
        args.base,
        args.title,
        args.body
    )

if __name__ == "__main__":
    main()