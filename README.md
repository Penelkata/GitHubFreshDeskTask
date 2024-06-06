# Craft Exercise: GitHub Account to Freshdesk Contact
This Python command line program uses GitHub API v3 and Freshdesk API v2 intending to perform the following tasks:

- Get the GitHub user(username) and Freshdesk subdomain from the command line.
- Use GitHub personal access token as **GITHUB_TOKEN** environmental variable and Freshdesk API key as **FRESHDESK_TOKEN** environmental variable for authentication.
- Transfer all compatible fields from the GitHub User to the Freshdesk Contact.
- Create contacts using the API.
- Update already existing contacts using the API (Unfinished).
- Unit tests for the main program functionality(Unfinished).
- Persist login, name, and the creation date of the GitHub user in a table in a relational database (Optional).

# Set up
## Set GitHub personal access token as **GITHUB_TOKEN** environmental variable:

<br/> **Mac & Linux** 
##
    export GITHUB_TOKEN=<Your GitHub personal access token>
<br/> **Windows**:
##
    set GITHUB_TOKEN=<Your GitHub personal access token>
<br/>

## Set Freshdesk API key as **FRESHDESK_TOKEN** environmental variable:

<br/> **Mac & Linux** 
##
    export FRESHDESK_TOKEN=<Your Freshdesk API key>
<br/> **Windows** 
##
    set FRESHDESK_TOKEN=<Your Freshdesk API key>
<br/>

## Have **PyGithub** library installed
##
    pip install PyGithub

# Usage
Start the program by passing it the GitHub username and Freshdesk subdomain as arguments.
<br/>The command line program can only create accounts that are not currently available (409 error)
