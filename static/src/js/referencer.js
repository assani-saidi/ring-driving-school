odoo.define("point_of_sale.OrderReferencer", function (require) {
  "use strict";

  const { useState, Component } = owl;
  const { xml } = owl.tags;
  const Registries = require("point_of_sale.Registries");
  const PosComponent = require("point_of_sale.PosComponent");
  const rpc = require("web.rpc");

  class OrderReferencer extends PosComponent {
    // is much simpler to call than the constructor
    setup() {
      super.setup();
      this.state = useState({
        reference: "",
      });
    }

    // called when component is mounted: React style
    mounted() {
      this.GetStuff();
    }

    async GetStuff() {
      const _order = await rpc.query({
        model: "pos.order",
        method: "search_read",
        args: [[["pos_reference", "=", this.currentOrder.name]], ["name"]],
      });

      console.warn("order_names", _order);
      this.state.reference = _order[0].name;
    }

    // borrowed: we are able to have access to our current order
    get currentOrder() {
      return this.env.pos.get_order();
    }
  }

  OrderReferencer.template = xml`
    <div style="padding-top: 4px; font-size: 1.3em;">
        <b><t t-esc="state.reference"/></b>
    </div>`;

  Registries.Component.add(OrderReferencer);

  return OrderReferencer;
});
