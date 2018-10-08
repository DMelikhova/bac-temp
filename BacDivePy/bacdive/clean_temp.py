import pandas as pd
import numpy as np
import json


def implode_fattened_df_temp(df):
    """
    Combines and cleans all data into multi-index pandas dataframe where columns are DSMZ numbers.

    """

    # build multi index
    index_set = list(set(['||'.join(x.split('||')[1:]) for x in list(set(df.index))]))
    arrays = np.array([x.split('||') for x in index_set]).T
    tuples = list(zip(*arrays))
    index = pd.MultiIndex.from_tuples(tuples, names=['Number', 'Field'])
    ids = [str(x) for x in list(set(df.DSMZ_id.values))]
    fill_ = np.zeros((len(index), len(ids),))
    fill_[:] = np.nan
    fill_ = pd.DataFrame(fill_, index=index, columns=ids).astype(object)
    df_field = df['Field']
    for fill_name, fill_item in zip(df_field.index, df_field.values):
        current_value = fill_item
        fill_.loc[fill_name.split('||')[1], fill_name.split('||')[2]][fill_name.split('||')[0]] = current_value
    fill_ = fill_.sort_index()
    fill_ = fill_.apply(pd.to_numeric, errors='ignore')
    fill_
    return fill_


def flatten_df_temp(results):
    flat_subsections = []
    flat_field_id = []
    flat_fields = []
    section_ = 'culture_growth_condition'
    sub_section = 'culture_temp'
    if sub_section in results[section_]:
        list_cult_temp = results[section_][sub_section]
    else:
        list_cult_temp = [{'ability': None, 'test_type': None, 'temp': None, 'temperature_range': None, 'ID_reference': None}]
    for temp_dict in list_cult_temp:
        for field_id, field in temp_dict.items():
            if field is None:
                field = np.nan
            flat_subsections.append(str(list_cult_temp.index(temp_dict)))
            flat_field_id.append(field_id)
            flat_fields.append(field)
    return pd.DataFrame([flat_subsections, flat_field_id, flat_fields],
                         index=['Number', 'Field_ID', 'Field']).T
    
        