from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
import os
import tempfile
from backend.services.docker_runner import DockerRunner
from backend.services.result_parser import ResultParser

app = FastAPI()

@app.post("/submit/")
def submit_code(file: UploadFile = File(...)):
    # Save uploaded file to a temp location
    with tempfile.NamedTemporaryFile(delete=False, suffix=".py") as tmp:
        tmp.write(file.file.read())
        tmp_path = tmp.name
    # Mount student code as read-only
    mount_map = {tmp_path: "/app/app/views.py"}
    runner = DockerRunner(image="django-basic:latest")
    result = runner.run(mount_map, command="/runner.sh")
    verdict = ResultParser.parse(result["exit_code"])
    os.remove(tmp_path)
    return JSONResponse({
        "stdout": result["stdout"],
        "stderr": result["stderr"],
        "exit_code": result["exit_code"],
        "verdict": verdict
    })
