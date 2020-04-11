# Copyright 2020 Jarred Vardy <vardy@riseup.net>
#
# This file is part of DemocracyBot.
#
# DemocracyBot is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# DemocracyBot is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with DemocracyBot. If not, see http://www.gnu.org/licenses/.

import os

from discord.ext import commands

from data.prefix import get_guild_prefix


def main():
    client = commands.Bot(command_prefix=get_guild_prefix())
    for filename in os.listdir("./src/commands"):
        if filename.endswith(".py"):
            client.load_extension(f"commands.{filename[:-3]}")
    client.run(os.environ.get("BOT_TOKEN"))


if __name__ == "__main__":
    main()
