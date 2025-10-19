[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/_8sc1GR8)
### Overview

This example illustrates RPC in Python using the RPyC library (https://rpyc.readthedocs.io/).

It consists of a server that exposes two remotely accessible procedures used to manipulate a list:

- value(): returns the current value of the list (its elements)
- append(): adds a new element to the end of the list

### Before running the example, you need to install the RPyC library:

Do the following on the two machines (AWS EC2 instances) that you will use for this activity:

    sudo apt update
    sudo apt install python3-rpyc

### Then edit the constRPYC.py file to use the IP address of the machine where you will run the server:

Also make sure it is using one of the ports left open for incoming TCP connections on the firewall (security group), such as 5678

### Then run the server on one machine

    python3 server.py

(and leave it running)

### Then run the client on the other machine

    python3 client.py

### Funcionalidades Implementadas

O `server.py` agora expõe um conjunto completo de manipulações da lista, tratando a concorrência com `threading.Lock`:

* `exposed_value()`: Retorna o valor atual da lista.
* `exposed_append(data)`: Adiciona um elemento ao final da lista.
* `exposed_search(data)`: Verifica se um elemento existe na lista.
* `exposed_remove(data)`: Remove a primeira ocorrência de um elemento.
* `exposed_insert(index, data)`: Insere um elemento em um índice específico.
* `exposed_sort(reverse=False)`: Ordena a lista (crescente ou decrescente).

O `client.py` foi atualizado para se conectar ao servidor e testar, em ordem, todas essas novas funcionalidades.
