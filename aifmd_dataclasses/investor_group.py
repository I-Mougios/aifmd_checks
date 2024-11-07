# investor_group.py
from common.errors import *
from common.data_processor import DataProcessor
import math


class Investor_Group(DataProcessor):
    all = []

    datatypes = {'pf_id': ('VARCHAR2', 35), 'provider_id': ('VARCHAR2', 20), 'report_date': 'DATE',
                 'nav_rate_bank': ('NUMBER', 5, 4), 'nav_rate_ociu': ('NUMBER', 5, 4),
                 'nav_rate_ofin': ('NUMBER', 5, 4), 'nav_rate_insc': ('NUMBER', 5, 4),
                 'nav_rate_pfnd': ('NUMBER', 5, 4), 'nav_rate_geng': ('NUMBER', 5, 4),
                 'nav_rate_hhld': ('NUMBER', 5, 4), 'nav_rate_nfco': ('NUMBER', 5, 4),
                 'nav_rate_unkn': ('NUMBER', 5, 4), 'nav_rate_none': ('NUMBER', 5, 4),
                 'nav_rate_prof': ('NUMBER', 5, 4), 'nav_rate_retail': ('NUMBER', 5, 4),
                 'top_5_rate': ('NUMBER', 5, 4)}

    prov_obl_codes = {'pf_id': 'M', 'provider_id': 'C(M)', 'report_date': 'M', 'nav_rate_bank': 'M',
                      'nav_rate_ociu': 'M', 'nav_rate_ofin': 'M', 'nav_rate_insc': 'M', 'nav_rate_pfnd': 'M',
                      'nav_rate_geng': 'M', 'nav_rate_hhld': 'M', 'nav_rate_nfco': 'M', 'nav_rate_unkn': 'M',
                      'nav_rate_none': 'M', 'nav_rate_prof': 'M', 'nav_rate_retail': 'M', 'top_5_rate': 'M'}

    def __init__(self, pf_id=None, provider_id=None, report_date=None, nav_rate_bank=None, nav_rate_ociu=None,
                 nav_rate_ofin=None, nav_rate_insc=None, nav_rate_pfnd=None, nav_rate_geng=None,
                 nav_rate_hhld=None, nav_rate_nfco=None, nav_rate_unkn=None, nav_rate_none=None, nav_rate_prof=None,
                 nav_rate_retail=None, top_5_rate=None, **kwargs):

        super().__init__()

        self.pf_id = pf_id
        self.provider_id = provider_id
        self.report_date = report_date
        self.nav_rate_bank = nav_rate_bank
        self.nav_rate_ociu = nav_rate_ociu
        self.nav_rate_ofin = nav_rate_ofin
        self.nav_rate_insc = nav_rate_insc
        self.nav_rate_pfnd = nav_rate_pfnd
        self.nav_rate_geng = nav_rate_geng
        self.nav_rate_hhld = nav_rate_hhld
        self.nav_rate_nfco = nav_rate_nfco
        self.nav_rate_unkn = nav_rate_unkn
        self.nav_rate_none = nav_rate_none
        self.nav_rate_prof = nav_rate_prof
        self.nav_rate_retail = nav_rate_retail
        self.top_5_rate = top_5_rate

        self.__class__.all.append(self)

    def __repr__(self):
        return (
            f"Investor_Group("
            f"pf_id={repr(self.pf_id)}, "
            f"provider_id={repr(self.provider_id)}, "
            f"report_date={repr(self.report_date)}, "
            f"nav_rate_bank={repr(self.nav_rate_bank)}, "
            f"nav_rate_ociu={repr(self.nav_rate_ociu)}, "
            f"nav_rate_ofin={repr(self.nav_rate_ofin)}, "
            f"nav_rate_insc={repr(self.nav_rate_insc)}, "
            f"nav_rate_pfnd={repr(self.nav_rate_pfnd)}, "
            f"nav_rate_geng={repr(self.nav_rate_geng)}, "
            f"nav_rate_hhld={repr(self.nav_rate_hhld)}, "
            f"nav_rate_nfco={repr(self.nav_rate_nfco)}, "
            f"nav_rate_unkn={repr(self.nav_rate_unkn)}, "
            f"nav_rate_none={repr(self.nav_rate_none)}, "
            f"nav_rate_prof={repr(self.nav_rate_prof)}, "
            f"nav_rate_retail={repr(self.nav_rate_retail)}, "
            f"top_5_rate={repr(self.top_5_rate)}"
            f")"
        )

    @property
    def prof(self):
        return sum(
                   [
                    self.safe_round(self.nav_rate_bank, 4),
                    self.safe_round(self.nav_rate_ociu, 4),
                    self.safe_round(self.nav_rate_ofin, 4),
                    self.safe_round(self.nav_rate_insc, 4),
                    self.safe_round(self.nav_rate_pfnd, 4),
                    self.safe_round(self.nav_rate_geng, 4),
                    self.safe_round(self.nav_rate_nfco, 4)
                    ])

    @property
    def total(self):
        return sum(
                   [
                    self.safe_round(self.nav_rate_bank, 4),
                    self.safe_round(self.nav_rate_ociu, 4),
                    self.safe_round(self.nav_rate_ofin, 4),
                    self.safe_round(self.nav_rate_insc, 4),
                    self.safe_round(self.nav_rate_pfnd, 4),
                    self.safe_round(self.nav_rate_geng, 4),
                    self.safe_round(self.nav_rate_hhld, 4),
                    self.safe_round(self.nav_rate_nfco, 4),
                    self.safe_round(self.nav_rate_unkn, 4),
                    self.safe_round(self.nav_rate_none, 4)
                    ])

    @classmethod
    def perform_quality_checks(cls):
        sheet_name = cls.__name__

        for idx, instance in enumerate(cls.all):
            if not math.isclose(instance.prof,
                                DataProcessor.safe_round(instance.nav_rate_prof, 4),
                                abs_tol=1e-10):
                print(InconsistencyError(sheet_name, idx+1, 'nav_rate_prof',
                                         instance.nav_rate_prof,
                                         message=f"Investor Groups: Sum of bank investors | "
                                                 f"UCITS investors | other financial institutions, "
                                                 f"insurance companies | pension funds, "
                                                 f"general government | non-financial corporations: "
                                                 f" [{instance.nav_rate_bank} | "
                                                 f"{instance.nav_rate_ociu} | {instance.nav_rate_ofin}, "
                                                 f"{instance.nav_rate_insc} | {instance.nav_rate_pfnd}, "
                                                 f"{instance.nav_rate_geng} | "
                                                 f"{instance.nav_rate_nfco}"
                                                 f" must be equal to Professional investor NaV rate:"
                                                 f" {instance.prof} | {instance.nav_rate_prof}]"))

            if not math.isclose(instance.total, 1, abs_tol=1e-10):
                print(InconsistencyError(sheet_name, idx+1, 'total', instance.total,
                                         message=f"Sum of investor groups nav rate must be equal to 1"))

            if sum([instance.safe_round(instance.nav_rate_unkn, 4),
                    instance.safe_round(instance.nav_rate_none, 4)]) > 0.2:

                print(InconsistencyError(sheet_name, idx+1, 'nav_rate_unkn | nav_rate_none',
                                         value=f"{instance.nav_rate_unkn} | {instance.nav_rate_none}",
                                         message=f"Sum of investor groups nav_rate_unkn and nav_rate_none must be"
                                                 f" less than 0.2 "))


__all__ = ['Investor_Group']
