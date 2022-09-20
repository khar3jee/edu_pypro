"""
commands for Bark app

class per command?
"""
from datetime import datetime
from database import DatabaseManager

db = DatabaseManager('bookmark.db')

class CreateBookmarkTableCommand:
    """creates table for bookmarks"""
    def execute(self):
        db.create_table('bookmarks', {
            'id': 'integer primary key autoincrement',
            'title': 'text not null',
            'url': 'text not null',
            'notes': 'text',
            'date_added': 'text not null',
        })

class AddBookmarkCommand:
    """Adds date to bookmark and
    executes add transaction to database"""
    def execute(self, input_data):
        input_data['date_added'] = str(datetime.utcnow().isoformat())
        db.add('bookmarks', input_data)
        return 'Bookmark Added'

#if __name__ == '__main__':
#    db._execute('CREATE TABLE IF NOT EXISTS testtable(test TEXT)')

"""
CREATE TABLE IF NOT EXISTS testtable(test TEXT)
id INTEGER PRIMARY KEY AUTOIINCREMENT,
title TEXT NOT NULL,
url TEXT NOT NULL,
notes TEXT NOT NULL,
date_added TEXT NOT NULL);
"""