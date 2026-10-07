class Hunter:
    jumlah_hunter_dibuat = 0

    def __init__(self, nama, level):
        self._nama = nama
        self.__level = level
        self._equipment = []

        Hunter.jumlah_hunter_dibuat += 1

    @property
    def nama(self):
        return self._nama

    @property
    def level(self):
        return self.__level

    @level.setter
    def level(self, level):
        if level < 1:
            raise ValueError("Level tidak boleh kurang dari 1.")

        self.__level = level

    def tampilkan_hunter(self):
        print("Nama  :", self._nama)
        print("Level :", self.level)

    def berburu(self, area):
        print(
            f"\n{self._nama} mulai berburu "
            f"di {area.nama}."
        )

        area.periksa_area(self)

    def tambah_equipment(self, equipment):
        self._equipment.append(equipment)

        print(
            f"{equipment.nama} ditambahkan "
            f"ke {self._nama}."
        )

    def keluarkan_equipment(self, equipment):
        if equipment in self._equipment:
            self._equipment.remove(equipment)

            print(
                f"{equipment.nama} dikeluarkan "
                f"dari {self._nama}."
            )

    def tampilkan_equipment(self):
        print(f"\nEquipment {self._nama}:")

        for equipment in self._equipment:
            print("-", equipment)

    @classmethod
    def jumlah_data(cls):
        return cls.jumlah_hunter_dibuat

    @staticmethod
    def cek_level(level):
        return level >= 1


class Warrior(Hunter):
    def __init__(self, nama, level, senjata):
        super().__init__(nama, level)
        self.senjata = senjata

    def tampilkan_hunter(self):
        print("Nama    :", self._nama)
        print("Role    : Warrior")
        print("Level   :", self.level)
        print("Senjata :", self.senjata)

    def serang(self):
        print(
            f"{self._nama} menyerang monster "
            f"dengan {self.senjata}."
        )


class Healer(Hunter):
    def __init__(self, nama, level, tipe_healing):
        super().__init__(nama, level)
        self.tipe_healing = tipe_healing

    def tampilkan_hunter(self):
        print("Nama         :", self._nama)
        print("Role         : Healer")
        print("Level        :", self.level)
        print("Tipe Healing :", self.tipe_healing)

    def menyembuhkan(self):
        print(
            f"{self._nama} menggunakan "
            f"{self.tipe_healing}."
        )


class Equipment:
    def __init__(self, nama, jenis):
        self.nama = nama
        self.jenis = jenis

    def __str__(self):
        return f"{self.nama} ({self.jenis})"

    def tampilkan_equipment(self):
        print("Equipment :", self.nama)
        print("Jenis     :", self.jenis)


class Monster:
    def __init__(self, nama, rarity, tingkat_bahaya):
        self.nama = nama
        self.rarity = rarity
        self.__tingkat_bahaya = tingkat_bahaya

    @property
    def tingkat_bahaya(self):
        return self.__tingkat_bahaya

    @tingkat_bahaya.setter
    def tingkat_bahaya(self, tingkat):
        if tingkat < 1:
            raise ValueError(
                "Tingkat bahaya minimal 1."
            )

        self.__tingkat_bahaya = tingkat

    def tampilkan_monster(self):
        print("Nama Monster :", self.nama)
        print("Rarity       :", self.rarity)
        print("Bahaya       :", self.tingkat_bahaya)

    @staticmethod
    def cek_bahaya(tingkat):
        return tingkat <= 2


class HuntingArea:
    jumlah_area_dibuat = 0

    def __init__(self, nama, keadaan, tingkat_bahaya):
        self.nama = nama
        self.keadaan = keadaan
        self.__tingkat_bahaya = tingkat_bahaya
        self._monster = []

        HuntingArea.jumlah_area_dibuat += 1

        self._buat_monster()

    @property
    def tingkat_bahaya(self):
        return self.__tingkat_bahaya

    @tingkat_bahaya.setter
    def tingkat_bahaya(self, tingkat):
        if tingkat < 1:
            raise ValueError(
                "Tingkat bahaya minimal 1."
            )

        self.__tingkat_bahaya = tingkat

    def _buat_monster(self):
        monster = Monster(
            "Monster Penjaga",
            "Basic",
            self.tingkat_bahaya
        )

        self._monster.append(monster)

    def ambil_monster(self):
        return self._monster[0]

    def tampilkan_monster(self):
        print("\nMonster di area:")

        for monster in self._monster:
            monster.tampilkan_monster()

    def periksa_area(self, hunter):
        print(
            f"[Area] {hunter.nama} berada "
            f"di {self.nama}."
        )

        if hunter.level >= self.tingkat_bahaya:
            print(
                "[Area] Hunter cukup kuat "
                "untuk area ini."
            )
        else:
            print(
                "[Area] Hunter terlalu lemah "
                "untuk area ini."
            )

    def tampilkan_area(self):
        print("Area           :", self.nama)
        print("Keadaan        :", self.keadaan)
        print(
            "Tingkat Bahaya :",
            self.tingkat_bahaya
        )

    @classmethod
    def jumlah_data(cls):
        return cls.jumlah_area_dibuat

    @staticmethod
    def cek_area(tingkat):
        return tingkat <= 1


