# -*- coding: utf-8 -*-
##############################################################################
# For copyright and license notices, see __openerp__.py file in module root
# directory
##############################################################################
from openerp import models, api
from openerp.exceptions import Warning as UserError


class Invoice(models.Model):
    _inherit = 'account.invoice'

    @api.multi
    def clean_internal_number(self):
        self.ensure_one()
        if int(self.sii_document_number) == self.journal_document_class_id.\
                sequence_id.number_next_actual-1:
            self.journal_document_class_id.sequence_id.number_next_actual -= 1
        # despliegue de wizard
        self.clean_relationships()
        self.write({'internal_number': False,
                    'sii_document_number': False,
                    # 'sii_document_class_id': False,
                    'sii_batch_number': False,
                    'sii_barcode': False,
                    'sii_barcode_img': False,'sii_message': False,
                    'sii_xml_request': False,
                    'sii_xml_response1': False,
                    'sii_xml_response2': False,
                    'sii_send_ident': False,
                    'sii_result': False})
