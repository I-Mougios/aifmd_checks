# fund_static.py

from typing import Dict, Tuple, Optional
import datetime
from common.data_processor import DataProcessor
from common.errors import *
from aifmd_dataclasses.manco import ManCo


class Fund_Static(DataProcessor):

    all = []
    prov_obl_codes = {'pf_id': 'M', 'provider_id': 'C(M)', 'nav_date': 'M', 'pf_name': 'M', 'manco_name': 'M',
                      'active': 'M', 'inception_date': 'M', 'member_ctry_code': 'M', 'nca_code': 'M', 'domicile': 'M',
                      'rep_freq': 'M', 'rep_code': 'M', 'rep_24_1_flag': 'M', 'rep_24_2_flag': 'M', 'rep_24_4_flag': 'M'
                      , 'ccy_pc': 'M', 'filing_type': 'M', 'last_rep_flag': 'M', 'no_rep_flag': 'M',
                      'master_feeder_status': 'M', 'master_pf_name': 'C(M)', 'master_member_ctry_code': 'O',
                      'master_nca_code': 'C(M)', 'pos_size_code': 'C(M)', 'rep_freq_chg_code': 'O',
                      'rep_content_chg_code': 'O', 'rep_qrtr_chg_code': 'C(M)', 'member_ctry_code_old': 'C(M)',
                      'nca_code_old': 'C(M)', 'withdrawal_red_right': 'C(M)', 'inv_red_freq_code': 'C(O)',
                      'invt_red_notice_period': 'O', 'invt_red_lockup_period': 'O', 'lei_code': 'C(M)', 'isin': 'O',
                      'cusip': 'O', 'sedol': 'O', 'bloomberg': 'O', 'ric_code': 'O', 'ecb_code': 'O',
                      'fund_src_ctry_code_1': 'O', 'fund_src_ctry_code_2': 'O', 'fund_src_ctry_code_3': 'O'}

    datatypes = {'pf_id': ('VARCHAR2', 35), 'provider_id': ('VARCHAR2', 20), 'nav_date': 'DATE',
                 'pf_name': ('VARCHAR2', 4000), 'manco_name': ('VARCHAR2', 200), 'active': ('CHAR', 1),
                 'inception_date': 'DATE', 'member_ctry_code': ('VARCHAR2', 2), 'nca_code': ('VARCHAR2', 30),
                 'domicile': ('VARCHAR2', 2), 'rep_freq': ('VARCHAR2', 2), 'rep_code': ('NUMBER', 2, 0),
                 'rep_24_1_flag': ('CHAR', 1), 'rep_24_2_flag': ('CHAR', 1), 'rep_24_4_flag': ('CHAR', 1),
                 'ccy_pc': ('VARCHAR2', 3), 'filing_type': ('VARCHAR2', 4), 'last_rep_flag': ('CHAR', 1),
                 'no_rep_flag': ('CHAR', 1), 'master_feeder_status': ('VARCHAR2', 6),
                 'master_pf_name': ('VARCHAR2', 300), 'master_member_ctry_code': ('VARCHAR2', 2),
                 'master_nca_code': ('VARCHAR2', 30), 'pos_size_code': ('VARCHAR2', 11),
                 'rep_freq_chg_code': ('VARCHAR2', 2), 'rep_content_chg_code': ('NUMBER', 3, 0),
                 'rep_qrtr_chg_code': ('VARCHAR2', 2), 'member_ctry_code_old': ('VARCHAR2', 2),
                 'nca_code_old': ('VARCHAR2', 30), 'withdrawal_red_right': ('CHAR', 1), 'inv_red_freq_code': ('CHAR', 1)
                 , 'invt_red_notice_period': ('NUMBER', 4, 0), 'invt_red_lockup_period': ('NUMBER', 4, 0),
                 'lei_code': ('VARCHAR2', 20), 'isin': ('VARCHAR2', 12), 'cusip': ('VARCHAR2', 9),
                 'sedol': ('VARCHAR2', 7), 'bloomberg': ('VARCHAR2', 20), 'ric_code': ('VARCHAR2', 20),
                 'ecb_code': ('VARCHAR2', 20), 'fund_src_ctry_code_1': ('VARCHAR2', 2),
                 'fund_src_ctry_code_2': ('VARCHAR2', 2), 'fund_src_ctry_code_3': ('VARCHAR2', 2)}

    rep_codes = [i for i in range(1, 46)]
    rep_content_chg_codes = [i for i in range(1, 26)]
    master_feeder_codes = ['MASTER', 'FEEDER', 'NONE']
    pos_size_codes = ['V_SMALL', 'SMALL', 'LOW_MID_MKT', 'UP_MID_MKT', 'L_CAP', 'M_CAP']
    inv_red_freq_codes = ['D', 'W', 'F', 'M', 'Q', 'H', 'Y', 'O', 'N']

    pos_size_codes_per_fund: Dict[Tuple[str, datetime.date], Optional[str]] = dict()

    def __init__(self, pf_id=None, provider_id=None, nav_date=None, pf_name=None, manco_name=None, active=None,
                 inception_date=None, member_ctry_code=None, nca_code=None, domicile=None, rep_freq=None, rep_code=None,
                 rep_24_1_flag=None, rep_24_2_flag=None, rep_24_4_flag=None, ccy_pc=None, filing_type=None,
                 last_rep_flag=None, no_rep_flag=None, master_feeder_status=None, master_pf_name=None,
                 master_member_ctry_code=None, master_nca_code=None, pos_size_code=None, rep_freq_chg_code=None,
                 rep_content_chg_code=None, rep_qrtr_chg_code=None, member_ctry_code_old=None, nca_code_old=None,
                 withdrawal_red_right=None, inv_red_freq_code=None, invt_red_notice_period=None,
                 invt_red_lockup_period=None, lei_code=None, isin=None, cusip=None, sedol=None,
                 bloomberg=None, ric_code=None, ecb_code=None, fund_src_ctry_code_1=None,
                 fund_src_ctry_code_2=None, fund_src_ctry_code_3=None, **kwargs):

        super().__init__()

        self.pf_id = pf_id
        self.provider_id = provider_id
        self.nav_date = nav_date
        self.pf_name = pf_name
        self.manco_name = manco_name
        self.active = active
        self.inception_date = inception_date
        self.member_ctry_code = member_ctry_code
        self.nca_code = nca_code
        self.domicile = domicile
        self.rep_freq = rep_freq
        self.rep_code = rep_code
        self.rep_24_1_flag = rep_24_1_flag
        self.rep_24_2_flag = rep_24_2_flag
        self.rep_24_4_flag = rep_24_4_flag
        self.ccy_pc = ccy_pc
        self.filing_type = filing_type
        self.last_rep_flag = last_rep_flag
        self.no_rep_flag = no_rep_flag
        self.master_feeder_status = master_feeder_status
        self.master_pf_name = master_pf_name
        self.master_member_ctry_code = master_member_ctry_code
        self.master_nca_code = master_nca_code
        self.pos_size_code = pos_size_code
        self.rep_freq_chg_code = rep_freq_chg_code
        self.rep_content_chg_code = rep_content_chg_code
        self.rep_qrtr_chg_code = rep_qrtr_chg_code
        self.member_ctry_code_old = member_ctry_code_old
        self.nca_code_old = nca_code_old
        self.withdrawal_red_right = withdrawal_red_right if DataProcessor.notnull(withdrawal_red_right) else 0
        self.inv_red_freq_code = inv_red_freq_code
        self.invt_red_notice_period = invt_red_notice_period
        self.invt_red_lockup_period = invt_red_lockup_period
        self.lei_code = lei_code
        self.isin = isin
        self.cusip = cusip
        self.sedol = sedol
        self.bloomberg = bloomberg
        self.ric_code = ric_code
        self.ecb_code = ecb_code
        self.fund_src_ctry_code_1 = fund_src_ctry_code_1
        self.fund_src_ctry_code_2 = fund_src_ctry_code_2
        self.fund_src_ctry_code_3 = fund_src_ctry_code_3

        # Gather the pos_size_code for each fund
        self.pos_size_codes_per_fund[(self.pf_id, self.nav_date)] = self.pos_size_code
        # Enlist all objects
        self.__class__.all.append(self)

    def __repr__(self):
        return (
            f"Fund_Static("
            f"pf_id={repr(self.pf_id)}, "
            f"provider_id={repr(self.provider_id)}, "
            f"nav_date={repr(self.nav_date)}, "
            f"pf_name={repr(self.pf_name)}, "
            f"manco_name={repr(self.manco_name)}, "
            f"active={repr(self.active)}, "
            f"inception_date={repr(self.inception_date)}, "
            f"member_ctry_code={repr(self.member_ctry_code)}, "
            f"nca_code={repr(self.nca_code)}, "
            f"domicile={repr(self.domicile)}, "
            f"rep_freq={repr(self.rep_freq)}, "
            f"rep_code={repr(self.rep_code)}, "
            f"rep_24_1_flag={repr(self.rep_24_1_flag)}, "
            f"rep_24_2_flag={repr(self.rep_24_2_flag)}, "
            f"rep_24_4_flag={repr(self.rep_24_4_flag)}, "
            f"ccy_pc={repr(self.ccy_pc)}, "
            f"filing_type={repr(self.filing_type)}, "
            f"last_rep_flag={repr(self.last_rep_flag)}, "
            f"no_rep_flag={repr(self.no_rep_flag)}, "
            f"master_feeder_status={repr(self.master_feeder_status)}, "
            f"master_pf_name={repr(self.master_pf_name)}, "
            f"master_member_ctry_code={repr(self.master_member_ctry_code)}, "
            f"master_nca_code={repr(self.master_nca_code)}, "
            f"pos_size_code={repr(self.pos_size_code)}, "
            f"rep_freq_chg_code={repr(self.rep_freq_chg_code)}, "
            f"rep_content_chg_code={repr(self.rep_content_chg_code)}, "
            f"rep_qrtr_chg_code={repr(self.rep_qrtr_chg_code)}, "
            f"member_ctry_code_old={repr(self.member_ctry_code_old)}, "
            f"nca_code_old={repr(self.nca_code_old)}, "
            f"withdrawal_red_right={repr(self.withdrawal_red_right)}, "
            f"inv_red_freq_code={repr(self.inv_red_freq_code)}, "
            f"invt_red_notice_period={repr(self.invt_red_notice_period)}, "
            f"invt_red_lockup_period={repr(self.invt_red_lockup_period)}, "
            f"lei_code={repr(self.lei_code)}, "
            f"isin={repr(self.isin)}, "
            f"cusip={repr(self.cusip)}, "
            f"sedol={repr(self.sedol)}, "
            f"bloomberg={repr(self.bloomberg)}, "
            f"ric_code={repr(self.ric_code)}, "
            f"ecb_code={repr(self.ecb_code)}, "
            f"fund_src_ctry_code_1={repr(self.fund_src_ctry_code_1)}, "
            f"fund_src_ctry_code_2={repr(self.fund_src_ctry_code_2)}, "
            f"fund_src_ctry_code_3={repr(self.fund_src_ctry_code_3)})"
        )

    @classmethod
    def perform_quality_checks(cls):
        sheet_name = cls.__name__
        for idx, instance in enumerate(cls.all):
            if instance.active not in instance.flags and DataProcessor.notnull(instance.active):
                print(InconsistencyError(sheet_name, idx + 1, 'active',
                                         instance.active, 'Invalid active code'))

            if (instance.member_ctry_code not in instance.country_codes
                    and DataProcessor.notnull(instance.member_ctry_code)):
                print(InconsistencyError(sheet_name, idx + 1, 'member_ctry_code',
                                         instance.member_ctry_code, 'Invalid country member code'))

            if (instance.domicile not in instance.country_codes
                    and DataProcessor.notnull(instance.domicile)):
                print(InconsistencyError(sheet_name, idx + 1, 'domicile',
                                         instance.domicile, 'Invalid domicile code'))

            if (instance.rep_freq not in instance.rep_freq_codes and
                    DataProcessor.notnull(instance.rep_freq)):
                print(InconsistencyError(sheet_name, idx + 1, 'rep_freq_code',
                                         instance.rep_freq, 'Invalid reporting frequency code'))

            if (instance.rep_code not in instance.rep_codes
                    and DataProcessor.notnull(instance.rep_code)):
                print(InconsistencyError(sheet_name, idx + 1, 'rep_code',
                                         instance.rep_code, 'Invalid reporting code'))

            if (instance.rep_24_1_flag not in instance.flags and
                    DataProcessor.notnull(instance.rep_24_1_flag)):
                print(InconsistencyError(sheet_name, idx + 1, 'rep_24_1_flag',
                                         instance.rep_24_1_flag, 'Invalid rep_24_1_flag'))

            if (instance.rep_24_2_flag not in instance.flags and
                    DataProcessor.notnull(instance.rep_24_2_flag)):
                print(InconsistencyError(sheet_name, idx + 1, 'rep_24_2_flag',
                                         instance.rep_24_2_flag, 'Invalid rep_24_2_flag'))

            if (instance.rep_24_4_flag not in instance.flags and
                    DataProcessor.notnull(instance.rep_24_4_flag)):
                print(InconsistencyError(sheet_name, idx + 1, 'rep_24_4_flag',
                                         instance.rep_24_4_flag, 'Invalid rep_24_4_flag'))

            if instance.ccy_pc not in instance.currency_codes and DataProcessor.notnull(instance.ccy_pc):
                print(InconsistencyError(sheet_name, idx + 1, 'ccy_pc',
                                         instance.ccy_pc, 'Invalid portfolio currency code'))

            if instance.filing_type not in instance.filing_type_codes and DataProcessor.notnull(instance.filing_type):
                print(InconsistencyError(sheet_name, idx + 1, 'filing_type',
                                         instance.filing_type, 'Invalid filing type'))

            if instance.last_rep_flag not in instance.flags and DataProcessor.notnull(instance.last_rep_flag):
                print(InconsistencyError(sheet_name, idx + 1, 'last_rep_flag',
                                         instance.last_rep_flag, 'Invalid last_rep_flag'))

            if instance.no_rep_flag not in instance.flags and DataProcessor.notnull(instance.no_rep_flag):
                print(InconsistencyError(sheet_name, idx + 1, 'no_rep_flag',
                                         instance.last_rep_flag, 'Invalid no_rep_flag'))
            # -----------------------MASTER FEEDER LOGIC ---------------------------------------------
            if (instance.master_feeder_status not in instance.master_feeder_codes and
                    DataProcessor.notnull(instance.master_feeder_status)):
                print(InconsistencyError(sheet_name, idx + 1, 'master_feeder_status',
                                         instance.master_feeder_status, 'Invalid master_feeder_status'))

            elif instance.master_feeder_status == 'FEEDER':
                if DataProcessor.isnull(instance.master_pf_name):
                    print(InconsistencyError(sheet_name, idx + 1, 'master_pf_name',
                                             instance.master_pf_name, f'Master AIF name is mandatory '
                                                                      f'when the fund is feeder'))
                if DataProcessor.notnull(instance.master_member_ctry_code):
                    if DataProcessor.isnull(instance.master_nca_code):
                        print(InconsistencyError(sheet_name, idx + 1,
                                                 column='master_nca_code',
                                                 value=instance.master_nca_code,
                                                 message=f"Master NCA code is mandatory when"
                                                 f" the Master's reporting member state is filled in"))

                    if instance.master_member_ctry_code not in instance.country_codes:
                        print(InconsistencyError(sheet_name, idx + 1,
                                                 column='master_member_ctry_code',
                                                 value=instance.master_member_ctry_code,
                                                 message='Invalid country code'))
                else:
                    if DataProcessor.notnull(instance.master_nca_code):
                        print(InconsistencyError(sheet_name, idx + 1,
                                                 column='master_nca_code',
                                                 value=instance.master_nca_code,
                                                 message=f"To be provided only if "
                                                         f"the Master's reporting member state is not empty"))

            else:
                if (DataProcessor.notnull(instance.master_member_ctry_code)
                        or DataProcessor.notnull(instance.master_nca_code)):
                    print(InconsistencyError(sheet_name, idx + 1,
                                             column='master_feeder_status | master_member_ctry_code | master_nca_code',
                                             value=f"{instance.master_feeder_status}|"
                                                   f"{instance.master_member_ctry_code}|{instance.master_nca_code}",
                                             message=f"Master reporting member state or NCA code should be filled only"
                                                     f" if the fund is feeder"))

        # -------------------------END OF MASTER FEEDER LOGIC---------------------------------------------
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
                print(InconsistencyError(sheet_name, idx+1, 'rep_qrtr_chg_code', instance.rep_qrtr_chg_code,
                                         message=f"The field is mandatory when the AIF"
                                                 f" changes reporting frequency or content type code"))

            elif (DataProcessor.notnull(instance.rep_qrtr_chg_code) and
                  (DataProcessor.isnull(instance.rep_freq_chg_code)
                   and DataProcessor.isnull(instance.rep_content_chg_code))):
                print(InconsistencyError(sheet_name, idx + 1, 'rep_qrtr_chg_code', instance.rep_qrtr_chg_code,
                                         message=f"The field must not be populated"
                                                 f" when no report or content code change occurred"))

            if instance.withdrawal_red_right not in [0, 1]:
                print(InconsistencyError(sheet_name, idx + 1,
                                         column='withdrawal_red_right',
                                         value=instance.withdrawal_red_right,
                                         message="Withdrawal red right must be 0 or 1"))

            if (instance.withdrawal_red_right != 1
                    and
                    any([instance.inv_red_freq_code,
                         instance.invt_red_notice_period,
                         instance.invt_red_lockup_period])):

                print(InconsistencyError(sheet_name, idx + 1,
                                         column='inv_red_freq_code | invt_red_notice_period | invt_red_lockup_period',
                                         value=(instance.inv_red_freq_code,
                                                instance.invt_red_notice_period,
                                                instance.invt_red_lockup_period),
                                         message=f"Fields: investor redemption frequency code,"
                                                 f" investor redemption notice period"
                                                 f" and investor redemption lock up "
                                                 f"can be provided only if"
                                                 f" withdrawal redemption rights flag is set to 1"))

            if (DataProcessor.notnull(instance.inv_red_freq_code)
                    and instance.inv_red_freq_code not in instance.inv_red_freq_code):
                print(InconsistencyError(sheet_name, idx + 1,
                                         column='inv_red_freq_code',
                                         value=instance.inv_red_freq_code,
                                         message="Invalid inv_red_freq_code"))

            if DataProcessor.notnull(instance.invt_red_notice_period):
                try:
                    if instance.invt_red_notice_period < 0:
                        print(InconsistencyError(sheet_name, idx + 1,
                                                 column='inv_red_notice_code',
                                                 value=instance.inv_red_notice_code,
                                                 message=f"Investor redemption notice period must be"
                                                         f" a non negative integer"))
                except TypeError:
                    pass

            if DataProcessor.notnull(instance.invt_red_lockup_period):
                try:
                    if instance.invt_red_lockup_period < 0:
                        print(InconsistencyError(sheet_name, idx + 1,
                                                 column='inv_red_lockup_code',
                                                 value=instance.inv_red_notice_code,
                                                 message=f"Investor redemption lockup period must be a non"
                                                         f" negative integer"))
                except TypeError:
                    pass

            if (DataProcessor.notnull(instance.fund_src_ctry_code_1)
                    and instance.fund_src_ctry_code_1 not in instance.country_codes):
                print(InconsistencyError(sheet_name, idx + 1,
                                         column='fund_src_ctry_code_1',
                                         value=instance.fund_src_ctry_code_1,
                                         message="Invalid country code"))

            if (DataProcessor.notnull(instance.fund_src_ctry_code_2)
                    and instance.fund_src_ctry_code_2 not in instance.country_codes):
                print(InconsistencyError(sheet_name, idx + 1,
                                         column='fund_src_ctry_code_2',
                                         value=instance.fund_src_ctry_code_2,
                                         message="Invalid country code"))

            if (DataProcessor.notnull(instance.fund_src_ctry_code_3)
                    and instance.fund_src_ctry_code_3 not in instance.country_codes):
                print(InconsistencyError(sheet_name, idx + 1,
                                         column='fund_src_ctry_code_3',
                                         value=instance.fund_src_ctry_code_3,
                                         message="Invalid country code"))

    @classmethod
    def check_rep_code(cls):
        """
        Purpose: This function checks for inconsistencies in reporting codes between a  fund  and
        its management companies (manco).

        """

        if ManCo.all and Fund_Static.all:
            message = (f"Inconsistent AIF reporting code. AIF's Reporting code must be inline with the reporting code"
                       f" of management company. For more details look up on Info Sheets.")

            for index, fund in enumerate(cls.all):
                for manco in ManCo.all:
                    flag = False
                    if manco.manco_name == fund.manco_name:
                        if manco.rep_code == 1 and fund.rep_code != 1:
                            flag = True
                        elif manco.rep_code == 2 and fund.rep_code not in [i for i in range(2, 8)]:
                            flag = True
                        elif manco.rep_code == 3 and fund.rep_code not in [i for i in range(8, 11)]:
                            flag = True
                        elif manco.rep_code == 4 and fund.rep_code not in [i for i in range(11, 26)]:
                            flag = True
                        elif manco.rep_code == 5 and fund.rep_code not in [i for i in range(26, 35)]:
                            flag = True
                        elif manco.rep_code == 6 and fund.rep_code not in [i for i in range(35, 37)]:
                            flag = True
                        elif manco.rep_code == 7 and fund.rep_code != 37:
                            flag = True
                        elif manco.rep_code == 8 and fund.rep_code not in [i for i in range(38, 43)]:
                            flag = True
                        elif manco.rep_code == 9 and fund.rep_code not in [i for i in range(43, 46)]:
                            flag = True

                        if flag:
                            print(InconsistencyError(sheet_name='Manco|Fund_Static',
                                                     index=index,
                                                     column='AIFM reporting code | AIF reporting code',
                                                     value=(manco.rep_code, fund.rep_code),
                                                     message=message))
                            break


__all__ = ['Fund_Static']
