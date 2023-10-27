from address import City

class Busanjin(City):
    def __init__(self) -> None:
        args = ["부산진구"]
        sub_citys = [
            ['부전1동', '범전동',],
            ['부전2동', '부전동',],
            ['연지동',],
            ['초읍동',],
            ['양정1동', '양정2동', '양정동',],
            ['전포1동', '전포2동', '전포동',],
            ['부암1동', '부암3동', '부암동',],
            ['당감1동', '당감2동', '당감4동', '당감동',],
            ['가야1동', '가야2동', '가야동',],
            ['개금1동', '개금2동', '개금3동', '개금동',],
            ['범천1동', '범천2동', '범천동',],
        ]
        
        super().__init__(*args)

        for sub_city in sub_citys:
            self.subclass.append(City(*sub_city))