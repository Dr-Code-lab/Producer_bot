from dotenv import dotenv_values


config = dotenv_values(".env")  # config = {"key": "value", ...}

token = config.get("BOT_TOKEN")
admin = config.get("ADMIN")
ip = config.get("IP")