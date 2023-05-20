games = [
'962 387 270 Joe Robles Alania',
'962 387 269 Guadalupe Martinez',
'976 331 340 Joe Robles',
'976 331 340 Roxana Robles',
'969 334 755 Robert Robles',
'969 334 755 Loana Robles',
'969 334 755 Damaris Robles',
'969 334 756 Geraldine Huamaní',
'914 068 043 Medlly Santolalla',
'980 914 278 Ronald Robles',
'969 334 754 Daniel Robles',
'969 334 754 Josué Robles',
'969 334 754 David Robles',
'969 334 753 Pamela Enciso',
'917 053 761 Tim Robles',
'999 028 838 Nemesio Torres',
'997 856 570 Yolanda Robles',
'962 808 146 Charo Torres',
'964 895 077 Tulio Rojas',
'933 581 651 Aaron Gallego Torres',
'932 960 958 Sharom Gallegos Torres',
'987 760 358 Edwin Torres',
'987 760 358 Edwin Torres Jr.',
'Rodrigo Robles',
'999 908 958 Maritza Verástegui',
'976 392 673 Andrea Robles Verástegui',
'972 154 029 Mari Robles Verástegui',
'918 652 488 Rita Paola Robles',
'993 295 174 Raquel Robles Alania',
'963 903 522 Gladys Robles Alania',
'950 171 007 Jimmy Shreiber Robles',
'950 171 007 Valery',
'950 171 007',
'991 151 300 Melisa Arias',
'968 088 764 Tefy Shreiber Robles',
'942 585 778 Favio Shreiber',
'991 905 390 Meche',
'991 337 348 Fiorela Shreiber',
'915 366 940 Mimba Robles',
'952 314 418 Clarita Robles',
'986 956 243 Antonio Capcha Hija',
'929 590 957 Li Alania',
'931 695 295 Leopoldo Reyes',
'950 171 776 Lupe Enciso',
'950 171 776 Francesca',
'956 903 329 Christian Reyes Enciso',
'956 903 329 Eli',
'937 445 986  Zosimo Quilca',
'966 282 885 Lloyser Chuquisuta',
'935 425 502 Hermana Mariluna Condori Cáceres',
'959 657 237 Walter Condori Cáceres',
'998 524 388 Irene de Condori',
'963 528 256',
'996 530 024 Tco Mamani, amigo de Walter C.',
'962 387 274 José Antón',
'963 725 044 Melsi Ramirez',
'946 983 508 Don Ramón',
'948 568 424 Alfredo Huaman Rojas',
'990 084 880 Yairis García',
'952 152 603 Karollay',
'952 152 603 Noelis',
'952 152 603 Amanda',
'952 152 603 José',
'952 152 603 Dalia',
'952 152 603 Yohendris',
'998 825 623 Virginia',
'998 825 623 Liam',
'964 543 151 Vicky',
'964 543 151 Jossmel',
'964 543 151 Samantha',
'974 156 690 Juan Carlos Torres',
'976 116 903 Zenón Mallqui',
'976 320 921 Mel',
'981 222 863 Yani',
'981 222 863 Mamá',
'979 743 674 Yane',
'983 848 395',
'980 270 683 David Carhuancho',
'980 270 683 Angely',
'980 270 683 David Fabricio',
'967 699 316 Hermana Pamela',
'987 806 555 Paola Mendival Laura',
'916 647 076 Ana Martel Ventosilla',
'965 342 595 Carmen Gonzales',
'969 999 623 Lucho Vila',
'993 309 270 Elizabet Llanos',
'999 080 198 Elva Romero',
'962 968 662 Hubertina Ferrer',
'987 806 232 Jovita',
'964 106 065 María Vera Picoy',
'961 647 358 Nancy',
'945 468 425 Susy Gomez',
'927 827 290 Jose Carlos Rojas',
'956 635 114 Alfredo Taype',
'964 772 350 Gladys Riofano Linares',
'955 363 657 Jesús Porras hijo de Gladys Riofano',
'972 838 775 Hermana Yenny',
'935 262 491 Yenny Saldaña',
'936 711 214 Maria Cajo',
'985 182 379 Santoc Cajo',
'963 525 941 Bachy',
'963 528 256 Ignacio',
'969 274 847 Juan Ballena',
'999 512 184 Juan Chafloque',
'980 136 664 Marilú Chavesta Tia de Chafloque',
'949 364 215 Marco Anton',
'992 057 986 Willy Alanya',
'922 691 565 Alejandro Tisa',
'925 194 211',
'930 241 184 Erica',
'936 764 731 Norbis',
'941 404 089 Mica',
'944 408 845 Edwin',
'947 634 002 Melanie',
'948 756 180 Ofelia Sanchez',
'991 762 171 Evelin',
'921 501 678',
'942 355 007 Karina',
'942 355 007 Jake'
]

for g in sorted(games, key=(lambda x: x)):
    nombre = g.replace(' ', '%20')
    print(f'<a href="https://storage.googleapis.com/iglesia/bingo/{nombre}.pdf">{g}</a><br>')
