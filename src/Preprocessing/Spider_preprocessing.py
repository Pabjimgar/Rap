from Preprocessing.Tags import DbTags


def df_cleaning(df):

    """
    Método para preparar el dataframe que vamos a representar en un diagrama
    de araña
    :param df: pandas.DataFrame a limpiar
    :return: pandas.DataFrame limpio
    """
    tags = DbTags

    df[tags.text_raw] = df[tags.text_raw].str.len()
    df[tags.text_no_sw] = df[tags.text_no_sw].str.len()
    df[tags.unique_words] = df[tags.unique_words].str.len()

    return df[[tags.text_raw, tags.text_no_sw, tags.unique_words]]
