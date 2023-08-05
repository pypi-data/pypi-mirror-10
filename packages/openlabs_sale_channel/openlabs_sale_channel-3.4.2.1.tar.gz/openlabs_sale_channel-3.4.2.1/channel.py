# -*- coding: utf-8 -*-
"""
    sale_channel.py

    :copyright: (c) 2015 by Openlabs Technologies & Consulting (P) Limited
    :license: BSD, see LICENSE for more details.
"""
from trytond.pool import PoolMeta, Pool
from trytond.transaction import Transaction
from trytond.pyson import Eval
from trytond.model import ModelView, fields, ModelSQL
from trytond.wizard import (
    Wizard, StateView, Button, StateTransition, StateAction
)

__metaclass__ = PoolMeta
__all__ = [
    'SaleChannel', 'ReadUser', 'WriteUser', 'ChannelException',
    'OrderImportWizard', 'OrderImportWizardStart'
]

STATES = {
    'readonly': ~Eval('active', True),
}
DEPENDS = ['active']

PRODUCT_STATES = {
    'invisible': ~(Eval('source') != 'manual'),
    'required': Eval('source') != 'manual',
}


class SaleChannel(ModelSQL, ModelView):
    """
    Sale Channel model
    """
    __name__ = 'sale.channel'

    name = fields.Char(
        'Name', required=True, select=True, states=STATES, depends=DEPENDS
    )
    code = fields.Char(
        'Code', select=True, states={'readonly': Eval('code', True)},
        depends=['code']
    )
    active = fields.Boolean('Active', select=True)
    company = fields.Many2One(
        'company.company', 'Company', required=True, select=True,
        states=STATES, depends=DEPENDS
    )
    address = fields.Many2One(
        'party.address', 'Address', domain=[
            ('party', '=', Eval('company_party')),
        ], depends=['company_party']
    )
    source = fields.Selection(
        'get_source', 'Source', required=True, states=STATES, depends=DEPENDS
    )

    read_users = fields.Many2Many(
        'sale.channel-read-res.user', 'channel', 'user', 'Read Users'
    )
    create_users = fields.Many2Many(
        'sale.channel-write-res.user', 'channel', 'user', 'Create Users'
    )

    warehouse = fields.Many2One(
        'stock.location', "Warehouse", required=True,
        domain=[('type', '=', 'warehouse')]
    )
    invoice_method = fields.Selection(
        [
            ('manual', 'Manual'),
            ('order', 'On Order Processed'),
            ('shipment', 'On Shipment Sent')
        ], 'Invoice Method', required=True
    )
    shipment_method = fields.Selection(
        [
            ('manual', 'Manual'),
            ('order', 'On Order Processed'),
            ('invoice', 'On Invoice Paid'),
        ], 'Shipment Method', required=True
    )
    currency = fields.Many2One(
        'currency.currency', 'Currency', required=True
    )
    price_list = fields.Many2One(
        'product.price_list', 'Price List', required=True
    )
    payment_term = fields.Many2One(
        'account.invoice.payment_term', 'Payment Term', required=True
    )
    company_party = fields.Function(
        fields.Many2One('party.party', 'Company Party'),
        'on_change_with_company_party'
    )

    # These fields would be needed at the time of product imports from
    # external channel
    default_uom = fields.Many2One(
        'product.uom', 'Default Product UOM',
        states=PRODUCT_STATES, depends=['source']
    )

    default_account_expense = fields.Property(fields.Many2One(
        'account.account', 'Account Expense', domain=[
            ('kind', '=', 'expense'),
            ('company', '=', Eval('company')),
        ], depends=['company', 'source'], states=PRODUCT_STATES
    ))

    default_account_revenue = fields.Property(fields.Many2One(
        'account.account', 'Account Revenue', domain=[
            ('kind', '=', 'revenue'),
            ('company', '=', Eval('company')),
        ], depends=['company', 'source'], states=PRODUCT_STATES,
    ))

    exceptions = fields.One2Many(
        'channel.exception', 'channel', 'Exceptions', readonly=True
    )

    @classmethod
    def __setup__(cls):
        """
        Setup the class before adding to pool
        """
        super(SaleChannel, cls).__setup__()
        cls._buttons.update({
            'import_orders_button': {},
        })

    @staticmethod
    def default_default_uom():
        Uom = Pool().get('product.uom')

        unit = Uom.search([('name', '=', 'Unit')])

        return unit and unit[0].id or None

    @classmethod
    def get_source(cls):
        """
        Get the source
        """
        return [('manual', 'Manual')]

    @staticmethod
    def default_active():
        return True

    @staticmethod
    def default_currency():
        pool = Pool()
        Company = pool.get('company.company')
        Channel = pool.get('sale.channel')

        company_id = Channel.default_company()
        company = Company(company_id)
        return company.currency.id

    @staticmethod
    def default_company():
        return Transaction().context.get('company')

    @fields.depends('company')
    def on_change_with_company_party(self, name=None):
        Company = Pool().get('company.company')
        company = self.company
        if not company:
            company = Company(SaleChannel.default_company())  # pragma: nocover
        return company and company.party.id or None

    def import_orders(self):
        """
        Import orders from external channel.

        Since external channels are implemented by downstream modules, it is
        the responsibility of those channels to implement importing or call
        super to delegate.

        :return: List of active records of sale orders that are imported
        """
        raise self.raise_user_error(
            "Import orders is not implemented for %s channels" % self.source
        )

    def import_order(self, order_info):
        """
        Import specific order from external channel based on order_info.

        Since external channels are implemented by downstream modules, it is
        the responsibility of those channels to implement importing or call
        super to delegate.

        :param order_info: The type of order_info depends on the channel. It
                           could be an integer ID, a dictionary or anything.

        :return: imported sale order active record
        """
        raise self.raise_user_error(
            "Import order is not implemented for %s channels" % self.source
        )

    @classmethod
    @ModelView.button_action('sale_channel.wizard_import_orders')
    def import_orders_button(cls, channels):
        pass  # pragma: nocover


