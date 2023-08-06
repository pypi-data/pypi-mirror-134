def baseline_subtract(df, window):
    """
    This function will baseline subtract a dataframe based on a given window.

    Arguments: 
    df - a pandas dataframe with columns p, ti, tp, and i.
    window - an iterable with the start and end coordinates of the baseline window.
    
    Returns:
    df - a modified pandas dataframe.
    """

    iblsub = []
    grouped = df.groupby('sweep')
    baselines = df.query('ti >= @window[0] and ti < @window[1]').groupby('sweep')['i'].mean()
                
    for name,group in grouped['i']:
        iblsub.append(group-baselines[name])
        
    flatList = [item for sublist in iblsub for item in sublist]
    df['i'] = flatList
    
    return(df)

def isolate_opening(df, sweepnum, window):
    subsetDf = df.query('sweep == @sweepnum')
    subsetDf = subsetDf.query('ti >= @window[0] and ti < @window[1]')
    return subsetDf