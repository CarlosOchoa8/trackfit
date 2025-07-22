from typing import List
from pydantic import Field
from pydantic_settings import BaseSettings

class CoreSettings(BaseSettings):
    """
    Application configuration settings.
    """

    # APP_SETTINGS
    APP_NAME: str = Field(default="Smithy API", description="Name of the application")
    VERSION: str = Field(default="0.1.0", description="Application version")

    # CORS settings
    CORS_ORIGINS: List[str] = Field(
        default=[
            "http://localhost:3000",
            "http://localhost:3000/",
            "http://localhost:8000",
            "http://localhost:8000/",
            "http://localhost:5173",
            "http://localhost:5173/",
            "https://trackfit-beta.vercel.app",
            "https://trackfit-beta.vercel.app/",
            ],
        description="CORS origins",
    )

core_settings = CoreSettings()
