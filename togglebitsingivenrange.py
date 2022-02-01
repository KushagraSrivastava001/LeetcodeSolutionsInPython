 # calculating a number
    # 'num' having 'r'
    # number of bits and
    # bits in the range l
    # to r are the only set bits
    num = ((1 << r) - 1) ^ ((1 << (l - 1)) - 1)
  
    # toggle bits in the
    # range l to r in 'n'
    # Besides this, we can calculate num as: num=(1<<r)-l .
 
    # and return the number
    return (n ^ num)
