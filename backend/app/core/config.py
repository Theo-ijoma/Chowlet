from pydantic import Field  # type: ignore[import]
from pydantic_settings import BaseSettings, SettingsConfigDict  # type: ignore[import]


class Settings(BaseSettings):
    DATABASE_URL: str
    SUPABASE_URL: str
    SUPABASE_KEY: str = Field(validation_alias="SUPABASE_ANON_KEY")
    JWT_SECRET: str = Field(validation_alias="SUPABASE_JWT_SECRET")

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )


settings = Settings()
