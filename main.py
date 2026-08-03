def menu_logins():
   while True:
     print(r"""

  _  
 | |               (_)          
 | |     ___   __ _ _ _ __  ___ 
 | |    / _ \ / _` | | '_ \/ __|
 | |___| (_) | (_| | | | | \__ \
 |______\___/ \__, |_|_| |_|___/
               __/ |            
              |___/             

              

              
[01]tiktok

[02]google

[00]exit
          """)
     selectlogin = input('>> ')
     if selectlogin == '01':
         print(r"""
___________.___ ____  __.___________________   ____  __.
\__    ___/|   |    |/ _|\__    ___/\_____  \ |    |/ _|
  |    |   |   |      <    |    |    /   |   \|      <  
  |    |   |   |    |  \   |    |   /    |    \    |  \ 
  |____|   |___|____|__ \  |____|   \_______  /____|__ \
                       \/                   \/        \/

         """)

         with open('database/logins/tiktok-logins.txt', "r") as arquivo:
            print(arquivo.read())
            input('pressione ENTER para voltar...')

     elif selectlogin == '02':
         print(r"""
                             .__          
   ____   ____   ____   ____ |  |   ____  
  / ___\ /  _ \ /  _ \ / ___\|  | _/ __ \ 
 / /_/  >  <_> |  <_> ) /_/  >  |_\  ___/ 
 \___  / \____/ \____/\___  /|____/\___  >
/_____/              /_____/           \/ 
        """)
         with open('database/logins/google-logins.txt', "r") as arquivo:
            print(arquivo.read())
            input('pressione ENTER para voltar...')

     elif selectlogin == '00':
      print('voltando...')
      break



while True:
    print("""












 /$$    /$$          /$$       /$$ /$$$$$$$  /$$$$$$$ 
| $$   | $$         |__/      | $$| $$__  $$| $$__  $$
| $$   | $$ /$$$$$$  /$$  /$$$$$$$| $$  \ $$| $$  \ $$
|  $$ / $$//$$__  $$| $$ /$$__  $$| $$  | $$| $$$$$$$ 
 \  $$ $$/| $$  \ $$| $$| $$  | $$| $$  | $$| $$__  $$
  \  $$$/ | $$  | $$| $$| $$  | $$| $$  | $$| $$  \ $$
   \  $/  |  $$$$$$/| $$|  $$$$$$$| $$$$$$$/| $$$$$$$/
    \_/    \______/ |__/ \_______/|_______/ |_______/ 
                                                      
                                                      
by manop3    



                                                      
    
[01]logins

[02]cc

[00]exit
           """)

    select = input('>> ')
    if select == '01':
        print('abrindo logins...')
        menu_logins()

    elif select == '02':
        print("""

   _____ _____ 
  / ____/ ____|
 | |   | |     
 | |   | |     
 | |___| |____ 
  \_____\_____|
               
        """)
        with open('database/cc/cc.txt', "r") as arquivo:
           print(arquivo.read())
           input('pressione ENTER para voltar...')

    elif select == '00':
        print('saindo...')
        break


 

    
    

    
    
    

