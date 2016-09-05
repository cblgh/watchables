import random
import pyperclip
# get the things
watchables = open("watchables.txt").read().splitlines()
print len(watchables)

# grab a thing
watchable = watchables.pop(random.randint(0, len(watchables)-1))
# print the thing
print watchable
# put the thing into your clipboard
pyperclip.copy(watchable)

# save the other things
with open("watchables.txt", "w") as src:
    src.write("\n".join(watchables) + "\n")
