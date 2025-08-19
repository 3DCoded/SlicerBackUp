from pathlib import Path
from git import Repo, Actor
from git.exc import InvalidGitRepositoryError
from dotenv import load_dotenv
import os
import shutil

ENV_PATH = Path(__file__).parent / 'env.txt'
AUTHOR = Actor('SlicerBackUp', 'info@3dcoded.xyz')

load_dotenv(ENV_PATH)

CONFIG_PATH = os.getenv('SLICERBACKUP_CONFIG_DIR')
REPO_URL = os.getenv('SLICERBACKUP_REPO_URL')

def backup():
    git_dir = Path(CONFIG_PATH) / ".git"
    if git_dir.exists():
        try:
            repo = Repo(CONFIG_PATH)
        except InvalidGitRepositoryError:
            shutil.rmtree(git_dir)
            repo = Repo.init(CONFIG_PATH)
    else:
        repo = Repo.init(CONFIG_PATH)

    if "origin" not in [r.name for r in repo.remotes]:
        repo.create_remote("origin", REPO_URL)

    repo.index.add(["filament", "machine", "process"])
    repo.index.commit("Slicer profile backup", author=AUTHOR)
    origin = repo.remote("origin")
    origin.push(refspec="main:main", force=True, set_upstream=True)

if __name__ == '__main__':
    backup()