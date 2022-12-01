s1 = input()
s2 = input()
s3 = input()
s4 = input()
alp = "ABCDEFG"
alp2 = "0123456789ABCDEFGHIJKLMN"
alp3 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
day_d = {'A':"MON", 'B':"TUE", 'C':"WED", 'D':"THU", 'E':"FRI", 'F':"SAT", 'G':"SUN"}
hour_d = dict(zip(list("0123456789ABCDEFGHIJKLMN"), list(range(0, 24))))

if __name__ == "__main__":
    cnt = 0
    for i, j in zip(s1, s2):
        if i == j:
            if cnt == 0 and i in alp and j in alp:
                day = day_d[i]
                cnt += 1
            elif cnt == 1 and i in alp2 and j in alp2:
                hour = hour_d[i]
                break
    
    
    p = 0
    for i, j in zip(s3, s4):
        if i == j and i in alp3 and j in alp3:
            minute = p
            break
        p += 1
    
    print(day, f"{hour:02}:{minute:02}")