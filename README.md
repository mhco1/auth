# 🔒 Auth

## 🔍 Sobre
Aplicativo **CLI** para gerenciamento de credenciais.

> ⚠️ **Obs:** as instalações ainda estão em teste

## 📁 Estrutura do Projeto

- **📌 App:** Código-fonte
- **📦 bin-\*:** Binários para execução do codigo
- **🐳 docker:** Diretório contendo arquivos utilizados na construção da imagem Docker

## ⚙️ Configuração e Execução

### 🐳 Instalação utilizando o Docker

> Execute `chmod +x` em `./exe` para torna-lo executável

- 1️⃣ Construir a imagem
    
    ```bash
    ./exe build
    ```
- 2️⃣ Iniciar o app

    ```bash
    ./exe run
    ```

### 📥 De forma nativa

- 1️⃣ Instalar o projeto de forma nativa em **/opt/auth**
    
    ```bash
    ./exe install-native
    ```

### 👾 Para desenvolvimento com Docker

Antes, baixe a imagem do **zsh** no repositório [docker-imagens/zsh](https://github.com/mhco1/docker-imagens/blob/main/docker/zsh/README.md)

- 1️⃣ Na raiz, crie um arquivo `.env` com o seguinte conteudo:

    ```bash
    ZSH=/diretorio/da/imagem/zsh
    ```
- 2️⃣ Execute o `build-dev` ao invés do `build`
    
    ```bash
    ./exe build-dev
    ```

- 3️⃣ Executar o container em background
    
    ```bash
    ./exe run-dev
    ```

- 4️⃣ Conectar ao container com o **Dev Containers** no VSCode
   - Utilize a extensão **Dev Containers** para abrir o projeto dentro do ambiente do container

## 📝 Licença  
Este projeto está sob a licença MIT.
