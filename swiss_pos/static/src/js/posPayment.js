odoo.define('swiss_pos.PaymentScreen', function(require) {
    "use strict";

    const PaymentScreen = require('point_of_sale.PaymentScreen');
    const Registries = require('point_of_sale.Registries');
    const { onMounted } = owl;
    const { useListener } = require("@web/core/utils/hooks");
    var {Payment} = require('point_of_sale.models')

    const swissPosPaymentScreen = PaymentScreen => class extends PaymentScreen {
        setup() {
        super.setup();
        useListener('update-payment-card-no', this.updatePaymentCardNo);
        }
        updatePaymentCardNo(event) {
            const { cid } = event.detail;
            const line = this.paymentLines.find((line) => line.cid === cid);
            const cardInput = $('input.input-card-number')
            if (cardInput.length > 0 && line){
                line.card_number = cardInput[0].value
            }

        }
    };
    const swssPosPayment = (Payment) => class swssPosPayment extends Payment{
        constructor(obj, options) {
            super(...arguments);
            this.card_number = this.card_number || options.card_number
        }
        init_from_JSON(json) {
            super.init_from_JSON(...arguments);
            this.card_number = json.card_number;

        }
        export_as_JSON() {
            const json = super.export_as_JSON(...arguments);
            json.card_number = this.card_number;
            return json;
        }

    }

    Registries.Component.extend(PaymentScreen, swissPosPaymentScreen);
    Registries.Model.extend(Payment, swssPosPayment);

    return {
        PaymentScreen,

    };
});
