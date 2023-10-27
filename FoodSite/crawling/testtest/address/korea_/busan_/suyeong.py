from address import City

class Suyeong(City):
    def __init__(self) -> None:
        args = ["수영구"]
        sub_citys = [
            ['광안동', '광안1동', '광안2동', '광안3동', '광안4동',],
            ['남천동', '남천1동', '남천2동',],
            ['망미동', '망미1동', '망미2동',],
            ['민락동',],
            ['수영동',],
        ]
        
        super().__init__(*args)

        for sub_city in sub_citys:
            self.subclass.append(City(*sub_city))