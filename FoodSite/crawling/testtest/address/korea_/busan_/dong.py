from address import City

class Dong(City):
    def __init__(self) -> None:
        args = ["동구"]
        sub_citys = [
            ['초량동', '초량1동', '초량2동', '초량3동', '초량6동'],
            ['수정동', '수정1동', '수정2동', '수정4동', '수정5동'],
            ['범일동', '범일1동', '범일2동', '범일5동'],
            ['촤천동'],
        ]
        
        super().__init__(*args)

        for sub_city in sub_citys:
            self.subclass.append(City(*sub_city))