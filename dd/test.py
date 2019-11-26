def is_valid_IP(strng):
    
    parts = strng.split(".")
    if len(parts) != 4:
        print("FalsE")
        return False
    
    d = part
    s.index("0")
        print("sa partsy > ",d)

    for item in parts:
        if not 10 <= int(item) <= 255:
            print("FALSE")
            return False
    print("True")
    return True
is_valid_IP("033.05.56.45")
