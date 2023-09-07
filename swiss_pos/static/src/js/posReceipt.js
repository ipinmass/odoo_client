/** @odoo-module **/
import { Order } from 'point_of_sale.models';
import Registries from 'point_of_sale.Registries';

const posQuantityInfo = (Order) => class posQuantityInfo extends Order {
    
    export_for_printing() {
        const result = super.export_for_printing(...arguments);
        var producIids = new Set();
        var qtys = 0;
        for (const line of this.orderlines){
            producIids.add(line.product.id);
            qtys = qtys + line.quantity;
        }
        result.QuantityInfo = {producIids: producIids.size, qtys: qtys}
        
        return result;
    }
}

Registries.Model.extend(Order, posQuantityInfo);