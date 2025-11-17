# 📂 Organizador de Diretórios (dir_organizer)

> Um script de console (CLI) em Python que organiza automaticamente uma pasta (ex: "Downloads"), movendo arquivos para subpastas com base em suas extensões.

---

## 🎯 Objetivo do Projeto

O objetivo deste projeto é demonstrar o domínio sobre a manipulação do sistema de arquivos local com Python. O script é focado em lógica pura e no uso das bibliotecas nativas `os` e `shutil` para automação de tarefas.

## 🛠️ Tecnologias e Habilidades Demonstradas

* **Python 3.10+**
* **`os`**: Para listar diretórios (`os.listdir`), criar pastas (`os.makedirs`), e manipular caminhos (`os.path.join`, `os.path.splitext`).
* **`shutil`**: Para mover arquivos de forma segura (`shutil.move`).
* **Lógica de Programação**:
    * Criação de um mapa de extensões (ex: `.png` -> "Imagens", `.pdf` -> "Documentos").
    * Implementação de lógica de tratamento de conflitos (o que fazer se um arquivo com o mesmo nome já existir no destino).

## 🚀 Como Executar

1.  Clone este repositório:
    ```bash
    git clone [SEU_LINK_GIT]
    cd dir_organizer
    ```

2.  (Opcional, mas recomendado) Crie um ambiente virtual:
    ```bash
    python -m venv venv
    source venv/bin/activate  # ou .venv\Scripts\activate no Windows
    ```

3.  Execute o script:
    ```bash
    python main.py
    ```

4.  O script solicitará o caminho absoluto da pasta que você deseja organizar.
