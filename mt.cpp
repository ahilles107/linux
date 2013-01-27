// maszyna turinga
// sorry, comments only in Polish
#include <iostream>
#include <string>
using namespace std;

// struktura opisujaca stan maszyny
struct mt_stan {
	string mt;
	int poz;
	int stan;
	int d;
	int tr;
};

// funkcja wypisujaca stan maszyny
// wstawia do opisu jej stan oraz ucina koncowe B
void podmien(mt_stan mt_s) {
	string buff = "";
	string c = "";
	int i;

	for (i = 0; i < mt_s.poz; i++)
		cout << mt_s.mt.at(i);
	cout << " q" << mt_s.stan << " ";
	for (i = mt_s.poz; i<=mt_s.d; i++)
		if(mt_s.mt.at(i) == 'B')
			buff += 'B';
		else {
			buff += mt_s.mt.at(i);
			c += buff;
			buff = "";
		}
	cout << c;

}

// pokazuje opis MT
void show_desc() {
	cout << " Emulator maszyny Turinga obliczajacy roznice wlasciwa" << endl;
	cout << " Autor: Maciej Plonski / sokoli.pl" << endl << endl;

	cout << " Roznica wlasciwa: " << endl;
	cout << "             | m - n dla m >= n" << endl;
	cout << "     m - n = |               " << endl;
	cout << "             | 0     dla m < n " << endl << endl;

	cout << " Postać maszyny Turinga:" << endl;
	cout << "     M = ({q0, q1, q2, q3, q4, a5, a6}, {0, 1}, {0, 1, B}, d, q0, B, 0)" << endl << endl;

	cout << " Tablica przejsc:" << endl;
	cout << "     ==========================================" << endl;
	cout << "     |   d   |     0    |     1    |     B    |" << endl;
	cout << "     ==========================================" << endl;
	cout << "     |   q0  | (q1,B,P) | (q5,B,P) |     -    |" << endl;
	cout << "     |   q1  | (q1,O,P) | (q2,1,P) |     -    |" << endl;
	cout << "     |   q2  | (q3,1,L) | (q2,1,P) | (q4,B,L) |" << endl;
	cout << "     |   q3  | (q3,0,L) | (q3,1,L) | (q0,B,P) |" << endl;
	cout << "     |   q4  | (q4,0,L) | (q4,B,L) | (q6,0,P) |" << endl;
	cout << "     |   q5  | (q5,B,P) | (q5,B,P) | (q6,B,P) |" << endl;
	cout << "     |   q6  |     -    |     -    |     -    |" << endl;
	cout << "     ==========================================" << endl;
}

// roznica wlasciwa matematycznie
int math_m(int m, int n) {
	if (m > n)
		return m-n;
	else
		return 0;
}

// generuje ciag do emulatora MT
string generuj_ciag(int m, int n) {
	string ciag = "";
	int i;
	for(i=0; i<m; i++) {
		ciag += '0';
	}
	ciag += '1';
	for(i=0; i<n; i++) {
		ciag += '0';
	}
	return ciag;
}

// funkcja przejscia z pozycji na pozycje
int przejdz(mt_stan *a, int il) {
	int g = (*a).poz,
	    m = (*a).d;
	if ((g == 0) && (il == -1)) {
		(*a).mt = 'B' + (*a).mt;
		(*a).d = m+1;
		return 0;
	}
	if ((g == m) && (il == 1)) {
		(*a).mt += 'B';
		(*a).d = m+1;
		return m+1;
	}
	return g+il;
}

