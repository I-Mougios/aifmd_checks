# ccp_clearing.py
from common.data_processor import DataProcessor
from common.errors import *


class CCP_Clearing(DataProcessor):
    all = []
    prov_obl_codes = {'pf_id': 'M', 'provider_id': 'M', 'report_date': 'M',
                      'ccp_name': 'M', 'lei_code': 'O', 'bic_code': 'O', 'exp_value_pc': 'M'}

    datatypes = {'pf_id': ('VARCHAR2', 35), 'provider_id': ('VARCHAR2', 20), 'report_date': 'DATE',
                 'ccp_name': ('VARCHAR2', 1200), 'lei_code': ('VARCHAR2', 20), 'bic_code': ('VARCHAR2', 11),
                 'exp_value_pc': ('NUMBER', 15, 0)}

    def __init__(self, pf_id=None, provider_id=None, report_date=None, ccp_name=None,
                 lei_code=None, bic_code=None, exp_value_pc=None, **kwargs):
        super().__init__()
        self.pf_id = pf_id
        self.provider_id = provider_id
        self.report_date = report_date
        self.ccp_name = ccp_name
        self.lei_code = lei_code
        self.bic_code = bic_code
        self.exp_value_pc = exp_value_pc

        self.__class__.all.append(self)

    def __repr__(self):
        return (
            f"CCP_Cleaning("
            f"pf_id={repr(self.pf_id)}, "
            f"provider_id={repr(self.provider_id)}, "
            f"report_date={repr(self.report_date)}, "
            f"ccp_name={repr(self.ccp_name)}, "
            f"lei_code={repr(self.lei_code)}, "
            f"bic_code={repr(self.bic_code)}, "
            f"exp_value_pc={repr(self.exp_value_pc)}"
            f")"
        )


__all__ = ['CCP_Clearing']



