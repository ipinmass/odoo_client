###################################################################################
# 
#    Copyright (C) Cetmix OÜ
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU LESSER GENERAL PUBLIC LICENSE as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU LESSER GENERAL PUBLIC LICENSE for more details.
#
#    You should have received a copy of the GNU LESSER GENERAL PUBLIC LICENSE
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###################################################################################

{
    "name": "POS swiss",
    "version": "16.0.0",
    "summary": """
    
""",
    "author": "Ipin",
    "category": "Productivity",
    "license": "LGPL-3",
    "website": "",
    "live_test_url": "",
    "depends": [
            "point_of_sale",
        ],
    'data':[
       

        ],
    "images": [],
    'assets': {
        'point_of_sale.assets': [
            'swiss_pos/static/src/js/**/*',
            'swiss_pos/static/src/xml/*.xml',
        ],
    },
    "installable": True,
    "application": False,
    "auto_install": False,
}
