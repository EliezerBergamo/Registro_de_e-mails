<h1 align="center">Registro de emails</h1>

<div>
  <h3>Descrição </h3>
  <p align="justify">
    Um projeto feito com Python e Django para um professor que precisava registrar o email de eventuais alunos que participam de alguns eventos como palestras
    que ocorrem na faculdade, e como pode ocorrer de alguns passarem o email errado ou desistirem, foi feito um sistema bem simples que permite que ele exclua
    os emails ou os altere.
  </p>
  <p align="justify">
    O projeto foi testado no Windows 11, para executar código é necessário ter o Python 3.x.
  </p>
</div><hr>

<div>
  <h3>Funcionalidades</h3>
  <p align="justify">
    Cadastra emails e os exibe numa tabela, e depois permite que eles sejam deletados ou editados.
  </p>
</div><hr>

<div>
  <h3>Tecnologias utilizadas</h3>
  <ul>
    <li>
      <a href="https://docs.djangoproject.com/pt-br/4.2/">Django</a>
    </li>
  </ul>
</div><hr>

<div>
  <h3>Rodando o projeto</h3>
  <p align="justify">
    Para rodar o projeto é necessário ter conhecimento em Python e Django
  </p>
  <h4>Criando ambiente virtual</h4>
  <p align="justify">
    A criação do ambiente virtual é opcional, mas caso queira fazer, basta seguir os seguintes comandos no terminal:

  ```
  python -m venv ./env
  ```
  </p>
  <p align="justify">
    Para ativar o ambiente virtual, execute o comando, se for ativado corretamente, o nome do ambiente virtual vai aparecer a esquerda no terminal.

  ```
  source ./env/scripts/activate
  ```
  </p><hr>
  <h4>Instalando o Django</h4>
  <p align="justify">
    Após a criação do ambiente virtual, é necessário instalar o Django, que pode ser feito usando os comandos:

  ```
  pip install django
  ```
  Para saber se foi instalado corretamenete, é necessário saber se está dentro da pasta que contém o arquivo <b><i>manage.py</i></b>, para saber
  se está na pasta correta, basta executar o comando <b><i>ls</i></b> no terminal, e então execute o comando:
  
  ```
  python manage.py runserver
  ```
  </p><hr>
  <h4>Criando um projeto no Django</h4>
  <p align="justify">
    Esse comando no faz com que um projeto seja criado no Django, e todos os arquivos que precisam para o processo funcionar. O uso do símbolo "." no final
    do comando faz com que não seja criado uma subpasta com o mesmo nome do projeto.

  ```
  django-admin startproject nome_do_projeto .
  ```
  </p><hr>
  <h4>Criando um app no Django</h4>
  <p align="justify">
    Esse comando faz com que um app seja criado no Django, mas para esse comando funcionar é necessário saber se está dentro da pasta que contém o arquivo
    <b><i>manage.py</i></b>.
    
  ```
  python manage.py startapp nome_do_app
  ```
  </p>
  </p>
  <h4>Configurações</h4><hr>
  <p align="justify">
    Para o projeto funcionar, é preciso configurar algumas coisas, que devem ser feitas dentro do arquivo <b><i>settings.py</i></b>.
    A primeira coisa é registrar o nome do app, ou não vai funcionar, basta ir no arquivo e procurar onde tem INSTALLED_APPS e adicionar o nome do app
    no final.
    
  ```
  INSTALLED_APPS = [
    'app_01',
  ]
  ```

  E para fazer os arquivos estáticos funcionarem, primeiro é preciso fazer uma importação.

  ```
  import os
  ```

  Depois basta ir no final e procurar onde tem STATIC_URL = 'static/' e abaixo disso adicionar o seguinte:
  
  ```
  STATICFILES_DIRS = [
      os.path.join(BASE_DIR, "static"),
  ]
  ```
  
  Com isso já é possível fazer o projeto funcionar, mas para tudo funcionar corretamente, execute dois comandos no terminal:
  
  ```
  python manage.py makemigrations
  ```

  ```
  python manage.py migrate
  ```
  </p>
</div><hr>

<div>
  <h3>Colaboradores</h3>
  <p>Eliezer Junior</p>
</div><hr>

<div>
  <h3>Status</h3>
  <p>Concluído</p>
</div>
