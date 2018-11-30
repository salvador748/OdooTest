from odoo import models, fields, exceptions, api, _
import base64


class LibWizard(models.TransientModel):
    _name = 'lib.wizard'

    fecha_inicio = fields.Date(string=_("Fecha inicio"))
    fecha_fin = fields.Date(string=_("Fecha fin"))

    fecha_hora_inicio = fields.Datetime(string=_("Fecha inicio"))
    fecha_hora_fin = fields.Datetime(string=_("Fecha fin"))

    usuario_creo_documento = fields.Many2one(
        comodel_name='res.users', string="Usuario creó documento")

    usuario_modifico_documento = fields.Many2one(
        comodel_name='res.users', string="Usuario modificó documento")

    tipo_reporte = fields.Char(string=("Tipo de reporte"))

    @api.multi
    def exportar_pdf(self):
        pass

    @api.multi
    def exportar_csv(self, registros=False, campos=[], encabezados=[], nombre_archivo=False, modelo=False):
        print("Principal")
        if registros and len(registros) > 0:
            print(registros)
            datas = registros.export_data(campos) or {}
            if datas.get('datas', False):
                filas = datas.get('datas')  # [[...],[...]]
                csv = ""
                for encabezado in encabezados:
                    csv = encabezado + ","
                csv += "\n"
                for fila in filas:
                    for valor in fila:
                        csv += str(valor) + ","
                    csv += "\n"
                archivo_base64 = base64.b64encode(bytes(csv.encode('utf-8')))
                archivo_area_ids = self.env['ir.attachment'].sudo().search([
                    ('res_model', '=', modelo)
                ])
                if len(archivo_area_ids) > 0:
                    archivo_area_ids.unlink()
                archivo_area_id = self.env['ir.attachment'].sudo().create({
                    'name': nombre_archivo + '.csv',
                    'datas_fname': nombre_archivo + '.csv',
                    'type': 'binary',  # url, store
                    'datas': archivo_base64,
                    'res_model': modelo,  # recursos_materiales.oficio
                    # 'res_id': ''  #  10
                    'mimetype': 'text/csv'  # application/csv text/html ....
                })
                return {
                    'type': 'ir.actions.act_url',
                    'url': '/web/content?id={}&download=True'.format(archivo_area_id.id),
                    'target': 'self'  # new https://qps.com
                }
        return False

    @api.multi
    def exportar_odt(self):
        pass

    @api.multi
    def export_xsl(self):
        pass

    @api.multi
    def enviar_por_correo(self):
        pass

    @api.model
    def obtener_rango_fechas(self):
        condicion = []
        if self.fecha_inicio:
            condicion.append(('create_date', '>=', self.fecha_inicio))
        if self.fecha_fin:
            condicion.append(('create_date', '<=', self.fecha_fin))
        return condicion

    @api.model
    def obtener_rango_fecha_horas(self):
        pass
