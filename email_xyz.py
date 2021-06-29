ex = "^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"

def email_check():

    for i in range(len(email_ent.get())):
        if re.search(ex, email_ent.get()):
            with open("text_file.txt", "a") as f:
                f.write(email_ent.get())
                f.write('\n')

        else:
            f.write('invalid')
