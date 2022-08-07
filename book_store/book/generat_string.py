import string
import random
def g_s():

    # initializing size of string
    N = 7

    # using random.choices()
    # generating random strings
    res = ''.join(random.choices(string.ascii_uppercase +
                                 string.digits, k=N))

    # print result
    return str(res)
