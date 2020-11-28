from instapy import *
from var import *

#Лайкать и фолловить людей с определенным тегом

#Не тогай
session = InstaPy(username=inst_log, password=inst_pass)
session.login()

#Отписаться от юзеров которые не являются твоими подпищами
session.unfollow_users(amount=300, instapy_followed_enabled= True , instapy_followed_param = "nonfollowers",style="FIFO",unfollow_after=60 * 60 * 24 * 3, sleep_delay=10)