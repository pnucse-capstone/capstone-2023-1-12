from address import City

class Sasang(City):
    def __init__(self) -> None:
        args = ["사상구"]
        sub_citys = [
            ['감전동',],
            ['괘법동',],
            ['덕포동', '덕포1동', '덕포2동',],
            ['모라동', '모라1동', '모라3동',],
            ['삼락동',],
            ['엄궁동',],
            ['주례동', '주례1동', '주례2동', '주례3동',],
            ['학장동',],
        ]
        
        super().__init__(*args)

        for sub_city in sub_citys:
            self.subclass.append(City(*sub_city))