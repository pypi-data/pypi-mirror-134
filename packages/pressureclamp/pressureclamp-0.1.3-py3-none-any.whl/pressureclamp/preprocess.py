def baseline_subtract(df, col, ref, window):
    """
    This function will baseline subtract a specified column of the dataframe based on a provided window within a reference column.

    Arguments
    -------------------
    df: dataframe
        A pandas dataframe with columns ``col`` and ``ref``.
    col: string
        A string indicating the name of the column to be baseline subtracted.
    ref: string
        A reference column over-which to find the window.
    window: list
        An iterable with the start and end coordinates of the reference window for baseline subtraction.
    
    Returns
    ------------------
    dataframe
        A modified pandas dataframe where the the column ``col`` has been baseline subtracted.
    """

    iblsub = []
    grouped = df.groupby('sweep')
    baselines = df.query(f'{ref} >= @window[0] and {ref} < @window[1]').groupby('sweep')[col].mean()
                
    for name,group in grouped[col]:
        iblsub.append(group-baselines[name])
        
    flatList = [item for sublist in iblsub for item in sublist]
    
    return(df)

def isolate_opening(df, sweepnum, window):
    """
    This function will isolate a window in a time series.

    Arguments
    -------------------
    df: dataframe
        A pandas dataframe with columns p, ti, tp, and i.
    sweepnum: int
        The 
    window: iterable
        an iterable with the start and end coordinates of the baseline window.
    
    Returns
    ------------------
    dataframe
        A modified pandas dataframe.
    """

    subsetDf = df.query('sweep == @sweepnum')
    subsetDf = subsetDf.query('ti >= @window[0] and ti < @window[1]')
    return subsetDf