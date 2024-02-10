from models import db, User, Post, Tag, PostTag
from app import app

# Create all tables
db.drop_all()
db.create_all()

User.query.delete()
Post.query.delete()
Tag.query.delete()
PostTag.query.delete()

# Add users and posts
u1 = User(first_name='User1', last_name='One', img_url=None)
u2 = User(first_name='User2', last_name='Two', img_url=None)
u3 = User(first_name='User3', last_name='Three', img_url=None)
u4 = User(first_name='User4', last_name='Four', img_url=None)

p1 = Post(title='Post1', content='Content1', user_id=1)
p2 = Post(title='Post2', content='Content2', user_id=1)
p3 = Post(title='Post3', content='Content3', user_id=1)
p4 = Post(title='Post4', content='Content4', user_id=2)
p5 = Post(title='Post5', content='Content5', user_id=2)
p6 = Post(title='Post6', content='Content6', user_id=3)
p7 = Post(title='Post7', content='Content7', user_id=3)

db.session.add_all([u1, u2, u3, u4, p1, p2, p3, p4, p5, p6, p7])
db.session.commit()

# Add tags

t1 = Tag(name='Art')
t2 = Tag(name='Fun')
t3 = Tag(name='Tech')
t4 = Tag(name='Fitness')
t5 = Tag(name='Food')
t6 = Tag(name='Travel')
t7 = Tag(name='Fashion')
t8 = Tag(name='Nature')

db.session.add_all([t1, t2, t3, t4, t5, t6, t7, t8])
db.session.commit()

# Add posttags

pt1 = PostTag(post_id=1, tag_id=1)
pt2 = PostTag(post_id=1, tag_id=3)
pt3 = PostTag(post_id=2, tag_id=1)
pt4 = PostTag(post_id=3, tag_id=1)
pt5 = PostTag(post_id=3, tag_id=3)
pt6 = PostTag(post_id=3, tag_id=4)
pt7 = PostTag(post_id=4, tag_id=5)
pt8 = PostTag(post_id=5, tag_id=3)
pt9 = PostTag(post_id=5, tag_id=4)
pt10 = PostTag(post_id=6, tag_id=2)
pt11 = PostTag(post_id=7, tag_id=1)
pt12 = PostTag(post_id=7, tag_id=4)
pt13 = PostTag(post_id=7, tag_id=5)
pt14 = PostTag(post_id=7, tag_id=7)

db.session.add_all([pt1, pt2, pt3, pt4, pt5, pt6, pt7, pt8, pt9, pt10, pt11, pt12, pt13, pt14])
db.session.commit()

