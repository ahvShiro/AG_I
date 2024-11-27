aluno = {
    "nome": "Adalberto",
    "sobrenome": "Pereira",
    "cpf": "123.456.789-10",
    "ra": "832119043134q1",
    "data_nascimento": "01/02/2003",
    "email": "adalbertopereira@mail.com",
    "periodo": 1
}

print(f"Olá {aluno["nome"]}, seu RA é {aluno["ra"]} e seu e-mail é {aluno["email"]}.")

for k in aluno:
    print(f"{k} é {aluno[k]}")



alunos = [""] * 50

alunos[1] = {}
alunos[1]["nome"] = "Adalberto"



















# dados = ["Adalberto", "Pereira", "123.456.789-10", "832119043134q1", "01/02/2003", "1"]
# chaves = ["nome", "sobrenome", "cpf", "ra", "data_nascimento", "periodo"]
# dicio = {}

# for i in range(0, len(dados)):
#     dicio[chaves[i]] = dados[i]

# print(dicio)


