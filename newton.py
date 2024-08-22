def d(x, f):
    """
    caculate the derivative

    Parameters:
    x: The value of x
    f: The function

    Returns:
    the derivative of f at x
    """
    e = 0.01
    return (f(x + e) - f(x)) / e


def dd(x, f):
    """
    caculate the second derivative
    """
    e = 0.01
    return (d(x + e, f) - d(x, f)) / e


def Newton(x0, f):
    """
    caculate the second derivative
    """
    x = [x0]  ##list，可更新
    i = 0
    while True:
        df = d(x[i], f)
        ddf = dd(x[i], f)  ##储存值，每次循环中只计算df、ddf，避免重复计算
        x_new = x[i] - df / ddf
        x.append(x_new)
        if abs(df / ddf) < 0.001:  ##绝对值 abs
            break

        i += 1  #
    return x
