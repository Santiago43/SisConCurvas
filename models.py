class Persona:
    def __init__(self, persona_ID,primerNombre,segundoNombre,primerApellido,segundoApellido,tipoDocumento,documento,telefono,correo):
        self.persona_ID=persona_ID
        self.primerNombre=primerNombre
        self.segundoNombre=segundoNombre
        self.primerApellido=primerApellido
        self.segundoApellido=segundoApellido
        self.tipoDocumento=tipoDocumento
        self.documento=documento
        self.telefono=telefono
        self.correo=correo
class Cliente(Persona):
    def __init__(self,cliente_ID,persona_ID,primerNombre,segundoNombre,primerApellido,segundoApellido,tipoDocumento,documento,telefono,correo):
        self.cliente_ID=cliente_ID
        Persona.__init__(persona_ID,primerNombre,segundoNombre,primerApellido,segundoApellido,tipoDocumento,documento,telefono,correo)
        