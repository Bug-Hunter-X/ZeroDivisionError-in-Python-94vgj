def my_function(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return 0

result = my_function(10, 0) #result will be 0
result2 = my_function(10,2) #result2 will be 5