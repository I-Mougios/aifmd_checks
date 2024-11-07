# risk_liquidity.py
from common.data_processor import DataProcessor
from common.errors import *


class Risk_Liquidity(DataProcessor):
    all = []
    datatypes = {'pf_id': ('VARCHAR2', 35), 'provider_id': ('VARCHAR2', 20), 'nav_date': 'DATE',
                 'pf_liq_rate_0_1': ('NUMBER', 15, 4), 'pf_liq_rate_2_7': ('NUMBER', 15, 4),
                 'pf_liq_rate_8_30': ('NUMBER', 15, 4), 'pf_liq_rate_31_90': ('NUMBER', 15, 4),
                 'pf_liq_rate_91_180': ('NUMBER', 15, 4), 'pf_liq_rate_181_365': ('NUMBER', 15, 4),
                 'pf_liq_rate_366_plus': ('NUMBER', 15, 4), 'unencumb_cash_pc': ('NUMBER', 15, 0),
                 'invt_red_rate_0_1': ('NUMBER', 15, 4), 'invt_red_rate_2_7': ('NUMBER', 15, 4),
                 'invt_red_rate_8_30': ('NUMBER', 15, 4), 'invt_red_rate_31_90': ('NUMBER', 15, 4),
                 'invt_red_rate_91_180': ('NUMBER', 15, 4), 'invt_red_rate_181_365': ('NUMBER', 15, 4),
                 'invt_red_rate_366_plus': ('NUMBER', 15, 4), 'side_pocket_rate': ('NUMBER', 3, 2),
                 'gates_rate': ('NUMBER', 3, 2), 'dealing_susp_rate': ('NUMBER', 3, 2),
                 'oth_arrangement_type': ('VARCHAR2', 1200), 'oth_arrangement_rate': ('NUMBER', 3, 2),
                 'total_arrangement_rate': ('NUMBER', 3, 2), 'invt_pref_trmt_flag': ('CHAR', 1),
                 'disc_pref_trmt_flag': ('CHAR', 1), 'liq_pref_trmt_flag': ('CHAR', 1),
                 'fee_pref_trmt_flag': ('CHAR', 1), 'oth_pref_trmt_flag': ('CHAR', 1),
                 'financing_total_pc': ('NUMBER', 15, 0), 'financing_rate_0_1': ('NUMBER', 15, 4),
                 'financing_rate_2_7': ('NUMBER', 15, 4), 'financing_rate_8_30': ('NUMBER', 15, 4),
                 'financing_rate_31_90': ('NUMBER', 15, 4), 'financing_rate_91_180': ('NUMBER', 15, 4),
                 'financing_rate_181_365': ('NUMBER', 15, 4), 'financing_rate_366_plus': ('NUMBER', 15, 4)}

    prov_obl_codes = {'pf_id': 'M', 'provider_id': 'C(M)', 'nav_date': 'M', 'pf_liq_rate_0_1': 'O',
                      'pf_liq_rate_2_7': 'O', 'pf_liq_rate_8_30': 'O', 'pf_liq_rate_31_90': '0',
                      'pf_liq_rate_91_180': 'O', 'pf_liq_rate_181_365': 'O', 'pf_liq_rate_366_plus': 'O',
                      'unencumb_cash_pc': 'C(M)', 'invt_red_rate_0_1': 'O', 'invt_red_rate_2_7': 'O',
                      'invt_red_rate_8_30': 'O', 'invt_red_rate_31_90': 'O', 'invt_red_rate_91_180': 'O',
                      'invt_red_rate_181_365': 'O', 'invt_red_rate_366_plus': 'O', 'side_pocket_rate': 'O',
                      'gates_rate': 'O', 'dealing_susp_rate': 'O', 'oth_arrangement_type': 'O',
                      'oth_arrangement_rate': 'C(M)', 'total_arrangement_rate': 'O', 'invt_pref_trmt_flag': 'O',
                      'disc_pref_trmt_flag': 'O', 'liq_pref_trmt_flag': 'O', 'fee_pref_trmt_flag': 'O',
                      'oth_pref_trmt_flag': 'O', 'financing_total_pc': 'O', 'financing_rate_0_1': 'C(M)',
                      'financing_rate_2_7': 'C(M)', 'financing_rate_8_30': 'C(M)', 'financing_rate_31_90': 'C(M)',
                      'financing_rate_91_180': 'C(M)', 'financing_rate_181_365': 'C(M)',
                      'financing_rate_366_plus': 'C(M)'}

    def __init__(self, pf_id=None, provider_id=None, nav_date=None, pf_liq_rate_0_1=None, pf_liq_rate_2_7=None,
                 pf_liq_rate_8_30=None, pf_liq_rate_31_90=None, pf_liq_rate_91_180=None, pf_liq_rate_181_365=None,
                 pf_liq_rate_366_plus=None, unencumb_cash_pc=None, invt_red_rate_0_1=None, invt_red_rate_2_7=None,
                 invt_red_rate_8_30=None, invt_red_rate_31_90=None, invt_red_rate_91_180=None,
                 invt_red_rate_181_365=None, invt_red_rate_366_plus=None, side_pocket_rate=None, gates_rate=None,
                 dealing_susp_rate=None, oth_arrangement_type=None, oth_arrangement_rate=None,
                 total_arrangement_rate=None, invt_pref_trmt_flag=None, disc_pref_trmt_flag=None,
                 liq_pref_trmt_flag=None, fee_pref_trmt_flag=None, oth_pref_trmt_flag=None, financing_total_pc=None,
                 financing_rate_0_1=None, financing_rate_2_7=None, financing_rate_8_30=None, financing_rate_31_90=None,
                 financing_rate_91_180=None, financing_rate_181_365=None, financing_rate_366_plus=None, **kwargs):

        super().__init__()

        self.pf_id = pf_id
        self.provider_id = provider_id
        self.nav_date = nav_date
        self.pf_liq_rate_0_1 = pf_liq_rate_0_1
        self.pf_liq_rate_2_7 = pf_liq_rate_2_7
        self.pf_liq_rate_8_30 = pf_liq_rate_8_30
        self.pf_liq_rate_31_90 = pf_liq_rate_31_90
        self.pf_liq_rate_91_180 = pf_liq_rate_91_180
        self.pf_liq_rate_181_365 = pf_liq_rate_181_365
        self.pf_liq_rate_366_plus = pf_liq_rate_366_plus
        self.unencumb_cash_pc = unencumb_cash_pc
        self.invt_red_rate_0_1 = invt_red_rate_0_1
        self.invt_red_rate_2_7 = invt_red_rate_2_7
        self.invt_red_rate_8_30 = invt_red_rate_8_30
        self.invt_red_rate_31_90 = invt_red_rate_31_90
        self.invt_red_rate_91_180 = invt_red_rate_91_180
        self.invt_red_rate_181_365 = invt_red_rate_181_365
        self.invt_red_rate_366_plus = invt_red_rate_366_plus
        self.side_pocket_rate = side_pocket_rate
        self.gates_rate = gates_rate
        self.dealing_susp_rate = dealing_susp_rate
        self.oth_arrangement_type = oth_arrangement_type
        self.oth_arrangement_rate = oth_arrangement_rate
        self.total_arrangement_rate = total_arrangement_rate
        self.invt_pref_trmt_flag = invt_pref_trmt_flag
        self.disc_pref_trmt_flag = disc_pref_trmt_flag
        self.liq_pref_trmt_flag = liq_pref_trmt_flag
        self.fee_pref_trmt_flag = fee_pref_trmt_flag
        self.oth_pref_trmt_flag = oth_pref_trmt_flag
        self.financing_total_pc = financing_total_pc
        self.financing_rate_0_1 = financing_rate_0_1
        self.financing_rate_2_7 = financing_rate_2_7
        self.financing_rate_8_30 = financing_rate_8_30
        self.financing_rate_31_90 = financing_rate_31_90
        self.financing_rate_91_180 = financing_rate_91_180
        self.financing_rate_181_365 = financing_rate_181_365
        self.financing_rate_366_plus = financing_rate_366_plus

        self.__class__.all.append(self)

    def __repr__(self):
        return (
            f"Risk_Liquidity("
            f"pf_id={repr(self.pf_id)}, "
            f"provider_id={repr(self.provider_id)}, "
            f"nav_date={repr(self.nav_date)}, "
            f"pf_liq_rate_0_1={repr(self.pf_liq_rate_0_1)}, "
            f"pf_liq_rate_2_7={repr(self.pf_liq_rate_2_7)}, "
            f"pf_liq_rate_8_30={repr(self.pf_liq_rate_8_30)}, "
            f"pf_liq_rate_31_90={repr(self.pf_liq_rate_31_90)}, "
            f"pf_liq_rate_91_180={repr(self.pf_liq_rate_91_180)}, "
            f"pf_liq_rate_181_365={repr(self.pf_liq_rate_181_365)}, "
            f"pf_liq_rate_366_plus={repr(self.pf_liq_rate_366_plus)}, "
            f"unencumb_cash_pc={repr(self.unencumb_cash_pc)}, "
            f"invt_red_rate_0_1={repr(self.invt_red_rate_0_1)}, "
            f"invt_red_rate_2_7={repr(self.invt_red_rate_2_7)}, "
            f"invt_red_rate_8_30={repr(self.invt_red_rate_8_30)}, "
            f"invt_red_rate_31_90={repr(self.invt_red_rate_31_90)}, "
            f"invt_red_rate_91_180={repr(self.invt_red_rate_91_180)}, "
            f"invt_red_rate_181_365={repr(self.invt_red_rate_181_365)}, "
            f"invt_red_rate_366_plus={repr(self.invt_red_rate_366_plus)}, "
            f"side_pocket_rate={repr(self.side_pocket_rate)}, "
            f"gates_rate={repr(self.gates_rate)}, "
            f"dealing_susp_rate={repr(self.dealing_susp_rate)}, "
            f"oth_arrangement_type={repr(self.oth_arrangement_type)}, "
            f"oth_arrangement_rate={repr(self.oth_arrangement_rate)}, "
            f"total_arrangement_rate={repr(self.total_arrangement_rate)}, "
            f"invt_pref_trmt_flag={repr(self.invt_pref_trmt_flag)}, "
            f"disc_pref_trmt_flag={repr(self.disc_pref_trmt_flag)}, "
            f"liq_pref_trmt_flag={repr(self.liq_pref_trmt_flag)}, "
            f"fee_pref_trmt_flag={repr(self.fee_pref_trmt_flag)}, "
            f"oth_pref_trmt_flag={repr(self.oth_pref_trmt_flag)}, "
            f"financing_total_pc={repr(self.financing_total_pc)}, "
            f"financing_rate_0_1={repr(self.financing_rate_0_1)}, "
            f"financing_rate_2_7={repr(self.financing_rate_2_7)}, "
            f"financing_rate_8_30={repr(self.financing_rate_8_30)}, "
            f"financing_rate_31_90={repr(self.financing_rate_31_90)}, "
            f"financing_rate_91_180={repr(self.financing_rate_91_180)}, "
            f"financing_rate_181_365={repr(self.financing_rate_181_365)}, "
            f"financing_rate_366_plus={repr(self.financing_rate_366_plus)}"
            f")"
        )

    @property
    def total_liq_rates(self):
        return sum(
                  [self.safe_round(self.pf_liq_rate_0_1, 4),
                   self.safe_round(self.pf_liq_rate_2_7, 4),
                   self.safe_round(self.pf_liq_rate_8_30, 4),
                   self.safe_round(self.pf_liq_rate_31_90, 4),
                   self.safe_round(self.pf_liq_rate_91_180, 4),
                   self.safe_round(self.pf_liq_rate_181_365, 4),
                   self.safe_round(self.pf_liq_rate_366_plus, 4)
                   ])

    @property
    def total_invt_rates(self):
        return sum(
                  [self.safe_round(self.invt_red_rate_0_1, 4),
                   self.safe_round(self.invt_red_rate_2_7, 4),
                   self.safe_round(self.invt_red_rate_8_30, 4),
                   self.safe_round(self.invt_red_rate_31_90, 4),
                   self.safe_round(self.invt_red_rate_91_180, 4),
                   self.safe_round(self.invt_red_rate_181_365, 4),
                   self.safe_round(self.invt_red_rate_366_plus,4)
                   ])

    @property
    def total_financing_rates(self):
        return sum(
                  [self.safe_round(self.financing_rate_0_1, 4),
                   self.safe_round(self.financing_rate_2_7, 4),
                   self.safe_round(self.financing_rate_8_30, 4),
                   self.safe_round(self.financing_rate_31_90, 4),
                   self.safe_round(self.financing_rate_91_180, 4),
                   self.safe_round(self.financing_rate_181_365, 4),
                   self.safe_round(self.financing_rate_366_plus, 4)])

    @classmethod
    def perform_quality_checks(cls):
        sheet_name = cls.__name__
        for idx, instance in enumerate(cls.all):
            if any([instance.pf_liq_rate_0_1, instance.pf_liq_rate_2_7,
                    instance.pf_liq_rate_8_30, instance.pf_liq_rate_31_90,
                    instance.pf_liq_rate_91_180, instance.pf_liq_rate_181_365,
                    instance.pf_liq_rate_366_plus]):
                if instance.total_liq_rates != 1:
                    print(InconsistencyError(sheet_name=sheet_name, index=idx+1,
                                             column=f'pf_liq_rate_0_1 | pf_liq_rate_2_7 | '
                                                    f'pf_liq_rate_8_30 | pf_liq_rate_31_90 | '
                                                    f'pf_liq_rate_91_180 | pf_liq_rate_181_365 | '
                                                    f'pf_liq_rate_366_plus',
                                             value=f"{instance.pf_liq_rate_0_1} | {instance.pf_liq_rate_2_7} |"
                                                   f"{instance.pf_liq_rate_8_30} | {instance.pf_liq_rate_31_90} |"
                                                   f"{instance.pf_liq_rate_91_180} | {instance.pf_liq_rate_181_365} | "
                                                   f"{instance.pf_liq_rate_366_plus}",
                                             message=f'Values should sum up to 1.'
                                                     f' Difference {1-instance.total_liq_rates}'))

                if DataProcessor.isnull(instance.unencumb_cash_pc):
                    print(InconsistencyError(sheet_name=sheet_name, index=idx+1,
                                             column='unencumb_cash_pc',
                                             value=instance.unencumb_cash_pc,
                                             message=f'Unencumb cash pc must be provided when liquidity rates are'
                                                     f'provided'))
            else:
                if DataProcessor.notnull(instance.unencumb_cash_pc):
                    print(InconsistencyError(sheet_name=sheet_name, index=idx+1,
                                             column='unencumb_cash_pc',
                                             value=instance.unencumb_cash_pc,
                                             message=f'Unencumb cash pc must be null when liquidity rates are not'
                                                     f'provided'))

            if (any([instance.invt_red_rate_0_1, instance.invt_red_rate_2_7,
                     instance.invt_red_rate_8_30, instance.invt_red_rate_31_90,
                     instance.invt_red_rate_91_180, instance.invt_red_rate_181_365,
                     instance.invt_red_rate_366_plus])):
                if instance.total_invt_rates != 1:
                    print(InconsistencyError(sheet_name=sheet_name, index=idx+1,
                                             column=f'invt_red_rate_0_1 | invt_red_rate_2_7 | '
                                                    f'invt_red_rate_8_30 | invt_red_rate_31_90 | '
                                                    f'invt_red_rate_91_180 | invt_red_rate_181_365 | '
                                                    f'invt_red_rate_366_plus',
                                             value=f"{instance.invt_red_rate_0_1} | {instance.invt_red_rate_2_7} |"
                                                   f"{instance.invt_red_rate_8_30} | {instance.invt_red_rate_31_90} |"
                                                   f"{instance.invt_red_rate_91_180} |"
                                                   f" {instance.invt_red_rate_181_365} | "
                                                   f"{instance.invt_red_rate_366_plus}",
                                             message=f'Values should sum up to 1.'
                                                     f' Difference {1-instance.total_invt_rates}'))

            if DataProcessor.notnull(instance.financing_total_pc):
                if any([DataProcessor.isnull(instance.financing_rate_0_1),
                        DataProcessor.isnull(instance.financing_rate_2_7),
                        DataProcessor.isnull(instance.financing_rate_8_30),
                        DataProcessor.isnull(instance.financing_rate_31_90),
                        DataProcessor.isnull(instance.financing_rate_91_180),
                        DataProcessor.isnull(instance.financing_rate_181_365),
                        DataProcessor.isnull(instance.financing_rate_366_plus)]):

                    print(InconsistencyError(sheet_name=sheet_name, index=idx+1,
                                             column=f'financing_total_pc | financing_rate_0_1 | financing_rate_2_7 | '
                                                    f'financing_rate_8_30 | financing_rate_31_90 | '
                                                    f'financing_rate_91_180 | financing_rate_181_365 | '
                                                    f'financing_rate_366_plus',
                                             value=f"'{instance.financing_total_pc} |{instance.financing_rate_0_1} |"
                                                   f" {instance.financing_rate_2_7} |"
                                                   f"{instance.financing_rate_8_30} | {instance.financing_rate_31_90} |"
                                                   f"{instance.financing_rate_91_180} |"
                                                   f" {instance.financing_rate_181_365} | "
                                                   f"{instance.financing_rate_366_plus}",
                                             message=f'Values for financing rates must be provided when'
                                                     f'financing total pc is not null'))

                if instance.total_financing_rates != 1:
                    print(InconsistencyError(sheet_name=sheet_name, index=idx + 1,
                                             column=f'financing_rate_0_1 | financing_rate_2_7 | '
                                                    f'financing_rate_8_30 | financing_rate_31_90 | '
                                                    f'financing_rate_91_180 | financing_rate_181_365 | '
                                                    f'financing_rate_366_plus',
                                             value=f"{instance.financing_rate_0_1} | {instance.financing_rate_2_7} |"
                                                   f"{instance.financing_rate_8_30} | {instance.financing_rate_31_90} |"
                                                   f"{instance.financing_rate_91_180} |"
                                                   f" {instance.financing_rate_181_365} | "
                                                   f"{instance.financing_rate_366_plus}",
                                             message=f'Values should sum up to 1.'
                                                     f' Difference {1 - instance.total_financing_rates}'))

            else:
                # financing_total_pc is null
                if any([DataProcessor.notnull(instance.financing_rate_0_1),
                        DataProcessor.notnull(instance.financing_rate_2_7),
                        DataProcessor.notnull(instance.financing_rate_8_30),
                        DataProcessor.notnull(instance.financing_rate_31_90),
                        DataProcessor.notnull(instance.financing_rate_91_180),
                        DataProcessor.notnull(instance.financing_rate_181_365),
                        DataProcessor.notnull(instance.financing_rate_366_plus)]):

                    print(InconsistencyError(sheet_name=sheet_name, index=idx + 1,
                                             column=f'financing_total_pc | financing_rate_0_1 | financing_rate_2_7 | '
                                                    f'financing_rate_8_30 | financing_rate_31_90 | '
                                                    f'financing_rate_91_180 | financing_rate_181_365 | '
                                                    f'financing_rate_366_plus',
                                             value=f"'{instance.financing_total_pc} |{instance.financing_rate_0_1} |"
                                                   f" {instance.financing_rate_2_7} |"
                                                   f"{instance.financing_rate_8_30} | {instance.financing_rate_31_90} |"
                                                   f"{instance.financing_rate_91_180} |"
                                                   f" {instance.financing_rate_181_365} | "
                                                   f"{instance.financing_rate_366_plus}",
                                             message=f'Values for financing rates must not be provided when'
                                                     f'financing total pc is null'))

            if DataProcessor.isnull(instance.invt_pref_trmt_flag):
                if any([instance.disc_pref_trmt_flag, instance.liq_pref_trmt_flag,
                        instance.fee_pref_trmt_flag, instance.oth_pref_trmt_flag]):
                    print(InconsistencyError(sheet_name=sheet_name, index=idx + 1,
                                             column=f'invt_pref_trmt_flag | disc_pref_trmt_flag |'
                                                    f' liq_pref_trmt_flag |fee_pref_trmt_flag | '
                                                    f' oth_pref_trmt_flag',
                                             value=f"{instance.invt_pref_trmt_flag} |"
                                                   f" {instance.disc_pref_trmt_flag} |"
                                                   f" {instance.liq_pref_trmt_flag} |"
                                                   f" {instance.fee_pref_trmt_flag} |"
                                                   f" {instance.oth_pref_trmt_flag}",
                                             message=f'Values in columns AA-AD should not be provided when'
                                                     f'invt_pref_trmt_flag is not Y'))

            else:
                if (any([instance.disc_pref_trmt_flag, instance.liq_pref_trmt_flag,
                         instance.fee_pref_trmt_flag, instance.oth_pref_trmt_flag])
                        and instance.invt_pref_trmt_flag != 'Y'):
                    print(InconsistencyError(sheet_name=sheet_name, index=idx + 1,
                                             column=f'invt_pref_trmt_flag | disc_pref_trmt_flag |'
                                                    f' liq_pref_trmt_flag |fee_pref_trmt_flag | '
                                                    f' oth_pref_trmt_flag',
                                             value=f"{instance.invt_pref_trmt_flag} |"
                                                   f" {instance.disc_pref_trmt_flag} |"
                                                   f" {instance.liq_pref_trmt_flag} |"
                                                   f" {instance.fee_pref_trmt_flag} |"
                                                   f" {instance.oth_pref_trmt_flag}",
                                             message=f'Values in columns AA-AD should not be provided when'
                                                     f'invt_pref_trmt_flag is not Y'))

                elif (not any([instance.disc_pref_trmt_flag == 'Y', instance.liq_pref_trmt_flag == 'Y',
                               instance.fee_pref_trmt_flag == 'Y', instance.oth_pref_trmt_flag == 'Y'])
                        and instance.invt_pref_trmt_flag == 'Y'):
                    print(InconsistencyError(sheet_name=sheet_name, index=idx + 1,
                                             column=f'invt_pref_trmt_flag | disc_pref_trmt_flag |'
                                                    f' liq_pref_trmt_flag |fee_pref_trmt_flag | '
                                                    f' oth_pref_trmt_flag',
                                             value=f"{instance.invt_pref_trmt_flag} |"
                                                   f" {instance.disc_pref_trmt_flag} |"
                                                   f" {instance.liq_pref_trmt_flag} |"
                                                   f" {instance.fee_pref_trmt_flag} |"
                                                   f" {instance.oth_pref_trmt_flag}",
                                             message=f'At least one value in columns AA-AD must be provided'
                                                     f' when invt_pref_trmt_flag is Y'))

                elif instance.invt_pref_trmt_flag not in DataProcessor.flags:
                    print(InconsistencyError(sheet_name=sheet_name, index=idx + 1,
                                             column=f'invt_pref_trmt_flag',
                                             value=f"{instance.invt_pref_trmt_flag}",
                                             message=f'Invalid value for invt_pref_trmt_flag'))

            if DataProcessor.notnull(instance.oth_arrangement_type):
                if DataProcessor.isnull(instance.oth_arrangement_rate):
                    print(InconsistencyError(sheet_name=sheet_name, index=idx + 1,
                                             column=f'oth_arrngement_type | oth_arrangement_rate',
                                             value=f"{instance.oth_arrangement_type}  |"
                                                   f"{instance.oth_arrangement_type}",
                                             message=f'Other arrangement rate must be provided when'
                                                     f'oth_arrangement_type is not null'))
            else:
                if DataProcessor.notnull(instance.oth_arrangement_rate):
                    print(InconsistencyError(sheet_name=sheet_name, index=idx + 1,
                                             column=f'oth_arrngement_type | oth_arrangement_rate',
                                             value=f"{instance.oth_arrangement_type}  |"
                                                   f"{instance.oth_arrangement_type}",
                                             message=f'Other arrangement rate must not be provided when'
                                                     f'oth_arrangement_type is null'))


_all_ = ['Risk_liquidity']

