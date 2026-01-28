import subprocess
import os
import uuid
from typing import Dict, Any

class DockerRunner:
    """
    Runs student code in a secure, resource-limited Docker container.
    """
    def __init__(self, image: str, timeout: int = 10):
        self.image = image
        self.timeout = timeout

    def run(self, mount_map: Dict[str, str], command: str) -> Dict[str, Any]:
        container_name = f"judge_{uuid.uuid4().hex[:8]}"
        mounts = []
        for host_path, container_path in mount_map.items():
            mounts.extend(["-v", f"{host_path}:{container_path}:ro"])
        # Add tmpfs for /tmp to allow pytest to create temporary files despite --read-only
        mounts.extend(["--tmpfs", "/tmp:rw,noexec,nosuid,size=50m"])
        docker_cmd = [
            "docker", "run", "--rm",
            "--name", container_name,
            "--network", "none",
            "--read-only",
            "--cpus=1",
            "--memory=512m",
            "--pids-limit=100",
            "--cap-drop", "ALL",
            "--security-opt", "no-new-privileges",
            *mounts,
            self.image,
            "/bin/sh", "-c", command
        ]
        try:
            proc = subprocess.run(
                ["gtimeout", str(self.timeout)] + docker_cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                timeout=self.timeout+2
            )
            return {
                "stdout": proc.stdout.decode(),
                "stderr": proc.stderr.decode(),
                "exit_code": proc.returncode
            }
        except subprocess.TimeoutExpired:
            # Hard kill fallback
            subprocess.run(["docker", "rm", "-f", container_name])
            return {
                "stdout": "",
                "stderr": "Time limit exceeded.",
                "exit_code": 124
            }
