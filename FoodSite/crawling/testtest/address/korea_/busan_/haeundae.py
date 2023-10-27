from address import City

class Haeundae(City):
    def __init__(self) -> None:
        args = ["해운대구"]
        sub_citys = [
            ['반송1동', '반송2동', '반송동', '석대동',],
            ['반여1동', '반여2동', '반여3동', '반여4동', '반여동',],
            ['송정동',],
            ['우1동', '우2동', '우3동', '우동',],
            ['좌1동', '좌2동', '좌3동', '좌4동', '좌동',],
            ['중1동', '중2동', '중동',],
            ['재송1동', '재송2동', '재송동',],
        ]
        
        super().__init__(*args)

        for sub_city in sub_citys:
            self.subclass.append(City(*sub_city))