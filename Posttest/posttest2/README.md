# Pada Posttest 2 ini melanjutkan dari Posttest 1 kemarin akan ditambahkan beberapa konsep oop yang belum ditambahkan sebelumnya antara lain:

# Relasi UML
Asosiasi diterapkan pada hubungan antara Hunter dan HuntingArea. Hunter dapat menggunakan HuntingArea untuk berburu, 
tetapi keduanya tetap merupakan objek yang berdiri sendiri. Contohnya Hunter memanggil method berburu() dengan memberikan objek HuntingArea.

Agregasi diterapkan pada hubungan antara Hunter dan Equipment. Equipment dibuat secara terpisah dari Hunter, 
kemudian dapat ditambahkan ke Hunter. Jika objek Hunter dihapus, Equipment tetap dapat digunakan sehingga hubungan keduanya bersifat agregasi.

Komposisi diterapkan pada hubungan antara HuntingArea dan Monster. Monster dibuat secara otomatis ketika objek HuntingArea dibuat. 
Monster menjadi bagian dari HuntingArea karena pembuatannya dilakukan oleh HuntingArea.

# Inheritance
Inheritance diterapkan dengan membuat Hunter sebagai superclass dan Warrior serta Healer sebagai subclass. 
Warrior dan Healer mewarisi atribut dan method dari Hunter.

Subclass menggunakan super().init() untuk memanggil konstruktor milik Hunter. Selain itu, 
masing-masing subclass memiliki atribut khusus, yaitu senjata pada Warrior dan tipe_healing pada Healer.

Method tampilkan_hunter() pada Hunter juga di-override oleh Warrior dan Healer 
sehingga setiap subclass dapat menampilkan informasi sesuai dengan perannya masing-masing.

Pada tingkat akses, atribut _nama digunakan sebagai protected sehingga dapat digunakan oleh subclass. Sementara itu, 
__level pada Hunter dan __tingkat_bahaya pada Monster serta HuntingArea digunakan sebagai private untuk membatasi akses langsung terhadap data tersebut.
