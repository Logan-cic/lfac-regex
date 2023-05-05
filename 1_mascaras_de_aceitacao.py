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
    
    senha = [
    ["518R2r5e", True],
    ["F123456A", True],
    ["1234567T", True],
    ["ropsSoq0", True],
    ["F1234567A", False],
    ["abcdefgH", False],
    ["1234567HI", False],
    ]
   
    cpf = [
    ["123.456.789-09", True],
    ["000.000.000-00", True],
    ["123.456.789-0", False],
    ["111.111.11-11", False],
    ]
    

    telefone = [
    ["(91) 99999-9999", True],
    ["(91) 999999999", True],
    ["91 999999999", True],
    ["(91) 59999-9999", True],
    ["99 99999-9999", True],
    ["(94)95555-5555", True],
    ]
    
    data_e_hora = [
    ["31/08/2019 20:14:55", True],
    ["99/99/9999 23:59:59", True],
    ["99/99/9999 3:9:9", False],
    ["9/9/99 99:99:99", False],
    ["99/99/999903:09:09", False],
    ]
    
    numeros_decimais = [
    ["-25.467", True],
    ["1", True],
    ["-1", True],
    ["+1", True],
    ["64.2", True],
    ["1.", False],
    [".2", False],
    ["+64,2", False],
    ]
    
    # Inisira a lista a ser testada após o "in" do for.
    # Dentro do print chame a função que validara ou não a cadeia dentro da lista.
    # A tabale retorna True para uma cadeia aceita e False para a cadeia rejeitada.
    
    print("|--------------|-------------------------------------------")
    print("| Função       | Cadeia de entrada                | Saída |")
    for cadeia, saida_esperada in numeros_decimais:
        print(f"| mascara_senha | {cadeia:<32} | {mascara_num_decimal(cadeia)} |")
        
    print()

    pass