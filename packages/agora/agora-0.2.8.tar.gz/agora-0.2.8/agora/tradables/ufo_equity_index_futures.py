###############################################################################
#
#   Agora Portfolio & Risk Management System
#
#   Copyright 2015 Carlo Sbraccia
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
###############################################################################

from onyx.core import (Structure, GraphNodeVt, GetVal, EvalBlock,
                       FloatField, StringField, ReferenceField)

from agora.corelibs.date_functions import DateOffset
from agora.corelibs.tradable_api import (AgingTradableObj,
                                         AddByInference, HashStoredAttrs)

from agora.tradables.ufo_cfd_fixed_leg import CfdFixedLeg
from agora.tradables.ufo_cfd_floating_leg import CfdFloatingLeg
from agora.tradables.ufo_forward_cash import ForwardCash

__all__ = ["EquityIndexFutures"]


###############################################################################
class EquityIndexFutures(AgingTradableObj):
    """
    Tradable class that represents a equity index futures contract.
    """
    Asset = ReferenceField(obj_type="EquityIndexCnt")
    FixedPrice = FloatField(positive=True)

    # --- the settlement currency can differ from the denomination of the asset
    SettlementCcy = ReferenceField(obj_type="Currency")

    # --- fx rate uesd to convert the fixed price (which is expressed in the
    #     currency of the asset) to the settlement currency
    SettlementFx = FloatField()

    # --- the date rule for the cash payment, defaults to 2 biz days after
    #     settlement
    PaymentDateRule = StringField("+2b")

    # -------------------------------------------------------------------------
    def __post_init__(self):
        asset_ccy = GetVal(self.Asset, "Denominated")

        self.SettlementCcy = self.SettlementCcy or asset_ccy

        if self.SettlementFx is None:
            # --- default to spot
            if asset_ccy == self.SettlementCcy:
                fx = 1.0
            else:
                asset_cross = "{0:3s}/USD".format(asset_ccy)
                sett_cross = "{0:3s}/USD".format(self.SettlementCcy)
                fx = GetVal(asset_cross, "Spot") / GetVal(sett_cross, "Spot")

            self.SettlementFx = fx

    # -------------------------------------------------------------------------
    @GraphNodeVt("Property")
    def Leaves(self, graph):
        asset = graph(self, "Asset")
        prc = graph(self, "FixedPrice")
        mul = graph(asset, "Multiplier")
        lot = graph(asset, "ContractSize")

        sett_ccy = graph(self, "SettlementCcy")
        sett_fx = graph(self, "SettlementFx")

        # --- leaves are created in memory
        floating = AddByInference(CfdFloatingLeg(Asset=asset), True)
        fixed = AddByInference(CfdFixedLeg(Currency=sett_ccy), True)

        return Structure({
            floating.Name: lot,
            fixed.Name: -lot*prc*mul*sett_fx,
        })

    # -------------------------------------------------------------------------
    @GraphNodeVt("Property")
    def MktValUSD(self, graph):
        mtm = 0.0
        for sec, qty in graph(self, "Leaves").items():
            mtm += qty*graph(sec, "MktValUSD")
        return mtm

    # -------------------------------------------------------------------------
    @GraphNodeVt("Property")
    def MktVal(self, graph):
        sett_ccy = graph(self, "SettlementCcy")
        spot_fx = graph("{0:3s}/USD".format(sett_ccy), "Spot")
        return graph(self, "MktValUSD") / spot_fx

    # -------------------------------------------------------------------------
    @GraphNodeVt("Property")
    def NextTransactionDate(self, graph):
        return graph(graph(self, "Asset"), "FutSettDate")

    # -------------------------------------------------------------------------
    @GraphNodeVt("Property")
    def TradeTypes(self, graph):
        mapping = super().TradeTypes
        mapping.update({
            "Settlement": "SettlementSecurities",
        })
        return mapping

    # -------------------------------------------------------------------------
    @GraphNodeVt("Property")
    def ExpectedTransaction(self, graph):
        return "Settlement"

    # -------------------------------------------------------------------------
    @GraphNodeVt("Property")
    def SettlementSecurities(self, graph):
        asset = graph(self, "Asset")
        sett_ccy = graph(self, "SettlementCcy")
        sett_date = graph(asset, "FutSettDate")
        pay_rule = graph(self, "PaymentDateRule")
        cal = graph(asset, "HolidayCalendar")

        cash = ForwardCash(Currency=sett_ccy,
                           PaymentDate=DateOffset(sett_date, pay_rule, cal))

        # --- the market value at the settlement date corresponds to the
        #     amount of cash that needs to exchange hands
        with EvalBlock() as eb:
            eb.set_diddle("Database", "MktDataDate", sett_date)
            pay_qty = graph(self, "MktVal")

        return [
            {"Security": AddByInference(cash, in_memory=True),
             "Quantity": pay_qty},
        ]

    # -------------------------------------------------------------------------
    @property
    def ImpliedName(self):
        sym = GetVal(self.Asset, "Symbol")
        mth = GetVal(self.Asset, "DeliveryMonth")
        mush = HashStoredAttrs(self, 4)
        return ("EqIdxFut {0:s} {1:3s} {2:3s} {3:4s} "
                "{{0:2d}}").format(sym, mth, self.SettlementCcy, mush)


# -----------------------------------------------------------------------------
def prepare_for_test():
    import agora.system.ufo_equity_index_contract as ufo_equity_index_contract
    import agora.tradables.ufo_forward_cash as ufo_forward_cash

    ufo_equity_index_contract.prepare_for_test()
    ufo_forward_cash.prepare_for_test()

    info = {
        "Asset": "CNT SX5E Z15",
        "FixedPrice": 3600.0,
    }

    securities = [AddByInference(EquityIndexFutures(**info))]

    return [sec.Name for sec in securities]
