import time
import six
import maggma
import abipy
import abipy.abilab 


def a_sleep_function():
    abipy.abilab.TaskManager.from_user_config()
    time.sleep(1)
