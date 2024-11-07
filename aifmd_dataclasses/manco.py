# manco.py
from common.data_processor import DataProcessor
from common.errors import *


class ManCo(DataProcessor):

    all = []
    prov_obl_codes = {'manco_name': 'M', 'report_date': 'M', 'member_ctry_code': 'M', 'nca_code': 'M',
                      'jurisdiction': 'M', 'rep_code': 'M', 'rep_freq_code': 'M', 'content_type_code': 'M',
                      'authorized_flag': 'M', 'filing_type': 'M', 'last_rep_flag': 'M', 'no_rep_flag': 'M',
                      'rep_freq_chg_code': 'O', 'rep_content_chg_code': 'O', 'rep_qrtr_chg_code': 'C(M)',
                      'lei_code': 'C(M)', 'bic_code': 'O', 'ctry_code_old': 'C(M)', 'nca_code_old': 'C(M)'}

    datatypes = {'manco_name': ('VARCHAR2', 200), 'report_date': 'DATE', 'member_ctry_code': ('VARCHAR2', 2),
                 'nca_code': ('VARCHAR2', 30), 'jurisdiction': ('VARCHAR2', 2), 'rep_code': ('NUMBER', 2, 0),
                 'rep_freq_code': ('VARCHAR2', 2), 'content_type_code': ('NUMBER', 1, 0),
                 'authorized_flag': ('CHAR', 1), 'filing_type': ('VARCHAR2', 4), 'last_rep_flag': ('CHAR', 1),
                 'no_rep_flag': ('CHAR', 1), 'rep_freq_chg_code': ('VARCHAR2', 2),
                 'rep_content_chg_code': ('NUMBER', 3, 0), 'rep_qrtr_chg_code': ('VARCHAR2', 2),
                 'lei_code': ('VARCHAR2', 20), 'bic_code': ('VARCHAR2', 11), 'ctry_code_old': ('VARCHAR2', 2),
                 'nca_code_old': ('VARCHAR2', 30)}

    rep_codes = [i for i in range(1, 10)]
    content_type_codes = [i for i in range(1, 5)]
    rep_content_chg_codes = [i for i in range(1, 7)]

    def __init__(self, manco_name=None, report_date=None, member_ctry_code=None,
                 nca_code=None, jurisdiction=None, rep_code=None,
                 rep_freq_code=None, content_type_code=None, authorized_flag=None,
                 filing_type=None, last_rep_flag=None, no_rep_flag=None,
                 rep_freq_chg_code=None, rep_content_chg_code=None,
                 rep_qrtr_chg_code=None, lei_code=None, bic_code=None,
                 ctry_code_old=None, nca_code_old=None, **kwargs):

        super().__init__()

        self.manco_name = manco_name
        self.report_date = report_date
        self.member_ctry_code = member_ctry_code
        self.nca_code = nca_code
        self.jurisdiction = jurisdiction
        self.rep_code = rep_code
        self.rep_freq_code = rep_freq_code
        self.content_type_code = content_type_code
        self.authorized_flag = authorized_flag
        self.filing_type = filing_type
        self.last_rep_flag = last_rep_flag
        self.no_rep_flag = no_rep_flag
        self.rep_freq_chg_code = rep_freq_chg_code
        self.rep_content_chg_code = rep_content_chg_code
        self.rep_qrtr_chg_code = rep_qrtr_chg_code
        self.lei_code = lei_code
        self.bic_code = bic_code
        self.ctry_code_old = ctry_code_old
        self.nca_code_old = nca_code_old

        # Enlist all mancos instances
        self.__class__.all.append(self)

    # Functions that define how the Item objects will be represented
    def __repr__(self):
        return (
            f"ManCo("
            f"manco_name={repr(self.manco_name)}, "
            f"report_date={repr(self.report_date)}, "
            f"member_ctry_code={repr(self.member_ctry_code)}, "
            f"nca_code={repr(self.nca_code)}, "
            f"jurisdiction={repr(self.jurisdiction)}, "
            f"rep_code={repr(self.rep_code)}, "
            f"rep_freq_code={repr(self.rep_freq_code)}, "
            f"content_type_code={repr(self.content_type_code)}, "
            f"authorized_flag={repr(self.authorized_flag)}, "
            f"filing_type={repr(self.filing_type)}, "
            f"last_rep_flag={repr(self.last_rep_flag)}, "
            f"no_rep_flag={repr(self.no_rep_flag)}, "
            f"rep_freq_chg_code={repr(self.rep_freq_chg_code)}, "
            f"rep_content_chg_code={repr(self.rep_content_chg_code)}, "
            f"rep_qrtr_chg_code={repr(self.rep_qrtr_chg_code)}, "
            f"lei_code={repr(self.lei_code)}, "
            f"bic_code={repr(self.bic_code)}, "
            f"ctry_code_old={repr(self.ctry_code_old)}, "
            f"nca_code_old={repr(self.nca_code_old)})"
        )

    @classmethod
    def perform_quality_checks(cls):
        sheet_name = cls.__name__
        for idx, instance in enumerate(cls.all):

            if (instance.member_ctry_code not in instance.country_codes
                    and DataProcessor.notnull(instance.member_ctry_code)):
                print(InconsistencyError(sheet_name, idx+1, 'member_ctry_code',
                                         instance.member_ctry_code, 'Invalid country member code'))

            if (instance.jurisdiction not in instance.country_codes
                    and DataProcessor.notnull(instance.jurisdiction)):
                print(InconsistencyError(sheet_name, idx + 1, 'jurisdiction',
                                         instance.jurisdiction, 'Invalid jurisdiction code'))

            if (instance.rep_code not in instance.rep_codes
                    and DataProcessor.notnull(instance.rep_code)):
                print(InconsistencyError(sheet_name, idx + 1, 'rep_code',
                                         instance.rep_code, 'Invalid rep_code'))

            if (instance.rep_freq_code not in instance.rep_freq_codes and
                    DataProcessor.notnull(instance.rep_freq_code)):
                print(InconsistencyError(sheet_name, idx + 1, 'rep_freq_code',
                                         instance.rep_freq_code, 'Invalid rep_freq_code'))

            if (instance.content_type_code not in instance.content_type_codes and
                    DataProcessor.notnull(instance.content_type_code)):
                print(InconsistencyError(sheet_name, idx + 1, 'content_type_code',
                                         instance.content_type_code, 'Invalid content_type_code'))

            if (instance.authorized_flag not in instance.flags and
                    DataProcessor.notnull(instance.authorized_flag)):
                print(InconsistencyError(sheet_name, idx + 1, 'authorized_flag',
                                         instance.authorized_flag, 'Invalid authorized_flag'))

            if instance.last_rep_flag not in instance.flags and DataProcessor.notnull(instance.last_rep_flag):
                print(InconsistencyError(sheet_name, idx + 1, 'last_rep_flag',
                                         instance.last_rep_flag, 'Invalid last_rep_flag'))

            if instance.no_rep_flag not in instance.flags and DataProcessor.notnull(instance.no_rep_flag):
                print(InconsistencyError(sheet_name, idx + 1, 'no_rep_flag',
                                         instance.last_rep_flag, 'Invalid no_rep_flag'))

            if (instance.rep_freq_chg_code not in instance.rep_freq_chg_codes and
                    DataProcessor.notnull(instance.rep_freq_chg_code)):
                print(InconsistencyError(sheet_name, idx + 1, 'rep_freq_chg_code',
                                         instance.rep_freq_chg_code, 'Invalid rep_freq_chg_code'))

            if (instance.rep_content_chg_code not in instance.rep_content_chg_codes and
                    DataProcessor.notnull(instance.rep_content_chg_code)):
                print(InconsistencyError(sheet_name, idx + 1, 'rep_content_chg_code',
                                         instance.rep_content_chg_code, 'Invalid rep_content_chg_code'))

            if (instance.rep_qrtr_chg_code not in instance.rep_qrtr_chg_codes and
                    DataProcessor.notnull(instance.rep_qrtr_chg_code)):
                print(InconsistencyError(sheet_name, idx + 1, 'rep_qrtr_chg_code',
                                         instance.rep_qrtr_chg_code, 'Invalid rep_qrtr_chg_code'))

            if ((DataProcessor.notnull(instance.rep_freq_chg_code)
                 or DataProcessor.notnull(instance.rep_content_chg_code))
                    and DataProcessor.isnull(instance.rep_qrtr_chg_code)):
                print(InconsistencyError(sheet_name, idx + 1, 'rep_qrtr_chg_code', instance.rep_qrtr_chg_code,
                                         message=f"The field is mandatory when the AIFM"
                                                 f" changes reporting frequency or content type code"))
            elif (DataProcessor.notnull(instance.rep_qrtr_chg_code) and
                  (DataProcessor.isnull(instance.rep_freq_chg_code)
                   and DataProcessor.isnull(instance.rep_content_chg_code))):
                print(InconsistencyError(sheet_name, idx + 1, 'rep_qrtr_chg_code', instance.rep_qrtr_chg_code,
                                         message=f"The field must not be populated"
                                                 f" when no report or content code change occurred"))

            if (instance.ctry_code_old not in instance.country_codes
                    and DataProcessor.notnull(instance.ctry_code_old)):
                print(InconsistencyError(sheet_name, idx+1, 'ctry_code_old',
                                         instance.ctry_code_old, 'Invalid country member code'))


__all__ = ['ManCo']