// emulator MT
mt_stan oblicz(mt_stan mt_s) {
	struct mt_stan tmp;
	char stan;

	if (mt_s.tr == 1)
		cout << " |- ";
	podmien(mt_s);

	mt_s.tr = 1;

	// najpierw sytuacje, ktore daja koniec pracy
	if ((mt_s.stan == 6) || ((mt_s.stan == 0) && (mt_s.mt.at(mt_s.poz) == 'B')) || ((mt_s.stan == 1) && (mt_s.mt.at(mt_s.poz) == 'B')) || (mt_s.d == 2 && mt_s.mt[0] == 'B')) {
		mt_s.poz = -1;
		return mt_s;
	}

	// osbluga przejsc
	if (mt_s.stan == 0) {
		if (mt_s.mt.at(mt_s.poz) == '0') {
			mt_s.stan = 1;
			mt_s.mt[mt_s.poz] = 'B';
			mt_s.poz = przejdz(&mt_s, 1);
		}else if (mt_s.mt.at(mt_s.poz) == '1') {
			mt_s.stan = 5;
			mt_s.mt[mt_s.poz] = 'B';
			mt_s.poz = przejdz(&mt_s, 1);
		}
	} else if (mt_s.stan == 1) {
		if (mt_s.mt.at(mt_s.poz) == '0') {
			mt_s.stan = 1;
			mt_s.mt[mt_s.poz] = '0';
			mt_s.poz = przejdz(&mt_s, 1);
		}else if (mt_s.mt.at(mt_s.poz) == '1') {
			mt_s.stan = 2;
			mt_s.mt[mt_s.poz] = '1';
			mt_s.poz = przejdz(&mt_s, 1);
		}
	} else if (mt_s.stan == 2) {
		if (mt_s.mt.at(mt_s.poz) == '0') {
			mt_s.stan = 3;
			mt_s.mt[mt_s.poz] = '1';
			mt_s.poz = przejdz(&mt_s, -1);
		}else if (mt_s.mt.at(mt_s.poz) == '1') {
			mt_s.stan = 2;
			mt_s.mt[mt_s.poz] = '1';
			mt_s.poz = przejdz(&mt_s, 1);
		}else if( mt_s.mt.at(mt_s.poz) == 'B') {
			mt_s.stan = 4;
			mt_s.mt[mt_s.poz] = 'B';
			mt_s.poz = przejdz(&mt_s, -1);
		}
	} else if (mt_s.stan == 3) {
		if (mt_s.mt.at(mt_s.poz) == '0') {
			mt_s.stan = 3;
			mt_s.mt[mt_s.poz] = '0';
			mt_s.poz = przejdz(&mt_s, -1);
		}else if (mt_s.mt.at(mt_s.poz) == '1') {
			mt_s.stan = 3;
			mt_s.mt[mt_s.poz] = '1';
			mt_s.poz = przejdz(&mt_s, -1);
		}else if( mt_s.mt.at(mt_s.poz) == 'B') {
			mt_s.stan = 0;
			mt_s.mt[mt_s.poz] = 'B';
			mt_s.poz = przejdz(&mt_s, 1);
		}
	} else if (mt_s.stan == 4) {
		if (mt_s.mt.at(mt_s.poz) == '0') {
			mt_s.stan = 4;
			mt_s.mt[mt_s.poz] = '0';
			mt_s.poz = przejdz(&mt_s, -1);
		}else if (mt_s.mt.at(mt_s.poz) == '1') {
			mt_s.stan = 4;
			mt_s.mt[mt_s.poz] = 'B';
			mt_s.poz = przejdz(&mt_s, -1);
		}else if( mt_s.mt.at(mt_s.poz) == 'B') {
			mt_s.stan = 6;
			mt_s.mt[mt_s.poz] = '0';
			mt_s.poz = przejdz(&mt_s, 1);
		}
	} else if (mt_s.stan == 5) {
		if (mt_s.mt.at(mt_s.poz) == '0') {
			mt_s.stan = 5;
			mt_s.mt[mt_s.poz] = 'B';
			mt_s.poz = przejdz(&mt_s, 1);
		}else if (mt_s.mt.at(mt_s.poz) == '1') {
			mt_s.stan = 5;
			mt_s.mt[mt_s.poz] = 'B';
			mt_s.poz = przejdz(&mt_s, 1);
		}else if( mt_s.mt.at(mt_s.poz) == 'B') {
			mt_s.stan = 6;
			mt_s.mt[mt_s.poz] = 'B';
			mt_s.poz = przejdz(&mt_s, 1);
		}
	}

	return oblicz(mt_s);
}

// glowna funkcja obliczen MT
int run_mt(string ciag, int d) {
	struct mt_stan poz;
	poz.mt = ciag;
	poz.poz = 0;
	poz.stan = 0;
	poz.d = d;
	poz.tr = 0;
	while ((poz = oblicz(poz)).poz != -1) {
		continue;
	}
	int i,w=0;
	for(i = 0; i < poz.mt.length(); i++) {
		if (poz.mt.at(i) == '0') w++;
	}
	return w;
}

int main () {
	int m, n, w;
	string ciag;

	show_desc();

	cout << "Podaj m >> ";
	cin >> m;
	cout << "Podaj n >> ";
	cin >> n;
	cout << endl;
	if((m < 0) || (n < 0)) {
		cout << "nieujemne..." << endl;
		return 1;
	}

	ciag = generuj_ciag(m, n);
	cout << endl << "Wygenerowana tasma wejsciowa: " << ciag << endl << endl;
	w = run_mt(ciag, m+n);

	cout << endl << endl << "Wynik (roznica wlasciwa) wynosi: " << w << endl;
	if (math_m(m, n) == w) {
		cout << "wynik zgodny z rownaniem roznicy wlasciwej obliczonym matematycznie" << endl;
		cout << endl << "wejscie zostalo zaakceptowane" << endl;
	} else
		cout << "wynik NIE JEST zgodny z rozwiazaniem roznicy wlasciwej oblocznym matematycznie" << endl;

	return 0;
}

