
class vertebrados():
    def __init__(self, num_patas, simetria, coluna_vertebral):
        self.num_patas = num_patas
        self.simetria = simetria
        self.col_vertebral = coluna_vertebral
    
    def definicao(self):
        return f"{vertebrados.__class__.__name__} são animais que possuem o sistema nervoso composto poruma coluna vertebral!"



class mamifero(vertebrados):
    def __init__(self, pelos=True, **kw):       # **kw - k_args, usado para guardar todos os atributos em um dicionário
        super().__init__(**kw)                  # Usamos para passar atributos de mais de uma classe pai para uma única classe-filha
        self.pelos = pelos
    
    def definicao(self):
        return super().definicao() + f"\nOs mamíferos possuem pelos cobrindo o corpo e glandulas mamárias"



class aves(vertebrados):
    def __init__(self, penas=True, ovo=True, **kw):
        super().__init__(**kw)
        self.penas = penas
        self.ovo = ovo
    
    def definicao(self):
        return super().definicao() + f"\nAves possuem penas cobrindo seu corpo e botam ovos!"
    
    def botar_ovo(self):
        if self.ovo:
            print('Esse animal bota ovo!')

        

class ornitorrinco(aves, mamifero):
    def info(self):
        return ornitorrinco.__mro__

Ornitorrinco = ornitorrinco(num_patas=4, simetria='Bilateral', coluna_vertebral=True,penas=False, ovo=True, pelos=True)

print(Ornitorrinco.pelos)
print(Ornitorrinco.botar_ovo())
print(Ornitorrinco.definicao())
print(Ornitorrinco.info())