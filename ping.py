import os


def myping(host):
    response = os.system("ping -n 1 " + host)
    return response == 0


print(myping("www.google.com"))