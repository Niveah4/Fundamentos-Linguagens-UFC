# 13 - Scripts-Web

# Contexto

- Trabalho em uma empresa que possui um sistema de cadastro de animais (pets), contendo várias fichas com informações como nome, espécie, raça, idade e dono. Essas fichas são armazenadas em arquivos no sistema.

- Semanalmente, o proprietário solicitava a realização de um backup manual dessas fichas, o que era repetitivo e sujeito a erros.
- Para resolver isso, criamos um script em Python que automatiza esse processo, realizando o backup das fichas em diretórios organizados por data.

# Código

```python

import os
import shutil
from datetime import datetime

# Caminhos das pastas
origem = 'fichas_pets'
destino_base = 'backup_fichas'

# Verifica se a pasta de origem existe
if not os.path.exists(origem):
    print(f"A pasta '{origem}' não foi encontrada. Verifique o caminho.")
    exit()

# Cria a pasta de backup com a data atual (YYYY-MM-DD)
data_hoje = datetime.now().strftime('%Y-%m-%d')
destino = os.path.join(destino_base, data_hoje)
os.makedirs(destino, exist_ok=True)

# Copia os arquivos da pasta de origem para o destino
total = 0
for arquivo in os.listdir(origem):
    caminho_origem = os.path.join(origem, arquivo)
    caminho_destino = os.path.join(destino, arquivo)

    if os.path.isfile(caminho_origem):
        shutil.copy2(caminho_origem, caminho_destino)
        total += 1
        print(f"Copiado: {arquivo}")

print(f"\nBackup concluído com sucesso. Total de fichas copiadas: {total}")
print(f"Backup salvo em: {destino}")

```