# errors.py

class LengthError:
    all = []

    def __init__(self, sheet_name, index, column, value, type):
        self.sheet_name = sheet_name
        self.index = index
        self.column = column
        self.value = value
        self.type = type

        self.all.append(self)

    def __repr__(self):
        return f'LengthError(sheet_name={self.sheet_name}, row={self.index}, column={self.column} value={self.value})'


class InvalidDataType:
    all = []

    def __init__(self, sheet_name, index, column, value):
        self.sheet_name = sheet_name
        self.index = index
        self.column = column
        self.value = value

        self.all.append(self)

    def __repr__(self):
        return (f'InvalidDataType'
                f'(sheet_name={self.sheet_name}, row={self.index}, column={self.column}, value={self.value})')


class MandatoryValueError:
    all = []

    def __init__(self, sheet_name, index, column, value):
        self.sheet_name = sheet_name
        self.index = index
        self.column = column
        self.value = value

        self.all.append(self)

    def __repr__(self):
        return (f'MandatoryValueError'
                f'(sheet_name={self.sheet_name}, row={self.index}, column={self.column}, value={self.value})')


class InconsistencyError:
    all = []

    def __init__(self, sheet_name, index, column, value, message):
        self.sheet_name = sheet_name
        self.index = index
        self.column = column
        self.value = value
        self.message = message

        self.all.append(self)

    def __repr__(self):
        return (f'InconsistencyError'
                f'(sheet_name={self.sheet_name}, row={self.index},'
                f' column={self.column}, value={self.value}, message={self.message})')


__all__ = ['LengthError', 'InvalidDataType', 'MandatoryValueError', 'InconsistencyError']
