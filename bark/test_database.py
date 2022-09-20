"""
unit testing for database with pytest
"""

from database import DatabaseManager
from commands import CreateBookmarkTableCommand

class TestDatabase:
    """
    must pass these test values
    CREATE TABLE IF NOT EXISTS testtable, (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    url TEXT NOT NULL,
    notes TEXT NOT NULL,
    date_added TEXT NOT NULL);
    """
    db = DatabaseManager('test_bookmark.db')

    def test_db_prep(self):
        self.db._execute('DROP TABLE IF EXISTS testtable')

    #def test_execute(self):
    #    self.db._execute('DROP TABLE testtable')
    #    self.db._execute('CREATE TABLE IF NOT EXISTS testtable(test TEXT)')

    def test_create_table(self):
        #CreateBookmarkTableCommand().execute()
        self.db.create_table('testtable', {
            'test_id': 'integer primary key autoincrement',
            'test_title': 'text not null',
            'test_url': 'text not null',
            'test_notes': 'text not null',
            'test_date_added': 'text not null',
        })
