broj_kupaca_ponedeljak = int(input( "Unesite broj kupaca za ponedeljak: " ))
broj_kupaca_utorak = int(input ("Unesite broj broj kupaca za utrorak: "))
broj_kupaca_sreda = int(input ("Unesite broj kupaca za sredu: "))
broj_kupaca_cetvrtak = int(input ("Unesite broj kupaca za cetvrtak: "))
broj_kupaca_petak = int(input ("Unesite broj kupaca za petak: "))
broj_kupaca_subota = int(input ("Unesite broj kupaca za subotu: "))
broj_kupaca_nedelja = int(input ("Unesite broj kupaca za nedelju: "))

ukupan_broj_kupaca = 0
ukupan_broj_kupaca += broj_kupaca_ponedeljak
ukupan_broj_kupaca += broj_kupaca_utorak
ukupan_broj_kupaca += broj_kupaca_sreda
ukupan_broj_kupaca += broj_kupaca_cetvrtak
ukupan_broj_kupaca += broj_kupaca_petak
ukupan_broj_kupaca += broj_kupaca_subota
ukupan_broj_kupaca += broj_kupaca_nedelja
print(f"Ukupan broj kupaca za celu nedelju je: {ukupan_broj_kupaca}")

ukupan_broj_kupaca_radnidan=0
ukupan_broj_kupaca_radnidan += broj_kupaca_ponedeljak
ukupan_broj_kupaca_radnidan += broj_kupaca_utorak
ukupan_broj_kupaca_radnidan += broj_kupaca_sreda
ukupan_broj_kupaca_radnidan += broj_kupaca_cetvrtak
ukupan_broj_kupaca_radnidan += broj_kupaca_petak
print(f"Ukupan broj kupaca u toku radnih dana je:{ukupan_broj_kupaca_radnidan}")

ukupan_broj_kupaca_vikend = 0
ukupan_broj_kupaca_vikend +=broj_kupaca_nedelja
ukupan_broj_kupaca_vikend +=broj_kupaca_subota
print(f"Ukupan broj kupaca u toku vikenda je: {ukupan_broj_kupaca_vikend}")

if broj_kupaca_nedelja > broj_kupaca_subota: 
    print(f"U nedelju je bilo vise kupaca nego u subotu")

if ukupan_broj_kupaca_radnidan > ukupan_broj_kupaca_vikend:
    print(f"Radnim danima je bilo vise kupaca nego za dva dana vikenda")

if ukupan_broj_kupaca > 1000 or ukupan_broj_kupaca_vikend > 500:
    print(f"Uspesna nedelja")

