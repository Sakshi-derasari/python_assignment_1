# post.py

from data import posts
import datetime


# ---------------- CREATE POST ----------------
def create_post(user):
    print("\n--- CREATE POST ---")

    title = input("Enter title: ").strip()
    description = input("Enter description: ").strip()

    # validation
    if title == "" or description == "":
        print("Error: Fields cannot be empty!")
        return

    # generate date automatically
    date = datetime.datetime.now().strftime("%Y-%m-%d")

    # create dictionary
    post = {
        "author": user["username"],
        "title": title,
        "description": description,
        "date": date
    }

    posts.append(post)

    print("Post created successfully!")


# ---------------- VIEW ALL POSTS ----------------
def view_posts():
    print("\n--- ALL POSTS ---")

    if not posts:
        print("No posts available.")
        return

    # loop through posts
    for index, post in enumerate(posts, start=1):
        print(f"\nPost Number: {index}")
        print("Author:", post["author"])
        print("Title:", post["title"])
        print("Date:", post["date"])
        print("Description:", post["description"])


# ---------------- SEARCH POSTS ----------------
def search_posts():
    print("\n--- SEARCH POSTS ---")

    username = input("Enter username to search: ").strip()

    if username == "":
        print("Error: Username cannot be empty!")
        return

    found = False

    # loop through posts
    for post in posts:
        if post["author"] == username:
            print("\n--- FOUND POST ---")
            print("Title:", post["title"])
            print("Date:", post["date"])
            print("Description:", post["description"])
            found = True

    if not found:
        print("No posts found for this user.")


# ---------------- UPDATE POST ----------------
def update_post(user):
    print("\n--- UPDATE POST ---")

    if not posts:
        print("No posts available.")
        return

    view_posts()

    try:
        choice = int(input("Enter post number to update: ")) - 1
    except ValueError:
        print("Invalid input! Enter a number.")
        return

    # check valid index
    if choice < 0 or choice >= len(posts):
        print("Invalid post number!")
        return

    # check ownership
    if posts[choice]["author"] != user["username"]:
        print("Error: You can only update your own posts!")
        return

    new_title = input("Enter new title: ").strip()
    new_description = input("Enter new description: ").strip()

    if new_title == "" or new_description == "":
        print("Error: Fields cannot be empty!")
        return

    posts[choice]["title"] = new_title
    posts[choice]["description"] = new_description

    print("Post updated successfully!")


# ---------------- DELETE POST ----------------
def delete_post(user):
    print("\n--- DELETE POST ---")

    if not posts:
        print("No posts available.")
        return

    view_posts()

    try:
        choice = int(input("Enter post number to delete: ")) - 1
    except ValueError:
        print("Invalid input! Enter a number.")
        return

    # check valid index
    if choice < 0 or choice >= len(posts):
        print("Invalid post number!")
        return

    # check ownership
    if posts[choice]["author"] != user["username"]:
        print("Error: You can only delete your own posts!")
        return

    posts.pop(choice)

    print("Post deleted successfully!")