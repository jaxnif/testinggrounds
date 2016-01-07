# import the logins file for usernames and passwords
dict = {}
with open("logins.txt") as f:
    for line in f:
       (user, password) = line.split()
       dict[(user)] = password

print ('This is a login procedure')
print ('What is your username?')
username = (input()).lower()

if username in dict.keys():
    print ('What is your password?')
    password = input()
    if password == dict[username]:
        print ('success')
    else:
        print ('password incorrect, please try again')
else:
    print ('username not found')

