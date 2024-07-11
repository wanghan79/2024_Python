import logging

# def use_logging(func):
#     def wrapper():
#         logging.warn ("%s is running" % func.__name__)
#         return func()
#     return wrapper

# def foo():
#     print("im foo")

# foo = use_logging(foo)   # foo为wrapper函数指针
# foo()



# def use_logging(func):
#     def wrapper():
#         logging.warn ("%s is running" % func.__name__)
#         return func()
#     return wrapper

#不带参数的修饰器
# @use_logging
# def foo():
#     print("im foo")
# 等价于
# # foo = use_logging(foo)

# foo()



# def use_logging(level):
#     def decorator(func):
#         def wrapper(*args,**kwargs):
#             if level =="warn":
#                 logging.warn("%s is running" % func.__name__)
#             elif level =="info":
#                 logging.info("%s is running running" % func.__name__)
#             return func(*args)
#         return wrapper
#     return decorator

#带参数的修饰器
# @use_logging(level="warn")
# def foo(name='foo'):
#     print("im %s" % name)
# 等价于
# #foo=use_logging(warn)(foo)
# 即
# #decorator=use_logging(warn)
# #foo=decorator(foo)

# foo()




def foo():
    print("%s is running"% foo.__name__)

def bar(func):
    func()

bar(foo)



def addLogging(func):
    logging.warning("%s is running"%func.__name__)
    func()
addLogging(foo)



def addLogging(func):
    def warpper():
        logging.warning("%s is run"%func.__name__)
        return func()
    return warpper
foo = addLogging(foo)
foo()


# 问
# from functools import wraps
# 在装饰器函数中的的wrapper函数定义前加@wraps(func)有什么用，删掉后一样不报错的运行

# 答
# 使用 @wraps(func) 装饰器来装饰内层函数（通常称为 wrapper）的目的主要是为了保留原始函数的元信息。这个装饰器来源于 Python 的 functools 模块，其主要作用包括：
# 1.保留原函数的名称和文档字符串：当你使用装饰器后，通常内层函数会替代外层函数。如果不使用 @wraps(func)，那么被装饰的函数的 __name__ 和 __doc__ 属性会变成内层函数（wrapper）的对应属性，这可能会导致一些问题，比如调试时无法得知原始函数的名称。
# 2.保持原函数的其它属性：包括注解（annotations）和任何通过赋值添加的自定义属性。

# 这里有一个示例来展示使用和不使用 @wraps 的区别：
# from functools import wraps

# def my_decorator(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         print("Something is happening before the function is called.")
#         return func(*args, **kwargs)
#     return wrapper

# @my_decorator
# def say_hello():
#     """This is the say_hello function."""
#     print("Hello!")

# print(say_hello.__name__)  # 输出 'say_hello'
# print(say_hello.__doc__)   # 输出 'This is the say_hello function.'

# def my_decorator_without_wraps(func):
#     def wrapper(*args, **kwargs):
#         print("Something is happening before the function is called.")
#         return func(*args, **kwargs)
#     return wrapper

# @my_decorator_without_wraps
# def say_bye():
#     """This is the say_bye function."""
#     print("Bye!")

# print(say_bye.__name__)  # 输出 'wrapper'
# print(say_bye.__doc__)   # 输出 None

# 在这个示例中，使用 @wraps(func) 的 say_hello 函数保留了其原始的名称和文档字符串，而没有使用 @wraps 的 say_bye 函数则丢失了这些信息，其 __name__ 属性变成了 wrapper，文档字符串变成了 None。
# 因此，虽然在很多情况下不使用 @wraps 并不会影响代码的功能性，但它是保持代码可维护性和透明度的好习惯，尤其是在创建库或大型应用时。