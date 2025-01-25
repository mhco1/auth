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

- 1️⃣ Construir a imagem
    
    ```bash
    ./bin-build
    ```
- 2️⃣ Iniciar o app

    ```bash
    ./bin-auth
    ```

### 📥 De forma nativa

- 1️⃣ Instalar o projeto de forma nativa em **/opt/auth**
    
    ```bash
    ./bin-install
    ```

### 👾 Em desenvolvimento com Docker

- 1️⃣ Executar o container em background
    
    ```bash
    ./bin-background
    ```

- 2️⃣ Conectar ao container com o **Dev Containers** no VSCode
   - Utilize a extensão **Dev Containers** para abrir o projeto dentro do ambiente do container

## 📝 Licença  
Este projeto está sob a licença MIT.
