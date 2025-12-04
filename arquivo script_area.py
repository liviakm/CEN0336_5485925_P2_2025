# Inicialização das variáveis
total = 0
contador_notas = 0

# Coletando 10 notas
while contador_notas < 10:
    try:
        # Solicita a entrada de uma nota
        nota = float(input(f"Digite a nota {contador_notas + 1}: "))
        
        # Verifica se a nota está dentro de um intervalo esperado (opcional)
        if nota < 0 or nota > 10:
            print("Nota inválida. A nota deve ser entre 0 e 10.")
            continue
        
        # Soma a nota ao total
        total += nota
        # Incrementa o contador
        contador_notas += 1
    except ValueError:
        print("Entrada inválida. Por favor, insira um número válido.")

# Calculando a média
media = total / 10

# Exibindo a média
print(f"A média da disciplina é: {media:.2f}")
