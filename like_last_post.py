from instapy import *
from var import *

#Поставить лайк последним записям 

#Не тогай
session = InstaPy(username=inst_log, password=inst_pass)
session.login()

#Игнор лист
session.set_ignore_users(['flikkkker'])

#Процент лайкания
session.set_do_like(True, percentage=100)

#Какое количество постов лайкать, если ставить 1 лайкает только самый последний
session.set_user_interact(amount=1)


#Лайкать последние записи своих Подписок, количество , рандом
session.interact_user_following(['roflbofl322'],amount= 3 , randomize= True)

#Лайкать последние записи ПОДПИСЧИКОВ, количество, рандом
session.interact_user_followers(['roflbofl322'],amount = 3, randomize = True)
