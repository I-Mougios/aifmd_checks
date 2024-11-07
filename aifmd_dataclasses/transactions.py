# transactions.py
from common.errors import *
from common.data_processor import DataProcessor


class Transactions(DataProcessor):

    all = []
    datatypes = {'pf_id': ('VARCHAR2', 35), 'provider_id': ('VARCHAR2', 20), 'trade_date': 'DATE',
                 'amt_pc': ('NUMBER', 18, 2), 'ccy_ic': ('VARCHAR2', 3), 'cp_name': ('VARCHAR2', 1200),
                 'tra_status': ('VARCHAR2', 40), 'amt_ic': ('NUMBER', 18, 2), 'tra_id': ('VARCHAR2', 20),
                 'qnt': ('NUMBER', 20, 6), 'notional_value_pc': ('NUMBER', 18, 6), 'market_type': ('VARCHAR2', 4),
                 'asset_sub_type': ('VARCHAR2', 12), 'tra_op_code': ('VARCHAR2', 10), 'tra_type': ('VARCHAR2', 20),
                 'ins_id_ext': ('VARCHAR2', 25), 'isin': ('VARCHAR2', 12), 'ins_name': ('VARCHAR2', 1000),
                 'ins_class': ('VARCHAR2', 400), 'ins_class_desc': ('VARCHAR2', 800),
                 'industry_sector_code': ('VARCHAR2', 100), 'industry_sector_desc': ('VARCHAR2', 800),
                 'industry_sub_sector_code': ('VARCHAR2', 320), 'industry_sub_sector_desc': ('VARCHAR2', 320),
                 'country_code': ('VARCHAR2', 20), 'rtg_grade': ('VARCHAR2', 5), 'listed_ins_flag': ('CHAR', 1),
                 'hedge_flag': ('CHAR', 1), 'asset_sub_type_gb': ('VARCHAR2', 12)}

    prov_obl_codes = {'pf_id': 'M', 'provider_id': 'C(M)', 'trade_date': 'M', 'amt_pc': 'M', 'ccy_ic': 'M',
                      'cp_name': 'C(M)', 'tra_status': 'O', 'amt_ic': 'O', 'tra_id': 'O', 'qnt': 'O',
                      'notional_value_pc': 'C(M)', 'market_type': 'O', 'asset_sub_type': 'C(M)', 'tra_op_code': 'C(M)',
                      'tra_type': 'C(M)', 'ins_id_ext': 'C(M)', 'isin': 'C(M)', 'ins_name': 'C(M)', 'ins_class': 'C(M)',
                      'ins_class_desc': 'C(M)', 'industry_sector_code': 'C(M)', 'industry_sector_desc': 'C(M)',
                      'industry_sub_sector_code': 'C(M)', 'industry_sub_sector_desc': 'C(M)', 'country_code': 'C(M)',
                      'rtg_grade': 'C(M)', 'listed_ins_flag': 'C(M)', 'hedge_flag': 'C(M)', 'asset_sub_type_gb': 'C(M)'}

    asset_sub_type_codes = ['SEC_CSH_CSH', 'SEC_LEQ_LEQ', 'SEC_UEQ_UEQ', 'SEC_CPN_IVG', 'SEC_CPN_NIG', 'SEC_CPI_CPI',
                            'SEC_SBD_EUB', 'SEC_SBD_NEU', 'SEC_MUN_MUN', 'SEC_CBD_CBD', 'SEC_LON_LON', 'SEC_SSP_SSP',
                            'DER_EQD_EQD', 'DER_FID_FID', 'DER_CDS_CDS', 'DER_FEX_INV', 'DER_FEX_HED', 'DER_IRD_IRD',
                            'DER_CTY_CTY', 'DER_OTH_OTH', 'PHY_RES_RES', 'PHY_CTY_CTY', 'PHY_TIM_TIM', 'PHY_ART_ART',
                            'PHY_TPT_TPT', 'PHY_OTH_OTH', 'CIU_CIU_CIU', 'OTH_OTH_OTH']

    def __init__(self, pf_id=None, provider_id=None, trade_date=None, amt_pc=None, ccy_ic=None, cp_name=None,
                 tra_status=None, amt_ic=None, tra_id=None, qnt=None, notional_value_pc=None, market_type=None,
                 asset_sub_type=None, tra_op_code=None, tra_type=None, ins_id_ext=None, isin=None, ins_name=None,
                 ins_class=None, ins_class_desc=None, industry_sector_code=None, industry_sector_desc=None,
                 industry_sub_sector_code=None, industry_sub_sector_desc=None,	country_code=None, rtg_grade=None,
                 listed_ins_flag=None, hedge_flag=None, asset_sub_type_gb=None, **kwargs):

        super().__init__()

        self.pf_id = pf_id
        self.provider_id = provider_id
        self.trade_date = trade_date
        self.amt_pc = amt_pc
        self.ccy_ic = ccy_ic
        self.cp_name = cp_name
        self.tra_status = tra_status
        self.amt_ic = amt_ic
        self.tra_id = tra_id
        self.qnt = qnt
        self.notional_value_pc = notional_value_pc
        self.market_type = market_type
        self.asset_sub_type = asset_sub_type
        self.tra_op_code = tra_op_code
        self.tra_type = tra_type
        self.ins_id_ext = ins_id_ext
        self.isin = isin
        self.ins_name = ins_name
        self.ins_class = ins_class
        self.ins_class_desc = ins_class_desc
        self.industry_sector_code = industry_sector_code
        self.industry_sector_desc = industry_sector_desc
        self.industry_sub_sector_code = industry_sub_sector_code
        self.industry_sub_sector_desc = industry_sub_sector_desc
        self.country_code = country_code
        self.rtg_grade = rtg_grade
        self.listed_ins_flag = listed_ins_flag
        self.hedge_flag = hedge_flag
        self.asset_sub_type_gb = asset_sub_type_gb

        self.__class__.all.append(self)

    def __repr__(self):
        return (
            f"Transactions(pf_id={repr(self.pf_id)}, "
            f"provider_id={repr(self.provider_id)}, "
            f"trade_date={repr(self.trade_date)}, "
            f"amt_pc={self.amt_pc}, "
            f"ccy_ic={repr(self.ccy_ic)}, "
            f"cp_name={repr(self.cp_name)}, "
            f"tra_status={repr(self.tra_status)}, "
            f"amt_ic={self.amt_ic}, "
            f"tra_id={repr(self.tra_id)}, "
            f"qnt={self.qnt}, "
            f"notional_value_pc={self.notional_value_pc}, "
            f"market_type={repr(self.market_type)}, "
            f"asset_sub_type={repr(self.asset_sub_type)}, "
            f"tra_op_code={repr(self.tra_op_code)}, "
            f"tra_type={repr(self.tra_type)}, "
            f"ins_id_ext={repr(self.ins_id_ext)}, "
            f"isin={repr(self.isin)}, "
            f"ins_name={repr(self.ins_name)}, "
            f"ins_class={repr(self.ins_class)}, "
            f"ins_class_desc={repr(self.ins_class_desc)}, "
            f"industry_sector_code={repr(self.industry_sector_code)}, "
            f"industry_sector_desc={repr(self.industry_sector_desc)}, "
            f"industry_sub_sector_code={repr(self.industry_sub_sector_code)}, "
            f"industry_sub_sector_desc={repr(self.industry_sub_sector_desc)}, "
            f"country_code={repr(self.country_code)}, "
            f"rtg_grade={repr(self.rtg_grade)}, "
            f"listed_ins_flag={repr(self.listed_ins_flag)}, "
            f"hedge_flag={repr(self.hedge_flag)})"
        )

    @classmethod
    def perform_quality_checks(cls):
        sheet_name = cls.__name__

        for idx, instance in enumerate(cls.all):
            if DataProcessor.notnull(instance.ccy_ic) and instance.ccy_ic not in instance.currency_codes:
                print(InconsistencyError(sheet_name, idx+1, 'currency_code', instance.ccy_ic,
                                         message='Invalid currency code'))

            if DataProcessor.notnull(instance.tra_status) and instance.tra_status.lower() not in ['closed, open']:
                print(InconsistencyError(sheet_name, idx+1, 'tra_status', instance.tra_status,
                                         message='Invalid tra_status'))

            if instance.asset_sub_type.startswith("DER") and DataProcessor.isnull(instance.notional_value_pc):
                print(InconsistencyError(sheet_name, idx+1, 'notional_value_pc',
                                         value=instance.notional_value_pc,
                                         message='Notional value is mandatory for derivatives'))

            if DataProcessor.notnull(instance.market_type) and instance.market_type.lower() not in ['reg', 'otc']:
                print(InconsistencyError(sheet_name, idx+1, 'market_type', instance.market_type,
                                         message='Invalid market_type code'))
            # any() returns true if there is one truthy object
            if (not any([instance.tra_op_code, instance.tra_type, instance.ins_id_ext,
                         instance.isin, instance.ins_name, instance.ins_class,
                         instance.ins_class_desc, instance.industry_sector_code,
                         instance.industry_sector_desc, instance.industry_sub_sector_code,
                         instance.industry_sub_sector_desc, instance.country_code,
                         instance.rtg_grade, instance.listed_ins_flag, instance.hedge_flag])
                    and
                    DataProcessor.isnull(instance.asset_sub_type)):
                print(InconsistencyError(sheet_name, idx+1, 'asset_sub_type', instance.asset_sub_type,
                                         message=f'Provide the asset sub type code or the adequate data in columns'
                                                 f'O-AC in order to define the asset sub type'))

            if (any([instance.tra_op_code, instance.tra_type, instance.ins_id_ext,
                     instance.isin, instance.ins_name, instance.ins_class,
                     instance.ins_class_desc, instance.industry_sector_code,
                     instance.industry_sector_desc,
                     instance.industry_sub_sector_code,
                     instance.industry_sub_sector_desc, instance.country_code,
                     instance.rtg_grade, instance.listed_ins_flag,
                     instance.hedge_flag])
                    and
                    DataProcessor.notnull(instance.asset_sub_type)):
                print(InconsistencyError(sheet_name, idx+1, 'asset_sub_type', instance.asset_sub_type,
                                         message=f'Columns O-AC must be empty when asset sub type code'
                                                 f' is provided directly '))

            if instance.asset_sub_type not in instance.asset_sub_type_codes:
                print(InconsistencyError(sheet_name, idx+1, 'asset_sub_type', instance.asset_sub_type,
                                         message=f'Invalid asset sub type code'))


__all__ = ['Transactions']
