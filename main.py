from cliente import Cliente
from banco import Banco
from conta_bancaria import ContaBancaria


banco = Banco("Banco Estudantil", 101)

cliente1 = Cliente("Ana Silva", "123.456.789-01", "11999998888", "ana@email.com")
cliente2 = Cliente("Carlos Souza", "98765432100", "21988887777", "carlos@email.com")
cliente3 = Cliente("Mariana Costa", "11122233344", "31977776666", "mariana@email.com")

conta1 = ContaBancaria(1001, cliente1, banco, 500)
conta2 = ContaBancaria(1002, cliente1, banco, 300)
conta3 = ContaBancaria(1003, cliente2, banco, 1000)
conta4 = ContaBancaria(1004, cliente3, banco, -200)

banco.adicionar_conta(conta1)
banco.adicionar_conta(conta2)
banco.adicionar_conta(conta3)
banco.adicionar_conta(conta4)

conta1.depositar(200)
conta2.depositar(150)
conta3.depositar(500)
conta4.depositar(100)

conta1.sacar(100)
conta2.sacar(50)
conta3.sacar(300)
conta4.sacar(30)

print("RELATÓRIO DE EXECUÇÃO")
print("----------------------")
print("Nome do banco:", banco.get_nome())
print("Código do banco:", banco.get_codigo())
print("Quantidade de contas:", banco.quantidade_contas())

saldo_total = 0

print("\nCONTAS CADASTRADAS")

for conta in banco.listar_contas():
    titular = conta.get_titular()

    print("----------------------")
    print("Cliente:", titular.get_nome())
    print("CPF:", titular.get_cpf())
    print("Telefone:", titular.get_telefone())
    print("E-mail:", titular.get_email())
    print("Número da conta:", conta.get_numero())
    print(f"Saldo: R$ {conta.consultar_saldo():.2f}")
    print("Conta ativa:", conta.esta_ativa())

    saldo_total += conta.consultar_saldo()

print("----------------------")
print(f"Saldo total armazenado pelo banco: R$ {saldo_total:.2f}")
