import datetime
x = datetime.datetime.today() - datetime.timedelta(days=1)
date = str((x.strftime("%b %d")))
file = open("test.txt", "r")
for line in file:
    if date in line:
        print(line, next(file), end="")
