szam1 = int(input("Adj meg egy számot: "))
szam2 = int(input("Adj meg egy másik számot számot: "))

if szam1 > 0 and szam2 > 0:
    print("A számok lehetnek a téglalap oldalai.")
    if szam1 == szam2:
        print("Ez egy négyzet")
        print("Terület ", szam1**2)
        print("Kerület ", 4*szam1)
    else:
        print("Ez egy téglalap")
        print("Terület: ",szam1*szam2)
        print ("Kerület ",2*(szam1+szam2))
else:
    print("Egyik szám sem lehet téglalap oldala.")
    print("Terület: ",szam1*szam2)
    print ("Kerület ",2*(szam1+szam2))