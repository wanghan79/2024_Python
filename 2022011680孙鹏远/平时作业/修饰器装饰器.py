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