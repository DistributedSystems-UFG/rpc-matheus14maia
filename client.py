import rpyc
from constRPYC import *

try:
  # Conecta ao servidor (lembre-se de atualizar o IP em constRPYC.py)
  conn = rpyc.connect(SERVER, PORT)
  print(f"--- Conectado ao servidor RPyC em {SERVER}:{PORT} ---")

  # 1. Pega o valor inicial (deve ser uma lista vazia se o servidor acabou de começar)
  print(f"\n[TESTE] Valor inicial: {conn.root.exposed_value()}")

  # 2. Teste de Append
  print("\n[TESTE] Adicionando 20, 5, 10")
  conn.root.exposed_append(20)
  conn.root.exposed_append(5)
  conn.root.exposed_append(10)
  print(f"Resultado: {conn.root.exposed_value()}") # Esperado: [20, 5, 10]

  # 3. Teste de Inserção
  print("\n[TESTE] Inserindo 15 na posição 1")
  conn.root.exposed_insert(1, 15)
  print(f"Resultado: {conn.root.exposed_value()}") # Esperado: [20, 15, 5, 10]

  # 4. Teste de Ordenação (Crescente)
  print("\n[TESTE] Ordenando (crescente)")
  conn.root.exposed_sort()
  print(f"Resultado: {conn.root.exposed_value()}") # Esperado: [5, 10, 15, 20]

  # 5. Teste de Ordenação (Decrescente)
  print("\n[TESTE] Ordenando (decrescente)")
  conn.root.exposed_sort(reverse=True)
  print(f"Resultado: {conn.root.exposed_value()}") # Esperado: [20, 15, 10, 5]

  # 6. Teste de Pesquisa
  print("\n[TESTE] Pesquisando por 10 (deve existir)")
  print(f"Resultado: {conn.root.exposed_search(10)}") # Esperado: True
  print("[TESTE] Pesquisando por 99 (não deve existir)")
  print(f"Resultado: {conn.root.exposed_search(99)}") # Esperado: False

  # 7. Teste de Remoção
  print("\n[TESTE] Removendo 15 (deve existir)")
  conn.root.exposed_remove(15)
  print(f"Resultado: {conn.root.exposed_value()}") # Esperado: [20, 10, 5]
  print("[TESTE] Removendo 99 (não deve existir)")
  removido = conn.root.exposed_remove(99)
  print(f"Resultado da remoção (99): {removido}") # Esperado: False
  print(f"Lista final: {conn.root.exposed_value()}") # Esperado: [20, 10, 5]

  print("\n--- Testes concluídos ---")
  conn.close()

except ConnectionRefusedError:
  print(f"Erro: Não foi possível conectar ao servidor em {SERVER}:{PORT}.")
  print("Verifique se o servidor está rodando e o IP em 'constRPYC.py' está correto.")
except Exception as e:
  print(f"Ocorreu um erro inesperado: {e}")