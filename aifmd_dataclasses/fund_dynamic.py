# fund_dynamic.py
from aifmd_dataclasses.holdings import Holdings
from aifmd_dataclasses.fund_static import Fund_Static
from common.data_processor import DataProcessor
from common.errors import *


class Fund_Dynamic(DataProcessor):

    all = []
    datatypes = {'pf_id': ('VARCHAR2', 35), 'provider_id': ('VARCHAR2', 20), 'nav_date': 'DATE',
                 'manco_name': ('VARCHAR2', 200), 'fx_rate': ('NUMBER', 19, 4), 'fx_rate_type': ('VARCHAR2', 10),
                 'fx_rate_desc': ('VARCHAR2', 1200), 'nav_pf': ('NUMBER', 22, 8), 'hft_tra_count': ('NUMBER', 25, 0),
                 'hft_tra_market_value_pc': ('NUMBER', 18, 6)}

    prov_obl_codes = {'pf_id': 'M', 'provider_id': 'C(M)', 'nav_date': 'M', 'manco_name': 'M', 'fx_rate': 'C(M)',
                      'fx_rate_type': 'C(M)', 'fx_rate_desc': 'C(M)', 'nav_pf': 'M', 'hft_tra_count': 'C(M)',
                      'hft_tra_market_value_pc': 'C(M)'}

    def __init__(self, pf_id=None, provider_id=None, nav_date=None,	manco_name=None, fx_rate=None, fx_rate_type=None,
                 fx_rate_desc=None, nav_pf=None, hft_tra_count=None, hft_tra_market_value_pc=None, **kwargs):

        super().__init__()
        self.pf_id = pf_id
        self.provider_id = provider_id
        self.nav_date = nav_date
        self.manco_name = manco_name
        self.fx_rate = fx_rate
        self.fx_rate_type = fx_rate_type
        self.fx_rate_desc = fx_rate_desc
        self.nav_pf = nav_pf
        self.hft_tra_count = hft_tra_count
        self.hft_tra_market_value_pc = hft_tra_market_value_pc

        self.__class__.all.append(self)

    def __repr__(self):
        return (
            f"Fund_Dynamic("
            f"pf_id={repr(self.pf_id)}, "
            f"provider_id={repr(self.provider_id)}, "
            f"nav_date={repr(self.nav_date)}, "
            f"manco_name={repr(self.manco_name)}, "
            f"fx_rate={repr(self.fx_rate)}, "
            f"fx_rate_type={repr(self.fx_rate_type)}, "
            f"fx_rate_desc={repr(self.fx_rate_desc)}, "
            f"nav_pf={repr(self.nav_pf)}, "
            f"hft_tra_count={repr(self.hft_tra_count)}, "
            f"hft_tra_market_value_pc={repr(self.hft_tra_market_value_pc)})"
        )

    @classmethod
    def perform_quality_checks(cls):
        sheet_name = cls.__name__

        if Fund_Static.all and Fund_Dynamic.all:
            for idx, f_d_instance in enumerate(Fund_Dynamic.all):
                for f_s_instance in Fund_Static.all:

                    if (f_d_instance.pf_id.strip() == f_s_instance.pf_id.strip() and
                            f_d_instance.nav_date == f_s_instance.nav_date):

                        if f_s_instance.ccy_pc == 'EUR':
                            if any([DataProcessor.notnull(f_d_instance.fx_rate),
                                    DataProcessor.notnull(f_d_instance.fx_rate_type),
                                    DataProcessor.notnull(f_d_instance.fx_rate_desc)]):

                                print(InconsistencyError(sheet_name, idx + 1,
                                                         column='fx_rate | fx_rate_type | fx_rate_desc',
                                                         value=f"{f_d_instance.fx_rate} | {f_d_instance.fx_rate_type}"
                                                               f" | {f_d_instance.fx_rate_desc}",
                                                         message=f'Columns fx_rate | fx_rate_type |'
                                                                 f' fx_rate_desc must be'
                                                                 f' populated only if portfolio currency is'
                                                                 f' different from EUR'))
                        else:
                            if DataProcessor.isnull(f_d_instance.fx_rate):
                                print(InconsistencyError(sheet_name, idx + 1,
                                                         column='fx_rate',
                                                         value=f_d_instance.fx_rate,
                                                         message=f'Columns fx_rate must be provided when '
                                                                 f'portfolio currency is different from EUR'))

                            if f_d_instance.fx_rate_type not in ['ECB', 'OTH']:
                                print(InconsistencyError(sheet_name, idx + 1,
                                                         column='fx_rate_type',
                                                         value=f_d_instance.fx_rate,
                                                         message=f'Invalid fx_rate_type'))
                            else:
                                if (f_d_instance.fx_rate_type == 'ECB' and
                                        DataProcessor.notnull(f_d_instance.fx_rate_desc)):

                                    print(InconsistencyError(sheet_name, idx + 1,
                                                             column='fx_rate_desc',
                                                             value=f_d_instance.fx_rate_desc,
                                                             message=f'Invalid fx_rate_desc must not be provided'
                                                                     f' when fx_rate_type is ECB'))

                                elif (f_d_instance.fx_rate_type == 'OTH' and
                                        DataProcessor.isnull(f_d_instance.fx_rate_desc)):

                                    print(InconsistencyError(sheet_name, idx + 1,
                                                             column='fx_rate_desc',
                                                             value=f_d_instance.fx_rate_desc,
                                                             message=f'fx_rate_desc must be provided when fx_rate_type'
                                                                     f' is OTH'))
                        break

    @classmethod
    def check_total_nav(cls):
        if Holdings.all:
            for idx, instance in enumerate(cls.all):
                try:
                    if (DataProcessor.safe_round(Holdings.sum_of_individual_nav[(instance.pf_id, instance.nav_date)]) !=
                            DataProcessor.safe_round(instance.nav_pf)):
                        diff = instance.nav_pf - Holdings.sum_of_individual_nav[(instance.pf_id, instance.nav_date)]
                        print(InconsistencyError(cls.__name__, idx + 1, column='nav_pf', value=instance.nav_pf,
                                                 message=f"Sum of individual holdings must be equal to total fund's nav"
                                                         f" Difference: {diff}"))
                except KeyError:
                    print(InconsistencyError(cls.__name__, idx + 1, column='----', value='----',
                                             message=f'No Holdings data for portfolio {instance.pf_id} '))
        else:
            print('No holdings at all')


__all__ = ['Fund_Dynamic']
