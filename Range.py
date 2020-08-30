def Range(mulai=0, akhir=0, langkah=1) :
    if muali > akhir:
        mulai, akhir = akhir, mulai
    while mulai < akhir:
        yield mulai
        mulai += langkah

for i in Range(10) :
    print(i)













