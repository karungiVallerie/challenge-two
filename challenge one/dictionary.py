new_dict = {}


def vallerie(start,stop):
    for k in range(start,stop):
        vallerie = k*k
        new_dict[k] = vallerie

vallerie(1,15)

print(new_dict)
