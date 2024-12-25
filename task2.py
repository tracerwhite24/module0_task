# 2nd program

def measuring(x, y):

    if x > 9.98:
        return True

    elif y != 1000.1:
        return True
    else:
        return False


result = measuring(9.99, 1000)
print(result)
