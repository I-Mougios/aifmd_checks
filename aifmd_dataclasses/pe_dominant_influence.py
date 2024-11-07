# pe_dominant_influence.py
from common.data_processor import DataProcessor
from common.errors import *


class PE_Dominant_Influence(DataProcessor):
    all = []
    prov_obl_codes = {'pf_id': 'M', 'provider_id': 'C(M)', 'report_date': 'M', 'company_name': 'M',
                      'tra_type': 'M', 'tra_type_oth': 'M', 'voting_rights_rate': 'M',
                      'lei_code': 'O', 'bic_code': 'O'}

    datatypes = {'pf_id': ('VARCHAR2', 35), 'provider_id': ('VARCHAR2', 20), 'report_date': 'DATE',
                 'company_name': ('VARCHAR2', 1200), 'tra_type': ('VARCHAR2', 20), 'tra_type_oth': ('VARCHAR2', 1200),
                 'voting_rights_rate': ('NUMBER', 5, 2), 'lei_code': ('VARCHAR2', 20), 'bic_code': ('VARCHAR2', 11)}

    def __init__(self, pf_id=None, provider_id=None, report_date=None, company_name=None, tra_type=None,
                 tra_type_oth=None, voting_rights_rate=None, lei_code=None, bic_code=None, **kwargs):
        super().__init__()
        self.pf_id = pf_id
        self.provider_id = provider_id
        self.report_date = report_date
        self.company_name = company_name
        self.tra_type = tra_type
        self.tra_type_oth = tra_type_oth
        self.voting_rights_rate = voting_rights_rate
        self.lei_code = lei_code
        self.bic_code = bic_code

        self.__class__.all.append(self)

    def __repr__(self):
        return (
            f"PE_Dominant_influence("
            f"pf_id={repr(self.pf_id)}, "
            f"provider_id={repr(self.provider_id)}, "
            f"report_date={repr(self.report_date)}, "
            f"company_name={repr(self.company_name)}, "
            f"tra_type={repr(self.tra_type)}, "
            f"tra_type_oth={repr(self.tra_type_oth)}, "
            f"voting_rights_rate={repr(self.voting_rights_rate)}, "
            f"lei_code={repr(self.lei_code)}, "
            f"bic_code={repr(self.bic_code)}"
            f")"
        )


__all__ = ['PE_Dominant_Influence']
