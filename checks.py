def jala_o_no(fer, alexa):
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
