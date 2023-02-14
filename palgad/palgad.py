from module1 import *


palgad=[1200,2500,750,395,1200]
inimesed=["A","B","C","D","E"]

while True:
    print(inimesed)
    print(palgad)
    print()
    menu=int(input("valik:\n1-lisa andmed\n2-Kustuta andmed\n3-Suurim palk\n4-Vähem palk\n5-Sort\n6-viige inimesi välja täiusliku salgataga\n7-otsi palka inimese nime järgi\n8-sisestatud palga põhjal kuvab inimeste madalamad ja kõrgemad palgad\n9-Leia top 3 vähem või rohkem\n10-Otsi keskmine palk ja kes on saada suurem\n11-Otsi maksuvaba palk\n12-Sort\n13-Otsige kes teenivad alla keskmise palga ja emalda nad\n14-Teeb nimekiri\n15-saate teada 5% tõusuga töötaja töötasu T-aastas\n16-Vaheta nimi kolmandale\n"))

    if menu==0:
        break
    elif menu==1:
        inimesed, palgad=lisa_palk(inimesed, palgad)
    elif menu==2:
        imimesed,palgad=kustutada(inimesed, palgad)
    elif menu==3:
        palk,nimi=suurim_palk(inimesed,palgad)
        print("Suurim palk on",palk, nimi)
    elif menu==4:
        palk,nimi=vähem_palk(inimesed,palgad)
        print("vähem palk pn", palk, nimi)
    elif menu==5:
        inimesed,palgad=tõusev_langev(inimesed,palgad)
    elif menu==6:
        iniemsed,palgad=sama_palk(inimesed,palgad)
    elif menu==7:
        iniemsed,palgad=palgaotsing(inimesed,palgad)
    elif menu==8:
        enam_vähem(inimesed,palgad)
    elif menu==9:
        top(inimesed,palgad)
    elif menu==10:
        Keskmine(inimesed,palgad)
    elif menu==11:
        Tulumaks(inimesed,palgad)
    elif menu==12:
        inimesed,palgad=sorteerimine(inimesed,palgad)
    elif menu==13:
        inimesed,palgad=emalda(inimesed,palgad)
    elif menu==14:
        inimesed,palgad=tint(inimesed,palgad)
    elif menu==15:
        inimesed,palgad=aasta(inimesed,palgad)
    elif menu==16:
        inimesed=Nimeta_ümber(inimesed)
    else:
        print("Kirjuta õige arv")
