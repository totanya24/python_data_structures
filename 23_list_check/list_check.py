def list_check(lst):
    """Are all items in lst a list?

        #>>> list_check([[1], [2, 3]])
        True

        #>>> list_check([[1], "nope"])
        False
    """
    for item in lst:
        #print("s",item)
        if not isinstance(item, list):
            print("False")
        else:
            print("True")

    return ""


print(list_check([[1], [2, 3]]))
print(list_check([[1], "nope"]))
