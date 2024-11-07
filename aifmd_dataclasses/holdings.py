# holdings.py
import datetime
from collections import defaultdict
from typing import Dict, Tuple
from common.data_processor import DataProcessor
from common.errors import *


class Holdings(DataProcessor):
    all = []
    datatypes = {'pf_id': ('VARCHAR2', 35), 'provider_id': ('VARCHAR2', 20), 'nav_date': 'DATE',
                 'ins_name': ('VARCHAR2', 1000), 'market_value_pc': ('NUMBER', 18, 2), 'cp_name': ('VARCHAR2', 1200),
                 'short_long': ('NUMBER', 1, 0), 'market_code_type': ('VARCHAR2', 3), 'mic_code': ('VARCHAR2', 4),
                 'country_code': ('VARCHAR2', 20), 'maturity_date': 'DATE', 'hedge_flag': ('CHAR', 1),
                 'isin': ('VARCHAR2', 12), 'ccy_ic': ('VARCHAR2', 3), 'aii_code': ('VARCHAR2', 80),
                 'product_code': ('VARCHAR2', 12), 'derivative_type': ('VARCHAR2', 1), 'put_call_type': ('VARCHAR2', 1),
                 'strike_price': ('NUMBER', 22, 6), 'cp_lei_code': ('VARCHAR2', 20), 'cp_bic_code': ('VARCHAR2', 11),
                 'asset_sub_type_code': ('VARCHAR2', 12), 'ins_type': ('VARCHAR2', 80),
                 'ins_type_desc': ('VARCHAR2', 80),
                 'ins_class': ('VARCHAR2', 400), 'ins_class_desc': ('VARCHAR2', 800),
                 'industry_sector_code': ('VARCHAR2', 100), 'industry_sector_desc': ('VARCHAR2', 800),
                 'industry_sub_sector_code': ('VARCHAR2', 320), 'industry_sub_sector_desc': ('VARCHAR2', 320),
                 'rtg_grade': ('VARCHAR2', 5), 'listed_ins_flag': ('CHAR', 1), 'aum_pc': ('NUMBER', 18, 2),
                 'qnt': ('NUMBER', 20, 6), 'market_price_pc': ('NUMBER', 18, 6), 'market_price_ic': ('NUMBER', 18, 6),
                 'market_value_ic': ('NUMBER', 18, 2), 'notional_contract_size': ('NUMBER', 22, 6),
                 'notional_value_pc': ('NUMBER', 18, 2), 'market_value_ul': ('NUMBER', 18, 2),
                 'delta': ('NUMBER', 12, 6),
                 'ref_swap_conv_amt': ('NUMBER', 22, 6), 'vola_rel': ('NUMBER', 22, 6), 'vola_impl': ('NUMBER', 22, 6),
                 'strike': ('NUMBER', 22, 6), 'vega_notional': ('NUMBER', 22, 6), 'vola_cap': ('NUMBER', 22, 6),
                 'asset_sub_type_code_gb': ('VARCHAR2', 12)}

    prov_obl_codes = {'pf_id': 'M', 'provider_id': 'C(M)', 'nav_date': 'M', 'ins_name': 'M', 'market_value_pc': 'M',
                      'cp_name': 'C(M)', 'short_long': 'M', 'market_code_type': 'M', 'mic_code': 'C(M)',
                      'country_code': 'C(M)', 'maturity_date': 'C(M)', 'hedge_flag': 'M', 'isin': 'C(M)',
                      'ccy_ic': 'C(M/O)', 'aii_code': 'C(O)', 'product_code': 'C(O)', 'derivative_type': 'C(O)',
                      'put_call_type': 'C(O)', 'strike_price': 'C(O)', 'cp_lei_code': 'O', 'cp_bic_code': 'O',
                      'asset_sub_type_code': 'C(M)', 'ins_type': 'C(M)', 'ins_type_desc': 'C(M)', 'ins_class': 'C(M)',
                      'ins_class_desc': 'C(M)', 'industry_sector_code': 'C(M)', 'industry_sector_desc': 'C(M)',
                      'industry_sub_sector_code': 'C(M)', 'industry_sub_sector_desc': 'C(M)', 'rtg_grade': 'C(M)',
                      'listed_ins_flag': 'C(M)', 'aum_pc': 'C(M)', 'qnt': 'C(M)', 'market_price_pc': 'C(M)',
                      'market_price_ic': 'C(M)', 'market_value_ic': 'C(M)', 'notional_contract_size': 'C(M)',
                      'notional_value_pc': 'C(M)', 'market_value_ul': 'C(M)', 'delta': 'C(M)',
                      'ref_swap_conv_amt': 'C(M)', 'vola_rel': 'C(M)', 'vola_impl': 'C(M)',
                      'strike': 'C(M)', 'vega_notional': 'C(M)', 'vola_cap': 'C(M)', 'asset_sub_type_code_gb': 'C(M)'}

    asset_sub_type_codes = ["SEC_CSH_CODP", "SEC_CSH_COMP", "SEC_CSH_OTHD", "SEC_CSH_OTHC", "SEC_LEQ_IFIN",
                            "SEC_LEQ_OTHR", "SEC_UEQ_UEQY", "SEC_CPN_INVG", "SEC_CPN_NIVG", "SEC_CPI_INVG",
                            "SEC_CPI_NIVG", "SEC_SBD_EUBY", "SEC_SBD_EUBM", "SEC_SBD_NOGY", "SEC_SBD_NOGM",
                            "SEC_SBD_EUGY", "SEC_SBD_EUGM", "SEC_MBN_MNPL", "SEC_CBN_INVG", "SEC_CBN_NIVG",
                            "SEC_CBI_INVG", "SEC_CBI_NIVG", "SEC_LON_LEVL", "SEC_LON_OTHL", "SEC_SSP_SABS",
                            "SEC_SSP_RMBS", "SEC_SSP_CMBS", "SEC_SSP_AMBS", "SEC_SSP_ABCP", "SEC_SSP_CDOC",
                            "SEC_SSP_STRC", "SEC_SSP_SETP", "SEC_SSP_OTHS", "DER_EQD_FINI", "DER_EQD_OTHD",
                            "DER_FID_FIXI", "DER_CDS_SNFI", "DER_CDS_SNSO", "DER_CDS_SNOT", "DER_CDS_INDX",
                            "DER_CDS_EXOT", "DER_CDS_OTHR", "DER_FEX_INVT", "DER_FEX_HEDG", "DER_IRD_INTR",
                            "DER_CTY_ECOL", "DER_CTY_ENNG", "DER_CTY_ENPW", "DER_CTY_ENOT", "DER_CTY_PMGD",
                            "DER_CTY_PMOT", "DER_CTY_OTIM", "DER_CTY_OTLS", "DER_CTY_OTAP", "DER_CTY_OTHR",
                            "DER_OTH_OTHR", "PHY_RES_RESL", "PHY_RES_COML", "PHY_RES_OTHR", "PHY_CTY_PCTY",
                            "PHY_TIM_PTIM", "PHY_ART_PART", "PHY_TPT_PTPT", "PHY_OTH_OTHR", "CIU_OAM_MMFC",
                            "CIU_OAM_AETF", "CIU_OAM_OTHR", "CIU_NAM_MMFC", "CIU_NAM_AETF", "CIU_NAM_OTHR",
                            "OTH_OTH_OTHR", "NTA_NTA_NOTA"]

    sum_of_individual_nav: Dict[Tuple[str, datetime.date], float] = defaultdict(float)  # Initialise  total NaV with 0
    sum_of_individual_aum: Dict[Tuple[str, datetime.date], float] = defaultdict(float)

    def __init__(self, pf_id=None, provider_id=None, nav_date=None, ins_name=None, market_value_pc=None, cp_name=None,
                 short_long=None, market_code_type=None, mic_code=None, country_code=None, maturity_date=None,
                 hedge_flag=None, isin=None, ccy_ic=None, aii_code=None, product_code=None, derivative_type=None,
                 put_call_type=None, strike_price=None, cp_lei_code=None, cp_bic_code=None, asset_sub_type_code=None,
                 ins_type=None, ins_type_desc=None, ins_class=None, ins_class_desc=None, industry_sector_code=None,
                 industry_sector_desc=None, industry_sub_sector_code=None, industry_sub_sector_desc=None,
                 rtg_grade=None, listed_ins_flag=None, aum_pc=None, qnt=None, market_price_pc=None,
                 market_price_ic=None, market_value_ic=None, notional_contract_size=None, notional_value_pc=None,
                 market_value_ul=None, delta=None, ref_swap_conv_amt=None, vola_rel=None, vola_impl=None, strike=None,
                 vega_notional=None, vola_cap=None, asset_sub_type_code_gb=None, **kwargs):

        super().__init__()

        self.pf_id = pf_id
        self.provider_id = provider_id
        self.nav_date = nav_date
        self.ins_name = ins_name
        self.market_value_pc = market_value_pc
        self.cp_name = cp_name
        self.short_long = short_long
        self.market_code_type = market_code_type
        self.mic_code = mic_code
        self.country_code = country_code
        self.maturity_date = maturity_date
        self.hedge_flag = hedge_flag
        self.isin = isin
        self.ccy_ic = ccy_ic
        self.aii_code = aii_code
        self.product_code = product_code
        self.derivative_type = derivative_type
        self.put_call_type = put_call_type
        self.strike_price = strike_price
        self.cp_lei_code = cp_lei_code
        self.cp_bic_code = cp_bic_code
        self.asset_sub_type_code = asset_sub_type_code
        self.ins_type = ins_type
        self.ins_type_desc = ins_type_desc
        self.ins_class = ins_class
        self.ins_class_desc = ins_class_desc
        self.industry_sector_code = industry_sector_code
        self.industry_sector_desc = industry_sector_desc
        self.industry_sub_sector_code = industry_sub_sector_code
        self.industry_sub_sector_desc = industry_sub_sector_desc
        self.rtg_grade = rtg_grade
        self.listed_ins_flag = listed_ins_flag
        self.aum_pc = aum_pc
        self.qnt = qnt
        self.market_price_pc = market_price_pc
        self.market_price_ic = market_price_ic
        self.market_value_ic = market_value_ic
        self.notional_contract_size = notional_contract_size
        self.notional_value_pc = notional_value_pc
        self.market_value_ul = market_value_ul
        self.delta = delta
        self.ref_swap_conv_amt = ref_swap_conv_amt
        self.vola_rel = vola_rel
        self.vola_impl = vola_impl
        self.strike = strike
        self.vega_notional = vega_notional
        self.vola_cap = vola_cap
        self.asset_sub_type_code_gb = asset_sub_type_code_gb

        # Calculate total nav and aum per fund
        self.__class__.sum_of_individual_nav[(self.pf_id, self.nav_date)] += self.safe_round(self.market_value_pc, 2)
        self.__class__.sum_of_individual_aum[(self.pf_id, self.nav_date)] += self.safe_round(self.aum_pc, 2)

        # Append the list with the individual holdings
        self.__class__.all.append(self)

    def __repr__(self):
        return (
            f"Holdings("
            f"pf_id={repr(self.pf_id)}, "
            f"provider_id={repr(self.provider_id)}, "
            f"nav_date={repr(self.nav_date)}, "
            f"ins_name={repr(self.ins_name)}, "
            f"market_value_pc={repr(self.market_value_pc)}, "
            f"cp_name={repr(self.cp_name)}, "
            f"short_long={repr(self.short_long)}, "
            f"market_code_type={repr(self.market_code_type)}, "
            f"mic_code={repr(self.mic_code)}, "
            f"country_code={repr(self.country_code)}, "
            f"maturity_date={repr(self.maturity_date)}, "
            f"hedge_flag={repr(self.hedge_flag)}, "
            f"isin={repr(self.isin)}, "
            f"ccy_ic={repr(self.ccy_ic)}, "
            f"aii_code={repr(self.aii_code)}, "
            f"product_code={repr(self.product_code)}, "
            f"derivative_type={repr(self.derivative_type)}, "
            f"put_call_type={repr(self.put_call_type)}, "
            f"strike_price={repr(self.strike_price)}, "
            f"cp_lei_code={repr(self.cp_lei_code)}, "
            f"cp_bic_code={repr(self.cp_bic_code)}, "
            f"asset_sub_type_code={repr(self.asset_sub_type_code)}, "
            f"ins_type={repr(self.ins_type)}, "
            f"ins_type_desc={repr(self.ins_type_desc)}, "
            f"ins_class={repr(self.ins_class)}, "
            f"ins_class_desc={repr(self.ins_class_desc)}, "
            f"industry_sector_code={repr(self.industry_sector_code)}, "
            f"industry_sector_desc={repr(self.industry_sector_desc)}, "
            f"industry_sub_sector_code={repr(self.industry_sub_sector_code)}, "
            f"industry_sub_sector_desc={repr(self.industry_sub_sector_desc)}, "
            f"rtg_grade={repr(self.rtg_grade)}, "
            f"listed_ins_flag={repr(self.listed_ins_flag)}, "
            f"aum_pc={repr(self.aum_pc)}, "
            f"qnt={repr(self.qnt)}, "
            f"market_price_pc={repr(self.market_price_pc)}, "
            f"market_price_ic={repr(self.market_price_ic)}, "
            f"market_value_ic={repr(self.market_value_ic)}, "
            f"notional_contract_size={repr(self.notional_contract_size)}, "
            f"notional_value_pc={repr(self.notional_value_pc)}, "
            f"market_value_ul={repr(self.market_value_ul)}, "
            f"delta={repr(self.delta)}, "
            f"ref_swap_conv_amt={repr(self.ref_swap_conv_amt)}, "
            f"vola_rel={repr(self.vola_rel)}, "
            f"vola_impl={repr(self.vola_impl)}, "
            f"strike={repr(self.strike)}, "
            f"vega_notional={repr(self.vega_notional)}, "
            f"vola_cap={repr(self.vola_cap)}, "
            f"asset_sub_type_code_gb={repr(self.asset_sub_type_code_gb)})"
        )

    @classmethod
    def perform_quality_checks(cls):

        sheet_name = cls.__name__
        for idx, instance in enumerate(cls.all):

            if instance.short_long not in [-1, 1] and DataProcessor.notnull(instance.short_long):
                print(InconsistencyError(sheet_name, idx+1,
                                         "short_long", instance.short_long,
                                         message='Invalid short long value'))

            if (instance.market_code_type not in ["MIC", "OTC",  "XXX"] and
                    DataProcessor.notnull(instance.market_code_type)):
                print(InconsistencyError(sheet_name, idx + 1,
                                         "market_code_type", instance.market_code_type,
                                         message='Invalid market code type'))

            if DataProcessor.isnull(instance.mic_code):
                if instance.market_code_type.upper() == 'MIC' and DataProcessor.isnull(instance.aii_code):
                    print(InconsistencyError(sheet_name, idx + 1,
                                             column='market code type | mic_code',
                                             value=f'{instance.market_code_type} | {instance.mic_code}',
                                             message='MIC code is mandatory when market code type is MIC and '
                                                     'aii code is not provided'))
            # MIC code is provided
            else:
                if instance.market_code_type.upper() != 'MIC':
                    print(InconsistencyError(sheet_name, idx + 1,
                                             column='market code type | mic_code',
                                             value=f'{instance.market_code_type} | {instance.mic_code}',
                                             message='MIC code must be provided only if market code type is MIC'))

            if DataProcessor.isnull(instance.country_code):
                if not (instance.asset_sub_type_code.startswith('SEC_CSH') or
                        instance.asset_sub_type_code.startswith('DER_FEX') or
                        instance.asset_sub_type_code.startswith('DER_IRD')):

                    print(InconsistencyError(sheet_name, idx + 1,
                                             column='country_code | asset_sub_type_code',
                                             value=f'{instance.country_code} | {instance.asset_sub_type_code}',
                                             message=f"Country code must be provided for all holdings apart from those "
                                                     f"whose asset sub type code is SEC_CSH or DER_FEX or DER_IRD"))
            else:
                if instance.country_code not in instance.country_codes:
                    print(InconsistencyError(sheet_name, idx + 1,
                                             column='country_code',
                                             value=instance.country_code,
                                             message="Invalid country code"))

            if instance.hedge_flag not in instance.flags:
                print(InconsistencyError(sheet_name, idx + 1,
                                         column='hedge_flag',
                                         value=instance.hedge_flag,
                                         message='Invalid hedge flag'))

            if instance.asset_sub_type_code.startswith('SEC_CSH') and instance.ccy_ic not in instance.currency_codes:
                print(InconsistencyError(sheet_name, idx + 1,
                                         column='currency_code | asset_sub_type_code',
                                         value=f'{instance.ccy_ic} | {instance.asset_sub_type_code}',
                                         message=f'Currency code must be provided for holdings whose asset sub type '
                                                 f'code is SEC_CSH'))

            if DataProcessor.notnull(instance.ccy_ic) and instance.ccy_ic not in instance.currency_codes:
                print(InconsistencyError(sheet_name, idx + 1,
                                         column='currency_code',
                                         value=instance.ccy_ic,
                                         message='Invalid currency code'))

            if DataProcessor.notnull(instance.derivative_type) and instance.derivative_type not in ["O", "F"]:
                print(InconsistencyError(sheet_name, idx + 1,
                                         column='derivative_type',
                                         value=instance.derivative_type,
                                         message='Invalid derivative type'))

            if DataProcessor.notnull(instance.put_call_type) and instance.put_call_type not in ["C", "P"]:
                print(InconsistencyError(sheet_name, idx + 1,
                                         column='put_call_type',
                                         value=instance.put_call_type,
                                         message='Invalid put call type'))

            if DataProcessor.notnull(instance.aii_code):
                if any([instance.product_code,
                        instance.derivative_type,
                        instance.put_call_type,
                        instance.strike_price]):
                    print(InconsistencyError(sheet_name, idx + 1,
                                             column=f'aii_code | product_code | derivative_type | put_call_type |'
                                                    f' strike_price',
                                             value=f'{instance.aii_code} |{instance.product_code} |'
                                                   f' {instance.derivative_type} |'
                                                   f' {instance.put_call_type} | {instance.strike_price}',
                                             message=f'When aii_code is provided, columns:  product_code |'
                                                     f' derivative_type | put_call_type | strike_price must be empty'))

            if ((not any([instance.ins_type, instance.ins_type_desc,
                          instance.ins_class, instance.ins_class_desc, instance.industry_sector_code,
                          instance.industry_sector_desc, instance.industry_sub_sector_code,
                          instance.industry_sub_sector_desc,
                          instance.rtg_grade, instance.listed_ins_flag]) and
                 DataProcessor.isnull(instance.asset_sub_type_code))):
                print(InconsistencyError(sheet_name, idx + 1,
                                         column='asset_sub_type_code',
                                         value=instance.asset_sub_type_code,
                                         message=f'Provide adequate data in columns X-AG'
                                                 f' if asset sub type code is empty'))

            if (any([instance.ins_type, instance.ins_type_desc, instance.ins_class,
                     instance.ins_class_desc, instance.industry_sector_code,
                     instance.industry_sector_desc, instance.industry_sub_sector_code,
                     instance.industry_sub_sector_desc,
                     instance.rtg_grade, instance.listed_ins_flag]) and
                    DataProcessor.notnull(instance.asset_sub_type_code)):

                print(InconsistencyError(sheet_name, idx + 1,
                                         column='asset_sub_type_code',
                                         value=instance.asset_sub_type_code,
                                         message=f'Column X-AG must not to be provided when'
                                                 f' asset sub type code is provided'))

            if (DataProcessor.notnull(instance.asset_sub_type_code) and
                    instance.asset_sub_type_code not in instance.asset_sub_type_codes):

                print(InconsistencyError(sheet_name, idx + 1,
                                         column='asset_sub_type_code',
                                         value=instance.asset_sub_type_code,
                                         message=f'Invalid asset sub type code'))

            if (DataProcessor.isnull(instance.aum_pc)
                    and
                    not all([instance.qnt, instance.market_price_pc, instance.market_price_ic, instance.market_value_ic,
                             instance.notional_contract_size, instance.notional_value_pc, instance.market_value_ul,
                             instance.delta, instance.ref_swap_conv_amt,	instance.vola_rel, instance.vola_impl,
                             instance.strike, instance.vega_notional, instance.vola_cap])):

                print(InconsistencyError(sheet_name, idx + 1,
                                         column='aum_pc',
                                         value=instance.aum_pc,
                                         message=f'When aum_pc not provided, the columns AI-AG must be filled in'))

            if (DataProcessor.notnull(instance.aum_pc)
                    and any([instance.qnt, instance.market_price_pc, instance.market_price_ic, instance.market_value_ic,
                             instance.notional_contract_size, instance.notional_value_pc, instance.market_value_ul,
                             instance.delta, instance.ref_swap_conv_amt, instance.vola_rel, instance.vola_impl,
                             instance.strike, instance.vega_notional, instance.vola_cap])):

                print(InconsistencyError(sheet_name, idx + 1,
                                         column='aum_pc',
                                         value=instance.aum_pc,
                                         message=f'When aum_pc is provided, the columns AI-AG must not be filled in'))

            if (DataProcessor.notnull(instance.aum_pc) and isinstance(instance.aum_pc, (float, int))
                    and instance.aum_pc < 0):

                print(InconsistencyError(sheet_name, idx + 1,
                                         column='aum_pc',
                                         value=instance.aum_pc,
                                         message=f'Aum_pc must be greater than or equal to zero'))


__all__ = ['Holdings']
