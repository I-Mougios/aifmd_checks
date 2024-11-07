# main.py
from pathlib import Path
from operator import methodcaller
import pandas as pd
from common.errors import *
from common.data_processor import DataProcessor
from aifmd_dataclasses import *
from utils import select_excel_file
"""
Perform Data Quality checks on the client Excel file and return an error
log. In more detail, it checks for:

1. Missing values based on the provision obligation of the column as 
   provided in the Data Requirement template.
2. Datatype check.
3. Checks the data on the report level to ensure that the data is consistent 
   with the regulatory framework and qualifies to produce a report that will 
   not be rejected by the regulator.
"""


def main(file_path):

    # Load reporting sheets into Dictionary that contains list of dictionaries
    reporting_sheets = DataProcessor.load_reporting_sheets(str(file_path))
    print('Number of non empty sheets: ', len(reporting_sheets))

    create_instances = methodcaller('instantiate_with_checks', reporting_sheets)
    perform_quality_checks = methodcaller('perform_quality_checks')

    for class_ in DataProcessor.__subclasses__():
        if class_.__name__ in reporting_sheets:
            print('\n'*2)
            print(f"----{class_.__name__}-----", end='\n')
            create_instances(class_)

        try:
            perform_quality_checks(class_)
        except AttributeError:
            print(f"Dataclass {class_.__name__} has no conditional checks", end='\n'*2)

    Fund_Static.check_rep_code()
    Fund_Dynamic.check_total_nav()
    Investment_Strategies.check_inv_stg_nav_rates()
    Investment_Strategies.check_aif_type()
    Investment_Strategies.check_pos_size_code()

    output_path = Path(__file__).parent.joinpath('output')
    output_path.mkdir(parents=True, exist_ok=True)
    error_report_file_path = Path(output_path, 'error_report.xlsx')

    with pd.ExcelWriter(error_report_file_path, engine='openpyxl') as writer:
        if MandatoryValueError.all:
            missing_mandatory_values = pd.DataFrame(
                {'Sheet Name': [error.sheet_name for error in MandatoryValueError.all],
                 'Row': [error.index for error in MandatoryValueError.all],
                 'Column': [error.column for error in MandatoryValueError.all],
                 'Value': [error.value for error in MandatoryValueError.all]})
            missing_mandatory_values.to_excel(writer, sheet_name='Missing Mandatory Values', index=False)

        if LengthError.all:
            length_errors = pd.DataFrame({'Sheet Name': [error.sheet_name for error in LengthError.all],
                                          'Row': [error.index for error in LengthError.all],
                                          'Column': [error.column for error in LengthError.all],
                                          'Value': [error.value for error in LengthError.all],
                                          'Type': [error.type for error in LengthError.all]})
            length_errors.to_excel(writer, sheet_name='Length Errors based on the datatype', index=False)

        if InvalidDataType.all:
            invalid_data_type = pd.DataFrame({'Sheet Name': [error.sheet_name for error in InvalidDataType.all],
                                              'Row': [error.index for error in InvalidDataType.all],
                                              'Column': [error.column for error in InvalidDataType.all],
                                              'Value': [error.value for error in InvalidDataType.all]
                                              })
            invalid_data_type.to_excel(writer, sheet_name='Invalid Datatype errors', index=False)

        if InconsistencyError.all:
            inconsistency_errors = pd.DataFrame({'Sheet Name': [error.sheet_name for error in InconsistencyError.all],
                                                 'Row': [error.index for error in InconsistencyError.all],
                                                 'Column': [error.column for error in InconsistencyError.all],
                                                 'Value': [error.value for error in InconsistencyError.all],
                                                 'Error Message': [error.message for error in InconsistencyError.all]})
            inconsistency_errors.to_excel(writer, sheet_name='Inconsistency Errors', index=False)


if __name__ == "__main__":
    file_path = select_excel_file()
    if file_path:
        main(file_path)
