from googlesearch import search
query = input("Search for (site.com): ")
a = int(input("Nbr of searches(1000): "))
for i in range(a):
    for t in search(query, tld = 'com', lang = 'en', num = 10, start = 0, stop = None, pause = 2.0 ):
        print(t)
