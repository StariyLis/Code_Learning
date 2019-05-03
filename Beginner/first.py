
from datetime import datetime
import time
from git import Repo









if __name__ == '__main__':
    repo = Repo('C:/Users\Stari\PycharmProjects\Learning_Code')
    s = repo.config_reader()
    print(list(s))
    now = datetime.now()
    time.sleep(1)
    now1 = datetime.now()
    str_now = now.strftime('%d.%m.%Y %H:%M:%S')
    str_now1 = now1.strftime('%d.%m.%Y %H:%M:%S')
    print(now < now1)
    print(str_now)
    print(str_now1)