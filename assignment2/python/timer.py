import time


def count(name, f, args):
    begin = time.clock()
    output = f(*args)
    end = time.clock()

    print name + ": %s seconds." % (end - begin)
    return output