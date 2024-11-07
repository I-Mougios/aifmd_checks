# shareclasses.py
from common.data_processor import DataProcessor
from common.errors import *


class Shareclasses(DataProcessor):
    all = []
    prov_obl_codes = {'pf_id': 'M', 'provider_id': 'C(M)', 'report_date': 'M', 'sc_id': 'M', 'sc_name': 'M',
                      'active': 'M', 'nca_code': 'O', 'isin': 'O', 'sedol': 'O', 'cusip': 'O', 'bloomberg': 'O',
                      'ric_code': 'O'}

    datatypes = {'pf_id': ('VARCHAR2', 35), 'provider_id': ('VARCHAR2', 20), 'report_date': 'DATE',
                 'sc_id': ('VARCHAR2', 20), 'sc_name': ('VARCHAR2', 1200), 'active': ('CHAR', 1),
                 'nca_code': ('VARCHAR2', 30), 'isin': ('VARCHAR2', 12), 'sedol': ('VARCHAR2', 7),
                 'cusip': ('VARCHAR2', 9), 'bloomberg': ('VARCHAR2', 20), 'ric_code': ('VARCHAR2', 20)}

    def __init__(self, pf_id=None, provider_id=None, report_date=None, sc_id=None, sc_name=None, active=None,
                 nca_code=None, isin=None, sedol=None, cusip=None, bloomberg=None, ric_code=None, **kwargs):

        super().__init__()
        self.pf_id = pf_id
        self.provider_id = provider_id
        self.report_date = report_date
        self.sc_id = sc_id
        self.sc_name = sc_name
        self.active = active
        self.nca_code = nca_code
        self.isin = isin
        self.sedol = sedol
        self.cusip = cusip
        self.bloomberg = bloomberg
        self.ric_code = ric_code

        self.__class__.all.append(self)

    def __repr__(self):
        return (
                f"Shareclasses("
                f"pf_id={repr(self.pf_id)}, "
                f"provider_id={repr(self.provider_id)}, "
                f"report_date={repr(self.report_date)}, "
                f"sc_id={repr(self.sc_id)}, "
                f"sc_name={repr(self.sc_name)}, "
                f"active={repr(self.active)}, "
                f"nca_code={repr(self.nca_code)}, "
                f"isin={repr(self.isin)}, "
                f"sedol={repr(self.sedol)}, "
                f"cusip={repr(self.cusip)}, "
                f"bloomberg={repr(self.bloomberg)}, "
                f"ric_code={repr(self.ric_code)}"
                f")"
            )


__all__ = ['Shareclasses']

