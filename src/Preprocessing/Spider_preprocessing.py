from Preprocessing.Tags import Tags


def df_cleaning(df):

    """
    Método para preparar el dataframe que vamos a representar en un diagrama
    de araña
    :param df: pandas.DataFrame a limpiar
    :return: pandas.DataFrame limpio
    """
    tags = Tags

    df[tags.text_raw] = df[tags.text_raw].str.len()
    df[tags.text_no_sw] = df[tags.text_no_sw].str.len()
    df[tags.unique_words] = df[tags.unique_words].str.len()
    df[tags.number_of_stopwords] = df[tags.number_of_stopwords]

    return df
