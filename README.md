# github-example
Set up of GitHub repo

generate public and private key and put into github exempt


VIRTUAL ENVIRONMENT

Create a virtual environment: `python3 -m venv venv`
Activate virtual environment: `source venv/bin/activate`
Install module(s): `pip install <module>`
Capture modules in text file: `pip freeze > requirements.txt`
Put venv into gitignore:  `venv/`
On another computer, install dependencies from requirements: `pip install -r requirements.txt` 
Deactivate virtual environment: `deactivate`


GIT COMMANDS

Make a new project in terminal: `mkdir <project>`
Move into new project: `cd <project>`
Initialize directory as git: `git init -b main`
Create repo in GitHub:  `gh repo create <project>`
Pull down new gitignore and license if necessary: `git pull --set-upstream origin main`
Add files:  `git add .`
Commit files:  `git commit -m "message"`
Push to repo: `git push`



Check out a repository:  `git clone /path/to/repository`
Add one or more files to staging:  `git add <filename>` or `git add .`
Commit changes to head (but not yet to the remote repository): `git commit -m "Commit message"`
Send changes to the master branch of your remote repository: `git push origin master`
