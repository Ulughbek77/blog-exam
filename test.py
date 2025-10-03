from database import SessionLocal
import crud

db = SessionLocal()

# Test: user qo‘shish
user = crud.create_user(db, "test_user", "test@example.com")
print("Created User:", user.username)

# Test: post qo‘shish
post = crud.create_post(db, user.id, "My First Post", "This is content")
print("Created Post:", post.title)

# Test: comment qo‘shish
comment = crud.create_comment(db, user.id, post.id, "Zor post ekan!")
print("Created Comment:", comment.text)

# Test: user postlari
posts = crud.get_user_posts(db, user.id)
print("User posts:", [p.title for p in posts])

# Test: comment soni
count = crud.get_post_comment_count(db, post.id)
print("Post comment count:", count)

# Test: oxirgi postlar
latest = crud.get_latest_posts(db, 3)
print("Latest posts:", [p.title for p in latest])

# Test: title bo‘yicha qidirish
search = crud.search_posts_by_title(db, "First")
print("Search result:", [p.title for p in search])

# Test: pagination
page1 = crud.paginate_posts(db, page=1, per_page=2)
print("Page 1 posts:", [p.title for p in page1])
