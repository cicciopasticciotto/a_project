import time
import six
import maggma
import abipy
import abipy.abilab 


def a_sleep_function():
    print("!!! ", abipy.__file__)
    abipy.abilab.TaskManager.from_user_config()
    time.sleep(1)
