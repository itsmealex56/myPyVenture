user_rate = []
ave_rate = 0
count = -1

while user_rate != '-999':
    user_rate = input("Enter rating of movie: ")
    ave_rate = ave_rate + int(user_rate)
    count = count + 1

ave_rate_compute = (ave_rate + 999)/count
print(ave_rate_compute)

