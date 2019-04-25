
from datetime import datetime
import time










if __name__ == '__main__':
    now = datetime.now()
    time.sleep(10)
    now1 = datetime.now()
    str_now = now.strftime('%d.%m.%Y %H:%M:%S')
    str_now1 = now1.strftime('%d.%m.%Y %H:%M:%S')
    print(now > now1)
    print(str_now)
    print(str_now1)