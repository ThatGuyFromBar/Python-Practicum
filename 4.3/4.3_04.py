def answer(func):
    def code(*args, **kwargs):
        return f'Результат функции: {func(*args, **kwargs)}'
    return code
