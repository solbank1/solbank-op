from odoo import models, fields

class Giro(models.Model):
    _name = 'solbank.giro'
    _description = 'Giros de dinero'

    nombre = fields.Char(string='Nombre del cliente', required=True)
    origen = fields.Char(string='País origen', required=True)
    destino = fields.Char(string='País destino', required=True)
    moneda = fields.Selection([
        ('USD', 'Dólar estadounidense'),
        ('ARS', 'Peso argentino'),
        ('USDT', 'USDT'),
        ('EUR', 'Euro'),
        ('BRL', 'Real'),
        ('CLP', 'Peso chileno'),
        ('PEN', 'Sol peruano'),
        ('PYG', 'Guaraní paraguayo')
    ], string='Moneda', required=True)
    monto = fields.Float(string='Monto')
    comision = fields.Float(string='Comisión (%)')
    total = fields.Float(string='Total con comisión', compute='_calcular_total', store=True)
    fecha = fields.Datetime(string='Fecha', default=fields.Datetime.now)
    estado = fields.Selection([
        ('pendiente', 'Pendiente'),
        ('enviado', 'Enviado'),
        ('entregado', 'Entregado'),
        ('cancelado', 'Cancelado')
    ], string='Estado', default='pendiente')

    def cambiar_estado(self, nuevo_estado):
        self.estado = nuevo_estado

    @api.depends('monto', 'comision')
    def _calcular_total(self):
        for record in self:
            if record.monto and record.comision:
                record.total = record.monto * (1 + (record.comision / 100))
            else:
                record.total = record.monto
