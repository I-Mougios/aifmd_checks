# risk_historical.py
from common.data_processor import DataProcessor
from common.errors import *


class Risk_Historical(DataProcessor):

    all = []
    datatypes = {'pf_id': ('VARCHAR2', 35), 'provider_id': ('VARCHAR2', 20), 'nav_date': 'DATE',
                 'gross_inv_return_rate': ('NUMBER', 17, 4), 'net_inv_return_rate': ('NUMBER', 17, 4),
                 'subscription_value': ('NUMBER', 22, 6), 'redemption_value': ('NUMBER', 22, 6),
                 'nav_chg_rate': ('NUMBER', 17, 4)}

    prov_obl_codes = {'pf_id': 'M', 'provider_id': 'C(M)', 'nav_date': 'M', 'gross_inv_return_rate': 'M',
                      'net_inv_return_rate': 'M', 'subscription_value': 'M',
                      'redemption_value': 'M', 'nav_chg_rate': 'M'}

    def __init__(self, pf_id=None, provider_id=None, nav_date=None, gross_inv_return_rate=None, net_inv_return_rate=None
                 , subscription_value=None, redemption_value=None, nav_chg_rate=None, **kwargs):

        super().__init__()
        self.pf_id = pf_id
        self.provider_id = provider_id
        self.nav_date = nav_date
        self.gross_inv_return_rate = gross_inv_return_rate
        self.net_inv_return_rate = net_inv_return_rate
        self.subscription_value = subscription_value
        self.redemption_value = redemption_value
        self.nav_chg_rate = nav_chg_rate

        self.__class__.all.append(self)


    def __repr__(self):
        return (
            f"Risk_Historical("
            f"pf_id={repr(self.pf_id)}, "
            f"provider_id={repr(self.provider_id)}, "
            f"nav_date={repr(self.nav_date)}, "
            f"gross_inv_return_rate={repr(self.gross_inv_return_rate)}, "
            f"net_inv_return_rate={repr(self.net_inv_return_rate)}, "
            f"subscription_value={repr(self.subscription_value)}, "
            f"redemption_value={repr(self.redemption_value)}, "
            f"nav_chg_rate={repr(self.nav_chg_rate)}"
            f")"
        )


__all__ = ['Risk_Historical']