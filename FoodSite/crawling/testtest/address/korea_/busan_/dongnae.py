from address import City

class Dongnae(City):
    def __init__(self) -> None:
        args = ["동래구"]
        sub_citys = [
            ['명륜동',],
            ['명장1동', '명장2동', '명장동',],
            ['복산동', '복천동', '칠산동',],
            ['사직1동', '사직2동', '사직3동', '사직동',],
            ['수민동', '수안동', '낙민동',],
            ['안락1동', '안락2동', '안락동',],
            ['온천1동', '온천2동', '온천3동', '온천동',],
        ]
        
        super().__init__(*args)

        for sub_city in sub_citys:
            self.subclass.append(City(*sub_city))