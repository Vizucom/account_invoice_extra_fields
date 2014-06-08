# -*- coding: utf-8 -*-
##############################################################################
#
#   Copyright (c) 2014- Vizucom Oy (http://www.vizucom.com)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': 'Extra invoice fields from Sale Order',
    'category': 'Sales',
    'version': '0.2',
    'author': 'Vizucom Oy',
    'website': 'http://www.vizucom.com',
    'depends': ['sale_basic_extensions'],
    'description': """
Extra invoice fields from Sale Order
====================================
Adds the following fields to customer invoice:
----------------------------------------------
* Customer contact person
* Shipping address
The default values get carried over from sale order. 
""",
    'data': [
        'view/account_invoice.xml',
    ],
}
