import mymodule


print("top level in two.py ")

mymodule.func()

if __name__ =="__main__" :
    print("two.py is being run directly")
else:
    print(" two.py has been imported")