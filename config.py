import requests
from faker import Faker
faker = Faker()

number_of_users = 2
user_data = []
for i in range(number_of_users):
    email = faker.email()
    password = faker.password()
    data = {
        "email": email,
        "password": password,
        "password_repeat": password
    }

    user_data.append(data)

number_of_posts = 2
number_of_likes = 2
post_data_list = []
likes_list = []
for b in range(number_of_posts):
    for k in range(number_of_likes):
        title = faker.job()
        description = faker.text()
        total_likes = faker.random_int()
        post_data = {
        'title': title,
        'description': description,
        'likes': total_likes,
        }
        like_data = {
        'likes': total_likes,
        }
        likes_list.append(like_data)
        post_data_list.append(post_data)

"""number_of_likes = 2
likes_list = []
for i in range(number_of_likes):
    likes = faker.random_int()
    like_data = {
        'likes': likes,
    }
    likes_list.append(like_data)"""

user_create_url = "http://127.0.0.1:8000/api/users/users/"
token_url = "http://127.0.0.1:8000/api/token/"
post_create_url = "http://127.0.0.1:8000/api/posts/posts/"
likes_create_url = "http://127.0.0.1:8000/api/posts/likes/"


def get_user_token(user_datas):
    user_token_data = []
    for item in user_datas:
        requests.post(url=user_create_url, data=item)
        a = requests.post(url=token_url, data=item)
        token_data = a.json()
        user_token_data.append(token_data['access'])
    return user_token_data


def create_user_post(user_token, posts_data, likes):
    result_data = []
    for token, post, likes in zip(user_token, posts_data, likes):
        responce = requests.post(url=post_create_url, data=post, headers={'Authorization': f"Bearer {token}"})
        responce = requests.post(url=likes_create_url, data=post)
        result_dict = {'data': responce.text, 'status_code': responce.status_code}
        result_data.append(result_dict)
    return result_data


def main():
    user_tokens = get_user_token(user_data)
    user_create_posts = create_user_post(user_tokens, post_data_list, likes_list)
    print(user_create_posts)


main()