# lfac-regex

## Nome completo

- O nome completo deve ser composto por nome, nome do meio (opcional) e sobrenome, separados por um espaço.
- Nome e sobrenome devem ser ambos não vazios.
- Não são permitidos caracteres especiais ou números.
- O primeiro símbolo do nome e sobrenome, e do nome do meio se existir, deve ser do alfabeto Γ e os outros símbolos devem ser do alfabeto Σ.

Exemplos de sentenças aceitas:
- Ada Lovelace
- Alan Turing
- Stephen Cole Kleene

Exemplos de cadeias rejeitadas:
- 1Alan
- Alan
- A1an
- A1an Turing
- Alan turing

![Validação de nomes](lfac/images/validação_nomes.png)

# Validação de E-mails

O texto a seguir descreve as regras de validação para e-mails.

### Aceitos
- a@a.br
- divulga@ufpa.br
- a@a.com.br

### Rejeitados
- @
- a@.br
- @a.br
- T@teste.br
- a@A.com.br

![Validação de emails](lfac/images/validação_email.png)

