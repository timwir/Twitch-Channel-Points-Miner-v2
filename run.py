import os
from TwitchChannelPointsMiner import TwitchChannelPointsMiner
from TwitchChannelPointsMiner.logger import LoggerSettings

# Sichere Konfiguration mit Umgebungsvariablen
twitch_miner = TwitchChannelPointsMiner(
    username=os.getenv("TimwirDE"),
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
twitch_miner.mine(streamers)
