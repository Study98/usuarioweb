# usuarioweb - Projeto que usei pra entrar na Pontotel
 Requisitos para o funcionamento do projeto:
 
 -Ter o Python 3.9.7 ou superior instalado na máquina
 
 Após copiar o projeto, fazer os seguintes procedimentos:
 
 1- criar um ambiente virtual python (Caso não tenha a configuração adquada no sistema, executar os seguintes comanados):
   - Em Windows:
     1.	Liberar a Política de Acesso de Scripts
       -	Buscar a opção Power Shell (Admin);
       - digitar o seguinte comando: Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
       
     2.	Criar Ambiente Virtual
       - Executar o seguinte código para a criação do ambiente virtual: ‘python3 –m venv venv’

 
   - Em Linux:
     -	Digitar o seguinte comando: sudo pip3 install virtualenv
     - Baixar o projeto
     - Abrir o terminal e localizar o projeto
     - Criar o ambiente virtual: --virtualenv venv

 2- ativar o ambiente virtual python:
 
    - Em Windows:
     - Abrir o PowerShell
     - Digitar o comando ‘\venv\Scripts\activate’
     - executar o comando: pip install -r requirements.txt
     - executar o programa: python manage.py runserver
    
    - Em Linux:
     -	Abrir o Shell;
     -	Digitar o comando ‘source venv/bin/activate’
     -	Digitar o comando: ‘pip3 install -r requirements.txt’
     -	Para executar ‘python3 manage.py runserver’
