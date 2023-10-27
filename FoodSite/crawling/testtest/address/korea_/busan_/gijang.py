from address import City

class Gijang(City):
    def __init__(self) -> None:
        args = ["기장군"]
        sub_citys = [
            ['기장읍'],
            ['장안읍'],
            ['정관읍'],
            ['일광읍'],
            ['철마면'],
        ]
        
        super().__init__(*args)

        for sub_city in sub_citys:
            self.subclass.append(City(*sub_city))