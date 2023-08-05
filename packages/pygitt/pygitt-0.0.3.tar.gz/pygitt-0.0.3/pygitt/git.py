def clone(repository_url):
    import os

    os.system(f'git clone {repository_url}')
def add():
    import os

    os.system('git add .')
def commit(commit_message):
    import os

    os.system(f'git commit -m "{commit_message}"')
def push():
    import os

    os.system('git push')
def pull():
    import os

    os.system('git pull')
def status():
    import os

    os.system('git status')