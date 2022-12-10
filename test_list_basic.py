import pytest
from list_basic import HEAD,TAIL,PAIR,PREPEND,APPEND,NIL


def test_list():
    list0 = PAIR(True)(NIL)
    list1 = PREPEND(list0)(1)
    list2 = PREPEND(list1)(2)
    list3 = PREPEND(list2)(3)
    list4 = APPEND(list3)(4)
    list5 = APPEND(list4)(5)
    list6 = PREPEND(list5)(6)
    
    print("@@ TEST @@")
    testlist = list6
    res = [6,3,2,1,4,5]
    for i in range(6):
        assert HEAD(testlist) == res[i]
        testlist = TAIL(testlist)
