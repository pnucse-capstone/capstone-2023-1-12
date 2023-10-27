from address import City

class Gangseo(City):
    def __init__(self) -> None:
        args = ["강서구"]
        sub_citys = [
            ['대저동', '대저1동',],
            ['대저2동',],
            ['강동동',],
            ['명지1동', '명지2동', '명지동',],
            ['가락동', '봉림동', '식만동', '죽동동', '죽림동',],
            ['녹산동', '구랑동', '미음동', '범방동', '생곡동', '송정동', '신호동', '지사동', '화전동',],
            ['가덕도동', '놀차동', '대항동', '동선동', '성북동', '천성동',],
        ]
        
        super().__init__(*args)

        for sub_city in sub_citys:
            self.subclass.append(City(*sub_city))