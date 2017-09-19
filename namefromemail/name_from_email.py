# Create a function that takes email address as input in the following format:
# firstName.lastName@exam.com
# and returns a string that represents the user name in the following format:
# last_name first_name
# example: "elek.viz@exam.com" for this input the output should be: "Viz Elek"
# accents does not matter

#print(name_from_email("elek.viz@exam.com"))


email_adress = str(input("Please enter ypur e-mail adress: "))


def name_from_email(entered_email_adress):   
    forename =entered_email_adress[entered_email_adress.index(".") :entered_email_adress.index("@")]
    name =entered_email_adress[:entered_email_adress.index(".")]
    return forename[1].upper() +forename[2:] + " " + name[0].upper() +name[1:]

print(name_from_email(email_adress))


