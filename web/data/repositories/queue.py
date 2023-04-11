from data.models    import Queue
from data           import db

from sqlalchemy     import extract, or_, and_, func
from datetime       import datetime

class QueuesRepo:
    
    # ==================================================================================
    # QUEUES
    
    def readQueue():
        return Queue.query.filter(func.date(Queue.created_at) == datetime.now().date()).order_by(Queue.created_at.asc()).all()
    
    def insertQueue(request):
    
        data = Queue(
            priority = request['priority'],
        )
        db.session.add(data)
        db.session.commit()

        return True
