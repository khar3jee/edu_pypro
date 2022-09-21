"""
commands for Bark app

class per command?
"""
import sys
from datetime import datetime
from database import DatabaseManager

db = DatabaseManager('test_bookmark.db')

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
        input_data['date_added'] = datetime.utcnow().isoformat()
        db.add('bookmarks', input_data)
        return 'Bookmark Added'

class DeleteBookmarkCommand:
    """deletes selected bookmarks from database"""
    def execute(self, data):
        print('DelBk exec')
        db.delete('bookmarks', {'id': data})
        return 'Bookmark deleted'

class ListBookmarkCommand:
    """list bookmarks from database"""
    def __init__(self, order_by='date_added'):
        self.order_by = order_by

    def execute(self):
        print('ListBk exec')
        return db.select('bookmarks', order_by=self.order_by).fetchall()

class UpdateBookmarkCommand:
    """updates a bookmark"""
    def execute(self):
        pass

class QuitCommand:
    def execute(self):
        sys.exit()

#if __name__ == '__main__':
#    db._execute('CREATE TABLE IF NOT EXISTS testtable(test TEXT)')
#    ListBookmarkCommand().execute()
