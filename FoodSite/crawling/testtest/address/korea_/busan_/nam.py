from address import City

class Nam(City):
    def __init__(self) -> None:
        args = ["남구"]
        sub_citys = [
            ['감만동', '감만1동', '감만2동',],
            ['대연동', '대연1동', '대연3동', '대연4동', '대연5동', '대연6동',],
            ['문현동', '문현1동', '문현2동', '문현3동', '문현4동',],
            ['용당동',],
            ['용호동', '용호1동', '용호2동', '용호3동', '용호4동',],
            ['우암동',],
        ]
        
        super().__init__(*args)

        for sub_city in sub_citys:
            self.subclass.append(City(*sub_city))