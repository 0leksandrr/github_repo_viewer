from fastapi import FastAPI
from .views import router


def create_app() -> FastAPI:
    app = FastAPI(
        title="GitHub REPO",
        version="0.0.1",
        debug=True,
    )
    app.include_router(router)
    return app


app = create_app()
