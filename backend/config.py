import os
import subprocess
import logging
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

# Configure logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def deploy_to_heroku():
    repo_url = os.getenv('HEROKU_REPO')
    if repo_url:
        logger.info(f"Deploying to Heroku repository: {repo_url}")
        try:
            # Add deployment code here
            subprocess.run(["git", "add", "."], check=True)
            subprocess.run(["git", "commit", "-m", "Deploy to Heroku"], check=True)
            subprocess.run(["git", "push", "heroku", "main"], check=True)
            logger.info("Deployment successful.")
        except subprocess.CalledProcessError as e:
            logger.error(f"An error occurred during deployment: {e}")
        except Exception as e:
            logger.error(f"An unexpected error occurred: {e}")
    else:
        logger.error("Heroku repository URL is not set.")

if __name__ == "__main__":
    deploy_to_heroku()
