try:
    x=4
    i=int(input("Enter a number: "))
    frac=1
    while i <= x:
        frac *= i
        i += 1
        if frac ==10:
            break
        elif frac < 10:
            print(f" {frac} < 10")
    else:    
        print(f" {frac}")
except ValueError:
    print("value error occured because you did not enter a correct value")
