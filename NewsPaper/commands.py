from django.contrib.auth.models import User

user1=User.objects.create(username="Ivan Ivanov", last_name="Ivan", first_name="Ivanov")
user2=User.objects.create(username="Petr Petrov", last_name="Petr", first_name="Petrov")

from news.models import Category

category1=Category.objects.create(name="Sport")
category2=Category.objects.create(name="Politico")
category3=Category.objects.create(name="Bissnes")
category4=Category.objects.create(name="Style")

from news.models import Post

article1=Post.objects.create(Article="Победа Майка Тайсона")
article2=Post.objects.create(Article="Смерть Коби Брайнта")

news1=Post.objects.create(News="Изобретен новый стероид")