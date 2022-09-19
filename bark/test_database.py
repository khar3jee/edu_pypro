"""
unit testing for database with pytest
"""

from database import DatabaseManager

class TestDatabase:
    """
    must pass these test values
    CREATE TABLE IF NOT EXISTS testtable(test TEXT)
    id INTEGER PRIMARY KEY AUTOIINCREMENT,
    title TEXT NOT NULL,
    url TEXT NOT NULL,
    notes TEXT NOT NULL,
    date_added TEXT NOT NULL);
    """
    db = DatabaseManager('test_bookmark.db')

    def test_execute(self):
        self.db._execute('CREATE TABLE IF NOT EXISTS testtable(test TEXT)')
        