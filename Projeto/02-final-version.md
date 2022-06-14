# **CSI606-2021-02 - Remoto - Trabalho Final - Resultados**

## *Aluna(o): Lucas Duarte Almeida*

--------------

<!-- Este documento tem como objetivo apresentar o projeto desenvolvido, considerando o que foi definido na proposta e o produto final. -->

### Resumo

   O trabalho se baseou na dificuldade de gerenciar e controlar o fluxo das comandas durante um expendiente em um bar. Com isso, foi desenvolvido um website para essa finalidade com foco na usabilidade.

### 1. Funcionalidades implementadas
<!-- Descrever as funcionalidades que eram previstas e foram implementas. -->
  Visualizar comandas.
  Adicionar pedidos.
  Fechar comandas.
  Interface de administração (adicionar novos itens, usuários e mesas no bar).
  Também foi adicionada um modal para a confirmação que a comanda foi realmente fechada.
### 2. Funcionalidades previstas e não implementadas
<!-- Descrever as funcionalidades que eram previstas e não foram implementas, apresentando uma breve justificativa do porquê elas não foram incluídas -->
Todas as funcionalidades previstas foram implementadas.
### 3. Outras funcionalidades implementadas
<!-- Descrever as funcionalidades implementas além daquelas que foram previstas, caso se aplique.  -->

### 4. Principais desafios e dificuldades
<!-- Descrever os principais desafios encontrados no desenvolvimento do trabalho, quais foram as dificuldades e como elas foram superadas e resolvidas. -->
Meu maior desafio (como sempre) é na parte de construção das views e das rotas. Não sou muito bom com desenhar o frontend, principalmente porque normalmente não consigo imaginar como estruturar corretamente as divs. Porém com a ajuda do boostrap, foi até relativamente tranquilo a construção das views e de certa forma recompensador.
### 5. Instruções para instalação e execução
<!-- Descrever o que deve ser feito para instalar (ou baixar) a aplicação, o que precisa ser configurando (parâmetros, banco de dados e afins) e como executá-la. -->
Os requerimentos são apenas o Python(3.8+) e o Django(4.0+)

O django pode ser instalado em uma Virtual Environment através do comando:

´pip install Django´

Por questôes de simplicidade, descomentei no gitignore a venv e o db.sqlite3 (banco de dados utilizado no projeto) para utilização.

Para rodar o servidor, ´source venv/bin/activate´ depois ´python manage.py runserver´

O usuário administrador é ´lucas´ com senha ´lucasbest´.
Os funcionários são ´lucas´/´funcionario1´ e ´josue´/´funcionario2´

### 6. Referências
<!-- Referências podem ser incluídas, caso necessário. Utilize o padrão ABNT. -->
  As únicas referências são a documentação do Boostrap e do Django.
  https://getbootstrap.com/docs/
  https://docs.djangoproject.com/en/4.0/