class ReadUser(ModelSQL):
    """
    Read Users for Sale Channel
    """
    __name__ = 'sale.channel-read-res.user'

    channel = fields.Many2One(
        'sale.channel', 'Channel', ondelete='CASCADE', select=True,
        required=True
    )
    user = fields.Many2One(
        'res.user', 'User', ondelete='RESTRICT', required=True
    )


class WriteUser(ModelSQL):
    """
    Write Users for Sale Channel
    """
    __name__ = 'sale.channel-write-res.user'

    channel = fields.Many2One(
        'sale.channel', 'Channel', ondelete='CASCADE', select=True,
        required=True
    )
    user = fields.Many2One(
        'res.user', 'User', ondelete='RESTRICT', required=True
    )


class ChannelException(ModelSQL, ModelView):
    """
    Channel Exception model
    """
    __name__ = 'channel.exception'

    origin = fields.Reference(
        "Origin", selection='models_get', select=True, readonly=True
    )
    log = fields.Text('Exception Log', readonly=True)
    channel = fields.Many2One(
        "sale.channel", "Channel", required=True, readonly=True
    )

    @classmethod
    def models_get(cls):
        '''
        Return valid models allowed for origin
        '''
        return [
            ('sale.sale', 'Sale'),
            ('sale.line', 'Sale Line'),
        ]


class OrderImportWizardStart(ModelView):
    "Import Sale Order Start View"
    __name__ = 'sale.channel.orders_import.start'

    message = fields.Text("Message", readonly=True)


class OrderImportWizard(Wizard):
    "Wizard to import sale order from channel"
    __name__ = 'sale.channel.orders_import'

    start = StateView(
        'sale.channel.orders_import.start',
        'sale_channel.import_order_start_view_form',
        [
            Button('Cancel', 'end', 'tryton-cancel'),
            Button('Continue', 'next', 'tryton-go-next'),
        ]
    )
    next = StateTransition()
    import_ = StateAction('sale_channel.act_sale_form_all')

    def default_start(self, data):
        """
        Sets default data for wizard

        :param data: Wizard data
        """
        Channel = Pool().get('sale.channel')

        channel = Channel(Transaction().context.get('active_id'))
        return {
            'message':
                "This wizard will import all sale orders placed on "
                "%s channel(%s) on after the Last Order Import "
                "Time. If Last Order Import Time is missing, then it will "
                "import all the orders from beginning of time. [This might "
                "be slow depending on number of orders]." % (
                    channel.name, channel.source
                )
        }

    def transition_next(self):
        """
        Downstream channel implementation can customize the wizard
        """
        return "import_"

    def do_import_(self, action):
        """
        Import Orders from channel
        """
        Channel = Pool().get('sale.channel')

        channel = Channel(Transaction().context.get('active_id'))
        sales = channel.import_orders()
        data = {'res_id': [sale.id for sale in sales]}
        return action, data
