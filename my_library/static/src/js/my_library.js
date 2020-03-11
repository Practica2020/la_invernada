odoo.define('my_library', function (require) {
    var core = require('web.core');

    alert(core._t('Su hola mundo piola'));
    return {
        // if you created functionality to export, add it here
    }
});
