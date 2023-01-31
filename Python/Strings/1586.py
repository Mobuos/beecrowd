# Problema 1586 - Beecrowd - Strings - Nível 8

# Vamos montar uma função para calcular a força padrão
def forca(nome):
    forca = 0
    for letra in nome:
        forca += ord(letra)
    
    return forca

def procuraEmpate(N):
    # Recebendo todos os estudantes e calculando suas forças
    estudantes = []
    for _ in range(N):
        estudante = input()
        estudantes.append((estudante, forca(estudante)))

    # For com a posição absoluta do estudante escolhido
    # E o nome dele
    # Unpack de (posição, (nome, forca)) retornado pelo enumerate
    bMin = 0
    bMax = N
    while bMin < bMax:
        i = (bMax - bMin)//2 + bMin
        escolhido = estudantes[i][0]
        # Cada for interno calcula somente a força total
        # da sua equipe em relação ao estudante escolhido

        # Fator é a distância entre as posições na lista
        # <---//------>
        # 2 1 0 // 1 2
        # A parte esquerda somamos 1 para ficar do jeito que
        # queremos
        # <-----//---->
        # 3 2 1 // 1 2
        equipeA = 0
        for j in range(i+1):
            fator = (abs(i - j)) + 1 # +1 pois queremos um mínimo de 1
            equipeA += fator * estudantes[j][1] # Pegando a força pré-calculada

        equipeB = 0
        for j in range(i+1,N):
            fator = abs(i - j) # Sem +1 pois i é exclusivo aqui
            equipeB += fator * estudantes[j][1] # Pegando a força pré-calculada
        
        if equipeA == equipeB:
            print(escolhido)
            return True
        elif equipeA < equipeB:
            bMin = i+1
        else:
            bMax = i

    # No caso de não encontrar nada a função retorna que não encontrou
    return False

## Loop de casos de teste
N = int(input())
while (N != 0):
    if not procuraEmpate(N):
        print("Impossibilidade de Empate.")
    N = int(input())