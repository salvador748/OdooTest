# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions, _
import re


class LibValidaciones(models.TransientModel):
    _name = 'lib.validaciones'

    @api.model
    def correo(self, correo):
        if correo:
            regex_email = re.compile(
                r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)'
            )
            if not bool(regex_email.match(correo)):
                raise exceptions.ValidationError(_("Formato incorrecto del correo"))

    @api.model
    def rfc(self, rfc, persona='fisica'):
        persona = str(self.eliminar_acentos(persona)).lower()
        if persona == 'fisica':
            pass
        elif persona == 'moral':
            pass
        else:
            raise exceptions.MissingError(_("El tipo de persona solo puede ser fisica/moral."))

    @api.model
    def rfc_moral(self, rfc):
        self.rfc(rfc, 'moral')

    @api.model
    def rfc_fisica(self, rfc):
        self.rfc(rfc, 'fisica')

    @api.model
    def eliminar_acentos(self, texto):
        texto = str(texto).replace('í', 'i')
        return texto

    @api.model
    def telefono(self):
        pass

    @api.model
    def seguro_social(self):
        pass

    @api.model
    def numero_cuenta_bancaria(self, cuenta):
        pass

    @api.model
    def clabe_bancaria(self, clabe):
        pass
   