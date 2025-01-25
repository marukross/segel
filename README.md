# segel
Actualizar apt
sudo apt update && sudo apt upgrade -y

Instalar herramienta git, sirve para clonar repositorios de codigos.
sudo apt install git

Configurar git, agregar tu nombre y tu correo
git config --global user.name "marcos bogarin"
git config --global user.email "marcosbogarincano@gmail.com"

Descargar de github odoo comunity 15, descargar solo la rama 15 y el ultimo commit, script:
git clone --single-branch --branch 15.0 https://github.com/odoo/odoo.git --depth 1

Instalar base de datos Postgresql
sudo apt install postgresql postgresql-client

Configurar base de datos, crear usuario y darle permisos para operar
sudo su postgres
psql
CREATE USER mbogarin WITH PASSWORD 'mbogarin123*';
ALTER USER mbogarin WITH SUPERUSER;

Instalar dependencias 
sudo apt install python3-pip libldap2-dev libpq-dev libsasl2-dev python3-venv python3-wheel

Generar entorno virtual
python3 -m venv odoo15-venv

Activar entorno virtual
source odoo15-venv/bin/activate

Ajustar requirements.txt segun instalacion de python o sistema operativo.

Actualizar Pip
python3 -m pip install --upgrade pip

Instalar dependencias para odoo con PIP
pip3 install -r odoo/requirements.txt

Crear archivo de configuracion personalizado
touch odoo.conf

Agregar parametros
[options]
db_host = 127.0.0.1
db_port = 5432
db_user = mbogarin
db_password = mbogarin123*
addons_path = /home/mbogarin/Documents/projects/vscode/segel/odoo/addons

Iniciar Servicio Odoo
python3 {ruta completa a}/odoo/odoo-bin -c {ruta completa a}/odoo.conf