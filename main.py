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
import asyncio
import signal

import discord
from discord.ext import commands

import demobot.commands as bot_commands
import demobot.config as config
from demobot import db
from demobot.data.prefix import get_guild_prefix


def create_bot():
    intents = discord.Intents.all()
    intents.presences = False
    return commands.Bot(
        intents=intents,
        fetch_offline_members=True,
        command_prefix=get_guild_prefix(),
        case_insensitive=True,
        owner_id=config.OWNERS,
        help_command=None,
    )


async def setup_db():
    async with await db.connection() as connection, connection.cursor() as cursor:
        await connection.begin()
        await cursor.execute(f"CREATE DATABASE IF NOT EXISTS {config.DB_DEFAULT_DATABASE}")
        await connection.commit()
        await cursor.execute(f"USE {config.DB_DEFAULT_DATABASE}")
        await cursor.execute(
            "CREATE TABLE IF NOT EXISTS test_table (a_number bigint NOT NULL PRIMARY KEY, some_name text)")
        await connection.commit()
        await cursor.execute("SELECT * FROM test_table")
        await cursor.fetchall()


async def main():
    try:
        await setup_db()
        bot = create_bot()
        for module_name in bot_commands.__all__:
            bot.load_extension(f"{bot_commands.__name__}.{module_name}")
        for c in bot.commands:
            print(c.name)
        await bot.start(config.BOT_TOKEN)
    finally:
        await db.close()


if __name__ == "__main__":
    asyncio.run(main())
