# data_processor.py
import pycountry
import numpy as np
import pandas as pd
import datetime
from typing import Dict, Tuple, List
from numbers import Real
from .errors import *
from decimal import Decimal


def number_check(value, precision, scale, sheet_name, index, column):

    if DataProcessor.notnull(value):
        try:
            int_part, dec_part = str(value).split('.')
            if '-' in int_part:
                precision += 1
            if len(int_part) + len(dec_part) > precision:
                print(LengthError(sheet_name, index+1, column, value, 'precision'))

            elif len(dec_part) > scale:
                print(LengthError(sheet_name, index+1, column, value, 'scale'))

        except (IndexError, ValueError):
            try:
                new_value = int(float(value))
                if new_value >= 0 and len(str(new_value)) > precision:
                    print(LengthError(sheet_name, index+1, column, value, 'precision'))
                elif new_value < 0 and len(str(new_value)) > precision + 1:
                    print(LengthError(sheet_name, index+1, column, value, 'precision'))
            except (ValueError, TypeError):
                pass


def varchar_check(value, length, sheet_name, index, column):
    if not DataProcessor.isnull(value):
        if len(str(value).strip()) > length and len(str(value).rstrip(".0")) > length:
            print(LengthError(sheet_name, index+1, column, value, 'length'))


class DataProcessor:
    # Placeholder for child classes
    prov_obl_codes = None
    datatypes = None
    all = None
    _REPORTING_SHEETS = ['ManCo',
                         'Fund_Static',
                         'Investment_Strategies',
                         'Fund_Dynamic',
                         'Investor_Group',
                         'Transactions',
                         'Holdings',
                         'Risk_Measures',
                         'Risk_Liquidity',
                         'Risk_Historical',
                         'Risk_Other',
                         'Assumptions',
                         'Shareclasses',
                         'Risk_Counterparty',
                         'Prime_Broker',
                         'CCP_Clearing',
                         'Controlled_Structures',
                         'LEV_Borrow_Source',
                         'PE_Dominant_Influence']

    # Class attributes used as library for other classes
    country_codes = set([country.alpha_2 for country in pycountry.countries] + ['XX'])
    currency_codes = set([currency.alpha_3 for currency in pycountry.currencies] + ['CNH', 'LVL', 'SIT'])
    rep_freq_codes = ['Q', 'H', 'Y']
    flags = ['Y', 'N']
    filing_type_codes = ['INIT', 'AMND']
    rep_freq_chg_codes = ['YH', 'YQ', 'HY', 'HQ', 'QY', 'QH', 'NQ', 'NH', 'NY']
    rep_qrtr_chg_codes = ['Q1', 'Q2', 'Q3', 'Q4']

    @staticmethod
    def load_reporting_sheets(path: str, header: int = 15,
                              rows_to_skip: int = 7,
                              column_name_to_drop: str = 'Technical Field :') -> Dict[str, List[Dict]]:

        import warnings
        warnings.filterwarnings('ignore', category=UserWarning)
        warnings.filterwarnings('ignore', category=FutureWarning)

        dataframes = {}
        excel_file = pd.ExcelFile(path)

        for sheet in DataProcessor._REPORTING_SHEETS:
            df = pd.read_excel(excel_file,
                               sheet_name=sheet,
                               header=header,
                               )
            # Drop the rows until find real clients data
            df.drop(index=[i for i in range(rows_to_skip)], inplace=True)
            # Drop the column A as client provides data from the column B
            df.drop(columns=column_name_to_drop, inplace=True)

            # Forcefully convert possible date columns
            for col in df.columns:
                if 'DATE' in col:
                    df[col] = pd.to_datetime(df[col], errors='ignore').dt.date

            for col in df.select_dtypes(include='object').columns:
                df[col] = df[col].apply(lambda x: x.strip() if isinstance(x, str) else x)

            # Transform the datetimes objects to date objects
            # date_columns = df.select_dtypes(include=['datetime64', 'datetime']).columns
            # if date_columns is not None:
            #     for date_col in date_columns:
            #         df[date_col] = pd.to_datetime(df[date_col]).dt.date

            # Do not include sheet that are completely null
            df.dropna(how='all', inplace=True)
            if not df.empty:
                df.columns = [col.lower() for col in df.columns]
                df = df.replace(u'\xa0', 'invisible_char', regex=True)
                dataframes[sheet] = df.to_dict('records')

        excel_file.close()

        return dataframes

    @staticmethod
    def is_integer(value, sheet_name, index, column):
        try:
            value = float(value)
            return value.is_integer()
        except (ValueError, TypeError):
            if value is not None:
                print(InvalidDataType(sheet_name, index+1, column, value))
            return False

    @staticmethod
    def safe_round(value, digits=0):
        return round(value, digits) if DataProcessor.notnull(value) and isinstance(value, Real) else 0

    @staticmethod
    def isnull(value):
        if value is None or value == 'nan' or value == 'NaN':
            return True
        elif isinstance(value, float) and np.isnan(value):
            return True
        elif isinstance(value, str) and value.strip() == '':
            return True
        elif (isinstance(value, (datetime.date, datetime.datetime))
              and pd.isna(pd.Timestamp(value)) or value == 'NaT'):
            return True
        elif isinstance(value, (pd.Timestamp, pd.Timedelta)) and pd.isna(value):
            return True

        return False

    @staticmethod
    def notnull(value):
        return not DataProcessor.isnull(value)

    @staticmethod
    def datatype_check(value,
                       datatype: (Tuple, str),
                       sheet_name: str,
                       index: int,
                       column: str):

        match datatype[0]:
            case 'VARCHAR2' | 'CHAR':  # (VARCHAR2, 20)
                varchar_check(value, datatype[1], sheet_name, index, column)
            case 'NUMBER':  # (NUMBER,5,3)
                number_check(value, datatype[1], datatype[2], sheet_name, index, column)
            case 'D':  # D --> DATE
                if (not (isinstance(value, (datetime.datetime, datetime.date)))
                        and not DataProcessor.isnull(value)):
                    print(InvalidDataType(sheet_name, index+1, column, value))
            case _:
                pass

    @staticmethod
    def mandatory_check(value, provision_of_obligation: str,
                        sheet_name: str,
                        index: int,
                        column: str):

        if provision_of_obligation == 'M' and DataProcessor.isnull(value):
            print(MandatoryValueError(sheet_name, index+1, column, value))

    @classmethod
    def instantiate_with_checks(cls, dataframes):
        sheet_name = cls.__name__

        for index, kwarg in enumerate(dataframes[sheet_name]):
            for column, value in kwarg.items():
                try:
                    datatype = cls.datatypes[column]
                except KeyError:
                    print(f"****Invalid column {column} in {sheet_name}******")
                    print(InvalidDataType(sheet_name, index + 1, column, value))

                if value == 'invisible_char':
                    print(InvalidDataType(sheet_name, index+1, column, value))
                elif datatype[0] == "NUMBER" and DataProcessor.is_integer(value, sheet_name, index, column):
                    value = int(float(value))
                    kwarg[column] = value

                if DataProcessor.isnull(value):
                    value = None
                    kwarg[column] = value

                DataProcessor.datatype_check(value=value,
                                             datatype=datatype,
                                             index=index,
                                             sheet_name=sheet_name,
                                             column=column)

                try:
                    prov_obl = cls.prov_obl_codes[column]
                    DataProcessor.mandatory_check(value=value,
                                                  provision_of_obligation=prov_obl,
                                                  sheet_name=sheet_name,
                                                  index=index,
                                                  column=column)
                except KeyError:
                    print(f"{column} does not exist in cls.prov_obl_codes")

            cls(**kwarg)


__all__ = ['DataProcessor']

