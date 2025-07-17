import os
from TwitchChannelPointsMiner import TwitchChannelPointsMiner
from TwitchChannelPointsMiner.logger import LoggerSettings

print("=== DEBUG: Starting Twitch Miner ===")
print(f"Username: {os.getenv('TWITCH_USERNAME')}")
print(f"Streamers: {os.getenv('TWITCH_STREAMERS')}")

# Sichere Konfiguration mit Umgebungsvariablen
twitch_miner = TwitchChannelPointsMiner(
    username=os.getenv("TWITCH_USERNAME"),  # ✅ Korrekte Environment Variable
    logger_settings=LoggerSettings(
        save=True,
        console_level="INFO",
        file_level="DEBUG",
        emoji=True,
        colored=True
    )
)

# Streamer aus Umgebungsvariable laden
streamers = os.getenv("TWITCH_STREAMERS", "CmdKrieger,zarbex,MontanaBlack88").split(",")
print(f"Mining streamers: {streamers}")

twitch_miner.mine(streamers)
