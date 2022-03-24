try:
    # a=10
    # b=0
    # c=a/b
    # print(c)
    age=19
    if age<=18:
       raise ValueError("age for voing is minimum 18+")
    else:
       print("eligible for vote")
except ZeroDivisionError as e:
    print("division not possible by zero"+str(e))
except ValueError as e:
    print(str(e))
except:
    print("Exception occured")

else:
    print("executed successfully")
finally:
    print("harman ltd")