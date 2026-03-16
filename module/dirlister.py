import os

def run(**args) :
    print("[*] In dirlister module.")
    filter = os.listdir(".")
    return str(filter)