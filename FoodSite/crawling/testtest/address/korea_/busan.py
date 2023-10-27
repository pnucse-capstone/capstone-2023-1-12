from address import City

class Busan(City):
    def __init__(self) -> None:
        args = ["부산", "부산시", "부산광역시"]
        super().__init__(*args)

        from korea_.busan_.buk        import Buk
        from korea_.busan_.busanjin   import Busanjin
        from korea_.busan_.dong       import Dong
        from korea_.busan_.dongnae    import Dongnae
        from korea_.busan_.gangseo    import Gangseo
        from korea_.busan_.gijang     import Gijang
        from korea_.busan_.guemjeong  import Guemjeong
        from korea_.busan_.haeundae   import Haeundae
        from korea_.busan_.jung       import Jung
        from korea_.busan_.nam        import Nam
        from korea_.busan_.saha       import Saha
        from korea_.busan_.sasang     import Sasang
        from korea_.busan_.seo        import Seo
        from korea_.busan_.suyeong    import Suyeong
        from korea_.busan_.yeongdo    import Yeongdo
        from korea_.busan_.yeonje     import Yeonje

        sub_citys = [
            Buk(),      Busanjin(), Dong(),         Dongnae(), 
            Gangseo(),  Gijang(),   Guemjeong(),    Haeundae(), 
            Jung(),     Nam(),      Saha(),         Sasang(), 
            Seo(),      Suyeong(),  Yeongdo(),      Yeonje(),
        ]

        for sub_city in sub_citys:
            self.subclass.append(sub_city)