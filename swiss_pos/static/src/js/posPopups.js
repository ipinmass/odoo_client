odoo.define('swiss.ClosePosPopup', function (require) {
    'use strict';

    const ClosePosPopup = require('point_of_sale.ClosePosPopup');
    const Registries = require('point_of_sale.Registries');

    const swissPosClosePopup = (ClosePosPopup) =>
        class extends ClosePosPopup {
            async downloadSalesReport() {
                await this.env.legacyActionManager.do_action('swiss_pos.sale_details_report', {
                    additional_context: {
                        active_ids: [this.env.pos.pos_session.id],
                        swissPosClosePopup: 1,
                    },
                });
            }
        };

    Registries.Component.extend(ClosePosPopup, swissPosClosePopup);

    return ClosePosPopup;
});
