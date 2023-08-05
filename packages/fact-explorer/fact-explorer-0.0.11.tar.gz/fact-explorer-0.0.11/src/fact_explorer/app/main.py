from fastapi import FastAPI
from pathlib import Path


from fact_explorer.app.db.db_session import db_instance as database_instance
from fact_explorer.app.frontend.bridge import SpaStaticFiles
from fact_explorer.app.api.router import router as api_router
from fact_explorer.app.api.registry import router as registry_router
from fact_explorer.app.business.registry import prewarm_caches

app = FastAPI()

app.include_router(api_router)
app.include_router(registry_router)


@app.get("/health-check")
async def health_check() -> bool:
    return True


app.mount(
    "/",
    SpaStaticFiles(
        directory=str(Path(__file__).resolve().parent.joinpath("frontend/static")),
        html=True,
    ),
    name="Next SPA",
)


@app.on_event("startup")
async def startup() -> None:
    await prewarm_caches()
    await database_instance.connect()
    app.state.db = database_instance
