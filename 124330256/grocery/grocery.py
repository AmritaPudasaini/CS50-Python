d = {}

while True:
    try:
        key = input().strip().upper()
        if key not in d:
            d[key]=1;
        else:
            d[key]=d[key]+1

    except EOFError:
        order_item = dict(sorted(list(d.items())))
        for item in order_item:
            print(order_item[item], item, sep=" ")
        break
    except KeyError:
        pass

