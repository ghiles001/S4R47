from googlesearch import search

query = str(input("Search for : "))
a = int(input("how many times: "))
mod = str(input("Mode of search (verbos/silent/no): "))

if mod == "verbos" or mod == "VERBOS" or mod == "Verbos":

    for i in range(a):

        for t in search(query, tld = 'com', lang = 'en', num = 10, start = 0, stop = None, pause = 2.0 ):
            print(t)

elif mod == "silent" or mod == "SILENT" or mod == "Silent":

    gen = input("Genrate file as: ")
    f = open(gen, "w+")

    def w_file(t):
        global  f
        f.write(t+"%d\r\n")
        res = "Results of Serch saved as "+ gen


    for i in range(a):
        k = 0
        for t in search(query, tld = 'com', lang = 'en', num = 10, start = 0, stop = None, pause = 2.0 ):
            k += 1
            w_file(t)
        print("{} Result".format(k))
elif mod == "no" or mod == "No" or mod == "NO":

    for i in range(a):
        for t in search(query, tld = 'com', lang = 'en', num = 10, start = 0, stop = None, pause = 2.0 ):
            k += 1
        print("{} Result".format(k))


else:
    print("EROR in mode of search !!!")
