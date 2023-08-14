from unittest_framework import UnitTest
import time
ut = UnitTest()

@ut.register
def check_on_pass():
    time.sleep(3)
    return True

@ut.register
def check_on_None():
    time.sleep(3)
    return None

@ut.register_nofail
def check_on_exception():
    time.sleep(3)
    raise Exception

@ut.register_nofail
def check_on_false():
    time.sleep(3)
    return False

ut.run()
