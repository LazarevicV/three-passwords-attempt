Termin 2 - zadatak2

Klijent server aplikacija

Klijent pri konektovanju unosi odgovrajuću lozinku (3 pokušaja)
 - ako je neispravna, dobija odgovarajuću poruku (posle prva dva promašena: pokušajte ponovo, a nakon trećeg: neispravna loznika) i prekida se konekcija
 - ako je ispravna, dobija odgovarajuću poruku i komunikacija se nastavlja
Klijent unosi poruku sa tastature i šalje serveru na obradu.
 -ako je redni broj klijenta paran, server vraća upper
 -ako je redni broj klijenta neparan, server vraća lower
Komunikacija traje sve dok Klijent ne unese "exit"
Server ostaje da sluša i po mogućnosti prihvata nove klijente, pre svakog accept-a Server dobija pitanje Continue? Y/n
 - ako je unos sa tastature Y, server čeka nove klijente
 - ako je unos n, server se gasi