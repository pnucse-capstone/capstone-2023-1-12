from address import City

class Saha(City):
    def __init__(self) -> None:
        args = ["사하구"]
        sub_citys = [
            ['감천동', '감천1동', '감천2동',], 
            ['괴정동', '괴정1동', '괴정2동', '괴정3동', '괴정4동',], 
            ['구평동',], 
            ['다대동', '다대1동', '다대2동',], 
            ['당리동',], 
            ['신평동', '신평1동', '신평2동',], 
            ['장림동', '장림1동', '장림2동',], 
            ['하단동', '하단1동', '하단2동',], 
        ]
        
        super().__init__(*args)

        for sub_city in sub_citys:
            self.subclass.append(City(*sub_city))