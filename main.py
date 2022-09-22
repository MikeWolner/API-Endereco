import requests

def endereco():
    print("Escolha uma opção \n [1]CEP \n [2]Nome da rua")
    escolha = int(input("Escolha um número: "))
    if escolha == 1:
        CEP = input("Digite seu CEP");
        URL = f"https://viacep.com.br/ws/{CEP}/json/"
        r = requests.get(URL)
        rua = r.json()["logradouro"]
        bairro = r.json()["bairro"]
        cidade = r.json()["localidade"]
        estado = r.json()["uf"]
        CEP_retorno = r.json()["cep"]
        return f"{rua}-{bairro},{cidade}-{estado},{CEP_retorno}"
    elif escolha == 2:
        rua = input("Digite o nome da rua")
        cidade = input("Digite o nome da cidade")
        estado  = input("Digite o nome do estado")

        URL = f"https://viacep.com.br/ws/{estado}/{cidade}/{rua}/json/"

        CEPretorno = requests.get(URL)
        CEP = CEPretorno.json()[0]["cep"]
        return f'{CEP}'
    else:
        print("Opção inválida")

print(endereco())