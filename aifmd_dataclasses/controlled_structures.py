# controlled_structures.py
from common.data_processor import DataProcessor
from common.errors import *


class Controlled_Structures(DataProcessor):
    all = []
    prov_obl_codes = {'pf_id': 'M', 'provider_id': 'C(M)', 'nav_date': 'M', 'entity_name': 'O',
                      'lei_code': 'O', 'bic_code': 'O', 'exp_value_pc': 'M'}

    datatypes = {'pf_id': ('VARCHAR2', 35), 'provider_id': ('VARCHAR2', 20), 'nav_date': 'DATE',
                 'entity_name': ('VARCHAR2', 1200), 'lei_code': ('VARCHAR2', 20), 'bic_code': ('VARCHAR2', 11),
                 'exp_value_pc': ('NUMBER', 15, 0)}

    def __init__(self, pf_id=None, provider_id=None, nav_date=None, entity_name=None,
                 lei_code=None, bic_code=None, exp_value_pc=None, **kwargs):
        super().__init__()
        self.pf_id = pf_id
        self.provider_id = provider_id
        self.nav_date = nav_date
        self.entity_name = entity_name
        self.lei_code = lei_code
        self.bic_code = bic_code
        self.exp_value_pc = exp_value_pc

        self.__class__.all.append(self)

    def __repr__(self):
        return (
            f"Controlled_Structures("
            f"pf_id={repr(self.pf_id)}, "
            f"provider_id={repr(self.provider_id)}, "
            f"nav_date={repr(self.nav_date)}, "
            f"entity_name={repr(self.entity_name)}, "
            f"lei_code={repr(self.lei_code)}, "
            f"bic_code={repr(self.bic_code)}, "
            f"exp_value_pc={repr(self.exp_value_pc)}"
            f")"
        )


__all__ = ['Controlled_Structures']