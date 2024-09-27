import os
import subprocess

# Set the environment variable for the Heroku repository
os.environ['HEROKU_REPO'] = os.getenv('HEROKU_REPO', 'https://git.heroku.com/pflege-app.git')

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'your_secret_key')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///site.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

def deploy_to_heroku():
    repo_url = os.getenv('HEROKU_REPO')
    if repo_url:
        print(f"Deploying to Heroku repository: {repo_url}")
        try:
            # Add deployment code here
            subprocess.run(["git", "add", "."], check=True)
            subprocess.run(["git", "commit", "-m", "Deploy to Heroku"], check=True)
            subprocess.run(["git", "push", "heroku", "main"], check=True)
            print("Deployment successful.")
        except subprocess.CalledProcessError as e:
            print(f"An error occurred during deployment: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
    else:
        print("Heroku repository URL is not set.")

if __name__ == "__main__":
    deploy_to_heroku()
