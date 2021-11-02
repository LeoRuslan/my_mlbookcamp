import re
import pandas as pd
import numpy as np


def split_resolution(x: str) -> list:
    width = int(x.split('x')[0])
    height = int(x.split('x')[1])
    return [width, height]


def extract_brand(x: str) -> str:
    return x.split(' ')[0]


def split_memory(x: str, type_memory: str) -> float:
    """
    x: str
    type_memory: str

    split `str` by "+"
    and extract storage size for each type_memory
    """
    res = x.split('+')

    ssd_value = 0
    hdd_value = 0
    flash_value = 0
    for _ in res:

        count_gb = int(re.findall(r'\d+', _)[0])
        if 'tb' in _:
            count_gb = count_gb * 1024

        if 'ssd' in _:
            ssd_value += count_gb
        elif 'hdd' in _:
            hdd_value += count_gb
        else:
            flash_value += count_gb

    if type_memory == 'ssd':
        return ssd_value
    elif type_memory == 'hdd':
        return hdd_value
    else:
        return flash_value


def clean_dataset(dataframe: pd.DataFrame, clean_price_outliers=True, th_hold=6) -> pd.DataFrame:
    """
    :param dataframe:
    :param clean_price_outliers:
    :param th_hold: - if in dataset count companies rows is lower that th_hold,  we don`t use in our model.
    :return:
    """
    # check on duplicates on all columns
    _df = dataframe.drop_duplicates(keep='first')

    # we need check situation when we have the same characteristics, but price isn`t the same.
    columns_without_price = _df.columns.drop('price_euros')
    _df = _df.drop_duplicates(columns_without_price, keep='first')
    _df = _df.reset_index(drop=True)
    if clean_price_outliers:
        # delete
        _df = _df[_df.price_euros < np.percentile(_df['price_euros'].values, 95)]
        _df['log_price'] = np.log(_df['price_euros'])

    # Delete `company` with lower counts in datasets.
    reraly_company = _df['company'].value_counts()[(_df['company'].value_counts() < th_hold)].keys()
    for company in reraly_company:
        _df = _df[_df['company'] != company]

    # Delete `ram` with lower counts in datasets.
    _df = _df[_df['ram'] != '64gb']
    _df = _df[_df['ram'] != '24gb']

    # Delete `opsys` with rarely counts in datasets
    _df = _df[_df['opsys'] != 'android']

    # Replace `mac os x` to `macos`, `windows 10 s` to `windows 10 s`, because they are very similar.
    _df['opsys'] = _df['opsys'].str.replace('mac os x', 'macos')
    _df['opsys'] = _df['opsys'].str.replace('windows 10 s', 'windows 10')

    # convert `weight` to numerical values.
    _df.loc[:, 'weight'] = _df.loc[:, 'weight'].apply(lambda x: float(x[:-2]))

    # lets extract resolution from `screenresolution`.
    _df['resolution'] = _df['screenresolution'].str.extract(r'(\d+x\d+)')
    _df['screenresolution'] = _df['screenresolution'].replace(r'(\d+x\d+)', '', regex=True)
    _df['width'] = _df['resolution'].apply(lambda x: split_resolution(x)[0])
    _df['height'] = _df['resolution'].apply(lambda x: split_resolution(x)[1])

    _df['touchscreen'] = (_df['screenresolution'].str.extract(r'(touchscreen)') == 'touchscreen').astype(int)
    _df['ips'] = (_df['screenresolution'].str.extract(r'(ips)') == 'ips').astype(int)
    _df['full_hd'] = (_df['screenresolution'].str.extract(r'(full hd)') == 'full hd').astype(int)
    _df['4k_ultra_hd'] = (_df['screenresolution'].str.extract(r'(4k ultra hd)') == '4k ultra hd').astype(int)
    _df['quad_hd'] = (_df['screenresolution'].str.extract(r'(quad hd+)') == 'quad hd').astype(int)

    # CPU
    _df['ghz'] = _df['cpu'].str.extract(r'(\d+(?:\.\d+)?ghz)')
    _df['ghz'] = _df['ghz'].apply(lambda x: x[:-3]).astype(float)
    _df['cpu'] = _df['cpu'].replace(r'(\d+(?:\.\d+)?ghz)', '', regex=True)

    # Delete `samsung` cpu brand with lower counts in datasets.
    _df = _df[~_df['cpu'].str.startswith('samsung')]

    _df['cpu_intel'] = (_df['cpu'].str.extract(r'(intel)') == 'intel').astype(int)
    _df['cpu_amd'] = (_df['cpu'].str.extract(r'(amd)') == 'amd').astype(int)

    # GPU
    _df['gpu_intel'] = (_df['gpu'].str.extract(r'(intel)') == 'intel').astype(int)
    _df['gpu_nvidia'] = (_df['gpu'].str.extract(r'(nvidia)') == 'nvidia').astype(int)
    _df['gpu_amd'] = (_df['gpu'].str.extract(r'(amd)') == 'amd').astype(int)

    # MEMORY
    _df['memory_ssd'] = (_df['memory'].str.extract(r'(ssd)') == 'ssd').astype(int)
    _df['memory_hdd'] = (_df['memory'].str.extract(r'(hdd)') == 'hdd').astype(int)
    _df['memory_flash'] = (_df['memory'].str.extract(r'(flash storage)') == 'flash storage').astype(int)

    _df['ssd_value'] = _df['memory'].apply(lambda x: split_memory(x, 'ssd'))
    _df['hdd_value'] = _df['memory'].apply(lambda x: split_memory(x, 'hdd'))
    _df['flash_value'] = _df['memory'].apply(lambda x: split_memory(x, 'flash'))

    _df = _df.drop(['product', 'screenresolution', 'cpu', 'gpu', 'memory', 'resolution'], axis=1)

    return _df


def is_in_company_list(x: str) -> bool:
    if x in ['lenovo', 'dell', 'hp', 'asus', 'acer', 'msi', 'toshiba', 'apple', 'samsung', 'mediacom']:
        return True

    return False
