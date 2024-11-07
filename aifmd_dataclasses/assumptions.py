# assumptions.py
from common.data_processor import DataProcessor
from common.errors import *


class Assumptions(DataProcessor):
    all = []

    prov_obl_codes = {'fm_name': 'M', 'pf_id': 'M', 'provider_id': 'C(M)', 'report_date': 'M',
                      'rep_type': 'M', 'question_nr': 'M', 'assum_desc': 'M', 'member_ctry_code': 'M'}

    datatypes = {'fm_name': ('VARCHAR2', 200), 'pf_id': ('VARCHAR2', 35), 'provider_id': ('VARCHAR2', 20),
                 'report_date': 'DATE', 'rep_type': ('VARCHAR2', 4), 'question_nr': ('NUMBER', 3, 0),
                 'assum_desc': ('VARCHAR2', 1200), 'member_ctry_code': ('VARCHAR2', 2)}

    def __init__(self, fm_name=None, pf_id=None, provider_id=None, report_date=None, rep_type=None, question_nr=None,
                 assum_desc=None, member_ctry_code=None, **kwargs):

        super().__init__()
        self.fm_name = fm_name
        self.pf_id = pf_id
        self.provider_id = provider_id
        self.report_date = report_date
        self.rep_type = rep_type
        self.question_nr = question_nr
        self.assum_desc = assum_desc
        self.member_ctry_code = member_ctry_code

        self.__class__.all.append(self)

    def __repr__(self):
        return (
            f"Assumptions("
            f"fm_name={repr(self.fm_name)}, "
            f"pf_id={repr(self.pf_id)}, "
            f"provider_id={repr(self.provider_id)}, "
            f"report_date={repr(self.report_date)}, "
            f"rep_type={repr(self.rep_type)}, "
            f"question_nr={repr(self.question_nr)}, "
            f"assum_desc={repr(self.assum_desc)}, "
            f"member_ctry_code={repr(self.member_ctry_code)}"
            f")"
        )


__all__ = ['Assumptions']

