n=int(input("Choose a number between 1 and 7:"))
match n:
    case 1:
        print("Today is Sunday.")
    case 2:
        print("Today is Monday.")
    case 3:
        print("Today is Tuesday.")
    case 4:
        print("Today is Wednesday.")
    case 5:
        print("Today is Thrusday.")
    case 6:
        print("Today is Friday.")
    case 7:
        print("Today is Saturday.")
    case _:
        print("Invalid Choice.")
        