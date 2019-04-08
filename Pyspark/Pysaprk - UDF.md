# Pysaprk - UDF



```py
@pandas_udf("dupl_index long, ids1 long, ids2 long, match_type string, all_matched boolean, asym boolean", PandasUDFType.GROUPED_MAP)
# Input/output are both a pandas.DataFrame
def athr_nm_mch(df):


pd.DataFrame({"dupl_index":dupl_index, "ids1":[0], "ids2":[0], "match_type":["no_match"], "all_matched":[False], "asym":[False]})
```

![1554724572769](C:\Users\nrchu\AppData\Roaming\Typora\typora-user-images\1554724572769.png)

```python
@pandas_udf("dupl_index long, ids1 long, ids2 long, match_type string, all_matched boolean, asym boolean", PandasUDFType.GROUPED_MAP)
# Input/output are both a pandas.DataFrame

def athr_nm_mch(df):
  try: 
    #initializing
    n_dupl = len(df)
    dupl_index = df.dupl_index.unique()
    dfs = {}
    
    #ids to df
    for i in range(n_dupl):  
      dfs[i] = pd.DataFrame(
          {"names":df.iloc[i].sci_names.split(","),
           "ids":df.iloc[i].sci_ids.split(",")}
          #"paper_id":df.iloc[i].paper_id}
           ).sort_values('ids')
      dfs[i]['ids'] = dfs[i]['ids'].astype(np.int64)
    
    df_pairs = itertools.combinations(range(n_dupl), 2)
    matched_res = []
    
    for p1, p2 in df_pairs:
      matched_res.append(author_name_match_func(dfs[p1], dfs[p2]))
    
    aggregated = pd.concat(matched_res).assign(dupl_index=dupl_index[0])
    aggregated['asym'] = aggregated['asym'].astype(bool)
    aggregated['ids1'] = aggregated['ids1'].astype(np.int64)
    aggregated['ids2'] = aggregated['ids2'].astype(np.int64)
    
    if len(aggregated): 
      return aggregated
    else: return pd.DataFrame({"dupl_index":dupl_index, "ids1":[0], "ids2":[0], "match_type":["no_match"], "all_matched":[False], "asym":[False]})
  except: return pd.DataFrame({"dupl_index":dupl_index, "ids1":[0], "ids2":[0], "match_type":["error"], "all_matched":[False], "asym":[False]})
```







```python
'''
Reference 2
https://recordlinkage.readthedocs.io/en/latest/ref-index.html#recordlinkage.base.BaseIndexAlgorithm
'''    
    
class FirstLetterIndex(BaseIndexAlgorithm):
    """Custom class for indexing"""

    def __init__(self, letter):
        super(FirstLetterIndex, self).__init__()

        # the letter to save
        self.letter = letter

    def _link_index(self, df_a, df_b):
        """Make record pairs that agree on the first letter of the given name."""

        # Select records with names starting with a 'letter'.
        a_startswith_w = df_a[df_a['given_name'].str.startswith(self.letter) == True]
        b_startswith_w = df_b[df_b['given_name'].str.startswith(self.letter) == True]

        # Make a product of the two numpy arrays
        return pandas.MultiIndex.from_product(
            [a_startswith_w.index.values, b_startswith_w.index.values],
            names=[df_a.index.name, df_b.index.name]
        )
```





```python
'''
Referene 3
Recordlinkage package in python
'''


class Block(BaseIndexAlgorithm):
    """Make candidate record pairs that agree on one or more variables.

    Returns all record pairs that agree on the given variable(s). This
    method is known as *blocking*. Blocking is an effective way to make a
    subset of the record space (A * B).

    Parameters
    ----------
    left_on : label, optional
        A column name or a list of column names of dataframe A. These
        columns are used to block on.
    right_on : label, optional
        A column name or a list of column names of dataframe B. These
        columns are used to block on. If 'right_on' is None, the `left_on`
        value is used. Default None.
    **kwargs :
        Additional keyword arguments to pass to
        :class:`recordlinkage.base.BaseIndexAlgorithm`.

    Examples
    --------
    In the following example, the record pairs are made for two historical
    datasets with census data. The datasets are named ``census_data_1980``
    and ``census_data_1990``.

    >>> indexer = recordlinkage.BlockIndex(on='first_name')
    >>> indexer.index(census_data_1980, census_data_1990)

    """

    def __init__(self, left_on=None, right_on=None, **kwargs):
        on = kwargs.pop('on', None)
        super(Block, self).__init__(**kwargs)

        # variables to block on
        self.left_on = left_on
        self.right_on = right_on

        if on is not None:
            warnings.warn(
                "The argument 'on' is deprecated. Use 'left_on=...' and "
                "'right_on=None' to simulate the behaviour of 'on'.",
                stacklevel=2)
            self.left_on, self.right_on = on, on

    def __repr__(self):

        class_name = self.__class__.__name__
        left_on, right_on = self._get_left_and_right_on()

        return "<{} left_on={!r}, right_on={!r}>".format(
            class_name, left_on, right_on)

    def _get_left_and_right_on(self):

        if self.right_on is None:
            return (self.left_on, self.left_on)
        else:
            return (self.left_on, self.right_on)

    def _link_index(self, df_a, df_b):

        left_on, right_on = self._get_left_and_right_on()
        left_on = listify(left_on)
        right_on = listify(right_on)

        blocking_keys = ["blocking_key_%d" % i for i, v in enumerate(left_on)]

        # make a dataset for the data on the left
        # 1. make a dataframe
        # 2. rename columns
        # 3. add index col
        # 4. drop na (last step to presever index)
        data_left = pandas.DataFrame(df_a[left_on], copy=False)
        data_left.columns = blocking_keys
        data_left['index_x'] = numpy.arange(len(df_a))
        data_left.dropna(axis=0, how='any', subset=blocking_keys, inplace=True)

        # make a dataset for the data on the right
        data_right = pandas.DataFrame(df_b[right_on], copy=False)
        data_right.columns = blocking_keys
        data_right['index_y'] = numpy.arange(len(df_b))
        data_right.dropna(
            axis=0, how='any', subset=blocking_keys, inplace=True)

        # ---------------- 여기가 핵심이다!!!!!!!!!!!!!!!!!!!!! ---------------
        # merge the dataframes
        pairs_df = data_left.merge(data_right, how='inner', on=blocking_keys)

        return pandas.MultiIndex(
            levels=[df_a.index.values, df_b.index.values],
            labels=[pairs_df['index_x'].values, pairs_df['index_y'].values],
            verify_integrity=False)
```

- Spark inner join을 쓰자
- 