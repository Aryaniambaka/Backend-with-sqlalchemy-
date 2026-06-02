from typing import List
from app import schema
from fastapi.exceptions import ResponseValidationError
from pydantic import ValidationError
import pytest
from fastapi.exceptions import ResponseValidationError
def test_posts(authorized_client,test_post):
    res=authorized_client.get("/post/mypost")
    assert len(res.json())==len(test_post)
    post=res.json()
    def validate(post):
        return schema.PostResponse(**post)
    post_map=map(validate,res.json())
    post_list=list(post_map)
    assert post_list[0].id == test_post[0].id
    assert res.status_code == 200
def test_unauthorized_user(client,test_post):
    res=client.get("/post/mypost")
    assert res.status_code == 401
def test_notoken(client,test_post):
    res=client.get(f"/post/lol/{test_post[0].id}")
    assert res.status_code == 200
def test_notoken_noid(client,test_post):
    with pytest.raises(ResponseValidationError) as exc_info:
        client.get(f"/post/lol/{600}")
    assert "Input should be a valid dictionary or object" in str(exc_info.value)
def test_notoken_noid_method2(client, test_post):
    try:
        res = client.get(f"/post/lol/{600}")
        schema.PostResponse(**res.json())
        pytest.fail("Response fulfilled the schema when it should have failed validation.")
    except (ValidationError, TypeError, ResponseValidationError):
        pass
@pytest.mark.parametrize("title, context, published", [
    ("awesome new title", "awesome new content", True),
    ("favorite pizza", "i love pepperoni", False),
    ("tallest skyscrapers", "wahoo", True),
])
def test_createpost(authorized_client, title, context, published):
    res = authorized_client.post("/post/new", json={
        "title": title,
        "context": context,
        "published": published
    })
    
    assert res.status_code == 200
    
    data = res.json()
    print(data)
    assert data["title"] == title
    assert data["context"] == context
    assert data["published"] == published
# @pytest.mark.parametrize("title, content, published", [
#     ("awesome new title", "awesome new content", True),
#     ("favorite pizza", "i love pepperoni", False),
#     ("tallest skyscrapers", "wahoo", True),
# ])
# def test_create_post(authorized_client, test_user, test_posts, title, content, published):
#     res = authorized_client.post(
#         "/posts/", json={"title": title, "content": content, "published": published})

#     created_post = schema.PostResponse(**res.json())
#     assert res.status_code == 201
#     assert created_post.title == title
#     assert created_post.context == content
    
#     assert created_post.owner_id == test_user['id']


# def test_create_post_default_published_true(authorized_client, test_user, test_posts):
#     res = authorized_client.post(
#         "/posts/", json={"title": "arbitrary title", "content": "aasdfjasdf"})

#     created_post = schema.PostResponse(**res.json())
#     assert res.status_code == 201
#     assert created_post.title == "arbitrary title"
#     assert created_post.context == "aasdfjasdf"
    
#     assert created_post.owner_id == test_user['id']


# def test_unauthorized_user_create_post(client, test_user, test_posts):
#     res = client.post(
#         "/posts/", json={"title": "arbitrary title", "content": "aasdfjasdf"})
#     assert res.status_code == 401


# def test_unauthorized_user_delete_Post(client, test_user, test_posts):
#     res = client.delete(
#         f"/posts/{test_posts[0].id}")
#     assert res.status_code == 401


# def test_delete_post_success(authorized_client, test_user, test_posts):
#     res = authorized_client.delete(
#         f"/posts/{test_posts[0].id}")

#     assert res.status_code == 204


# def test_delete_post_non_exist(authorized_client, test_user, test_posts):
#     res = authorized_client.delete(
#         f"/posts/8000000")

#     assert res.status_code == 404


# def test_delete_other_user_post(authorized_client, test_user, test_posts):
#     res = authorized_client.delete(
#         f"/posts/{test_posts[3].id}")
#     assert res.status_code == 403


# def test_update_post(authorized_client, test_user, test_posts):
#     data = {
#         "title": "updated title",
#         "content": "updatd content",
#         "id": test_posts[0].id

#     }
#     res = authorized_client.put(f"/posts/{test_posts[0].id}", json=data)
#     updated_post = schema.PostResponse(**res.json())
#     assert res.status_code == 200
#     assert updated_post.title == data['title']
#     assert updated_post.context == data['content']


# def test_update_other_user_post(authorized_client, test_user, test_user2, test_posts):
#     data = {
#         "title": "updated title",
#         "content": "updatd content",
#         "id": test_posts[3].id

#     }
#     res = authorized_client.put(f"/posts/{test_posts[3].id}", json=data)
#     assert res.status_code == 403


# def test_unauthorized_user_update_post(client, test_user, test_posts):
#     res = client.put(
#         f"/posts/{test_posts[0].id}")
#     assert res.status_code == 401


# def test_update_post_non_exist(authorized_client, test_user, test_posts):
#     data = {
#         "title": "updated title",
#         "content": "updatd content",
#         "id": test_posts[3].id

#     }
#     res = authorized_client.put(
#         f"/posts/8000000", json=data)

#     assert res.status_code == 404

    