from print_lol import print_lol

movies = ["The holy Grail", "The Life of Brian", "The Meaning of Life"]

count = 1
for year in (1975, 1979, 1983):
    movies.insert(count, year)
    count += 2

movies.extend(['Mount Tai',['TaiShan',['ZhenNi', 'Gorila']]])

print_lol(movies)
