from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    TWILIO_ACCOUNT_SID: str = ""
    TWILIO_AUTH_TOKEN: str = ""
    TWILIO_WHATSAPP_NUMBER: str = ""
    GLPI_URL: str = ""
    GLPI_APP_TOKEN: str = ""
    GLPI_USER_TOKEN: str = ""

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()
