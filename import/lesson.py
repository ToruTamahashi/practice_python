"""
import lesson_package.utils
r = lesson_package.utils.say_twice('hello')
"""

from lesson_package import utils
# ./lesson_package/talkのhuman.pyをインポート
from lesson_package.talk import human
r = utils.say_twice('hello')
print(r)

print(human.sing())