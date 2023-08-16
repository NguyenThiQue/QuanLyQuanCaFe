odoo.define("POS.pos", function(require){
    "use strict";

    var dis_btn = require('pos_discount.pos_discount')
    var session = require('web.session')
    var core = require('web.core')
    var _t = core._t

    dis_btn.DiscountButton.include({
        button_clik:function(){

            var self = this;
            var sup = self._super()

            session.user_has_group('POS.qlcf_group_user').then(
                function(has_group){
                    if(has_group){
                        return sup
                    }
                    else {
                        self.gui.show_popup('error', {
                            'title': _t('Discount restriction'),
                            'body': _t("You have no access to discount")
                        })
                    }
                }
            )
        }
    })
})