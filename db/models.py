from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.String(50), unique=True, nullable=False)
    task_id = db.Column(db.String(100))  # task id from Meshy
    model_status = db.Column(db.String(10), default='pending')  # pending, processing, completed
    new_sizes = db.Column(db.String(100), default='{}')

    def __repr__(self):
        return f'<Post {self.post_id}> <Task {self.task_id}> <Status {self.model_status}> <Sizes {self.new_sizes}>'