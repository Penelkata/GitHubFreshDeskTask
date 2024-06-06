import os
import sys
import json
import requests
import base64
from github import Github

def get_github_user_data(username, github_token=None):
    if github_token:
        g = Github(github_token)
    else:
        g = Github()

    try:
        # Create dictionary with relevant/compatible information for the Contact
        # P.S The only ones we use are "name", "email", "bio"
        user = g.get_user(username)
        user_data = {
            "login": user.login,
            "name": user.name,
            "bio": user.bio,
            "company": user.company,
            "location": user.location,
            "email": user.email
        }
        return user_data
    except Exception as e:
        print(f"Error: {e}")
        return None

def create_freshdesk_contact(contact_data, freshdesk_subdomain, freshdesk_token):
    url = f"https://{freshdesk_subdomain}.freshdesk.com/api/v2/contacts"
    headers = {
        "Content-Type": "application/json",
        # Without using base64 encoder we will get unauthorized error 401
        "Authorization": "Basic " + base64.b64encode(freshdesk_token.encode()).decode()
    }
    response = requests.post(url, headers=headers, data=json.dumps(contact_data))
    if response.status_code == 201:
        print("Contact created successfully!")
        return response.json()
    else:
        print(f"Failed to create contact. Status code: {response.status_code}")
        return None

def main():
    if len(sys.argv) !=3:
        print("Enter valid number of arguments")
        sys.exit(1)

    github_username = sys.argv[1]
    github_token = os.getenv("GITHUB_TOKEN")

    # Initialize the PyGithub client
    g = Github(github_token)

    # Fetch user data from GitHub
    user = g.get_user(github_username)

    # Contact data for Freshdesk
    contact_data = {
        "name": user.name,
        "email": user.email,
        "description": user.bio
    }
    freshdesk_subdomain = sys.argv[2]
    freshdesk_token = os.getenv("FRESHDESK_TOKEN")

    # Create the contact
    create_freshdesk_contact(contact_data, freshdesk_subdomain, freshdesk_token)

if __name__ == "__main__":
    main()