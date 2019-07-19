characters = ['t', 'a', 'c', 'o']

output = '' #Initiated empty value
length = len(characters) #len of characters is 4
i=0 #initiated i is 0

while (i < length):                     #meaning 0<4, 1<4, 2<4, 3<4
    output = output + characters[i]     # t, t+a, t+a+c, t+a+c+o
    i = i + 1                           #increament +1 to i

length = length * -1                    # 4*-1 = -4
i = -2                                  # i is now -2

while (i >= length):                    #-2 >= -4, 
    output = output + characters[i]     #c, a, t
    i = i - 1                           # -2 , -3, -4

print(output)                           #tacocat
