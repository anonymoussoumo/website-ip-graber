import subprocess
import pyfiglet

text = pyfiglet.figlet_format("Website IP Grabber")
print(text)
print("                                         By anonymous group")
print("                                     Version 1.0.0")
print("Enter An IP or website name down below")
i = input()
subprocess.call("ping "+ i ,shell=True)
