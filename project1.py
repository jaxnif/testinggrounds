# import the logins file for usernames and passwords
dict = {}
with open("logins.txt") as f:
    for line in f:
       (key, val) = line.split()
       dict[(key)] = val

print ('This is a login procedure')
print ('What is your username?')
username = input()

if username in dict[]