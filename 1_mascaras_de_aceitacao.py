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
    
    # testes telefone
    
    # print(mascara_telefone("(91) 99999-9999"))
    # print(mascara_telefone("(91) 999999999"))
    # print(mascara_telefone("91 999999999"))
    
    # print(mascara_telefone("(91) 59999-9999"))
    # print(mascara_telefone("99 99999-9999"))
    # print(mascara_telefone("(94)95555-5555"))
    
    # print(re.search(r'\((?=.{6}\))[a-z]*\)?', "(asdasd)"))
    
    print(mascara_data_hora("31/08/2019 20:14:55"))
    print(mascara_data_hora("99/99/9999 23:59:59"))

    print(mascara_data_hora("99/99/9999 3:9:9,"))
    print(mascara_data_hora("9/9/99 99:99:99"))
    print(mascara_data_hora("99/99/999903:09:09"))
    
    #teste para mascara de numeros decimais
    # lista = ['-25.467', '1', '-1', '+1', '64.2', '1.', '.2', '+64,2']
    
    # for i in lista:
    #     print(mascara_num_decimal(i))
        
    pass