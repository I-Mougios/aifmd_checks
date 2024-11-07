# lev_borrow_source.py
from common.data_processor import DataProcessor
from common.errors import *


class LEV_Borrow_Source(DataProcessor):
    all = []
    prov_obl_codes = {'pf_id': 'M', 'provider_id': 'C(M)', 'report_date': 'M', 'entity_name': 'M',
                      'lei_code': 'O', 'bic_code': 'O', 'lev_received_pc': 'M'}

    datatypes = {'pf_id': ('VARCHAR2', 35), 'provider_id': ('VARCHAR2', 20),
                 'report_date': 'DATE', 'entity_name': ('VARCHAR2', 1200), 'lei_code': ('VARCHAR2', 20),
                 'bic_code': ('VARCHAR2', 11), 'lev_received_pc': ('NUMBER', 15, 0)}

    def __init__(self, pf_id=None, provider_id=None, report_date=None, entity_name=None,
                 lei_code=None, bic_code=None, lev_received_pc=None, **kwargs):
        super().__init__()
        self.pf_id = pf_id
        self.provider_id = provider_id
        self.report_date = report_date
        self.entity_name = entity_name
        self.lei_code = lei_code
        self.bic_code = bic_code
        self.lev_received_pc = lev_received_pc

        self.__class__.all.append(self)

    def __repr__(self):
        return (
            f"LEV_Borrow_Source("
            f"pf_id={repr(self.pf_id)}, "
            f"provider_id={repr(self.provider_id)}, "
            f"report_date={repr(self.report_date)}, "
            f"entity_name={repr(self.entity_name)}, "
            f"lei_code={repr(self.lei_code)}, "
            f"bic_code={repr(self.bic_code)}, "
            f"lev_received_pc={repr(self.lev_received_pc)}"
            f")"
        )


__all__ = ['LEV_Borrow_Source']

