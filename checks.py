def jala_o_no(fer, alexa):
    """_description_
        Regresa un mensaje que indica el riesgo de seguridad de la entrada. El riesgo de seguridad se calcula con base en
        dos valores: fer y alexa. fer es un valor entre 0 y 100 que indica el riesgo de seguridad de la entrada. alexa es
        un valor entre 0 y 5 que indica el riesgo de seguridad de la entrada. Si alexa es mayor o igual a 4, la entrada
        presenta un alto riesgo de seguridad. Si alexa es 3, la entrada presenta un riesgo de seguridad. Si alexa es menor
        o igual a 0, la entrada presenta un bajo riesgo de seguridad. Si alexa es mayor o igual a 1 y menor o igual a 2,
        se evalúa el valor de fer. Si fer es mayor o igual a 50, la entrada presenta un alto riesgo de seguridad. Si fer es
        menor o igual a 25, la entrada presenta un riesgo de seguridad. Si fer es mayor a 25 y menor a 50, la entrada
        presenta un bajo riesgo de seguridad.
    Args:
        fer (int): Un valor entre 0 y 100 que indica el riesgo de seguridad de la entrada.
        alexa (int): Un valor entre 0 y 5 que indica el riesgo de seguridad de la entrada.

    Returns:
        str: Un mensaje que indica el riesgo de seguridad de la entrada.
    """

    if alexa >= 4:
        return "La entrada presenta un alto riesgo de seguridad."
    elif alexa == 3:
        return "La entrada presenta un riesgo de seguridad."
    elif alexa <= 0:
        return "La entrada presenta un bajo riesgo de seguridad."
    else:
        if fer >= 50:
            return "La entrada presenta un alto riesgo de seguridad."
        elif fer <= 25:
            return "La entrada presenta un riesgo de seguridad."
        else:
            return "La entrada presenta un bajo riesgo de seguridad."
