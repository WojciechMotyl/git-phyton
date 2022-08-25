one_line_string = "To jest string w jednej lini."
muli_line_string = """
Ten String
Jest w kilku linikach

    i tak wyglada"""

user = "WojtekMotyl"
##print("%s" % (muli_line_string) )    

#print("-------------------------------")

#print("{} to jest pierwsza zmienna. {} to jest druga zmienna".format(one_line_string, muli_line_string))

#print("--------------------------------")

#print(f"{one_line_string} to jest pierwsza zmienna. {muli_line_string} to jest druga zmienna")

pozycja_litery = muli_line_string.find("a")

#print("Pozycja {}".format(pozycja_litery))
#print("Pozycja 30 to: {}".format(muli_line_string[30]))

#print("Zmienna multi_line_string jest: {}".format(type(muli_line_string)))

#print("Nazwa Uzytkowanika w systemie Linux: {}".format(user.lower()))
print("Rozdzielone\tTabem ")
print("To jest pierwsza linia\nTo druga linia")