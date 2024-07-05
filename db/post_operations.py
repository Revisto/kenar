from db.models import db, Post

def create_new_post(post_id, task_id, new_sizes={}):
    new_post = Post(post_id=post_id, task_id=task_id, new_sizes=new_sizes)
    db.session.add(new_post)
    db.session.commit()

def get_post_by_id(post_id):
    return Post.query.filter_by(post_id=post_id).first()

def update_post_status(post_id, new_status):
    post = get_post_by_id(post_id)
    if post:
        post.model_status = new_status
        db.session.commit()

def delete_post(post_id):
    post = get_post_by_id(post_id)
    if post:
        db.session.delete(post)
        db.session.commit()

def get_all_posts():
    return Post.query.all()