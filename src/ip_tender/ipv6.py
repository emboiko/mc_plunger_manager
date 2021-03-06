# emboiko
# 11/7/2020 - Initial commit(s)
# 11/19/2020 - Changed modpack to MC_Eternal & directory structure cleanup
# MC_Eternal_manager 
# Keep discord updated with a working hostname for MC_Eternal 1.3.7.1
# automated with windoze task-scheduler

from os import getenv
from subprocess import run
from datetime import datetime
from discord import Client
from dotenv import load_dotenv
import asyncio


class IPV6_Poll:

    def __init__(self):
        self.current_ipv6 = self.get_current_ipv6()
        self.compare_ipv6()


    def get_current_ipv6(self):
        result = run("ipconfig", capture_output=True).stdout.decode("utf-8")
        line = [
            line for line in result.split("\n") 
            if line.startswith("   IPv6 Address")
            ][0]
        return line.split(":",1)[1].strip()


    def compare_ipv6(self):
        with open("ipv6.txt", "r+") as f:
            previous_ipv6 = f.read()
            if self.current_ipv6 != previous_ipv6:
                f.seek(0)
                f.truncate(0)
                f.write(self.current_ipv6)
                self.update_discord()


    def update_discord(self):
        load_dotenv()
        TOKEN = getenv("DISCORD_TOKEN")
        client = Client()


        @client.event
        async def on_ready():
            for channel in client.get_all_channels():
                if channel.name == "MC_Eternal":
                    now = datetime.now()
                    date = now.strftime("%x")
                    time = now.strftime("%X")

                    await channel.purge(limit=1)
                    await channel.send(
                        f"MC_Eternal - Hostname updated {date} @ {time}\n"
                        f"{self.current_ipv6}\n"
                        f"Port is default @ 25565 and can be omitted."
                    )
                    await client.close()


        client.run(TOKEN)


def main():
    IPV6_Poll()


if __name__ == "__main__":
    main()
