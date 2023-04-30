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

# def mascara_data_horario(data_horario: str) -> bool:
#     match = re.search(r'^(0[1-9]|[12]\d|3[01])/(0[1-9]|1[0-2])/\d{4} ([01]\d|2[0-3]):[0-5]\d:[0-5]\d', data_horario)
#     return valida_regex(match, data_horario)
    
def mascara_num_real(num) -> bool:
    match = re.search(r'^[-+]?[0-9]{1,2}(\.[0-9]+|[0-9]+\.)?(e[-+]?[0-9]+)?$'
, num)
    
    return valida_regex(match, num)

if __name__ == "__main__":
    
    # teste num decimal
    lista = ["-25.467", "1", "-1","+1", "64.2","1."," .2","+64,2"]
    for i in lista:
        print(mascara_num_real(i))
    
    pass