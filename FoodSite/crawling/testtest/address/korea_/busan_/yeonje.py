from address import City

class Yeonje(City):
    def __init__(self) -> None:
        args = ["연제구"]
        sub_citys = [
            ['연산동', '연산1동', '연산2동', '연산3동', '연산4동', '연산5동', '연산6동', '연산8동', '연산9동',],
            ['거제동', '거제1동', '거제2동', '거제3동', '거제4동',],
        ]
        
        super().__init__(*args)

        for sub_city in sub_citys:
            self.subclass.append(City(*sub_city))