import pyAesCrypt
import os,time
from rich.console import Console
from rich import print

c= Console()

class FileEnc:
    def encryption(self,filename,password):
        self.filename = filename
        self.password = password
        self.buffersize = 64*1024
        try:
            pyAesCrypt.encryptFile(self.filename, self.filename+".aes", self.password, self.buffersize)
            os.remove(self.filename)
            print("\n[b green]File Encrypted![/b green]\n")
            time.sleep(2)
        except:
            print("\n[b bright_red]File Not Found[/b bright_red]")
            print("\n[b bright_red]Returning To Menu![/b bright_red]\n")
            time.sleep(2.5)

    def decryption(self,filename,password):
        self.filename = filename
        self.password = password
        self.buffersize = 64*1024
        try:
            pyAesCrypt.decryptFile(self.filename+".aes", self.filename, self.password, self.buffersize)
            os.remove(self.filename + ".aes")
            print("\n[b green]File Decrypted![/b green]\n")
            time.sleep(2.5)
        except:
            print("\n[b bright_red]Wrong Filename or Password![/b bright_red]\n")
            print("[b bright_red]Returning To Menu![/b bright_red]\n")
            time.sleep(3)

file_enc_dec = FileEnc()

if __name__ == '__main__':
    while(True):
        logo = '''
                                        ███████╗██╗██╗░░░░░███████╗
                                        ██╔════╝██║██║░░░░░██╔════╝
                                        █████╗░░██║██║░░░░░█████╗░░
                                        ██╔══╝░░██║██║░░░░░██╔══╝░░
                                        ██║░░░░░██║███████╗███████╗
                                        ╚═╝░░░░░╚═╝╚══════╝╚══════╝

███████╗███╗░░██╗░█████╗░██████╗░██╗░░░██╗██████╗░░░░░░░██████╗░███████╗░█████╗░██████╗░██╗░░░██╗██████╗░
██╔════╝████╗░██║██╔══██╗██╔══██╗╚██╗░██╔╝██╔══██╗░░░░░░██╔══██╗██╔════╝██╔══██╗██╔══██╗╚██╗░██╔╝██╔══██╗
█████╗░░██╔██╗██║██║░░╚═╝██████╔╝░╚████╔╝░██████╔╝█████╗██║░░██║█████╗░░██║░░╚═╝██████╔╝░╚████╔╝░██████╔╝
██╔══╝░░██║╚████║██║░░██╗██╔══██╗░░╚██╔╝░░██╔═══╝░╚════╝██║░░██║██╔══╝░░██║░░██╗██╔══██╗░░╚██╔╝░░██╔═══╝░
███████╗██║░╚███║╚█████╔╝██║░░██║░░░██║░░░██║░░░░░░░░░░░██████╔╝███████╗╚█████╔╝██║░░██║░░░██║░░░██║░░░░░
╚══════╝╚═╝░░╚══╝░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░░░░░░░░░░╚═════╝░╚══════╝░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░░░░'''
        print(logo)
        print("\nGit -[link=https://github.com/lazyprogrammerrr]LazyProgrammerrr[/link]")
        menu = '''\n[b bright_cyan]----- MENU -----
        1. ENCRYPT YOUR FILE [b bright_yellow][Press (1) or (E)][/b bright_yellow]
        2. DECRYPT YOUR FILE [b bright_yellow][Press (2) or (D)][/b bright_yellow]
        3. EXIT[b bright_yellow]              [Press (3) or (Q)][/b bright_yellow][/b bright_cyan]'''
        print(menu)
        menuinput = c.input("\n[b deep_pink4]Enter Your Choice -> [/b deep_pink4]")
        if menuinput == '1' or menuinput.casefold() == 'E'.casefold():
            encfilename =c.input("\n[b gold3]Enter File Name You Want To Encrypt -> [/b gold3]")
            encpass = c.input("\n[b dark_goldenrod]Enter Password(Remember This)\nThis Will Be Used Decrypt Your File Further -> [/b dark_goldenrod]")
            file_enc_dec.encryption(encfilename,encpass)
        elif menuinput == '2' or menuinput.casefold() == 'D'.casefold():
            decfilename =c.input("\n[b medium_purple1]Enter File Name You Want To Decrypt -> [/b medium_purple1]")
            decpass = c.input("\n[b medium_purple1]Enter Password To Decrypt Your File -> [/b medium_purple1]")
            file_enc_dec.decryption(decfilename,decpass)
        elif menuinput == '3' or menuinput.casefold() == 'Q'.casefold():
            print("\n\t\t[b green1]     Thankyou For Using!\n\t\t-----File Encryp-Decryp-----[/b green1]\n")
            time.sleep(1.5)
            exit()
        else:
            print("\n[b blink red3]Wrong Menu Option Selected! Please Choose From Given Ones.[/b blink red3]\n")
            time.sleep(1)