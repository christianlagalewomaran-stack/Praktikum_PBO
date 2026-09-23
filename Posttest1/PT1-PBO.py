class Hunter:
    jumlah_hunter = 0

    def __init__(self, nama, role, level):
        self.nama = nama
        self.role = role
        self.__level = level
        Hunter.jumlah_hunter += 1

    @property
    def level(self):
        return self.__level

    @level.setter
    def level(self, level):
        if level < 1:
            raise ValueError("Level tidak boleh kurang dari 1.")
        self.__level = level

    def tampilkan_hunter(self):
        print("Nama  :", self.nama)
        print("Role  :", self.role)
        print("Level :", self.level)

    @classmethod
    def jumlah_data(cls):
        return cls.jumlah_hunter           

    @staticmethod
    def cek_level(level):
        return level >= 1


class Monster:
    jumlah_monster = 0

    def __init__(self, nama, rarity, tingkat_bahaya):
        self.nama = nama
        self.rarity = rarity
        self.__tingkat_bahaya = tingkat_bahaya
        Monster.jumlah_monster += 1

    @property
    def tingkat_bahaya(self):
        return self.__tingkat_bahaya

    @tingkat_bahaya.setter
    def tingkat_bahaya(self, tingkat):
        if tingkat < 1:
            raise ValueError("Tingkat bahaya minimal 1.")
        self.__tingkat_bahaya = tingkat

    def tampilkan_monster(self):
        print("Nama Monster :", self.nama)
        print("Rarity         :", self.rarity)
        print("Bahaya       :", self.tingkat_bahaya)

    @classmethod
    def jumlah_data(cls):
        return cls.jumlah_monster

    @staticmethod
    def cek_bahaya(tingkat):
        return tingkat <= 2


class HuntingArea:
    jumlah_area = 0

    def __init__(self, nama, keadaan, tingkat_bahaya):
        self.nama = nama
        self.keadaan = keadaan
        self.__tingkat_bahaya = tingkat_bahaya
        HuntingArea.jumlah_area += 1

    @property
    def tingkat_bahaya(self):
        return self.__tingkat_bahaya

    @tingkat_bahaya.setter
    def tingkat_bahaya(self, tingkat):
        if tingkat < 1:
            raise ValueError("Tingkat bahaya minimal 1.")
        self.__tingkat_bahaya = tingkat

    def tampilkan_area(self):
        print("Area          :", self.nama)
        print("Keadaan         :", self.keadaan)
        print("Tingkat Bahaya:", self.tingkat_bahaya)

    @classmethod
    def jumlah_data(cls):
        return cls.jumlah_area

    @staticmethod
    def cek_area(tingkat):
        return tingkat <= 1



print("===}> PERSIAPAN MONSTER HUNTING <{===\n")


hunter1 = Hunter("ragnvindr", "Warrior", 10)
hunter2 = Hunter("Gunnhildr", "Healer", 7)

print("| Hunter 1 |")
hunter1.tampilkan_hunter()

print("\n| Hunter 2 |")
hunter2.tampilkan_hunter()

print("\nJumlah Hunter:", Hunter.jumlah_data())

print("Hunter 1 bisa menjelajahi area dasar:",
    Hunter.cek_level(hunter1.level))


monster1 = Monster("Thamuz", "Epic", 3)
monster2 = Monster("Small skeleton dragon", "basic", 1)

print("\n| Monster 1 |")
monster1.tampilkan_monster()

print("\n| Monster 2 |")
monster2.tampilkan_monster()

print("\nJumlah Monster:", Monster.jumlah_data())

print("Monster 1 aman untuk pemula:",
    Monster.cek_bahaya(monster1.tingkat_bahaya))


area1 = HuntingArea("Ancient desert valley", "badai pasir", 3)
area2 = HuntingArea("Dragon hill", "normal", 5)

print("\n| Area 1 |")
area1.tampilkan_area()

print("\n| Area 2 |")
area2.tampilkan_area()

print("\nJumlah Area:", HuntingArea.jumlah_data())

print("Area 1 terbuka untuk pemula:",
    HuntingArea.cek_area(area1.tingkat_bahaya))


print("\n!!!--PENGUJIAN SETTER--!!!")

hunter1.level = 12
print("Level Hunter setelah diubah:", hunter1.level)

try:
    hunter1.level = 0
except ValueError as e:
    print("Error:", e)

monster1.tingkat_bahaya = 5
print("Bahaya Monster setelah diubah:",
    monster1.tingkat_bahaya)

try:
    monster1.tingkat_bahaya = 0
except ValueError as e:
    print("Error:", e)

area1.tingkat_bahaya = 2
print("Bahaya Area setelah diubah:",
    area1.tingkat_bahaya)

try:
    area1.tingkat_bahaya = 0
except ValueError as e:
    print("Error:", e)