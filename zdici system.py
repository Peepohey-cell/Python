print("Konfigurátor zdícího systému")
print("*****************************")

ploch_tvar = 0.1

sprv_jmen = "stavebnik"
sprv_hesl = "stavba"

jmeno = input("Zadej uživatelské jméno: ")
heslo = input("Zadej heslo: ")

if jmeno == sprv_jmen and heslo == sprv_hesl:
    print(" ")

    delk_sten = float(input("Zadej délku stěny (metry):"))
    vys_sten = float(input("Zadej výšku stěny (metry):"))
    vys_okn = float(input("Zadej výšku okna (metry):"))
    sir_okn = float(input("Zadej šířku okna (metry):"))

    ploch_sten = delk_sten * vys_sten
    ploch_okn = vys_okn * sir_okn
    poc_tvarn = (ploch_sten - ploch_okn) / ploch_tvar

    print(f"Plocha stěny včetně okna: {ploch_sten} m^2")
    print(f"Plocha okna je: {ploch_okn}m^2 ")
    print(f"plocha stěny bez okna: {ploch_sten - ploch_okn} m^2")
    print(f"počet tvárnic potřebných k vyzdění plochy stěny: {poc_tvarn} ks")

    print("Dostupnost materiálu na pobočkách v ČR")
    print("****************************************")

    print(("{:<20}|{:<25}|{:<25}|".format("Město", "Druh materiálu", "Počet kusů na pobočce")))
    print("*********************************************************************************")

    pocet_Praha = 500
    pocet_Brno = 300
    pocet_Ostrava = 700
    if poc_tvarn <= pocet_Praha:
        print(("{:<20}|{:<25}|{:<25}|".format("Praha", "tvárnice", str(pocet_Praha))))
    if poc_tvarn <= pocet_Brno:
        print(("{:<20}|{:<25}|{:<25}|".format("Brno", "tvárnice", str(pocet_Brno))))
    if poc_tvarn <= pocet_Ostrava:
        print(("{:<20}|{:<25}|{:<25}|".format("Ostrava", "tvárnice", str(pocet_Ostrava))))
    if poc_tvarn > pocet_Praha and poc_tvarn > pocet_Brno and poc_tvarn > pocet_Ostrava:
        print("Žádná pobočka nemá dost materiálů")

else:
    print("Špatné údaje")
