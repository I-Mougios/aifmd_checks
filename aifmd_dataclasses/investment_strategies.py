# investment_strategies.py
from collections import defaultdict
from numbers import Real
import math
from typing import Dict, Tuple, Set
import datetime
from common.errors import *
from common.data_processor import DataProcessor
from aifmd_dataclasses.fund_static import Fund_Static


class Investment_Strategies(DataProcessor):

    all = []
    datatypes = {'pf_id': ('VARCHAR2', 35), 'provider_id': ('VARCHAR2', 20), 'nav_date': 'DATE',
                 'predom_aif_type': ('VARCHAR2', 4), 'inv_stg_code': ('VARCHAR2', 9),
                 'inv_stg_nav_rate': ('NUMBER', 23, 6), 'inv_stg_type_desc': ('VARCHAR2', 1200)}

    prov_obl_codes = {'pf_id': 'M', 'provider_id': 'C(M)', 'nav_date': 'M', 'predom_aif_type': 'M', 'inv_stg_code': 'M',
                      'inv_stg_nav_rate': 'C(M)', 'inv_stg_type_desc': 'C(M)'}

    inv_stg_codes = {
        'HFND': ["EQTY_LGBS", "EQTY_LGST", "EQTY_MTNL", "EQTY_STBS", "RELV_FXIA",
                 "RELV_CBAR", "RELV_VLAR", "EVDR_DSRS", "EVDR_RAMA", "EVDR_EYSS",
                 "CRED_LGST", "CRED_ABLG", "MACR_MACR", "MANF_CTAF", "MANF_CTAQ",
                 "MULT_HFND", "OTHR_HFND"],
        'PEQF': ["VENT_CAPL", "GRTH_CAPL", "MZNE_CAPL", "MULT_PEQF", "OTHR_PEQF"],
        'REST': ["RESL_REST", "COML_REST", "INDL_REST", "MULT_REST", "OTHR_REST"],
        'FOFS': ["FOFS_FHFS", "FOFS_PRIV", "OTHR_FOFS"],
        'OTHR': ["OTHR_COMF", "OTHR_EQYF", "OTHR_FXIF", "OTHR_INFF", "OTHR_OTHF"],

        'NONE': ["EQTY_LGBS", "EQTY_LGST", "EQTY_MTNL", "EQTY_STBS", "RELV_FXIA"
                 "RELV_CBAR", "RELV_VLAR", "EVDR_DSRS", "EVDR_RAMA", "EVDR_EYSS",
                 "CRED_ABLG", "MACR_MACR", "MANF_CTAF", "MANF_CTAQ", "MULT_HFND",
                 "VENT_CAPL", "GRTH_CAPL", "MZNE_CAPL", "MULT_PEQF", "OTHR_PEQF",
                 "RESL_REST", "COML_REST", "INDL_REST", "MULT_REST", "OTHR_REST",
                 "FOFS_FHFS", "FOFS_PRIV", "OTHR_FOFS", "OTHR_COMF", "OTHR_EQYF",
                 "CRED_LGST", "OTHR_HFND", "OTHR_FXIF", "OTHR_INFF", "OTHR_OTHF"
                 ]
                    }
    # Sum the investment strategies NaV rate per fund
    total_invest_nav_rate: Dict[Tuple[str, datetime.date], float] = defaultdict(int)  # initialize with 0
    # Gathering the different investment strategies per fund
    unique_invest_stg_codes: Dict[Tuple[str, datetime.date], Set] = defaultdict(set)  # initialize with an empty set
    # Unique predominant aif types per fund
    unique_aif_types: Dict[Tuple[str, datetime.date], Set] = defaultdict(set)  # empty set

    def __init__(self, pf_id=None, provider_id=None, nav_date=None, predom_aif_type=None, inv_stg_code=None,
                 inv_stg_nav_rate=None, inv_stg_type_desc=None, **kwargs):
        super().__init__()

        self.pf_id = pf_id
        self.provider_id = provider_id
        self.nav_date = nav_date
        self.predom_aif_type = predom_aif_type
        self.inv_stg_code = inv_stg_code
        self.inv_stg_nav_rate = inv_stg_nav_rate
        self.inv_stg_type_desc = inv_stg_type_desc

        self.__class__.all.append(self)
        # Calculate the total investment nav rate per report.
        if isinstance(self.inv_stg_nav_rate, Real):
            self.__class__.total_invest_nav_rate[(self.pf_id, self.nav_date)] += self.safe_round(self.inv_stg_nav_rate,
                                                                                                 digits=6)
        # Gather the unique investment strategies codes per fund.
        self.__class__.unique_invest_stg_codes[(self.pf_id, self.nav_date)].add(self.inv_stg_code)

        # Gather the aif types per fund
        self.__class__.unique_aif_types[(self.pf_id, self.nav_date)].add(self.predom_aif_type)

    def __repr__(self):
        return (
            f"Investment_Strategies("
            f"pf_id={repr(self.pf_id)}, "
            f"provider_id={repr(self.provider_id)}, "
            f"nav_date={repr(self.nav_date)}, "
            f"predom_aif_type={repr(self.predom_aif_type)}, "
            f"inv_stg_code={repr(self.inv_stg_code)}, "
            f"inv_stg_nav_rate={repr(self.inv_stg_nav_rate)}, "
            f"inv_stg_type_desc={repr(self.inv_stg_type_desc)}"
            f")"
        )

    @classmethod
    def perform_quality_checks(cls):
        sheet_name = cls.__name__

        for idx, instance in enumerate(cls.all):
            if (DataProcessor.notnull(instance.inv_stg_code)
                    and instance.inv_stg_code.strip().upper() not in ["MULT_PEQF", "MULT_HFND", "MULT_REST"]
                    and DataProcessor.isnull(instance.inv_stg_nav_rate)):
                print(InconsistencyError(sheet_name, idx+1, 'inv_stg_nav_rate',
                      value=instance.inv_stg_nav_rate,
                      message=f"Missing inv_stg_nav_rate value."
                                         f" The field is mandatory for reported investment"
                                         f" strategy codes different from MULT_PEQF, MULT_HFND or MULT_REST"
                                         )
                      )

            if (DataProcessor.notnull(instance.inv_stg_code) and
                    instance.inv_stg_code.strip().upper() in ["OTHR_HFND", "OTHR_PRIV",
                                                              "OTHR_REST", "OTHR_FOFS", "OTHR_OTHF"]):

                if DataProcessor.isnull(instance.inv_stg_type_desc):
                    print(InconsistencyError(sheet_name, idx+1, 'inv_stg_type_desc',
                                             value=instance.inv_stg_type_desc,
                                             message=f"Missing inv_stg_type_desc value."
                                                     f" The field is mandatory for reported investment "
                                                     f"strategies OTHR_HFND, OTHR_PRIV "
                                                     f"OTHR_REST, OTHR_FOFS, OTHR_OTHF"
                                             )
                          )
            else:
                if DataProcessor.notnull(instance.inv_stg_type_desc):
                    print(InconsistencyError(sheet_name, idx+1, 'inv_stg_type_desc',
                                             value=f"{instance.inv_stg_type_desc}| {instance.inv_stg_code}",
                                             message=f"This field must be provided only when reported investment. "
                                                     f"strategy is OTHR_HFND, OTHR_PRIV "
                                                     f"OTHR_REST, OTHR_FOFS, OTHR_OTHF"
                                             )
                          )
            # Check the validity of the predominant aif type
            try:
                cls.inv_stg_codes[instance.predom_aif_type]
            except KeyError:
                if DataProcessor.notnull(instance.predom_aif_type):
                    print(InconsistencyError(sheet_name, idx+1, 'predom_aif_type',
                                             value=instance.predom_aif_type,
                                             message='Invalid predominant aif type'
                                             )
                          )
            # Consistency check between predominant aif type and investment strategy
            if (DataProcessor.notnull(instance.inv_stg_code) and
                    instance.inv_stg_code.strip() not in cls.inv_stg_codes.get(instance.predom_aif_type)):
                print(InconsistencyError(sheet_name, idx+1, 'inv_stg_code',
                                         value=f"{instance.inv_stg_code} | {instance.predom_aif_type}",
                                         message=f'Investment strategy code not in line with the predominant aif type'
                                         )
                      )

    @classmethod
    def check_aif_type(cls):
        sheet_name = cls.__name__
        # for each fund retrieve the aif_types
        for key, aif_types in cls.unique_aif_types.items():
            # Only one aif type is acceptable per fund
            if len(aif_types) > 1:
                print(InconsistencyError(sheet_name, '--',
                                         column='predom_aif_type',
                                         value=f"{key[0]} | {aif_types}",
                                         message='When the fund has investment strategy codes from more than one'
                                                 ' aif types, the predominant aif type must be NONE'))
            else:
                # Check if the predominant aif type is NONE and all strategy codes belong to the same aif type
                predom_aif_type = next(iter(aif_types))
                if predom_aif_type == 'NONE':
                    aif_types_of_inv_stg = set()
                    # Iterate over the  investment strategies of the fund
                    for stg_code in cls.unique_invest_stg_codes[key]:
                        for aif_type in cls.inv_stg_codes:
                            # Gather the aif types in which the investment strategies belong to
                            if stg_code in cls.inv_stg_codes[aif_type]:
                                aif_types_of_inv_stg.add(aif_type)
                                break  # exhaust the inner for loop and continue with the next investment strategy

                    if len(aif_types_of_inv_stg) < 2:
                        print(InconsistencyError(sheet_name, '--',
                                                 column='predom_aif_type',
                                                 value=f"{key[0]} | {predom_aif_type} |"
                                                       f" {cls.unique_invest_stg_codes[key]} ",
                                                 message='When the predominant AIF type is NONE the investment'
                                                         ' strategies must belong to more than one AIF type'))

    @classmethod
    def check_inv_stg_nav_rates(cls):
        sheet_name = cls.__name__
        for key, total_nav_rate in cls.total_invest_nav_rate.items():
            if not math.isclose(total_nav_rate, 1, abs_tol=1e-10):
                print(InconsistencyError(sheet_name, '--', column='inv_nav_rate',
                                         value=f"{key[0]} | {total_nav_rate}",
                                         message='Investment strategy nav rates per fund must sum to 1'))

    @classmethod
    def check_pos_size_code(cls):
        sheet_name = cls.__name__
        for key, value in cls.unique_aif_types.items():
            aif_type = next(iter(value))
            if aif_type == 'PEQF':
                if Fund_Static.pos_size_codes_per_fund.get(key) not in Fund_Static.pos_size_codes:
                    print(InconsistencyError(sheet_name, '--',
                                             column='Predom_aif_type | Fund_Static.pos_size_codes',
                                             value=f"{key[0]} | {aif_type} |"
                                                   f" {Fund_Static.pos_size_codes_per_fund.get(key)}",
                                             message=f'Position size code in Fund static tab is mandatory'
                                                     f' when predominant aif type is PEQF'
                                             )
                          )
            else:
                if DataProcessor.notnull(Fund_Static.pos_size_codes_per_fund.get(key)):
                    print(InconsistencyError(sheet_name, '--',
                                             column='Predom_aif_type | Fund_Static.pos_size_codes',
                                             value=f"{key[0]} | {aif_type} | "
                                                   f"{Fund_Static.pos_size_codes_per_fund.get(key)}",
                                             message=f'Position size code in Fund static must be provided only if '
                                                     f'aif type is PEQF and forbidden otherwise.'))


__all__ = ['Investment_Strategies']


