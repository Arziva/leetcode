#strs = ["cir","car"]
#strs = ["flower","flow","flight"]
#strs = ["dog","racecar","car"]
strs = ""
if not strs: print("") 

else:
    mina = min(strs)
    maxa = max(strs)


    for i, c in enumerate(mina):
        if c != maxa[i]:
            print (mina[:i])

    