# main BSTS algorithm

import numpy as np
import pandas as pd
from statsmodels.tsa.arima_process import ArmaProcess
from causalimpact import CausalImpact
import re
import warnings
warnings.filterwarnings('ignore')

res = dates[['Date published','pre_period', 'post_period','amount', 'index']]

for x in range(0, len(list_years)):
    print(list_years[x].columns[0])
    
    params = []
    errors = []
    list2 = []
    data = list_years[x].copy()
    data.columns = ['y', 'X1', 'X2', 'X3']
    
    for n in range(0,len(dates)):
        pre_period = [b[n], a[n]]
        post_period = [d[n], c[n]]
        try:
            ci = CausalImpact(data, pre_period, post_period)
            r1 = re.search('tail-area probability p: (.+?)\nPosterior prob.', ci.summary())
            params.append(r1.group(1))
            list2.append(ci.summary())

        except ValueError as err:
            params.append('NaN')
            errors.append(err)
            list2.append('error')
            pass
    
    try:
        print(len(params))
        print('sig numbers:', len([float(n) for n in params if float(n) <= 0.05]))
        print('non-sig numbers:', len([float(n) for n in params if float(n) > 0.05]))
        print(len(errors))
    except TypeError:
        print('weird')
    
    listtemp = []
    for num in range(0, len(list2)):
        try:
            actual_average = re.search('\nActual[\t ]*(.+?)[\t ]', list2[num]).group(1)
            actual_cumulative = re.search('\nActual[\t ]*\d.\d*[\t ]*(.+?)\nPrediction', list2[num]).group(1)

            rel_average = re.search('\n\nRelative effect \(s.d.\)[\t ]*(.+?)\s', list2[num]).group(1)
            rel_cumulative = re.search('\n\nRelative effect \(s.d.\).*-.*\)[\t ]*(.+?)\s', list2[num]).group(1)

            abs_average = re.search('\nAbsolute effect \(s.d.\)[\t ]*(.+?)\s', list2[num]).group(1)
            abs_cumulative = re.search('\nAbsolute effect \(s.d.\).*-.*\)[\t ]*(.+?)\s', list2[num]).group(1)

            listtemp.append([actual_average,actual_cumulative,rel_average,rel_cumulative,abs_average,abs_cumulative])
        
        except:
            listtemp.append(['error','error','error','error','error','error'])
            
    if x == 0:
        res['year3_p-value'] = params
        
        dtemp = pd.DataFrame.from_records(listtemp, columns =['actual_average','actual_cumulative','rel_average',
                                                              'rel_cumulative','abs_average','abs_cumulative'])
        dtemp.columns = [str(col) + 'year3' for col in dtemp.columns]
        
        res = pd.concat([res.reset_index(drop=True),dtemp.reset_index(drop=True)], axis=1)
        
    elif x == 1:
        res['year4_p-value'] = params
        dtemp = pd.DataFrame.from_records(listtemp, columns =['actual_average','actual_cumulative','rel_average',
                                                              'rel_cumulative','abs_average','abs_cumulative'])
        dtemp.columns = [str(col) + 'year4' for col in dtemp.columns]
        res = pd.concat([res.reset_index(drop=True),dtemp.reset_index(drop=True)], axis=1)
        
    elif x == 2:
        res['year5_p-value'] = params
        dtemp = pd.DataFrame.from_records(listtemp, columns =['actual_average','actual_cumulative','rel_average',
                                                              'rel_cumulative','abs_average','abs_cumulative'])
        dtemp.columns = [str(col) + 'year5' for col in dtemp.columns]
        res = pd.concat([res.reset_index(drop=True),dtemp.reset_index(drop=True)], axis=1)
    elif x == 3:
        res['year6_p-value'] = params
        dtemp = pd.DataFrame.from_records(listtemp, columns =['actual_average','actual_cumulative','rel_average',
                                                              'rel_cumulative','abs_average','abs_cumulative'])
        dtemp.columns = [str(col) + 'year6' for col in dtemp.columns]
        res = pd.concat([res.reset_index(drop=True),dtemp.reset_index(drop=True)], axis=1)
        
    elif x == 4:
        res['year7_p-value'] = params
        dtemp = pd.DataFrame.from_records(listtemp, columns =['actual_average','actual_cumulative','rel_average',
                                                              'rel_cumulative','abs_average','abs_cumulative'])
        dtemp.columns = [str(col) + 'year7' for col in dtemp.columns]
        res = pd.concat([res.reset_index(drop=True),dtemp.reset_index(drop=True)], axis=1)
    elif x == 5:
        res['year8_p-value'] = params
        dtemp = pd.DataFrame.from_records(listtemp, columns =['actual_average','actual_cumulative','rel_average',
                                                              'rel_cumulative','abs_average','abs_cumulative'])
        dtemp.columns = [str(col) + 'year8' for col in dtemp.columns]
        res = pd.concat([res.reset_index(drop=True),dtemp.reset_index(drop=True)], axis=1)
    elif x == 6:
        res['year9_p-value'] = params
        dtemp = pd.DataFrame.from_records(listtemp, columns =['actual_average','actual_cumulative','rel_average',
                                                              'rel_cumulative','abs_average','abs_cumulative'])
        dtemp.columns = [str(col) + 'year9' for col in dtemp.columns]
        res = pd.concat([res.reset_index(drop=True),dtemp.reset_index(drop=True)], axis=1)
    elif x == 7:
        res['year10_p-value'] = params
        dtemp = pd.DataFrame.from_records(listtemp, columns =['actual_average','actual_cumulative','rel_average',
                                                              'rel_cumulative','abs_average','abs_cumulative'])
        dtemp.columns = [str(col) + 'year10' for col in dtemp.columns]
        res = pd.concat([res.reset_index(drop=True),dtemp.reset_index(drop=True)], axis=1)
    
    elif x == 8:
        res['year11_p-value'] = params
        dtemp = pd.DataFrame.from_records(listtemp, columns =['actual_average','actual_cumulative','rel_average',
                                                              'rel_cumulative','abs_average','abs_cumulative'])
        dtemp.columns = [str(col) + 'year11' for col in dtemp.columns]
        res = pd.concat([res.reset_index(drop=True),dtemp.reset_index(drop=True)], axis=1)
        
    elif x == 9:
        res['year12_p-value'] = params
        dtemp = pd.DataFrame.from_records(listtemp, columns =['actual_average','actual_cumulative','rel_average',
                                                              'rel_cumulative','abs_average','abs_cumulative'])
        dtemp.columns = [str(col) + 'year12' for col in dtemp.columns]
        res = pd.concat([res.reset_index(drop=True),dtemp.reset_index(drop=True)], axis=1)
        
    elif x == 10:
        res['year13_p-value'] = params
        dtemp = pd.DataFrame.from_records(listtemp, columns =['actual_average','actual_cumulative','rel_average',
                                                              'rel_cumulative','abs_average','abs_cumulative'])
        dtemp.columns = [str(col) + 'year13' for col in dtemp.columns]
        res = pd.concat([res.reset_index(drop=True),dtemp.reset_index(drop=True)], axis=1)
    
    elif x == 11:
        res['year14_p-value'] = params
        dtemp = pd.DataFrame.from_records(listtemp, columns =['actual_average','actual_cumulative','rel_average',
                                                              'rel_cumulative','abs_average','abs_cumulative'])
        dtemp.columns = [str(col) + 'year14' for col in dtemp.columns]
        res = pd.concat([res.reset_index(drop=True),dtemp.reset_index(drop=True)], axis=1)   
        
    elif x == 12:
        res['year15_p-value'] = params
        dtemp = pd.DataFrame.from_records(listtemp, columns =['actual_average','actual_cumulative','rel_average',
                                                              'rel_cumulative','abs_average','abs_cumulative'])
        dtemp.columns = [str(col) + 'year15' for col in dtemp.columns]
        res = pd.concat([res.reset_index(drop=True),dtemp.reset_index(drop=True)], axis=1)


