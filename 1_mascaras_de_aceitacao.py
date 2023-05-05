import re

def valida_regex(match: re.Match, cadeia: str) -> bool:
    if not match:
        return False

    if match.group(0) != cadeia:
        return False
    return True

def mascara_nome(nome: str) -> bool:
    
    match = re.search(r'[A-Z][a-z]+( [A-Z][a-z]+)? [A-Z][a-z]+', nome)
    
    return valida_regex(match, nome)

def mascara_email(email: str) -> bool:
    
    match = re.search(r'[a-z]+@[a-z]+(.com)?.br', email)
    
    return valida_regex(match, email)

def mascara_senha(senha: str) -> bool:
    if len(senha) != 8:
        return False
    
    match = re.search(r'(?=.*[A-Z])(?=.*[0-9])[a-z|A-Z|0-9]*', senha)
    
    return valida_regex(match, senha)

def mascara_cpf(cpf: str) -> bool:
    
    match = re.search(r'[0-9]{3}.[0-9]{3}.[0-9]{3}-[0-9]{2}', cpf)
    
    return valida_regex(match, cpf)

def mascara_telefone(telefone: str) -> bool:
    
    # match = re.search(r'(\((?=.{2}\))(?=.{10}-))?[0-9]{2}\)? 9[0-9]{4}[0-9]{4}', telefone)
    match = re.search(r'(\([0-9]{2}\) 9[0-9]{4}-?[0-9]{4})|([0-9]{2} 9[0-9]{8})', telefone)
    
    return valida_regex(match, telefone)

def mascara_data_hora(data_hora: str) -> bool:

    match = re.search(r'[0-9]{2}/[0-9]{2}/[0-9]{4} ([0-1][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]', data_hora)

    return valida_regex(match, data_hora)

def mascara_num_decimal(num: str) -> bool:
    match = re.search(r'^[-+]?[0-9]{1,2}(\.[0-9]+|[0-9]+\.)?(e[-+]?[0-9]+)?$', num)
    
    return valida_regex(match, num)
    
    


