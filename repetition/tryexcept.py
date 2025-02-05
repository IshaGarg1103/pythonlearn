while True:
    try:
        value=eval(input("Enter an integer :"))
        print(value)
        if isinstance(value,int):
            print(f"valid input! result is :{value}")
            break
    except NameError:
        print("No string as input. Try again!")
    except SyntaxError:
        print("invalid Expression. Try again!")
    except ZeroDivisionError as err:
        print(f"{err} Try again!")