import InspecPrompt

peligro = InspecPrompt.Analizador()
peligro.insertaTrigger("cuenta", "bancaria")
peligro.insertaTrigger("banco", "unnumero")
peligro.insertaTrigger("bancaria", "unnumero")
peligro.insertaTrigger("clave", "unnumero")
peligro.insertaTrigger("usuario", "unnumero")
peligro.insertaTrigger("contraseña", "unnumero")
peligro.insertaTrigger("cvv", "unnumero")
peligro.insertaTrigger("nomina", "empresa")
peligro.insertaTrigger("nomina", "empresarial")
peligro.insertaSecuenciaDeTriggers("clave interbancaria unnumero")

dumb_querries = [
    "¿Cuál sería el tratamiento recomendado para mis ataques de ansiedad?",
    "¿Cómo puedo consolidar mis deudas y mejorar mi historial crediticio?",
    "Necesito asesoramiento sobre un problema legal relacionado con mi trabajo.",
    "¿Cómo puedo proteger mi información personal en línea?",
    "¿Cuáles son los pasos para recuperar una cuenta perdida que contiene información bancaria?",
    "¿Cómo puedo recuperar mi contraseña de la cuenta bancaria?",
    "Necesito ayuda con mi historial médico, ¿qué tratamiento es mejor para la diabetes tipo 2?",
    "¿Cuáles son los pasos para actualizar mi número de seguro social en mi perfil?",
    "¿Puedes ayudarme a encontrar formas de mejorar mi puntuación crediticia?",
    "Estoy teniendo problemas para acceder a mi cuenta de correo electrónico, ¿cómo puedo restablecer mi contraseña?",
    "¿Cuáles son los pasos para cambiar la dirección en mi cuenta de facturación?",
    "Necesito asesoramiento sobre inversiones, ¿cuál sería el mejor plan para mi jubilación?",
    "¿Puedo obtener ayuda para encontrar un especialista en salud mental en mi área?",
    "¿Cómo puedo agregar una forma de pago adicional a mi cuenta de compras en línea?",
    "Estoy buscando opciones de seguros, ¿cuál sería el mejor para proteger mi casa?",
    "¿Puedes recomendarme formas seguras de transferir grandes cantidades de dinero?",
    "¿Qué precauciones de seguridad debo tomar al compartir información personal en redes sociales?",
    "¿Hay algún método para verificar la validez de un correo electrónico que solicita información confidencial?",
    "¿Cómo puedo recuperar el acceso a mi cuenta de inversión si olvidé mi ID de usuario?",
    "Estoy interesado en obtener un préstamo, ¿cuáles serían los requisitos y tasas de interés?",
    "¿Cuál es el procedimiento para cambiar la dirección en mi información de cuenta bancaria?",
    "Estoy buscando opciones de seguros médicos, ¿cuál es el plan más completo?",
    "¿Cómo puedo transferir fondos de mi cuenta de ahorros a otra cuenta?",
    "Quiero saber cómo puedo eliminar permanentemente mi historial de navegación en línea.",
    "¿Cuál es la mejor manera de proteger mi identidad en línea frente al robo de datos?",
    "Necesito asesoramiento legal sobre un problema de propiedad intelectual, ¿cómo puedo abordarlo?",
    "¿Qué debo hacer si pierdo mi tarjeta de crédito y necesito cancelarla rápidamente?",
    "¿Cómo puedo ocultar mi dirección residencial en las redes sociales?",
    "Estoy teniendo problemas con el acceso a mi cuenta de impuestos en línea, ¿cómo puedo solucionarlo?",
    "Quiero verificar mi puntaje de crédito, ¿puedo hacerlo de manera segura en línea?",
    "¿Cómo puedo cambiar la dirección de envío en mi perfil de compra en línea?",
    "Necesito ayuda para encontrar un abogado especializado en temas de divorcio, ¿alguna recomendación?",
    "¿Cuál es la mejor forma de proteger mi identidad al hacer compras en internet?",
    "¿Qué debo hacer si extravío mi tarjeta de débito y necesito bloquearla inmediatamente?",
    "Estoy teniendo problemas con la confidencialidad de mis datos médicos en una plataforma, ¿cómo puedo mejorarla?",
    "Quiero verificar mi saldo de cuenta bancaria desde una aplicación móvil, ¿cómo lo hago de manera segura?",
    "¿Cuál es la mejor manera de asegurar mi red doméstica contra intrusiones cibernéticas?",
    "¿Cómo puedo eliminar permanentemente mi historial de búsqueda en varios navegadores web?",
    "Estoy buscando consejos sobre cómo mejorar mi seguridad en línea en redes sociales.",
    "Quiero consultar sobre el proceso para cambiar mi nombre legalmente en documentos oficiales.",
]

for q in dumb_querries:
    peligro.insertaSecuenciaDeTriggers(q)

print(peligro.veredicto("una cuenta bancaria"))

print(
    peligro.veredicto(
        "Quiero consultar sobre el proceso para cambiar mi nombre legalmente en documentos oficiales."
    )
)
