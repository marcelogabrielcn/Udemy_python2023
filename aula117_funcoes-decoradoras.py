class MyReprMixin:
    def __repr__(self) -> str:
        class_name = self.__class__.__name__
        class_dict = self.__dict__
        class_repr = f'{class_name}({class_dict})'
        return class_repr
    

class Time(MyReprMixin):
    def __init__(self, nome):
        self.nome = nome
    

class Planeta(MyReprMixin):
    def __init__(self, nome):
        self.nome = nome


brasil = Time('Brasil')
espanha = Time('Espanha')

saturno = Planeta('Saturn')
netuno = Planeta('Neptune')

print(brasil)
print(espanha)
print(saturno)
print(netuno)
