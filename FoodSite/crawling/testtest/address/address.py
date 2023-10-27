import re


class City():
    def __init__(self, *args) -> None:
        self.name = []
        self.subclass = []
        self.setting_city(*args)

        self.datalist = []

    def setting_city(self, *args):
        self.name += args

    def sort_rule(self, s, cnt=0):
        if s in self.name:
            return cnt+1
        if s[-1] == "로": return 600
        for subclass in self.subclass:
            res = subclass.sort_rule(s, cnt+1)
            if res: return res
        return None

    def calculate(self, string='', want_class=[], except_class=[]):
        lines = string.split("\n")
        res = []
        res2 = []
        for line in lines:
            words = [re.sub(r'^\d+', '', ''.join(re.findall(r'[가-힣0-9\- ]', word))) for word in line.split()]
            value = 0
            for i in range(len(words)):
                value, _ = self.check(words[i:], want_class, except_class)
                if value >= 2: 
                    res.append(line)
                    res2.append(_)
                    break
        return '\n'.join(res), res2

    def check(self, words, want_class, except_class):
        if len(words) == 0:
            return 0, [""]
        if len(except_class) != 0 and type(self) in except_class:
            return 0, [""]
        if len(want_class) != 0   and type(self) not in want_class:
            return 0, [""]
        
        if type(self) in want_class:
            idx = want_class.index(type(self))
            want_class = want_class[:idx]+want_class[idx+1:]
        
        val = 0
        
        if words[0] in self.name:
            val = 1
        if len(self.subclass) == 0 and len(words[0]) > 0 and words[0][-1] in ['로', '길']: return 1, [words[0]]
        check_result = [subclass.check(words[val:], want_class, except_class) for subclass in self.subclass] + [(0, [""])]
        return val+max(map(lambda x: x[0], check_result)), ([words[0]] if val == 1 else []) + sorted(check_result, key=lambda x: -x[0])[0][1]

    # def insert(self, address_name, )


class Korea(City):
    def __init__(self) -> None:
        args = []
        super().__init__(*args)

        from korea_.busan import Busan
        self.subclass.append(Busan())