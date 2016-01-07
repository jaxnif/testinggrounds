# import the logins file for usernames and passwords
dict = {}
with open("logins.txt") as f:
    for line in f:
       (key, val) = line.split()
       dict[(key)] = val

