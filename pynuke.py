import os
import time
from cryptography.fernet import Fernet
import random


banner = """\u001b[38;5;240m
                              ____                      
                      __,-~~/~    `---.                 
                    _/_,---(      ,    )                
                __ /        <    /   )  \___            
               ====------------------===;;;==           
                   \/  ~"~"~"~"~"~\~"~)~",1/            
                   (_ (   \  (     >    \)              
                    \_( _ <         >_>'                
\u001b[38;5;202m                       ~ `-i' ::>|--"                   
                           I;|.|.|                      
                          <|i::|i|>                     
\u001b[38;5;220m                           |[::|.|                      
                            ||: |                       \u001b[0m
\u001b[41m───────────────────────────PY-NUKE───────────────────────────\u001b[0m

"""







def main():
  print(banner)
  time.sleep(1)
  firstchoice = input("""
V1.0
\u001b[0m\u001b[7m[1]\u001b[0m Nuke a file
\u001b[0m\u001b[7m[2]\u001b[0m Nuke a folder
\u001b[1m[CNTRL + C TO EXIT]\u001b[0m

-¬=> """)


main()
