def make_linear(lst):
    answer = []
    for item in lst:
        if isinstance(item, list):
            answer.extend(make_linear(item))
        else:
            answer.append(item)
    return answer
