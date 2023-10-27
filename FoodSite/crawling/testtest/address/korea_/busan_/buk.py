from address import City

class Buk(City):
    def __init__(self) -> None:
        args = ['북구']
        sub_citys = [
            ['구포동', '구포1동', '구포2동', '구포3동',],
            ['금곡동',],
            ['덕천동', '덕천1동', '덕천2동', '덕천3동',],
            ['만덕동', '만덕1동', '만덕2동', '만덕3동',],
            ['화명동', '화명1동', '화명2동', '화명3동',],
        ]
        
        super().__init__(*args)

        for sub_city in sub_citys:
            self.subclass.append(City(*sub_city))