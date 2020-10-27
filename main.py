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

import discord
from discord.ext import commands
import MySQLdb

import demobot.config as config
from demobot.data.prefix import get_guild_prefix


def create_bot():
    return commands.Bot(
        intents=discord.Intents(members=True),
        fetch_offline_members=True,
        command_prefix=get_guild_prefix(),
        case_insensitive=True,
        owner_id=config.OWNERS,
        help_command=None,
    )


def setup_db():
    db = MySQLdb.connect(user=config.DB_USER, passwd=config.DB_PASSWORD,
                         host=config.DB_HOST, port=config.DB_PORT)

    cur = db.cursor()
    cur.execute("CREATE DATABASE IF NOT EXISTS " + config.DB_DEFAULT_DATABASE)
    db.commit()

    cur.execute("USE " + config.DB_DEFAULT_DATABASE)
    cur.execute("CREATE TABLE IF NOT EXISTS test_table (a_number bigint NOT NULL PRIMARY KEY, some_name text)")
    # cur.execute("INSERT INTO test_table (a_number, some_name) VALUES (%s, %s)", (12345678955555, "A string value"))
    db.commit()

    cur.execute("SELECT * FROM test_table")
    cur.fetchall()


def init_db():
    pass


def main():
    setup_db()
    client = create_bot()
    for filename in os.listdir("./demobot/commands"):
        if filename.endswith(".py"):
            client.load_extension(f"demobot.commands.{filename[:-len('.py')]}")
    client.run(config.BOT_TOKEN)


if __name__ == "__main__":
    main()
