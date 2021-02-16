# todo-list-aws

## Prerequisitos 

### Docker 
Docker & Docker compose son indispensables para ejectuar este repositorio 

Versiones probadas 
* Docker version 19.03.13-ce, build 4484c46

### Python 
Todos los paquetes que se necesitan se encuentran descriptos en los requirements.txt. Si desea ejecturarlo fuera de la automatización 
pip install -r requirements.txt

La version elegida de python preferida Python 3.7.9


## Setup Inicial 

El archivo make te permitira ejectuar acciones localmente. 

### Instalar software necesario para correr los tests 
    make setupLocalEnv
    
### Correr test localmente
    
    make localTest


### Correr Dynamo DB localmente
Es necesario para poder hacer pruebas locales 

    make startLocalDB
    make stopLocalDB
    
Dynamo correra como docker en nuestra maquina como un contenedor docker en el puerto 8000

### Probar funciones lambdas localmente 

    make sartSamLocal
    
Nota: SE DEBE EJECTUAR LA BASE DE DATOS LOCAL PRIMERO, DESCRIPTO EN EL PASO ANTERIOR 


## ESTRUCTURA 

### Codigo fuente de las funciones 
    * todos
### Configuración SAM 
    * template.yaml
### Tests estáticos, unitarios y de integración 
    * tests 
    * integration-tests
    
### CI / CD

Jenkins pipelines 
    * pipelines
    

### Desplegar Jenkins 

Para poder desplegar jenkins se recomienda usar el plan de terraform 
    * terraform
    
Se recomienda ajustar las variables antes de ejecturarlo
    * variables.tf

    Ejecucción ./configure_environment.sh

