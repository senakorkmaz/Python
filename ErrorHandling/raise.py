def check_password(psw):
    import re
    if len(psw) < 8:
        raise Exception('Parola en az 8 karakter olamalidir.')
    elif not re.search('[a-z]',psw):
        raise Exception("Parola kucuk harf icermelidir.")
    elif not re.search('[A-Z]',psw):
        raise Exception("Parola buyuk harf icermelidir.")
    elif not re.search('[0-9]',psw):
        raise Exception("Parola rakam icermelidir.")
    elif not re.search('[_$@]',psw):
        raise Exception("Parola alpha numeric karakter icermelidir.")
    elif re.search("\s",psw):
        raise Exception("Parola bosluk icermemelidir.")

password = "12345@6aA78"
try:
    check_password(password)
except Exception as ex:
    print(ex)
else: 
    print("Gecerli parola.")
finally:
    print("Validation is completed.")
    