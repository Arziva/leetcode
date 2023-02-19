strs = ["cir","car"]
#strs = ["flower","flow","flight"]
def get_min_str(lst):
    return min(lst, key=len)
str1 = get_min_str(strs)

lens = len(strs)
x = ""
mlen = len(str1)

if(lens == 1):
    print(strs[0])

for i in range(0, mlen):
    for j in range(0, lens-1):

        print(j, i)
        print("and")
        print(j+1,i)

        if( strs[j][i] == strs[j+1][i]):
            if(j == lens-2):
                x = x +  strs[j][i]    
        else:
            break
        print(strs[j][i] == strs[j+1][i])
            
       


print(x)

                    

      