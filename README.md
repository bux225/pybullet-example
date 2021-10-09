# github-example
Set up of GitHub repo

generate public and private key and put into github exempt


VIRTUAL ENVIRONMENT

`$ python3 -m venv venv`

`$ cd venv\Scripts`
`$ activate.bat`

`$ python -m pip freeze > requirements.txt`

`$ deactivate.bat`


GIT COMMANDS

Make a new project in terminal: `mkdir <project>`
Move into new project: `cd <project>`
Initialize directory as git: `git init -b main`
Create repo in GitHub:  `gh repo create <project>`
Pull down new gitignore and license if necessary: `git pull --set-upstream origin main`
Check out a repository:  `git clone /path/to/repository`
Add one or more files to staging:  `git add <filename>` or `git add .`
Commit changes to head (but not yet to the remote repository): `git commit -m "Commit message"`
Send changes to the master branch of your remote repository: `git push origin master`
