Instruções de instalação

1-) Crie um ambiente virtual com sua biblioteca preferida. Eu utilizei o virtualenv.

# Criar comando:

python3 -m venv authdj

# Ativar o ambiente virtual

source auth/bin/activate

# Instalar as bibliotecas necessárioa inicialmente

pip install django

2-) Agora vamos criar um diretório para o projeto:

# Criar a pasta

mkdir auth

# criar as sub pastas

cd auth
mkdir backend
madir frontend

3-) Dentro da pasta backend vamos criar o projeto django

# Criar projeto django

django-admin startproject core .

Este comando criará a estrutura do projeto dentro da pasta auth. O 'core ." faz com que o projeto seja criado na raiz da pasta auth e não dentro de alguma outra subpasta.dj
