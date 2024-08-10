from dataclasses import dataclass, field
# import random

@dataclass
class Order:
    order: int = field(default=None, metadata={"description": "Generated code", "error": "Invalid code"})

    def generate_code(self):
        """Generate a random code."""
        code = 1234
        return code

    def verify_code(self, supplied_code):
        """Check if the supplied code matches the generated code."""
        generated_code = self.generate_code()
        return supplied_code == generated_code, generated_code

    def validate(self):
        errors = {}
        if not self.order:
            errors['order'] = self.__dataclass_fields__['order'].metadata.get("error", "Required field")
        return errors


def validar_cpf(cpf: str) -> bool:
    # Remove caracteres não numéricos
    cpf = ''.join([c for c in cpf if c.isdigit()])

    # Verifica se o CPF tem 11 dígitos
    if len(cpf) != 11:
        return False

    # Verifica se todos os dígitos são iguais (CPF inválido)
    if cpf == cpf[0] * len(cpf):
        return False

    # Calcula o primeiro dígito verificador
    nove_digitos = cpf[:9]
    resultado_digito_1 = 0
    contador_regressivo_1 = 10

    for digito_1 in nove_digitos:
        resultado_digito_1 += int(digito_1) * contador_regressivo_1
        contador_regressivo_1 -= 1

    digito_1 = (resultado_digito_1 * 10) % 11
    digito_1 = digito_1 if digito_1 < 10 else 0

    # Calcula o segundo dígito verificador
    dez_digitos = nove_digitos + str(digito_1)
    resultado_digito_2 = 0
    contador_regressivo_2 = 11

    for digito_2 in dez_digitos:
        resultado_digito_2 += int(digito_2) * contador_regressivo_2
        contador_regressivo_2 -= 1

    digito_2 = (resultado_digito_2 * 10) % 11
    digito_2 = digito_2 if digito_2 < 10 else 0

    # Gera o CPF completo a partir dos 9 dígitos e os dígitos verificadores calculados
    cpf_gerado = f'{nove_digitos}{digito_1}{digito_2}'

    # Verifica se o CPF gerado é igual ao CPF fornecido
    if cpf_gerado == cpf:
        return cpf_gerado
    else:
        return False
