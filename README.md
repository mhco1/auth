# 🔒 Auth

## 🔍 Sobre
Aplicativo **CLI** para gerenciamento de credenciais

## 📁 Estrutura do Projeto

- **📌 `./app:`** Código-fonte principal da aplicação
- **⚒️ `./build:`** Arquivos para construção da imagem Docker
- **🚀 `./exe:`** Binário para execução e construção do codigo

### 📁 Estrutura do App

- **📜 `./cmd:`** Aplicação em bash para a execução das princípais operações do sistema
- **⚙️ `./etc:`** Arquivos de modelo para configuração
- **🖥️ `./tui:`** Aplicação em python pelo terminal de forma interativa

## ⚙️ Configuração e Execução

### 🐳 Instalação utilizando o Docker

> 💡 **Dica:** Torne `./exe` executável com o comando:
>
> ```bash
> chmod +x ./exe
> ```

- 1️⃣ Baixe uma imagem `base` (ex: Debian):
  
    ```bash
    docker pull debian:latest
    ```

- 2️⃣ Rode um container temporário e comite como `app.base`:

    ```bash
    docker run --name run.debian --rm -it debian /bin/bash
    docker commit -p run.debian app.debian
    ```

- 3️⃣ Construa a imagem do projeto com esta imagem:

    ```bash
    ./exe build debian auth
    ```

- 4️⃣ Inicie o progama:

    ```bash
    ./exe run auth
    ```

### 👨‍💻 Para desenvolvimento com Docker

> 🧩 Requer a imagem do **Zsh**, disponível em:
> 
> 🔗 [docker-imagens/zsh](https://github.com/mhco1/docker-imagens/blob/main/docker/zsh/README.md)

- 1️⃣ Crie um arquivo `.env` na raiz do projeto com o seguinte conteúdo:

    ```bash
    ZSH=/diretorio/da/imagem/zsh
    ```

- 2️⃣ Com a imagem do programa já criada, sobreponha com o ambiente de desenvolvimento:
    
    ```bash
    ./exe build-dev auth auth.dev
    ```

- 3️⃣ Executar o container em background:

    ```bash
    ./exe run-dev auth.dev
    ```

- 4️⃣ Conectar ao container com o **Dev Containers** no VSCode
   - Utilize a extensão **Dev Containers** para abrir o projeto dentro do ambiente do container

- 5️⃣ (Opcional) Conecte-se diretamente ao shell Zsh:

    ```bash
    ./exe shell auth.dev
    ```

## 📝 Licença  
Este projeto está sob a licença MIT.
