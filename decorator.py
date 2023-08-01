def new_decorator(func):

    def wrap_func():
        print("some code before executing func")

        func()

        print("code here! func()")

    return wrap_func

@new_decorator
def func_needs_decorator():
    print("please decorate me!!")


func_needs_decorator()