TRUE = lambda a: lambda b: a
FALSE = lambda a: lambda b: b

PAIR = lambda a: lambda b: lambda c: c(a)(b)
FIRST  = lambda p: p(TRUE)
SECOND  = lambda p: p(FALSE)

NIL  = PAIR(TRUE)(TRUE)
IS_EMPTY = lambda xs: FIRST(xs)
HEAD  = lambda xs: FIRST(SECOND(xs))
TAIL  = lambda xs: SECOND(SECOND(xs))

# == Start ==
# APPEND  <LIST> ELEM = <LIST, ELEM>
# PREPEND <LIST> ELEM = <ELEM, LIST>
# LIST :: PAIR(EMPTY)(PAIR(HEAD)(TAIL))

# Armor: 
# FIRST PAIR, SECOND PAIR
# list2 = APPEND list elem

PREPEND = lambda li: lambda el: PAIR(False)(PAIR(el)(li))

# Define: APPENDER -- PAIR
# APPENEDLIST :: PAIR(EMPTY)(APPENDER(HEAD)(TAIL))

APPEND = lambda li: lambda el: PAIR(False)(APPENDER(el)(li))



if __name__=="__main__":
    list0 = PAIR(True)(NIL)
    list1 = PREPEND(list0)(1)
    list2 = APPEND(list1)(0)

    print(HEAD(list2))
    print(HEAD(TAIL(list2)))
    
