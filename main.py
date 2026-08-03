import os


cookies = r'database/cookies'

tokens = r'database/tokens'

passw = r'database/passw'


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

[03]protonmail

[04]kabum

[05]serasa

[00]exit
          """)
     selectlogin = input('>> ')
     if selectlogin == '01':
         print(r"""
  _______ _ _    _        _    
 |__   __(_) |  | |      | |   
    | |   _| | _| |_ ___ | | __
    | |  | | |/ / __/ _ \| |/ /
    | |  | |   <| || (_) |   < 
    |_|  |_|_|\_\\__\___/|_|\_\
                               
                               
         """)

         with open('database/logins/tiktok-logins.txt', "r") as arquivo:
            print(arquivo.read())
            input('pressione ENTER para voltar...')

     elif selectlogin == '02':
         print(r"""
   _____                   _      
  / ____|                 | |     
 | |  __  ___   ___   __ _| | ___ 
 | | |_ |/ _ \ / _ \ / _` | |/ _ \
 | |__| | (_) | (_) | (_| | |  __/
  \_____|\___/ \___/ \__, |_|\___|
                      __/ |       
                     |___/        
        """)
         with open('database/logins/google-logins.txt', "r") as arquivo:
            print(arquivo.read())
            input('pressione ENTER para voltar...')

     elif selectlogin == '03':
        print(r"""
  _____           _              __  __       _ _ 
 |  __ \         | |            |  \/  |     (_) |
 | |__) | __ ___ | |_ ___  _ __ | \  / | __ _ _| |
 |  ___/ '__/ _ \| __/ _ \| '_ \| |\/| |/ _` | | |
 | |   | | | (_) | || (_) | | | | |  | | (_| | | |
 |_|   |_|  \___/ \__\___/|_| |_|_|  |_|\__,_|_|_|
                                                  
      
    """)
        with open('database/logins/protonmail-logins.txt', "r") as arquivo:
           print(arquivo.read())
           input('pressione ENTER para voltar...')   

     elif selectlogin == '04':
        print(r"""
  _  __     _                     
 | |/ /    | |                    
 | ' / __ _| |__  _   _ _ __ ___  
 |  < / _` | '_ \| | | | '_ ` _ \ 
 | . \ (_| | |_) | |_| | | | | | |
 |_|\_\__,_|_.__/ \__,_|_| |_| |_|
                                  
                                  
    """)
        with open('database/logins/kabum-logins.txt', "r") as arquivo:
           print(arquivo.read())
           input('pressione ENTER para voltar...')    

     elif selectlogin == '05':
        print(r"""
   _____                          
  / ____|                         
 | (___   ___ _ __ __ _ ___  __ _ 
  \___ \ / _ \ '__/ _` / __|/ _` |
  ____) |  __/ | | (_| \__ \ (_| |
 |_____/ \___|_|  \__,_|___/\__,_|
                                  
                                  
    """)
        with open('database/logins/serasa-logins.txt', "r") as arquivo:
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

[03]cookies

[04]tokens

[05]passw

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

    elif select == '03':
        print(r"""
   _____            _    _           
  / ____|          | |  (_)          
 | |     ___   ___ | | ___  ___  ___ 
 | |    / _ \ / _ \| |/ / |/ _ \/ __|
 | |___| (_) | (_) |   <| |  __/\__ \
  \_____\___/ \___/|_|\_\_|\___||___/
                                     
                                                         
        """)
        for item in os.listdir(cookies):
         print(item)
        input('pressione ENTER para sair...')

    elif select == '04':
        print(r"""
  _______    _                  
 |__   __|  | |                 
    | | ___ | | _____ _ __  ___ 
    | |/ _ \| |/ / _ \ '_ \/ __|
    | | (_) |   <  __/ | | \__ \
    |_|\___/|_|\_\___|_| |_|___/
                                
                                      
        """)
        for item in os.listdir(tokens):
          print(item)
        input('pressione ENTER para sair...')

    elif select == '05':
        print(r"""
  _____                                    _ 
 |  __ \                                  | |
 | |__) |_ _ ___ _____      _____  _ __ __| |
 |  ___/ _` / __/ __\ \ /\ / / _ \| '__/ _` |
 | |  | (_| \__ \__ \\ V  V / (_) | | | (_| |
 |_|   \__,_|___/___/ \_/\_/ \___/|_|  \__,_|
                                             
                                             
        """)
        for item in os.listdir(passw):
             print(item)

        input('pressione ENTER para voltar... ')

    elif select == '00':
             print('saindo...')
             break


 

    
    

    
    
    

