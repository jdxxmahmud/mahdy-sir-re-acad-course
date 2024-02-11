def get_val_from_series(val: int):

    res = 0

    if val < 0:
        while val < 0:
            print("Please enter a value greater than 0!")
            val = int(input())
    else:
        for i in range(val + 1):
        # print(i, pow(i, 2)/5)
            res  += pow(i, 2)/5
    
    return round(res, 2)


if __name__ == "__main__":
    val = int(input("Input Number: "))
    print(get_val_from_series(val))