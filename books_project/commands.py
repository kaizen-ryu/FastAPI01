""""
    FastAPI CLI(Command Line Interface)
    commands for running fastapi applications...
"""
from fastapi import FastAPI

app=FastAPI()

@app.get("/fastapi-cli-commands")
async def fastapi_cli_commands(file_name: str):
    return [
        f"uvicorn {file_name}:app --reload",
        f"fastapi dev {file_name}.py",
        f"fastapi run {file_name}.py"
    ]