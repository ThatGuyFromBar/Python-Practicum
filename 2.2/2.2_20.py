s1 = input()
s2 = input()
s3 = input()
s = []
if s1.count("зайка") > 0:
    s.append(s1)
if s2.count("зайка") > 0:
    s.append(s2)
if s3.count("зайка") > 0:
    s.append(s3)
print(min(s), len(min(s)))