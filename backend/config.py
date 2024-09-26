import os

# Set the environment variable for the Heroku repository
os.environ['HEROKU_REPO'] = 'https://git.heroku.com/pflege-app.git'

def deploy_to_heroku():
    repo_url = os.getenv('HEROKU_REPO')
    if repo_url:
        print(f"Deploying to Heroku repository: {repo_url}")
        # Add deployment code here
    else:
        print("Heroku repository URL is not set.")

if __name__ == "__main__":
    deploy_to_heroku()
