for hora in range(0, 24):
    for minutos in range(0, 60, 15):
        if hora == 0:
            print("12:", minutos, "am")
        elif hora < 12:
            print(hora, ":",minutos ,"am")
        elif hora == 12:
            print("12:",minutos,"pm")
        else:
            print((hora-12),":",minutos, "pm")