import os
import time
import hashlib
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




def clear():
  print("\n" * 300)

def animation():
  time.sleep(0.5)
  clear()
  print("""
                       
                   
                     
                   
                  
                 
\u001b[38;5;70m                   []\u001b[0m     
\u001b[38;5;70m                   ||                      
                   \/







\u001b[0m
""")
  time.sleep(0.5)
  clear()
  print("""
                                 
                          
                      
                        
                             
                      
                           
\u001b[38;5;70m                   
                   []     
                   ||                      
                   \/


\u001b[0m


""")
  time.sleep(0.5)
  clear()
  print("""
                                   
                                   
                             
                               
                                 
                             
                             
                   
                   
\u001b[38;5;70m                   
                   
                   []     
                   ||                      
                   \/

\u001b[0m
""")
  time.sleep(0.5)
  clear()
  print("""
                                              
                                       
                                   
                                   
                                      
                                     
                               
                   
                   
                   
                   
                   
\u001b[38;5;70m                                      
                   []     
                   ||                      
                   \/
\u001b[0m
""")
  time.sleep(0.5)
  clear()
  print("""
                                        
                              
                                
                                
                                  
                                      
                                        
                   
                   
                   
                   
\u001b[38;5;220m                
                       
                  ^  ^  
             . ' ,    ,' .
                  \\// \u001b[0m
""")
  time.sleep(0.1)
  clear()
  print("""
                                        
                              
                                
                                
                                  
                                      
                                        
                   
                   
                   
\u001b[38;5;202m                   
                
            '.  \ | /  ,'
              `. `.' ,'
             ( .`.|,' .)
          \\\u001b[38;5;220m - ~ -0- ~ - \u001b[0m//
""")
  time.sleep(0.2)
  clear()
  print("""
                                        
                   
                   
                   
\u001b[38;5;240m                  
                
           _.-^^---....,,--       
       _--                  --_  
      <                        >)
      |                         | 
       \._                   _./  
          ```--. . , ; .--'''       
\u001b[38;5;202m                | |   |             
             .-=||  | |=-.   
             `-=#$%&%$#=-'   
\u001b[0m     \\\ \u001b[38;5;220m        | ;  :|\u001b[0m        ///
    __\\\___.,-#%&$@%#&#~,.___///__
""")
  time.sleep(3)
  print("""
   _____.,-\u001b[1mNUKED SUCCESFULLY\u001b[0m-,._____
  """)
  time.sleep(3)
        
        
        
def main():
  print(banner)
  time.sleep(1)
  firstchoice = str(input("""
V1.0
\u001b[0m\u001b[7m[1]\u001b[0m Nuke a file
\u001b[0m\u001b[7m[2]\u001b[0m Nuke a folder
\u001b[1m[CNTRL + C TO EXIT]\u001b[0m

-¬=> """))
  
  if firstchoice == "1":
    filename = input("""\nWhat is the file path of the file?
\u001b[1m[CNTRL + C TO EXIT]\u001b[0m    
     
-¬=> """)
    
    print("\nNuking " + str(filename) + ". . .")
    with open(filename, "rb") as f:
      
      for i in range(1, 100):
        md5 = hashlib.md5()
        data = str(f.read())
        data = data.encode()
        md5.update(data)
        encrypteddata = md5.digest()
        data = encrypteddata
        print("\rEncrypting File... [" + str(i) + "/100]", end="", flush=True)
        time.sleep(0.4)
      f.close()  
      with open(filename, "w") as f2:
        f2.write(str(data))
        f2.close()
      key = "idk"
    
    animation()
    exit()
        

try:
  main()
except KeyboardInterrupt:
  print("\nExiting . . .\n")
