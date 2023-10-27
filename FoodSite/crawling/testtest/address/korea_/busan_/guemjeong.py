from address import City

class Guemjeong(City):
    def __init__(self) -> None:
        args = ["금정구"]
        sub_citys = [
            ["구서동", "구서1동", "구서2동"],
            ["금사회동동", "금사동", "회동동"],
            ["금성동"],
            ["남산동"],
            ["부곡동", "부곡1동", "부곡2동", "부곡3동", "부곡4동", "오륜동"],
            ["서1동", "서2동", "서3동", "서동"],
            ["장전동"],
            ["청룡노포동", "청룡동", "노포동"],
        ]
        
        super().__init__(*args)

        for sub_city in sub_citys:
            self.subclass.append(City(*sub_city))