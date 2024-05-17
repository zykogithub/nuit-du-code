class Fruit :
    def __init__(self) -> None:
        self.__mass : int = 100
    def __str__(self) -> str:
        return f"classe mère : {self.__mass}\n"
    def get_masse (self) :
        return self.__mass
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        pass
class Citron(Fruit) :
    def __init__(self) -> None:
        super().__init__()
        self.__mass = 200
    def __str__(self) -> str:
        return super().__str__() + f"classe fille : {self.__mass}"
if __name__ == "__main__" :
    citron1 = Citron()
    print(citron1)
    print(citron1.__dict__)
        