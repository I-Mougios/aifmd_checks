# risk_other.py
from common.data_processor import DataProcessor
from common.errors import *


class Risk_Other(DataProcessor):

    all = []
    datatypes = {'pf_id': ('VARCHAR2', 35), 'provider_id': ('VARCHAR2', 20), 'nav_date': 'DATE',
                 'unsecured_brw_pc': ('NUMBER', 15, 0), 'secured_brw_pc': ('NUMBER', 15, 0),
                 'secured_brw_repo_pc': ('NUMBER', 15, 0), 'secured_brw_oth_pc': ('NUMBER', 15, 0),
                 'exp_deriv_et_pc': ('NUMBER', 15, 0), 'exp_deriv_otc_pc': ('NUMBER', 15, 0),
                 'short_pos_brw_sec_pc': ('NUMBER', 15, 0), 'open_position': ('NUMBER', 15, 0)}

    prov_obl_codes = {'pf_id': 'M', 'provider_id': 'C(M)', 'nav_date': 'M', 'unsecured_brw_pc': 'M',
                      'secured_brw_pc': 'M', 'secured_brw_repo_pc': 'M', 'secured_brw_oth_pc': 'M',
                      'exp_deriv_et_pc': 'O', 'exp_deriv_otc_pc': 'O', 'short_pos_brw_sec_pc': 'M',
                      'open_position': 'O'}

    def __init__(self, pf_id=None, provider_id=None, nav_date=None, unsecured_brw_pc=None, secured_brw_pc=None,
                 secured_brw_repo_pc=None, secured_brw_oth_pc=None, exp_deriv_et_pc=None, exp_deriv_otc_pc=None,
                 short_pos_brw_sec_pc=None, open_position=None, **kwargs):
        super().__init__()

        self.pf_id = pf_id
        self.provider_id = provider_id
        self.nav_date = nav_date
        self.unsecured_brw_pc = unsecured_brw_pc
        self.secured_brw_pc = secured_brw_pc
        self.secured_brw_repo_pc = secured_brw_repo_pc
        self.secured_brw_oth_pc = secured_brw_oth_pc
        self.exp_deriv_et_pc = exp_deriv_et_pc
        self.exp_deriv_otc_pc = exp_deriv_otc_pc
        self.short_pos_brw_sec_pc = short_pos_brw_sec_pc
        self.open_position = open_position

        self.__class__.all.append(self)

    def __repr__(self):
        return (
            f"Risk_Other("
            f"pf_id={repr(self.pf_id)}, "
            f"provider_id={repr(self.provider_id)}, "
            f"nav_date={repr(self.nav_date)}, "
            f"unsecured_brw_pc={repr(self.unsecured_brw_pc)}, "
            f"secured_brw_pc={repr(self.secured_brw_pc)}, "
            f"secured_brw_repo_pc={repr(self.secured_brw_repo_pc)}, "
            f"secured_brw_oth_pc={repr(self.secured_brw_oth_pc)}, "
            f"exp_deriv_et_pc={repr(self.exp_deriv_et_pc)}, "
            f"exp_deriv_otc_pc={repr(self.exp_deriv_otc_pc)}, "
            f"short_pos_brw_sec_pc={repr(self.short_pos_brw_sec_pc)}, "
            f"open_position={repr(self.open_position)}"
            f")"
        )


__all__ = ['Risk_Other']
