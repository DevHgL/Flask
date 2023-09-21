def test_main(nome, sobrenome, idade):
  """
  Imprime uma mensagem de boas-vindas com o nome, sobrenome e idade da pessoa.

  Args:
    nome: O nome da pessoa.
    sobrenome: O sobrenome da pessoa.
    idade: A idade da pessoa.

  """

  if not isinstance(idade, int):
    raise ValueError("A idade deve ser um número inteiro.")

  print("Olá, meu nome é {} {} e possuo {} anos".format(nome, sobrenome, idade))


test_main("Gabi", "Quadra", 22)
test_main("Hugo", "Leo", 22)