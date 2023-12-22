
class jogador():

    def __init__(self, nome=None, num_pontos=None):
        self.nome = nome
        self.pontos = num_pontos
    
    def clacular_pontos(self,nome, resultado):
        pontos = 0
        if resultado.upper() == 'V':
            pontos += 3
        
        elif resultado.upper() == 'E':
            pontos += 1
        
        return jogador(nome, pontos)

j1 = jogador().clacular_pontos('victor','v')
print(j1.nome, j1.pontos)


# Criar um método de classe

class jogador():

    def __init__(self, nome=None, num_pontos=None):
        self.nome = nome
        self.pontos = num_pontos
    
    # Vai criar um método da classe, evitando uma instanciamento repetido
    @classmethod
    def clacular_pontos(self,nome, resultado):
        pontos = 0
        if resultado.upper() == 'V':
            pontos += 3
        
        elif resultado.upper() == 'E':
            pontos += 1
        
        return jogador(nome, pontos)



j1 = jogador.clacular_pontos('victor','v')
print(j1.nome, j1.pontos)



# Criar método estático
class jogador():

    def __init__(self, nome=None, num_pontos=None):
        self.nome = nome
        self.pontos = num_pontos
    
    # Criar método de classe
    @classmethod
    def clacular_pontos(self,nome, resultado):
        pontos = 0
        if resultado.upper() == 'V':
            pontos += 3
        
        elif resultado.upper() == 'E':
            pontos += 1
        
        return jogador(nome, pontos)

    #Criar método estático
    @staticmethod
    def analisar_vitoria(pontuacao):
        return 'Vitoria' if pontuacao > 50 else 'Derrota'


j1 = jogador().clacular_pontos('victor','v')
print(j1.nome, j1.pontos)
print(j1.analisar_vitoria(60))