# Password_Checker.py

password = input ("Enter Your User Password: ")

if len (password) > 7:
    print("Weak Password, Pleases use a stronger Password")
elif len (password) < 10:
    print ("Medium Password")
else:
    print ("Strong Password")
