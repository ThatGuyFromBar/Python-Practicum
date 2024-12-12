def result_accumulator(func):
    queue = []

    def decorated(*args, method='accumulate', **kwargs):
        if method == 'accumulate':
            queue.append(func(*args, **kwargs))
        if method == 'drop':
            queue.append(func(*args, **kwargs))
            final = queue[:]
            queue.clear()
            return final
    return decorated
