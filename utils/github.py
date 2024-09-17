import requests
from utils.cmd_runner import CMD_RUNNER

class GITHUB(CMD_RUNNER):
    def __init__(self):
        super().__init__()

    def clone(self, url):
        """Clone a GitHub repository to a local directory."""
        name = "_".join(url.split("/")[-2:]).lower()
        path = f"repos/{name}"
        cmd = f"git clone {url} {path}"
        try:
            self._runCmd(cmd)
        except Exception as e:
            raise RuntimeError(f"Failed to clone repository: {e}")
        return name, path

    def check_dockerfile(self, url):
        """Check if the GitHub repository contains a Dockerfile."""
        ghp_key = None
        if "https://ghp_" in url:
            ghp_key = url.split("https://ghp_")[1].split("@")[0]
        
        x = url.split("/")
        repo_owner, repo_name = x[3], x[4]
        api_url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/contents/Dockerfile"
        
        headers = {}
        if ghp_key:
            headers["Authorization"] = f"token {ghp_key}"
        
        try:
            response = requests.get(api_url, headers=headers)
            response.raise_for_status()  # Raises HTTPError for bad responses
            res = response.json()
        except requests.RequestException as e:
            raise RuntimeError(f"Failed to check Dockerfile: {e}")

        return res.get("name") == "Dockerfile"

    def delete(self, path):
        """Remove the cloned repository directory."""
        cmd = f"rm -rf {path}"
        try:
            self._runCmd(cmd)
        except Exception as e:
            raise RuntimeError(f"Failed to delete repository: {e}")
