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

from discord.ext import commands
import MySQLdb

import config


conn = db = MySQLdb.connect(user=config.DB_USER, passwd=config.DB_PASSWORD,
                            host=config.DB_HOST, port=config.DB_PORT)


class Bot(commands.Bot):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @property
    def conn(self):
        return conn
