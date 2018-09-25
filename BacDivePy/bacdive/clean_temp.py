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
    df_grouped = df.groupby(df.index)['Field'].apply(list)
    for fill_name, fill_item in zip(df_grouped.index, df_grouped.values):
        # clean all items in values
        # clean fill list of nans and None if needed
        if isinstance(fill_item, list):  # pragma: no cover
            # make sure not a list of lists
            if isinstance(fill_item[0], list):
                fill_item = list(np.array(fill_item).flatten())
            fill_item = list(set(fill_item))
            fill_item = [fill_ for fill_ in fill_item if fill_ is not None and fill_ != np.nan and str(fill_) != 'nan']
            if len(fill_item) == 0:
                continue
            else:
                fill_item = list(set(fill_item))
        # if not a list check if none or nan
        elif fill_item is not None and fill_item != np.nan and str(fill_item) != 'nan':  # pragma: no cover
            continue
        else:  # pragma: no cover
            # if not none or nan and not a list make a list
            fill_item = [fill_item]

        current_values = fill_.loc[fill_name.split('||')[1], fill_name.split('||')[2]][fill_name.split('||')[0]]
        if current_values != np.nan and str(current_values) != 'nan' and current_values is not None:  # pragma: no cover
            # current_values list and fill_item list combine them
            current_values += fill_item
        # make new values first values
        else:
            current_values = fill_item
        # filter check current_values
        current_values_clean = []
        for value_new in current_values:
            if value_new is not None and value_new != np.nan and str(value_new) != 'nan':  # pragma: no cover
                if isinstance(value_new, list):
                    for value_new_ in value_new:  # pragma: no cover
                        if value_new_ is not None and value_new_ != np.nan and str(
                                value_new_) != 'nan':  # pragma: no cover
                            current_values_clean.append(value_new_)
                else:
                    current_values_clean.append(value_new)
        current_values_clean = list(set(current_values_clean))
        # let see what happens without this if
        # if 'temp' == fill_name.split('||')[3]:
        #    tmps_ = []
        #   for tmp in current_values_clean:
        #        if tmp is not None and tmp != np.nan and str(tmp) != 'nan':
        #            if '-' in tmp:  # pragma: no cover
        #                tmps_ += [tmp_ for tmp_ in range(int(tmp.split('-')[0][:2]), int(tmp.split('-')[1][:2]))]
        #            elif '>' in tmp or '<' in tmp:
        #                tmps_.append(tmp[:3])
        #            else:
        #                tmps_.append(int(tmp[:2]))
        #        else:  # pragma: no cover
        #            tmps_.append(tmp)
        #    current_values_clean = tmps_

        fill_.loc[fill_name.split('||')[1], fill_name.split('||')[2]][fill_name.split('||')[0]] = current_values_clean

    fill_ = fill_.sort_index()
    fill_ = fill_.apply(pd.to_numeric, errors='ignore')
    fill_.columns = ['DSMZ_' + str(x) for x in fill_.columns]
    return fill_


def flatten_df_temp(results):
    flat_subsections = []
    flat_field_id = []
    flat_fields = []
    section_ = 'culture_growth_condition'
    sub_section = 'culture_temp'
    list_cult_temp = results[section_][sub_section]
    for temp_dict in list_cult_temp:
        for field_id, field in temp_dict.items():
            if field is None:
                field = np.nan
            flat_subsections.append(str(list_cult_temp.index(temp_dict)))
            flat_field_id.append(field_id)
            flat_fields.append(field)

    return pd.DataFrame([flat_subsections, flat_field_id, flat_fields],
                        index=['Number', 'Field_ID', 'Field']).T