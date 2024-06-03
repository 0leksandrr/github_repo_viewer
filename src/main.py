from fastapi import FastAPI


def create_app() -> FastAPI:
    app = FastAPI(title="GitHub REPO", version="0.0.1")
    return app


app = create_app()
