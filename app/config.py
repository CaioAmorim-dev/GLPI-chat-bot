from pydantic import BaseSettings

class Settings(BaseSettings):
    TWILIO_ACCOUNT_SID: str = ""
    TWILIO_AUTH_TOKEN: str = ""
    TWILIO_WHATSAPP_NUMBER: str = ""
    GLPI_URL: str = ""
    GLPI_APP_TOKEN: str = ""
    GLPI_USER_TOKEN: str = ""

    class Config:
        env_file = ".env"

settings = Settings()
