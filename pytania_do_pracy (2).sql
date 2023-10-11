-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Czas generowania: 11 Paź 2023, 11:53
-- Wersja serwera: 10.4.25-MariaDB
-- Wersja PHP: 7.4.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Baza danych: `pytania`
--

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `pytania_do_pracy`
--

CREATE TABLE `pytania_do_pracy` (
  `numeracja` int(11) NOT NULL,
  `pytania` text COLLATE utf8_polish_ci NOT NULL,
  `odpowiedz` int(11) NOT NULL,
  `odpowiedz_A` text COLLATE utf8_polish_ci NOT NULL,
  `odpowiedz_B` text COLLATE utf8_polish_ci NOT NULL,
  `odpowiedz_C` text COLLATE utf8_polish_ci NOT NULL,
  `odpowiedz_D` text COLLATE utf8_polish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_polish_ci;

--
-- Zrzut danych tabeli `pytania_do_pracy`
--

INSERT INTO `pytania_do_pracy` (`numeracja`, `pytania`, `odpowiedz`, `odpowiedz_A`, `odpowiedz_B`, `odpowiedz_C`, `odpowiedz_D`) VALUES
(1, 'W Polsce wchodzimy po angielsku. Po jakiemu wchodza Anglicy?', 12, 'po grecku ', 'po fransusku', 'po rosyjsku', 'po wlosku'),
(2, 'Jaki znak interpunkcyjny stawiamy po cyfrze arabskiej sprawia, ze odczytujemy ja jako liczebnik porzadkowy?', 14, 'myslnik', 'przecinek', 'srednik', 'kropka'),
(3, 'Ile kosztuje chleb, ktory pierwotnie kosztowal 10zl, nastepnie potanial do 8zl, a pozniej jego cena wzrosla o 20 proc.?', 13, '8,20zl', '9zl', '9.60zl', '10zl'),
(4, 'Gdzie najczesciej mozna spotkac aparaty sluchowe telefoniczne samoinkasujace?', 11, 'w wiezieniach', 'w sklepach', 'w przystankach', 'w szkolach'),
(5, 'Awanturka to pasta...', 14, 'polerska', 'cukrowa', 'do butow', 'do kanapek'),
(6, 'Ktory z ptakow kuka?', 12, 'samice kukulki', 'samiec kukulki', 'samica gzegozolki', 'samica zazuli'),
(7, 'Kojot wyglada jak cos pomiedzy...', 14, 'kuna a lasica', 'bobrem a wiewiorka', 'rysiem a zbikiem', 'wilkiem a szakalem'),
(8, 'Ile dni ma lutego w roku przestepnym?', 12, '28', '29', '30', '31'),
(9, 'Który gaz jest najbardziej obecny w atmosferze ziemi?', 12, 'Tlen', 'Azot', 'Wodór', 'Hel'),
(10, 'Która z tych planet jest najbliższa Słońcu?', 11, 'Wenus', 'Mars', 'Uran', 'Neptun'),
(11, 'Kto napisał powieść \"Zbrodnia i kara\"?', 14, 'William Shakespeare', 'Leo Tolstoj', 'Charles Dickens', 'Fiodor Dostojewski'),
(12, 'Który narząd w ciele człowieka jest odpowiedzialny za pompowanie krwi?', 13, 'Wątroba', 'Nerka', 'Serca', 'Żołądek'),
(13, 'Jaki jest symbol chemiczny dla złota?', 11, 'Au', 'Ag', 'Fe', 'Cu'),
(14, 'Który z tych zwierząt jest drapieżnikiem?', 13, 'Koza', 'Krowa', 'Orzeł', 'Królik'),
(15, 'Które z tych miast jest stolicą Francji?', 14, 'London', 'Madryt', 'Rzym', 'Paryż'),
(16, 'Jak nazywa się największa planeta w Układzie Słonecznym?', 11, 'Jowisz', 'Mars', 'Wenus', 'Saturn'),
(17, 'Który z tych oceanów jest największy pod względem powierzchni?', 12, 'Ocean Atlantycki', 'Ocean Spokojny', 'Ocean Indyjski', 'Ocean Arktyczny'),
(18, 'Który pierwiastek chemiczny ma symbol \"H\"?', 13, 'Węgiel', 'Tlen', 'Wodór', 'Azot'),
(19, 'Który kolor jest skojarzony z sygnałem \"stop\" na sygnalizacji świetlnej?', 11, 'Czerwony', 'Zielony', 'Niebieski', 'Żółty'),
(20, 'Gdzie człowiek ma najwięcej zwykłych gruczołów potowych?', 12, 'na udach', 'na dłoniach', 'na brzuchu', 'na karku '),
(21, 'Mostek to nie:', 11, 'napowietrzna linia energetyczna', 'ćwiczenie gimnastyczne', 'proteza stomatologiczna', 'nadbudówka na statku'),
(22, 'Który to frazeologizm oznaczający zimną krew?', 14, 'chiński śluz', 'hiszpańska plwocina', 'polska żółć', 'angielska flegma'),
(23, 'Gdzie najprędzej znajdziemy klawiaturę typu AZERTY?', 13, 'w Chinach', 'w Australii', 'we Francji', 'w Argentynie'),
(24, 'Jedna ze sztuk Williama Szekspira to:', 11, '„Miarka za miarkę”', '„Miarka się przebrała”', '„Miarka do miarki”', '„Miarka w miarkę”'),
(25, 'Rozrusznik nożny motocykla popularnie nazywany jest:', 11, 'kopniakiem', 'kuksańcem', 'sójką', 'szturchańcem'),
(26, 'Czego nie mają koty rasy manx?', 13, 'uszu', 'pazurów', 'ogona', 'pigmentu'),
(27, 'Dochrapać się to:', 13, 'niewiele wskórać', 'porządnie się wyspać', 'coś osiągnąć', 'chybić celu'),
(28, 'Czyje młode w gwarze myśliwskiej nazywane są pasiakami?', 12, 'lisa', 'dzika', 'łosia', 'bobra'),
(29, '„Uwaga, grupa! Kierunek – wschód! Tam musi być jakaś cywilizacja”. Z którego to filmu?', 11, '\"Seksmisja\"', '„Miś”', '„Kingsajz”', '\"Rejs\"'),
(30, 'Chasydom tradycja nakazuje pobierać się pod chupą, czyli:', 14, 'pod czarnym parasolem', 'pod wiązką jemioły', 'pod wiązką jemioły', 'pod baldachimem'),
(31, 'Kto wjechał na górę fasiągiem, dostał się tam:', 11, 'końskim zaprzęgiem', 'wyciągiem krzesełkowym', 'końskim zaprzęgiem', 'wyciągiem orczykowym'),
(32, 'Co zawiera ooteka?', 13, 'kolekcję skamielin', 'bogaty księgozbiór', 'pakiet jaj', 'dźwiękowe sample'),
(33, 'Kto łapał raki w palindromie?', 14, 'Dedal', 'Rakarz', 'Kot', 'Ikar'),
(34, 'W trakcie obłóczyn:', 14, 'chorzy przyjmują sakrament', 'krochmali się pościel', 'panna młoda rzuca welonem', 'klerycy przywdziewają sutanny'),
(35, 'Znajdź błąd:', 12, 'na przełaj', 'na przeciw', 'na przemian', 'na przekór'),
(36, 'Wieże, której budowli wieńczą różnokolorowe cebulaste kopuły?', 11, 'cerkwi Wasyla Błogosławionego', 'katedry Notre Dame', 'mauzoleum Tadż Mahal', 'zamku na Wawelu'),
(37, 'Demi-glace to:', 12, 'półmrozek', 'sos pieczeniowy', 'kieliszeczki do likieru', 'półmrozek'),
(38, 'Barokowe, bogato zdobione meble, wśród których najlepiej znane są masywne drewniane szafy, to tak zwane meble:', 12, 'warszawskie', 'gdańskie', 'krakowskie', 'lubelskie'),
(39, 'Brytyjski bankier, polityk i zoolog Walter Rothschild szokował londyńczyków, powożąc zaprzęgiem złożonym:', 14, 'z żółwi', 'z hipopotamów', 'z tygrysów szablo zębnych', 'z zebr'),
(40, 'Czyje to słowa: „Pon se ino serce ziębi tym myśleniem, sumowaniem: boby się pon usroł na niem”?', 13, 'Jana Kochanowskiego', 'Witolda Gombrowicza', 'Stanisława Wyspiańskiego', 'Witkacego');

--
-- Indeksy dla zrzutów tabel
--

--
-- Indeksy dla tabeli `pytania_do_pracy`
--
ALTER TABLE `pytania_do_pracy`
  ADD PRIMARY KEY (`numeracja`);

--
-- AUTO_INCREMENT dla zrzuconych tabel
--

--
-- AUTO_INCREMENT dla tabeli `pytania_do_pracy`
--
ALTER TABLE `pytania_do_pracy`
  MODIFY `numeracja` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=41;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
