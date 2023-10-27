from address import City

class Yeongdo(City):
    def __init__(self) -> None:
        args = ["영도구"]
        sub_citys = [
            ['남항동', '남항동1가', '남항동2가', '남항동3가', '대교동1가', '대교동2가', '대평동1가', '대평동2가'], 
            ['영선동', '영선1동', '영선동1가', '영선동2가'], 
            ['영선2동', '영선동3가', '영선동4가'], 
            ['신선동', '신선동1가', '신선동2가', '신선동3가'], 
            ['봉래동', '봉래1동', '봉래동1가', '봉래동2가', '봉래동3가'], 
            ['봉래2동', '봉래동4가', '봉래동5가'], 
            ['청학1동', '청학2동', '청학동'], 
            ['동삼1동', '동삼2동', '동삼3동', '동삼동'], 
        ]
        
        super().__init__(*args)

        for sub_city in sub_citys:
            self.subclass.append(City(*sub_city))