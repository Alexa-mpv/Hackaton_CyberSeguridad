# Hackaton_CyberSeguridad
## Repositorio para desarrollar el proyecto del Hackaton 2023 organizado por la representación POJO del ITAM.


Es importante concientizar a los usuarios sobre los peligros de las distintas inteligencias artificiales. En el momento en que alguien escribe y envia un query que contiene información sensible o comprometedora, en ese momento renuncia a la privacidad de esa información y pasa a convertirse en dominio público. 

Proyecto: buscamos crear un filtro de seguridad en el que los usuarios puedan ingresar sus consultas; esta será evaluada de tal forma que se detecte la posibilidad de que contenga información sensible y palabras clave que comprometan la privacidad de esta información.

Ventajas: tiene tanto escalabilidad, ya que puede evolucionar y crecer con el desarrollo de las inteligencias artificiales; como personalización, ya que quien desee implementarlo puede otorgarle las palabras y secuencias de palabras de mayor peligro a detectar y por ende encontrarse más seguro.

Entrega: Jueves 17/11/2023 a las 11:59 pm.

Repartición de tareas:
    Alexa: 
        Función en la que se conecte las consultas con el API de las inteligencias artificiales (ChatGPT) y que se obtenga la respuesta de la consulta segura en el sitio web.
        Función en la que se evalua si una secuencia de caracteres tiene contenido peligroso a partir de un puntaje que se le asigna a partir de distintos parámetros.
    
    Braulio:
        Diseño de la información útil para la concientización de nuestros usuarios y enseñarles el por qué no deben publicar información personal en línea, incluso si parece inofensivo. Se divide en categorías según el peligro de la consulta.
    
    Fernando:
        Función de analisís de la consulta. Se separa la consulta en palabras, se obtienen las palabras clave y se verifica si alguna se debe marcar como información sensible.

    Santiago:
        Creación de la interfaz del sitio web.
        Integración de todas las funciones anteriores.

Tecnologías utilizadas:
    - Python.
    - API.
    - HTML.
    - Bootstrap con CSS.
    - JavaSccript.
    - Ajax.
    - Jqueries.
    - Servidores de AWS, c2 virtual server.
