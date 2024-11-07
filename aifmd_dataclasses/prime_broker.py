# prime_broker.py
from common.data_processor import DataProcessor
from common.errors import *


class Prime_Broker(DataProcessor):
    all = []
    prov_obl_codes = {'pf_id': 'M', 'report_date': 'M', 'broker_name': 'O',
                      'lei_code': 'C(O)', 'bic_code': 'C(O)'}

    datatypes = {'pf_id': ('VARCHAR2', 35), 'report_date': 'DATE', 'broker_name': ('VARCHAR2', 1200),
                 'lei_code': ('VARCHAR2', 20), 'bic_code': ('VARCHAR2', 11)}

    def __init__(self, pf_id=None, report_date=None, broker_name=None, lei_code=None, bic_code=None, **kwargs):

        super().__init__()
        self.pf_id = pf_id
        self.report_date = report_date
        self.broker_name = broker_name
        self.lei_code = lei_code
        self.bic_code = bic_code

        self.__class__.all.append(self)

    def __repr__(self):
        return (
            f"Prime_Broker("
            f"pf_id={repr(self.pf_id)}, "
            f"report_date={repr(self.report_date)}, "
            f"broker_name={repr(self.broker_name)}, "
            f"lei_code={repr(self.lei_code)}, "
            f"bic_code={repr(self.bic_code)}"
            f")"
        )


__all__ = ['Prime_Broker']
