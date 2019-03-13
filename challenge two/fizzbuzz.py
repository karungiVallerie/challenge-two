#list1 = [int(x) for x in input("enter your 1st list of numbers with spaces: ").split()]
#list2 = [ int(x) for x in input("enter your 2nd list of numbers wit spaces: ").split()]
def fizz_buzz(list1, list2):
    total_length = len(list1) + len(list2)
    if total_length% 3==0:
        print("fizz")
        return "fizz"
    elif total_length % 5==0:
        print("buzz")
        return"buzz"
    else:
        print(total_length)
        return total_length