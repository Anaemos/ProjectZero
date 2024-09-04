def author_interests():
    print("I like football, f1, tennis and coding")
    details = input("To know my favourites in each, write fav_'sportname': ")
    if details == "fav_football":
        print("My favourite footballer is Luka Modric")
    elif details == "fav_tennis":
        print("My favourite tennis player is Rafael Nadal")
    elif details == "fav_f1":
        print("My favourite F1 driver is Fernando Alonso")
author_interests()