# risk_measures.py
from common.data_processor import DataProcessor
from common.errors import *


class Risk_Measures(DataProcessor):
    all = []
    prov_obl_codes = {'pf_id': 'M', 'provider_id': 'C(M)', 'nav_date': 'M', 'expct_annu_return_rate': 'M',
                      'stress_test_result_a': 'M', 'stress_test_result_b': 'M', 'lev_rate_gross_mthd': 'M',
                      'lev_rate_comm_mthd': 'M', 'rehex_flag': 'M', 'rehex_rate': 'C(O)', 'net_fx_delta': 'C(M)',
                      'net_fx_risk_measure_desc': 'C(M)', 'net_cty_delta': 'C(M)', 'net_cty_risk_measure_desc': 'C(M)',
                      'net_eqty_delta': 'M', 'net_eqty_risk_measure_desc': 'C(M)', 'net_dv_5': 'M', 'net_dv_5_15': 'M',
                      'net_dv_15': 'M', 'net_dv_risk_measure_desc': 'C(M)', 'net_cs_5': 'M', 'net_cs_5_15': 'M',
                      'net_cs_15': 'M', 'net_cs_risk_measure_desc': 'C(M)', 'vega_value_curr': 'C(M)',
                      'vega_value_down_10': 'C(M)', 'vega_value_up_10': 'C(M)', 'vega_risk_measure_desc': 'C(M)',
                      'var_value': 'C(M)', 'var_cal_method_code_type': 'C(M)', 'var_risk_measure_desc': 'C(M)'}

    datatypes = {'pf_id': ('VARCHAR2', 35), 'provider_id': ('VARCHAR2', 20), 'nav_date': 'DATE',
                 'expct_annu_return_rate': ('NUMBER', 19, 4), 'stress_test_result_a': 'CLOB',
                 'stress_test_result_b': 'CLOB', 'lev_rate_gross_mthd': ('NUMBER', 19, 4),
                 'lev_rate_comm_mthd': ('NUMBER', 19, 4), 'rehex_flag': ('CHAR', 1),
                 'rehex_rate': ('NUMBER', 5, 4), 'net_fx_delta': ('NUMBER', 15, 2),
                 'net_fx_risk_measure_desc': ('VARCHAR2', 1200), 'net_cty_delta': ('NUMBER', 15, 2),
                 'net_cty_risk_measure_desc': ('VARCHAR2', 1200), 'net_eqty_delta': ('NUMBER', 15, 2),
                 'net_eqty_risk_measure_desc': ('VARCHAR2', 1200), 'net_dv_5': ('NUMBER', 15, 2),
                 'net_dv_5_15': ('NUMBER', 15, 2), 'net_dv_15': ('NUMBER', 15, 2),
                 'net_dv_risk_measure_desc': ('VARCHAR2', 1200), 'net_cs_5': ('NUMBER', 15, 2),
                 'net_cs_5_15': ('NUMBER', 15, 2), 'net_cs_15': ('NUMBER', 15, 2),
                 'net_cs_risk_measure_desc': ('VARCHAR2', 1200), 'vega_value_curr': ('NUMBER', 15, 2),
                 'vega_value_down_10': ('NUMBER', 15, 2), 'vega_value_up_10': ('NUMBER', 15, 2),
                 'vega_risk_measure_desc': ('VARCHAR2', 1200), 'var_value': ('NUMBER', 7, 4),
                 'var_cal_method_code_type': ('VARCHAR2', 5), 'var_risk_measure_desc': ('VARCHAR2', 1200)}

    def __init__(self, pf_id=None, provider_id=None, nav_date=None, expct_annu_return_rate=None,
                 stress_test_result_a=None, stress_test_result_b=None, lev_rate_gross_mthd=None,
                 lev_rate_comm_mthd=None, rehex_flag=None, rehex_rate=None, net_fx_delta=None,
                 net_fx_risk_measure_desc=None, net_cty_delta=None, net_cty_risk_measure_desc=None,
                 net_eqty_delta=None, net_eqty_risk_measure_desc=None, net_dv_5=None, net_dv_5_15=None,
                 net_dv_15=None, net_dv_risk_measure_desc=None, net_cs_5=None, net_cs_5_15=None, net_cs_15=None,
                 net_cs_risk_measure_desc=None, vega_value_curr=None, vega_value_down_10=None, vega_value_up_10=None,
                 vega_risk_measure_desc=None, var_value=None, var_cal_method_code_type=None,
                 var_risk_measure_desc=None, **kwargs):

        super().__init__()

        self.pf_id = pf_id
        self.provider_id = provider_id
        self.nav_date = nav_date
        self.expct_annu_return_rate = expct_annu_return_rate
        self.stress_test_result_a = stress_test_result_a
        self.stress_test_result_b = stress_test_result_b
        self.lev_rate_gross_mthd = lev_rate_gross_mthd
        self.lev_rate_comm_mthd = lev_rate_comm_mthd
        self.rehex_flag = rehex_flag
        self.rehex_rate = rehex_rate
        self.net_fx_delta = net_fx_delta
        self.net_fx_risk_measure_desc = net_fx_risk_measure_desc
        self.net_cty_delta = net_cty_delta
        self.net_cty_risk_measure_desc = net_cty_risk_measure_desc
        self.net_eqty_delta = net_eqty_delta
        self.net_eqty_risk_measure_desc = net_eqty_risk_measure_desc
        self.net_dv_5 = net_dv_5
        self.net_dv_5_15 = net_dv_5_15
        self.net_dv_15 = net_dv_15
        self.net_dv_risk_measure_desc = net_dv_risk_measure_desc
        self.net_cs_5 = net_cs_5
        self.net_cs_5_15 = net_cs_5_15
        self.net_cs_15 = net_cs_15
        self.net_cs_risk_measure_desc = net_cs_risk_measure_desc
        self.vega_value_curr = vega_value_curr
        self.vega_value_down_10 = vega_value_down_10
        self.vega_value_up_10 = vega_value_up_10
        self.vega_risk_measure_desc = vega_risk_measure_desc
        self.var_value = var_value
        self.var_cal_method_code_type = var_cal_method_code_type
        self.var_risk_measure_desc = var_risk_measure_desc

        # Gather all the instances
        self.__class__.all.append(self)

    def __repr__(self):
        return (
            f"Risk_Measures("
            f"pf_id={repr(self.pf_id)}, "
            f"provider_id={repr(self.provider_id)}, "
            f"nav_date={repr(self.nav_date)}, "
            f"expct_annu_return_rate={repr(self.expct_annu_return_rate)}, "
            f"stress_test_result_a={repr(self.stress_test_result_a)}, "
            f"stress_test_result_b={repr(self.stress_test_result_b)}, "
            f"lev_rate_gross_mthd={repr(self.lev_rate_gross_mthd)}, "
            f"lev_rate_comm_mthd={repr(self.lev_rate_comm_mthd)}, "
            f"rehex_flag={repr(self.rehex_flag)}, "
            f"rehex_rate={repr(self.rehex_rate)}, "
            f"net_fx_delta={repr(self.net_fx_delta)}, "
            f"net_fx_risk_measure_desc={repr(self.net_fx_risk_measure_desc)}, "
            f"net_cty_delta={repr(self.net_cty_delta)}, "
            f"net_cty_risk_measure_desc={repr(self.net_cty_risk_measure_desc)}, "
            f"net_eqty_delta={repr(self.net_eqty_delta)}, "
            f"net_eqty_risk_measure_desc={repr(self.net_eqty_risk_measure_desc)}, "
            f"net_dv_5={repr(self.net_dv_5)}, "
            f"net_dv_5_15={repr(self.net_dv_5_15)}, "
            f"net_dv_15={repr(self.net_dv_15)}, "
            f"net_dv_risk_measure_desc={repr(self.net_dv_risk_measure_desc)}, "
            f"net_cs_5={repr(self.net_cs_5)}, "
            f"net_cs_5_15={repr(self.net_cs_5_15)}, "
            f"net_cs_15={repr(self.net_cs_15)}, "
            f"net_cs_risk_measure_desc={repr(self.net_cs_risk_measure_desc)}, "
            f"vega_value_curr={repr(self.vega_value_curr)}, "
            f"vega_value_down_10={repr(self.vega_value_down_10)}, "
            f"vega_value_up_10={repr(self.vega_value_up_10)}, "
            f"vega_risk_measure_desc={repr(self.vega_risk_measure_desc)}, "
            f"var_value={repr(self.var_value)}, "
            f"var_cal_method_code_type={repr(self.var_cal_method_code_type)}, "
            f"var_risk_measure_desc={repr(self.var_risk_measure_desc)}"
            f")"
        )

    @classmethod
    def perform_quality_checks(cls):
        sheet_name = cls.__name__
        for idx, instance in enumerate(cls.all):
            if DataProcessor.notnull(instance.rehex_flag) and instance.rehex_flag not in instance.flags:
                print(InconsistencyError(sheet_name=sheet_name, index=idx+1, column='rehex_flag',
                                         value=instance.rehex_flag,
                                         message='Invalid rehex flag'))

            if instance.rehex_flag.upper != 'Y' and DataProcessor.notnull(instance.rehex_rate):
                print(InconsistencyError(sheet_name=sheet_name, index=idx+1, column='rehex_flag | rehex_rate',
                                         value=f"{instance.rehex_rate} | {instance.rehex_flag}",
                                         message='rehex_rate can be provided when rehex_flag is set to Y'))

            if instance.net_eqty_delta == 0:
                if DataProcessor.isnull(instance.net_eqty_risk_measure_desc):
                    print(InconsistencyError(sheet_name=sheet_name, index=idx+1,
                                             column='net_eqty_delta | net_eqty_risk_measure_desc',
                                             value=f"{instance.net_eqty_delta} | {instance.net_eqty_risk_measure_desc}",
                                             message=f'net_eqty_risk_measure_desc cannot be null'
                                                     f' when net_eqty_delta is 0'))
            else:
                if DataProcessor.notnull(instance.net_eqty_risk_measure_desc):
                    print(InconsistencyError(sheet_name=sheet_name, index=idx+1,
                                             column='net_eqty_risk_measure_desc | net_eqty_risk_measure_desc',
                                             value=f"{instance.net_eqty_delta} | {instance.net_eqty_risk_measure_desc}",
                                             message=f'net_eqty_risk_measure_desc must be null'
                                                     f' when net_eqty_delta is not 0'))

            if instance.net_cty_delta == 0:
                if DataProcessor.isnull(instance.net_cty_risk_measure_desc):
                    print(InconsistencyError(sheet_name=sheet_name, index=idx+1,
                                             column='net_cty_delta | net_cty_risk_measure_desc',
                                             value=f"{instance.net_cty_delta} | {instance.net_cty_risk_measure_desc}",
                                             message=f'net_cty_risk_measure_desc cannot be null'
                                                     f' when net_cty_delta is 0'))
            else:
                if DataProcessor.notnull(instance.net_cty_risk_measure_desc):
                    print(InconsistencyError(sheet_name=sheet_name, index=idx + 1,
                                             column='net_cty_risk_measure_desc | net_cty_risk_measure_desc',
                                             value=f"{instance.net_cty_delta} | {instance.net_cty_risk_measure_desc}",
                                             message=f'net_cty_risk_measure_desc must be null'
                                                     f' when net_cty_delta is not 0'))

            if instance.net_fx_delta == 0:
                if DataProcessor.isnull(instance.net_fx_risk_measure_desc):
                    print(InconsistencyError(sheet_name=sheet_name, index=idx+1,
                                             column='net_fx_delta | net_fx_risk_measure_desc',
                                             value=f"{instance.net_fx_delta} | {instance.net_fx_risk_measure_desc}",
                                             message=f'net_fx_risk_measure_desc cannot be null'
                                                     f' when net_fx_delta is 0'))
            else:
                if DataProcessor.notnull(instance.net_fx_risk_measure_desc):
                    print(InconsistencyError(sheet_name=sheet_name, index=idx + 1,
                                             column='net_fx_risk_measure_desc | net_fx_risk_measure_desc',
                                             value=f"{instance.net_fx_delta} | {instance.net_fx_risk_measure_desc}",
                                             message=f'net_fx_risk_measure_desc must be null'
                                                     f' when net_fx_delta is not 0'))

            if instance.net_dv_5 == 0 and instance.net_dv_5_15 == 0 and instance.net_dv_15 == 0:
                if DataProcessor.isnull(instance.net_dv_risk_measure_desc):
                    print(InconsistencyError(sheet_name=sheet_name, index=idx+1,
                                             column='net_dv_5 | net_dv_5_15 | net_dv_15 | net_dv_risk_measure_desc',
                                             value=f"{instance.net_dv_5} | {instance.net_dv_5_15} |"
                                                   f" {instance.net_dv_15}"
                                                   f" | {instance.net_dv_risk_measure_desc}",
                                             message=f'net_dv_risk_measure_desc must be provided only when all the '
                                                     f'corresponding values are 0'))
            else:
                if DataProcessor.notnull(instance.net_dv_risk_measure_desc):
                    print(InconsistencyError(sheet_name=sheet_name, index=idx + 1,
                                             column='net_dv_5 | net_dv_5_15 | net_dv_15 | net_dv_risk_measure_desc',
                                             value=f"{instance.net_dv_5} | {instance.net_dv_5_15} |"
                                                   f" {instance.net_dv_15}"
                                                   f" | {instance.net_dv_risk_measure_desc}",
                                             message=f'net_dv_risk_measure_desc should be filled '
                                                     f'only when all the corresponding values are 0'))

            if instance.net_cs_5 == 0 and instance.net_cs_5_15 == 0 and instance.net_cs_15 == 0:
                if DataProcessor.isnull(instance.net_cs_risk_measure_desc):
                    print(InconsistencyError(sheet_name=sheet_name, index=idx+1,
                                             column='net_cs_5 | net_cs_5_15 | net_cs_15 | net_cs_risk_measure_desc',
                                             value=f"{instance.net_cs_5} | {instance.net_cs_5_15} |"
                                                   f" {instance.net_cs_15}"
                                                   f" | {instance.net_cs_risk_measure_desc}",
                                             message=f'net_cs_risk_measure_desc must be provided only when all the '
                                                     f'corresponding values are 0'))
            else:
                if DataProcessor.notnull(instance.net_cs_risk_measure_desc):
                    print(InconsistencyError(sheet_name=sheet_name, index=idx + 1,
                                             column='net_cs_5 | net_cs_5_15 | net_cs_15 | net_cs_risk_measure_desc',
                                             value=f"{instance.net_cs_5} | {instance.net_cs_5_15} |"
                                                   f" {instance.net_cs_15}"
                                                   f" | {instance.net_cs_risk_measure_desc}",
                                             message=f'net_cs_risk_measure_desc should be filled '
                                                     f'only when all the corresponding values are 0'))

            if (any([DataProcessor.notnull(instance.vega_value_curr),
                     DataProcessor.notnull(instance.vega_value_down_10),
                     DataProcessor.notnull(instance.vega_value_up_10)])):
                if (instance.vega_value_curr == 0 and
                        instance.vega_value_down_10 == 0 and instance.vega_value_up_10 == 0):
                    if DataProcessor.isnull(instance.vega_risk_measure_desc):
                        print(InconsistencyError(sheet_name=sheet_name, index=idx+1,
                                                 column=f'vega_value_curr | vega_value_down_10 |'
                                                        f' vega_value_up_10 | vega_risk_measure_desc',
                                                 value=f"{instance.vega_value_curr} |"
                                                       f" {instance.vega_value_down_10} |"
                                                       f" {instance.vega_value_up_10}"
                                                       f" | {instance.vega_risk_measure_desc}",
                                                 message=f'vega_risk_measure_desc must be'
                                                         f' provided only when all the '
                                                         f'corresponding values are 0'))
                else:
                    if DataProcessor.notnull(instance.vega_risk_measure_desc):
                        print(InconsistencyError(sheet_name=sheet_name, index=idx + 1,
                                                 column=f'vega_value_curr | vega_value_down_10 |'
                                                        f' vega_value_up_10 | vega_risk_measure_desc',
                                                 value=f"{instance.vega_value_curr} |"
                                                       f" {instance.vega_value_down_10} |"
                                                       f" {instance.vega_value_up_10}"
                                                       f" | {instance.vega_risk_measure_desc}",
                                                 message=f'vega_risk_measure_desc must be filled '
                                                         f'only when all the corresponding values are 0'))

            if DataProcessor.notnull(instance.var_value):
                if instance.var_cal_method_code_type.upper() not in ['HISTO', 'CARLO', 'PARAM']:
                    print(InconsistencyError(sheet_name=sheet_name, index=idx + 1,
                                             column=f'var_value | var_cal_method_code_type',
                                             value=f"{instance.var_value} | {instance.var_cal_method_code_type}",
                                             message=f'var_cal_method_code_type must be one of HISTO, CARLO, PARAM'
                                                     f'in case var_value is provided'))
            else:
                if DataProcessor.notnull(instance.var_cal_method_code_type):
                    print(InconsistencyError(sheet_name=sheet_name, index=idx + 1,
                                             column=f'var_value | var_cal_method_code_type',
                                             value=f"{instance.var_value} | {instance.var_cal_method_code_type}",
                                             message=f'var_cal_method_code_type cannot be provided when'
                                                     f'var_value is null'))

            if instance.var_value == 0:
                if DataProcessor.isnull(instance.var_risk_measure_desc):
                    print(InconsistencyError(sheet_name=sheet_name, index=idx + 1,
                                             column=f'var_value | var_risk_measure_desc',
                                             value=f"{instance.var_value} | {instance.var_risk_measure_desc}",
                                             message=f'var_risk_measure_desc must be provided when var_value is 0'))
            else:
                if DataProcessor.notnull(instance.var_risk_measure_desc):
                    print(InconsistencyError(sheet_name=sheet_name, index=idx + 1,
                                             column=f'var_value | var_risk_measure_desc',
                                             value=f"{instance.var_value} | {instance.var_risk_measure_desc}",
                                             message=f'var_risk_measure_desc must not be provided'
                                                     f' when var_value is not0 '))


__all__ = ['Risk_Measures']

