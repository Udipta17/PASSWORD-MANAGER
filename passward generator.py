import random

name=input("enter a your name")
print(f"Hello{name},welcome to the passward generator")
pass_len = int(input("enter the length of passward ->"))
pass_data="qwertyuiopasdfghjklzxcvbnm123456789[];:',.//*-+?><:!@#$%^&*()_"
passward = "".join(random.sample(pass_data,paa_len))
print(password)