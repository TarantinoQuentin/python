floppy_disc_capacity_megabytes = 1.44
pages_per_book = 100
strings_per_page = 50
chars_per_string = 25
char_volume_bytes = 4

book_volume_bytes = pages_per_book * strings_per_page * chars_per_string * char_volume_bytes
book_volume_megabytes = (book_volume_bytes / 1024) / 1024

books_per_floppy_disc = int(floppy_disc_capacity_megabytes // book_volume_megabytes)

print("Количество книг, помещающихся на дискету:", books_per_floppy_disc)
