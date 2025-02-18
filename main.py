import json
import os
import shutil
import requests
from urllib.parse import urlparse
from sys import argv
import tempfile


def download(url: str, dest=None):
    split = url.split("/")
    try:
        s1, s2, s3, owner, repo, _, branch, *path = split
        path = "/".join(path)
    except:
        try:
            s1, s2, s3, owner, repo = split
            path = None
        except:
            print("Invalid URL")
    gh_base = "/".join([s1, s2, s3, owner, repo])
    if not dest:
        if path:
            dest = path
        else:
            dest = repo
    print(f"Owner: {owner}")
    print(f"Repo: {repo}")
    print(f"Branch: {branch}")
    print(f"Path: {path}")
    print(f"Destination: {dest}")

    # clone into a temporary directory
    with tempfile.TemporaryDirectory() as tmpdir:
        os.system(f"git clone {gh_base} {tmpdir}/{repo}")
        s = os.path.join(tmpdir, repo)
        shutil.rmtree(os.path.join(s, ".git"))
        if path:
            s = os.path.join(s, path)
        d = os.path.join(os.getcwd(), dest)
        shutil.copytree(s, d, dirs_exist_ok=True)


def main():
    download(argv[1])


if __name__ == "__main__":
    download(argv[1])