print("===}> PERSIAPAN MONSTER HUNTING <{===\n")

warrior = Warrior(
    "Ragnvindr",
    10,
    "Great Sword"
)

healer = Healer(
    "Gunnhildr",
    7,
    "Holy Staff"
)

print("INHERITANCE")

print("\nWarrior")
warrior.tampilkan_hunter()

print("\nHealer")
healer.tampilkan_hunter()

print("\nCek instance():")

print(
    "warrior adalah Hunter:",
    isinstance(warrior, Hunter)
)

print(
    "warrior adalah Warrior:",
    isinstance(warrior, Warrior)
)

print(
    "healer adalah Hunter:",
    isinstance(healer, Hunter)
)

print(
    "healer adalah Healer:",
    isinstance(healer, Healer)
)

print("\nCek subclass():")

print(
    "Warrior subclass Hunter:",
    issubclass(Warrior, Hunter)
)

print(
    "Healer subclass Hunter:",
    issubclass(Healer, Hunter)
)

print("\nMETHOD KHUSUS SUBCLASS")

warrior.serang()
healer.menyembuhkan()

print("\nCLASS METHOD & STATIC METHOD")

print(
    "Jumlah Hunter dibuat:",
    Hunter.jumlah_data()
)

print(
    "Level Warrior valid:",
    Hunter.cek_level(warrior.level)
)

print("\nAGGREGATION HUNTER - EQUIPMENT")

sword = Equipment(
    "Great Sword",
    "Senjata"
)

staff = Equipment(
    "Holy Staff",
    "Senjata"
)

warrior.tambah_equipment(sword)
healer.tambah_equipment(staff)

warrior.tampilkan_equipment()
healer.tampilkan_equipment()

print("\nPENGUJIAN AGGREGATION")

print("Equipment sebelum Hunter dihapus:")

sword.tampilkan_equipment()

del warrior

print("\nWarrior sudah dihapus.")

print(
    "Equipment masih dapat digunakan:"
)

sword.tampilkan_equipment()

print("\nHUNTING AREA")

area1 = HuntingArea(
    "Ancient Desert Valley",
    "Badai pasir",
    3
)

area2 = HuntingArea(
    "Dragon Hill",
    "Normal",
    5
)

print("\nArea 1")
area1.tampilkan_area()

print("\nArea 2")
area2.tampilkan_area()

print(
    "\nJumlah Area dibuat:",
    HuntingArea.jumlah_data()
)

print("\nCOMPOSITION HUNTING AREA - MONSTER")

print(
    "Monster dibuat otomatis "
    "ketika HuntingArea dibuat."
)

print("\nMonster di Area 1:")
area1.tampilkan_monster()

print("\nMonster di Area 2:")
area2.tampilkan_monster()

print("\nASSOCIATION HUNTER - HUNTING AREA")

hunter1 = Warrior(
    "Ragnvindr",
    10,
    "Great Sword"
)

hunter2 = Healer(
    "Gunnhildr",
    7,
    "Holy Staff"
)

hunter1.berburu(area1)
hunter2.berburu(area2)

print("\nHunter lain menggunakan area yang sama:")

hunter2.berburu(area1)

print("\nPENGUJIAN SETTER HUNTER")

hunter1.level = 12

print(
    "Level Hunter setelah diubah:",
    hunter1.level
)

try:
    hunter1.level = 0

except ValueError as e:
    print("Error:", e)

print("\nPENGUJIAN SETTER AREA")

area1.tingkat_bahaya = 2

print(
    "Bahaya Area setelah diubah:",
    area1.tingkat_bahaya
)

try:
    area1.tingkat_bahaya = 0

except ValueError as e:
    print("Error:", e)

print("\nPENGUJIAN SETTER MONSTER")

monster_area1 = area1.ambil_monster()

monster_area1.tingkat_bahaya = 4

print(
    "Bahaya Monster setelah diubah:",
    monster_area1.tingkat_bahaya
)

try:
    monster_area1.tingkat_bahaya = 0

except ValueError as e:
    print("Error:", e)