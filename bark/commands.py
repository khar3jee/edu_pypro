"""
commands for Bark app

"""
from database import DatabaseManager

db = DatabaseManager('test_bookmark.db')


if __name__ == '__main__':
    db._execute('CREATE TABLE IF NOT EXISTS testtable(test TEXT)')

"""
id INTEGER PRIMARY KEY AUTOIINCREMENT,
title TEXT NOT NULL,
url TEXT NOT NULL,
notes TEXT NOT NULL,
date_added TEXT NOT NULL);
"""