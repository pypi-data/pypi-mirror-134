import cerberus
import pandas as pd
import numpy as np

from balsam.selection import Selection

_data_frame = cerberus.TypeDefinition('data_frame', (pd.DataFrame, ), ())

cerberus.Validator.types_mapping['data_frame'] = _data_frame

_array = cerberus.TypeDefinition('array', (np.ndarray, ), ())

cerberus.Validator.types_mapping['array'] = _array

_selection = cerberus.TypeDefinition('selection', (Selection, ), ())

cerberus.Validator.types_mapping['selection'] = _selection
