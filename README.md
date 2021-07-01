# Flask Simple & Clean Boilerplate

Aplicación de Python3 con Flask que toma la cara de una imagen y busca la de mayor similitud en una base
de datos de caras codificadas de obras del museo del Prado.

## Desarrollo Local

Para poder trabajar en local es necesario tener un entorno virtual de Python en el que correr Flask.

### Entorno Virtual

Primero instalaremos los paquetes y virtualenv si no lo tenemos:

```shell
# Step 1: Actualizamos los repositorios del sistema
sudo apt-get update
# Step 2: Instalamos pip para Python 3
sudo apt-get install build-essential libssl-dev libffi-dev python-dev
sudo apt install python3-pip
# Step 3: Utilizamos pip para instalar virtualenv
sudo pip3 install virtualenv 
```

A continuación creamos nuestro entorno virtual, lo activamos e instalamos los paquetes necesarios:

```shell
# Creamos el entorno virtual 'my_env'
python3 -m venv my_env
# Activamos el entorno virtual
source my_env/bin/activate
# Instalamos los paquetes necesarios de desarrollo
pip install -r requirements.txt
```

#### Arrancando Flask

Una vez que tenemos nuestro entorno virtual, arrancamos Flask situándolos en el directorio raíz de este proyecto:

```shell
flask run
```

## Deploy

Para automatizar los deployment utilizaremos PM2 donde es necesario crear la carpeta en el `host` que situamos
en `ecosystem.config.js` bajo el apartado de `path`.

Tras esto hacemos un primer setup de nuestro trabajo con:

```shell
pm2 deploy ecosystem.config.js production setup
```

Cuando se realiza una modificación en el código de una aplicación se deben actualizar los cambios en el servidor de
producción. Esto es lo que llamamos el deploy o despliegue a producción. Esta tarea también la realizamos con PM2. El
procedimiento es el siguiente:

Un usuario realiza cambios en su PC de desarrollo (pc local). **Antes de hacer deploy los cambios se suben a git**
(git push). Desde un terminal nos movemos al directorio del proyecto, donde se encuentra el archivo
`ecosystem.config.js`. Ahora ejecutamos el deploy:

```shell
pm2 deploy ecosystem.config.js production update
```

A partir de aquí sucede la magia donde PM2 se conecta al servidor remoto por SSH, actualiza en el remoto los últimos
cambios de git y reinicia el proceso de la aplicación.

Todo se realiza desde el pc local del desarrollador. En el terminal se puede ver un output con todo el proceso y el
resultado final. En este punto se deberá estar pendiente de este resultado para comprobar que no se hayan producido
errores.

Nota: Para poder realizar el update en el servidor es necesario que hayamos realizado un push previo y nuestro trabajo
este actualizada a la version del repositorio.

Nota: Si cambiamos el `repo` de nuestro `ecosystem.config.js` será necesario realizar el `setup` de nuevo.

### Resolución de problemas

#### EventSource

Para poder lanzar Server-Sent Events y manejarlos, es necesario configurar apropiadamente nginx. Para ello,
siguiendo la siguiente [respuesta](https://stackoverflow.com/a/13673298/6689880), debemos añadir lo siguiente
en la sección `location` de la configuración de nuestro servidor nginx para el proyecto:

```shell
proxy_set_header Connection '';
proxy_http_version 1.1;
chunked_transfer_encoding off;

proxy_buffering off;
proxy_cache off;
```
