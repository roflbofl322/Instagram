from instapy import *
from var import *

#Лайкать и фолловить людей с определенным тегом

#Не тогай
session = InstaPy(username=inst_log, password=inst_pass)
session.login()

#Взаимодействовать только с пользователями которые подходят по количество подписок/фоловеров
session.set_relationship_bounds(enabled=True,potency_ratio=None,delimit_by_numbers=True,max_followers=100,max_following=100,min_followers=40,min_following=5)

#Взаимодействовать только с пользователями которые подходят по количеству постов
session.set_relationship_bounds(min_posts=10, max_posts=None)


#Процент того как часто будут ставится лайки.
session.set_do_like(True, percentage=70 )

#Фоловится ли
session.set_do_follow(enabled=True, percentage=100 , times=1)

#Лайкать юзеров по оппределенному хештегу
session.like_by_tags(['octfestfarely'], amount= 10 , skip_top_posts= False , randomize= True)

