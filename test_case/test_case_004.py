from nose.tools import ok_

def test_lean_1():
    print ("test_learn_1")
    ok_(4==3,msg="Error")


from nose.tools import eq_

def test_learn_2():
    eq_(5, 6, msg="Wrong")


from nose.tools import assert_in

def test_lean_3():
    assert_in("aaa",'bbb',msg="test  in failed")


from nose.tools import assert_in
from nose.tools import set_trace

def test_lean_4():
    set_trace()
    assert_in("aaa",'bbb',msg="test  in failed")

from nose.tools import timed
import time

@timed(1)
def test_lean_5():
    time.sleep(2)
    pass