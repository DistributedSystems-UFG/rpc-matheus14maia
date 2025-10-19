import rpyc
from constRPYC import * #-
from rpyc.utils.server import ThreadedServer

class DBList(rpyc.Service):
  value = []
  lock = threading.Lock()

  def exposed_append(self, data):
    self.value = self.value + [data]
    return self.value

  def exposed_value(self):
    return self.value

  def exposed_search(self, data):
    with self.lock:
      print(f"[LOG] search({data})...")
      result = data in self.value
      print(f"[LOG] Resultado da busca: {result}")
      return result

  def exposed_remove(self, data):
    with self.lock:
      print(f"[LOG] remove({data})...")
      try:
        self.value.remove(data)
        print(f"[LOG] Removido. Lista atual: {self.value}")
        return True # Sucesso
      except ValueError:
        print(f"[LOG] Falha ao remover (não encontrado).")
        return False # Item não estava na lista

  def exposed_insert(self, index, data):
    with self.lock:
      try:
        self.value.insert(index, data)
        print(f"[LOG] insert({index}, {data}). Lista atual: {self.value}")
        return True
      except Exception as e:
        print(f"[LOG] Falha ao inserir: {e}")
        return False

  def exposed_sort(self, reverse=False):
    with self.lock:
      print(f"[LOG] sort(reverse={reverse})...")
      self.value.sort(reverse=reverse)
      print(f"[LOG] Lista ordenada. Lista atual: {self.value}")
      return self.value

if __name__ == "__main__":
  server = ThreadedServer(DBList(), port = PORT)
  server.start()

