# risk_counterparty.py
from common.data_processor import DataProcessor
from common.errors import *


class Risk_Counterparty(DataProcessor):
    all = []
    prov_obl_codes = {'pf_id': 'M', 'nav_date': 'M', 'market_value_rate_sec_regm': 'O',
                      'market_value_rate_sec_otc': 'O', 'trade_volume_rate_deriv_regm': 'O',
                      'trade_volume_rate_deriv_otc': 'O', 'trade_volume_rate_deriv_ccp': 'O',
                      'trade_volume_rate_deriv_bltl': 'O', 'market_value_rate_repo_ccp': 'O',
                      'market_value_rate_repo_bltl': 'O', 'market_value_rate_repo_tdp': 'O',
                      'col_cash_pc': 'O', 'col_sec_pc': 'O', 'col_oth_pc': 'O'}

    datatypes = {'pf_id': ('VARCHAR2', 35), 'provider_id': ('VARCHAR2', 20), 'nav_date': 'DATE',
                 'market_value_rate_sec_regm': ('NUMBER', 5, 4), 'market_value_rate_sec_otc': ('NUMBER', 5, 4),
                 'trade_volume_rate_deriv_regm': ('NUMBER', 5, 4), 'trade_volume_rate_deriv_otc': ('NUMBER', 5, 4),
                 'trade_volume_rate_deriv_ccp': ('NUMBER', 5, 4), 'trade_volume_rate_deriv_bltl': ('NUMBER', 5, 4),
                 'market_value_rate_repo_ccp': ('NUMBER', 5, 4), 'market_value_rate_repo_bltl': ('NUMBER', 3, 2),
                 'market_value_rate_repo_tdp': ('NUMBER', 3, 2), 'col_cash_pc': ('NUMBER', 15, 0),
                 'col_sec_pc': ('NUMBER', 15, 0), 'col_oth_pc': ('NUMBER', 15, 0)}

    def __init__(self, pf_id=None, provider_id=None, nav_date=None, market_value_rate_sec_regm=None,
                 market_value_rate_sec_otc=None, trade_volume_rate_deriv_regm=None, trade_volume_rate_deriv_otc=None,
                 trade_volume_rate_deriv_ccp=None, trade_volume_rate_deriv_bltl=None, market_value_rate_repo_ccp=None,
                 market_value_rate_repo_bltl=None, market_value_rate_repo_tdp=None, **kwargs):

        super().__init__()
        self.pf_id = pf_id
        self.provider_id = provider_id
        self.nav_date = nav_date
        self.market_value_rate_sec_regm = market_value_rate_sec_regm
        self.market_value_rate_sec_otc = market_value_rate_sec_otc
        self.trade_volume_rate_deriv_regm = trade_volume_rate_deriv_regm
        self.trade_colume_rate_deriv_otc = trade_volume_rate_deriv_otc
        self.trade_volume_rate_deriv_ccp = trade_volume_rate_deriv_ccp
        self.trade_volume_rate_deriv_bltl = trade_volume_rate_deriv_bltl
        self.market_value_rate_repo_ccp = market_value_rate_repo_ccp
        self.market_value_rate_repo_bltl = market_value_rate_repo_bltl
        self.market_value_rate_repo_tdp = market_value_rate_repo_tdp

        self.__class__.all.append(self)

    def __repr__(self):
        return (
            f"Risk_Counterparty("
            f"pf_id={repr(self.pf_id)}, "
            f"provider_id={repr(self.provider_id)}, "
            f"nav_date={repr(self.nav_date)}, "
            f"market_value_rate_sec_regm={repr(self.market_value_rate_sec_regm)}, "
            f"market_value_rate_sec_otc={repr(self.market_value_rate_sec_otc)}, "
            f"trade_volume_rate_deriv_regm={repr(self.trade_volume_rate_deriv_regm)}, "
            f"trade_volume_rate_deriv_otc={repr(self.trade_volume_rate_deriv_otc)}, "
            f"trade_volume_rate_deriv_ccp={repr(self.trade_volume_rate_deriv_ccp)}, "
            f"trade_volume_rate_deriv_bltl={repr(self.trade_volume_rate_deriv_bltl)}, "
            f"market_value_rate_repo_ccp={repr(self.market_value_rate_repo_ccp)}, "
            f"market_value_rate_repo_bltl={repr(self.market_value_rate_repo_bltl)}, "
            f"market_value_rate_repo_tdp={repr(self.market_value_rate_repo_tdp)}"
            f")"
        )


__all__ = ['Risk_Counterparty']
