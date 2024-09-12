
a= "Nazir is from mbstu ict department"

# string split letter by letter up to index 4[N a z i r]
for i in a[:5]:
  print(i)

#splits strings upon empty space[Nazir , is, from, mbstu , ict, department ]
b=a.split(" ")
for w in b:
  print(w)

#capitalize from index 3 to 5 (here index means each words)
c=b[3:6]
for sw in c:
  print(sw.upper())
