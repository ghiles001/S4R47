from googlesearch import search
from colorama import Fore, init, Style
import sys

init(autoreset=True)
query = ""
for arg in sys.argv[1:]:
    query = query + str(arg) + " "
print(Fore.RED+Style.BRIGHT+"""
                                                                          
                                                                          
   SSSSSSSSSSSSSSS       444444444  RRRRRRRRRRRRRRRRR          444444444  
 SS:::::::::::::::S     4::::::::4  R::::::::::::::::R        4::::::::4  
S:::::SSSSSS::::::S    4:::::::::4  R::::::RRRRRR:::::R      4:::::::::4  
S:::::S     SSSSSSS   4::::44::::4  RR:::::R     R:::::R    4::::44::::4  
S:::::S              4::::4 4::::4    R::::R     R:::::R   4::::4 4::::4  
S:::::S             4::::4  4::::4    R::::R     R:::::R  4::::4  4::::4  
 S::::SSSS         4::::4   4::::4    R::::RRRRRR:::::R  4::::4   4::::4  
  SS::::::SSSSS   4::::444444::::444  R:::::::::::::RR  4::::444444::::444
    SSS::::::::SS 4::::::::::::::::4  R::::RRRRRR:::::R 4::::::::::::::::4
       SSSSSS::::S4444444444:::::444  R::::R     R:::::R4444444444:::::444
            S:::::S         4::::4    R::::R     R:::::R          4::::4  
            S:::::S         4::::4    R::::R     R:::::R          4::::4  
SSSSSSS     S:::::S         4::::4  RR:::::R     R:::::R          4::::4  
S::::::SSSSSS:::::S       44::::::44R::::::R     R:::::R        44::::::44
S:::::::::::::::SS        4::::::::4R::::::R     R:::::R        4::::::::4
 SSSSSSSSSSSSSSS          4444444444RRRRRRRR     RRRRRRR        4444444444
                                                                By Mazy_lan""")
def main(strr):
    if len(sys.argv) > 1:
        for result in search(strr, tld="com", lang="en", num=20, start=0, stop=None, pause=2.0):
            print(Fore.GREEN+Style.BRIGHT+"[*]>> "+Fore.RESET+Style.NORMAL+result)
    if len(sys.argv) == 1:
        print("""
Usage : {} FirstName LastName
""".format(sys.argv[0]))


main(query)