if __name__ == "__main__":
    #TESTE NOME
    # nome_teste1 = "Victor Goncalves Oliveira"   #True
    # nome_teste2 = "victor Goncalves Oliveira"   #False
    # nome_teste3 = "Victor Oliveira"             #True
    # nome_teste4 = "Victor goncalves Oliveira"   #False
    # nome_teste5 = "Victor oliveira"             #False
    # nome_teste6 = "Victor OliveirA"             #False
    
    # print(mascara_nome(nome_teste1))
    # print(mascara_nome(nome_teste2))
    # print(mascara_nome(nome_teste3))
    # print(mascara_nome(nome_teste4))
    # print(mascara_nome(nome_teste5))
    # print(mascara_nome(nome_teste6))
    
    # print("\n\n")
    
    
    # print(mascara_nome("Ada Lovelace"))
    # print(mascara_nome("Alan Turing"))
    # print(mascara_nome("Stephen Cole Kleene"))
    
    # print(mascara_nome("1Alan"))
    # print(mascara_nome("Alan"))
    # print(mascara_nome("A1an"))
    # print(mascara_nome("A1an Turing"))
    # print(mascara_nome("Alan turing"))
    
    
    # #testes email
    
    # print(mascara_email("a@a.br"))
    # print(mascara_email("divulga@ufpa.br"))
    # print(mascara_email("a@a.com.br"))
    
    # print(mascara_email("@"))
    # print(mascara_email("a@.br"))
    # print(mascara_email("@a.br"))
    # print(mascara_email("T@teste.br"))
    # print(mascara_email("a@A.com.br"))    
    
    
    # #testes senha
    
    # print(mascara_senha("518R2r5e"))
    # print(mascara_senha("F123456A"))
    # print(mascara_senha("1234567T"))
    # print(mascara_senha("ropsSoq0"))
    
    # print(mascara_senha("F1234567A"))
    # print(mascara_senha("abcdefgH"))
    # print(mascara_senha("1234567HI"))
    
    # print(mascara_senha("asdfvc2Z"))
    # print(mascara_senha("7Xasas2A"))
    # print(mascara_senha("2asdasdZ"))
    # print(mascara_senha("aaaaaaaa"))
    
    # # testes cpf
    
    # print(mascara_cpf("123.456.789-09"))
    # print(mascara_cpf("000.000.000-00"))
    
    # print(mascara_cpf("123.456.789-0"))
    # print(mascara_cpf("11.111.11-11"))
    
    # # testes telefone
    
    # print(mascara_telefone("(91) 99999-9999"))
    # print(mascara_telefone("(91) 999999999"))
    # print(mascara_telefone("91 999999999"))
    
    # print(mascara_telefone("(91) 59999-9999"))
    # print(mascara_telefone("99 99999-9999"))
    # print(mascara_telefone("(94)95555-5555"))
    
    # print(re.search(r'\((?=.{6}\))[a-z]*\)?', "(asdasd)"))
    
    # print(mascara_data_hora("31/08/2019 20:14:55"))
    # print(mascara_data_hora("99/99/9999 23:59:59"))

    # print(mascara_data_hora("99/99/9999 3:9:9,"))
    # print(mascara_data_hora("9/9/99 99:99:99"))
    # print(mascara_data_hora("99/99/999903:09:09"))
    
    # # teste para mascara de numeros decimais
    # lista = [' 123.456.789-0', '111.111.11-11']
    
    # for i in lista:
    #     print(mascara_cpf(i))
    
    nomes = [
    ["Ada Lovelace", True],
    ["Alan Turing", True],
    ["Stephen Cole Kleene", True],
    ["1Alan", False],
    ["Alan", False],
    ["A1an", False],
    ["A1an Turing", False],
    ["Alan turing", False],
    ]

        
    # Realiza os testes e exibe os resultados na tabela
    print("| Função       | Cadeia de entrada                | Saída |")
    print("|--------------|----------------------------------|-------|")
    for cadeia, saida_esperada in nomes:
        print(f"| mascara_nome | {cadeia:<32} | {mascara_nome(cadeia)} |")
    
    print()
    emails = [
    ["a@a.br", True], 
    ["divulga@ufpa.br", True],
    ["a@a.com.br", True],
    ["@", False],
    ["a@.br", False],
    ["@a.br", False],
    ["T@teste.br", False],
    ["a@A.com.br", False],
    ]

    print("|--------------|-------------------------------------------")
    print("| Função       | Cadeia de entrada                | Saída |")
    for cadeia, saida_esperada in emails:
        print(f"| mascara_email | {cadeia:<32} | {mascara_email(cadeia)} |")
    
    print()
    senha = [
    ["518R2r5e", True],
    ["F123456A", True],
    ["1234567T", True],
    ["ropsSoq0", True],
    ["F1234567A", False],
    ["abcdefgH", False],
    ["1234567HI", False],
    ]

    print("|--------------|-------------------------------------------")
    print("| Função       | Cadeia de entrada                | Saída |")
    for cadeia, saida_esperada in senha :
        print(f"| mascara_senha | {cadeia:<32} | {mascara_senha(cadeia)} |")
    
    print()
    cpf = [
    ["123.456.789-09", True],
    ["000.000.000-00", True],
    ["123.456.789-0", False],
    ["111.111.11-11", False],
    ]
    
    print("|--------------|-------------------------------------------")
    print("| Função       | Cadeia de entrada                | Saída |")
    for cadeia, saida_esperada in cpf :
        print(f"| mascara_senha | {cadeia:<32} | {mascara_cpf(cadeia)} |")
        
    print()

    telefone = [
    ["(91) 99999-9999", True],
    ["(91) 999999999", True],
    ["91 999999999", True],
    ["(91) 59999-9999", True],
    ["99 99999-9999", True],
    ["(94)95555-5555", True],
    ]
    
    print("|--------------|-------------------------------------------")
    print("| Função       | Cadeia de entrada                | Saída |")
    for cadeia, saida_esperada in telefone :
        print(f"| mascara_senha | {cadeia:<32} | {mascara_telefone(cadeia)} |")
        
    print()
    
    data_e_hora = [
    ["31/08/2019 20:14:55", True],
    ["99/99/9999 23:59:59", True],
    ["99/99/9999 3:9:9", False],
    ["9/9/99 99:99:99", False],
    ["99/99/999903:09:09", False],
    ]
    
    print("|--------------|-------------------------------------------")
    print("| Função       | Cadeia de entrada                | Saída |")
    for cadeia, saida_esperada in data_e_hora :
        print(f"| mascara_senha | {cadeia:<32} | {mascara_data_hora(cadeia)} |")
        
    print()
    
    numeros = [
    ["-25.467", True],
    ["1", True],
    ["-1", True],
    ["+1", True],
    ["64.2", True],
    ["1.", False],
    [".2", False],
    ["+64,2", False],
    ]
    
    print("|--------------|-------------------------------------------")
    print("| Função       | Cadeia de entrada                | Saída |")
    for cadeia, saida_esperada in numeros :
        print(f"| mascara_senha | {cadeia:<32} | {mascara_num_decimal(cadeia)} |")
        
    print()




    pass