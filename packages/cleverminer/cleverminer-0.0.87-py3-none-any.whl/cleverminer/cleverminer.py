import time #line:1
import pandas as pd #line:3
class cleverminer :#line:5
    version_string ="0.0.87"#line:7
    def __init__ (OOOO0OOOO00O0000O ,**OOOO0000OOO0OOO00 ):#line:9
        OOOO0OOOO00O0000O ._print_disclaimer ()#line:10
        OOOO0OOOO00O0000O .stats ={'total_cnt':0 ,'total_valid':0 ,'control_number':0 ,'start_prep_time':time .time (),'end_prep_time':time .time (),'start_proc_time':time .time (),'end_proc_time':time .time ()}#line:18
        OOOO0OOOO00O0000O ._init_data ()#line:19
        OOOO0OOOO00O0000O ._init_task ()#line:20
        if len (OOOO0000OOO0OOO00 )>0 :#line:21
            OOOO0OOOO00O0000O .kwargs =OOOO0000OOO0OOO00 #line:22
            OOOO0OOOO00O0000O ._calc_all (**OOOO0000OOO0OOO00 )#line:23
    def _init_data (O00000O00OO0O0O00 ):#line:25
        O00000O00OO0O0O00 .data ={}#line:27
        O00000O00OO0O0O00 .data ["varname"]=[]#line:28
        O00000O00OO0O0O00 .data ["catnames"]=[]#line:29
        O00000O00OO0O0O00 .data ["vtypes"]=[]#line:30
        O00000O00OO0O0O00 .data ["dm"]=[]#line:31
        O00000O00OO0O0O00 .data ["rows_count"]=int (0 )#line:32
        O00000O00OO0O0O00 .data ["data_prepared"]=0 #line:33
    def _init_task (OOO0000OO00O000OO ):#line:35
        OOO0000OO00O000OO .cedent ={'cedent_type':'none','defi':{},'num_cedent':0 ,'trace_cedent':[],'traces':[],'generated_string':'','filter_value':int (0 )}#line:44
        OOO0000OO00O000OO .task_actinfo ={'proc':'','cedents_to_do':[],'cedents':[]}#line:48
        OOO0000OO00O000OO .hypolist =[]#line:49
        OOO0000OO00O000OO .stats ['total_cnt']=0 #line:51
        OOO0000OO00O000OO .stats ['total_valid']=0 #line:52
        OOO0000OO00O000OO .stats ['control_number']=0 #line:53
        OOO0000OO00O000OO .result ={}#line:54
    def _get_ver (OO00O00OO0O0000OO ):#line:56
        return OO00O00OO0O0000OO .version_string #line:57
    def _print_disclaimer (OOOO0OOOOOOOO0O0O ):#line:59
        print ("***********************************************************************************************************************************************************************")#line:60
        print ("Cleverminer version ",OOOO0OOOOOOOO0O0O ._get_ver ())#line:61
        print ("IMPORTANT NOTE: this is preliminary development version of CleverMiner procedure. This procedure is under intensive development and early released for educational use,")#line:62
        print ("    so there is ABSOLUTELY no guarantee of results, possible gaps in functionality and no guarantee of keeping syntax and parameters as in current version.")#line:63
        print ("    (That means we need to tidy up and make proper design, input validation, documentation and instrumentation before launch)")#line:64
        print ("This version is for personal and educational use only.")#line:65
        print ("***********************************************************************************************************************************************************************")#line:66
    def _prep_data (OOO0000O0O0O0OO0O ,OOO00OO0000O00O00 ):#line:68
        print ("Starting data preparation ...")#line:69
        OOO0000O0O0O0OO0O ._init_data ()#line:70
        OOO0000O0O0O0OO0O .stats ['start_prep_time']=time .time ()#line:71
        OOO0000O0O0O0OO0O .data ["rows_count"]=OOO00OO0000O00O00 .shape [0 ]#line:72
        for OO0OO0000OOO00O00 in OOO00OO0000O00O00 .select_dtypes (exclude =['category']).columns :#line:73
            OOO00OO0000O00O00 [OO0OO0000OOO00O00 ]=OOO00OO0000O00O00 [OO0OO0000OOO00O00 ].apply (str )#line:74
        O0O0OO000OO00O00O =pd .DataFrame .from_records ([(OO00OO0O000OO0O0O ,OOO00OO0000O00O00 [OO00OO0O000OO0O0O ].nunique ())for OO00OO0O000OO0O0O in OOO00OO0000O00O00 .columns ],columns =['Column_Name','Num_Unique']).sort_values (by =['Num_Unique'])#line:76
        print ("Unique value counts are:")#line:77
        print (O0O0OO000OO00O00O )#line:78
        for OO0OO0000OOO00O00 in OOO00OO0000O00O00 .columns :#line:79
            if OOO00OO0000O00O00 [OO0OO0000OOO00O00 ].nunique ()<100 :#line:80
                OOO00OO0000O00O00 [OO0OO0000OOO00O00 ]=OOO00OO0000O00O00 [OO0OO0000OOO00O00 ].astype ('category')#line:81
            else :#line:82
                print (f"WARNING: attribute {OO0OO0000OOO00O00} has more than 100 values, will be ignored.")#line:83
                del OOO00OO0000O00O00 [OO0OO0000OOO00O00 ]#line:84
        print ("Encoding columns into bit-form...")#line:85
        OO00OO00000O0O00O =0 #line:86
        O0O0OO0000OOO0000 =0 #line:87
        for O0O0OO00O00000O00 in OOO00OO0000O00O00 :#line:88
            print ('Column: '+O0O0OO00O00000O00 )#line:90
            OOO0000O0O0O0OO0O .data ["varname"].append (O0O0OO00O00000O00 )#line:91
            OO00O000O0OO0OOO0 =pd .get_dummies (OOO00OO0000O00O00 [O0O0OO00O00000O00 ])#line:92
            OOO0OO000O0O0OO0O =0 #line:93
            if (OOO00OO0000O00O00 .dtypes [O0O0OO00O00000O00 ].name =='category'):#line:94
                OOO0OO000O0O0OO0O =1 #line:95
            OOO0000O0O0O0OO0O .data ["vtypes"].append (OOO0OO000O0O0OO0O )#line:96
            OO000OO00OOO0OO0O =0 #line:99
            O0O00000OOOOOO00O =[]#line:100
            OO00OOO00OOO0OO00 =[]#line:101
            for O0OO0O0OO00OO00O0 in OO00O000O0OO0OOO0 :#line:103
                print ('....category : '+str (O0OO0O0OO00OO00O0 )+" @ "+str (time .time ()))#line:105
                O0O00000OOOOOO00O .append (O0OO0O0OO00OO00O0 )#line:106
                OOOOOO00OOO000OO0 =int (0 )#line:107
                O00O00O0OOO0O0OO0 =OO00O000O0OO0OOO0 [O0OO0O0OO00OO00O0 ].values #line:108
                for O0O0O0OOO00O0000O in range (OOO0000O0O0O0OO0O .data ["rows_count"]):#line:110
                    if O00O00O0OOO0O0OO0 [O0O0O0OOO00O0000O ]>0 :#line:111
                        OOOOOO00OOO000OO0 +=1 <<O0O0O0OOO00O0000O #line:112
                OO00OOO00OOO0OO00 .append (OOOOOO00OOO000OO0 )#line:113
                OO000OO00OOO0OO0O +=1 #line:123
                O0O0OO0000OOO0000 +=1 #line:124
            OOO0000O0O0O0OO0O .data ["catnames"].append (O0O00000OOOOOO00O )#line:126
            OOO0000O0O0O0OO0O .data ["dm"].append (OO00OOO00OOO0OO00 )#line:127
        print ("Encoding columns into bit-form...done")#line:129
        print ("Encoding columns into bit-form...done")#line:130
        print (f"List of attributes for analysis is: {OOO0000O0O0O0OO0O.data['varname']}")#line:131
        print (f"List of category names for individual attributes is : {OOO0000O0O0O0OO0O.data['catnames']}")#line:132
        print (f"List of vtypes is (all should be 1) : {OOO0000O0O0O0OO0O.data['vtypes']}")#line:133
        OOO0000O0O0O0OO0O .data ["data_prepared"]=1 #line:135
        print ("Data preparation finished ...")#line:136
        print ('Number of variables : '+str (len (OOO0000O0O0O0OO0O .data ["dm"])))#line:137
        print ('Total number of categories in all variables : '+str (O0O0OO0000OOO0000 ))#line:138
        OOO0000O0O0O0OO0O .stats ['end_prep_time']=time .time ()#line:139
        print ('Time needed for data preparation : ',str (OOO0000O0O0O0OO0O .stats ['end_prep_time']-OOO0000O0O0O0OO0O .stats ['start_prep_time']))#line:140
    def bitcount (OO0O00000O0O00OO0 ,OOO00OOO000O0O000 ):#line:143
        OOO000OOO000O0000 =0 #line:144
        while OOO00OOO000O0O000 >0 :#line:145
            if (OOO00OOO000O0O000 &1 ==1 ):OOO000OOO000O0000 +=1 #line:146
            OOO00OOO000O0O000 >>=1 #line:147
        return OOO000OOO000O0000 #line:148
    def _verifyCF (OO00OO00OO000O0O0 ,_O0O0OOO00O00OOOOO ):#line:151
        OO0O00OOOO000O000 =bin (_O0O0OOO00O00OOOOO ).count ("1")#line:152
        O000O0O0O00000OO0 =[]#line:153
        OO000O000O00OOO0O =[]#line:154
        O0OOO00O000O00O00 =0 #line:155
        O000OO0OO0000OOO0 =0 #line:156
        O0O0O0O00000OOOO0 =0 #line:157
        OO00000OOO00000O0 =0 #line:158
        O000O0O0O00000O0O =0 #line:159
        OO0O0O000O0OO0OO0 =0 #line:160
        OOOO000OOOOOOO00O =0 #line:161
        OO0O0O00000O0OOOO =0 #line:162
        O000000OO0OO0OOO0 =0 #line:163
        OOO0OO0O0O000O0OO =OO00OO00OO000O0O0 .data ["dm"][OO00OO00OO000O0O0 .data ["varname"].index (OO00OO00OO000O0O0 .kwargs .get ('target'))]#line:164
        for OO00OO0O0OO0000O0 in range (len (OOO0OO0O0O000O0OO )):#line:165
            O000OO0OO0000OOO0 =O0OOO00O000O00O00 #line:166
            O0OOO00O000O00O00 =bin (_O0O0OOO00O00OOOOO &OOO0OO0O0O000O0OO [OO00OO0O0OO0000O0 ]).count ("1")#line:167
            O000O0O0O00000OO0 .append (O0OOO00O000O00O00 )#line:168
            if OO00OO0O0OO0000O0 >0 :#line:169
                if (O0OOO00O000O00O00 >O000OO0OO0000OOO0 ):#line:170
                    if (O0O0O0O00000OOOO0 ==1 ):#line:171
                        OO0O0O00000O0OOOO +=1 #line:172
                    else :#line:173
                        OO0O0O00000O0OOOO =1 #line:174
                    if OO0O0O00000O0OOOO >OO00000OOO00000O0 :#line:175
                        OO00000OOO00000O0 =OO0O0O00000O0OOOO #line:176
                    O0O0O0O00000OOOO0 =1 #line:177
                    OO0O0O000O0OO0OO0 +=1 #line:178
                if (O0OOO00O000O00O00 <O000OO0OO0000OOO0 ):#line:179
                    if (O0O0O0O00000OOOO0 ==-1 ):#line:180
                        O000000OO0OO0OOO0 +=1 #line:181
                    else :#line:182
                        O000000OO0OO0OOO0 =1 #line:183
                    if O000000OO0OO0OOO0 >O000O0O0O00000O0O :#line:184
                        O000O0O0O00000O0O =O000000OO0OO0OOO0 #line:185
                    O0O0O0O00000OOOO0 =-1 #line:186
                    OOOO000OOOOOOO00O +=1 #line:187
                if (O0OOO00O000O00O00 ==O000OO0OO0000OOO0 ):#line:188
                    O0O0O0O00000OOOO0 =0 #line:189
                    O000000OO0OO0OOO0 =0 #line:190
                    OO0O0O00000O0OOOO =0 #line:191
        O00OOO0O000OO0OO0 =True #line:194
        for OO0000OO00OOOOO00 in OO00OO00OO000O0O0 .quantifiers .keys ():#line:195
            if OO0000OO00OOOOO00 =='Base':#line:196
                O00OOO0O000OO0OO0 =O00OOO0O000OO0OO0 and (OO00OO00OO000O0O0 .quantifiers .get (OO0000OO00OOOOO00 )<=OO0O00OOOO000O000 )#line:197
            if OO0000OO00OOOOO00 =='RelBase':#line:198
                O00OOO0O000OO0OO0 =O00OOO0O000OO0OO0 and (OO00OO00OO000O0O0 .quantifiers .get (OO0000OO00OOOOO00 )<=OO0O00OOOO000O000 *1.0 /OO00OO00OO000O0O0 .data ["rows_count"])#line:199
            if OO0000OO00OOOOO00 =='S_Up':#line:200
                O00OOO0O000OO0OO0 =O00OOO0O000OO0OO0 and (OO00OO00OO000O0O0 .quantifiers .get (OO0000OO00OOOOO00 )<=OO00000OOO00000O0 )#line:201
            if OO0000OO00OOOOO00 =='S_Down':#line:202
                O00OOO0O000OO0OO0 =O00OOO0O000OO0OO0 and (OO00OO00OO000O0O0 .quantifiers .get (OO0000OO00OOOOO00 )<=O000O0O0O00000O0O )#line:203
            if OO0000OO00OOOOO00 =='S_Any_Up':#line:204
                O00OOO0O000OO0OO0 =O00OOO0O000OO0OO0 and (OO00OO00OO000O0O0 .quantifiers .get (OO0000OO00OOOOO00 )<=OO00000OOO00000O0 )#line:205
            if OO0000OO00OOOOO00 =='S_Any_Down':#line:206
                O00OOO0O000OO0OO0 =O00OOO0O000OO0OO0 and (OO00OO00OO000O0O0 .quantifiers .get (OO0000OO00OOOOO00 )<=O000O0O0O00000O0O )#line:207
            if OO0000OO00OOOOO00 =='Max':#line:208
                O00OOO0O000OO0OO0 =O00OOO0O000OO0OO0 and (OO00OO00OO000O0O0 .quantifiers .get (OO0000OO00OOOOO00 )<=max (O000O0O0O00000OO0 ))#line:209
            if OO0000OO00OOOOO00 =='Min':#line:210
                O00OOO0O000OO0OO0 =O00OOO0O000OO0OO0 and (OO00OO00OO000O0O0 .quantifiers .get (OO0000OO00OOOOO00 )<=min (O000O0O0O00000OO0 ))#line:211
            if OO0000OO00OOOOO00 =='Relmax':#line:212
                if sum (O000O0O0O00000OO0 )>0 :#line:213
                    O00OOO0O000OO0OO0 =O00OOO0O000OO0OO0 and (OO00OO00OO000O0O0 .quantifiers .get (OO0000OO00OOOOO00 )<=max (O000O0O0O00000OO0 )*1.0 /sum (O000O0O0O00000OO0 ))#line:214
                else :#line:215
                    O00OOO0O000OO0OO0 =False #line:216
            if OO0000OO00OOOOO00 =='Relmin':#line:217
                if sum (O000O0O0O00000OO0 )>0 :#line:218
                    O00OOO0O000OO0OO0 =O00OOO0O000OO0OO0 and (OO00OO00OO000O0O0 .quantifiers .get (OO0000OO00OOOOO00 )<=min (O000O0O0O00000OO0 )*1.0 /sum (O000O0O0O00000OO0 ))#line:219
                else :#line:220
                    O00OOO0O000OO0OO0 =False #line:221
        O00O00O00O00OOO00 ={}#line:222
        if O00OOO0O000OO0OO0 ==True :#line:223
            OO00OO00OO000O0O0 .stats ['total_valid']+=1 #line:225
            O00O00O00O00OOO00 ["base"]=OO0O00OOOO000O000 #line:226
            O00O00O00O00OOO00 ["rel_base"]=OO0O00OOOO000O000 *1.0 /OO00OO00OO000O0O0 .data ["rows_count"]#line:227
            O00O00O00O00OOO00 ["s_up"]=OO00000OOO00000O0 #line:228
            O00O00O00O00OOO00 ["s_down"]=O000O0O0O00000O0O #line:229
            O00O00O00O00OOO00 ["s_any_up"]=OO0O0O000O0OO0OO0 #line:230
            O00O00O00O00OOO00 ["s_any_down"]=OOOO000OOOOOOO00O #line:231
            O00O00O00O00OOO00 ["max"]=max (O000O0O0O00000OO0 )#line:232
            O00O00O00O00OOO00 ["min"]=min (O000O0O0O00000OO0 )#line:233
            O00O00O00O00OOO00 ["rel_max"]=max (O000O0O0O00000OO0 )*1.0 /OO00OO00OO000O0O0 .data ["rows_count"]#line:234
            O00O00O00O00OOO00 ["rel_min"]=min (O000O0O0O00000OO0 )*1.0 /OO00OO00OO000O0O0 .data ["rows_count"]#line:235
            O00O00O00O00OOO00 ["hist"]=O000O0O0O00000OO0 #line:236
        return O00OOO0O000OO0OO0 ,O00O00O00O00OOO00 #line:238
    def _verify4ft (OOO000O00OOOO0000 ,_O0OOO0O0O0OOOOOOO ):#line:240
        O0OO0OO0OO00OO000 ={}#line:241
        OOO0O0OO0OO0O0000 =0 #line:242
        for O0OOOOOOOOOO0O000 in OOO000O00OOOO0000 .task_actinfo ['cedents']:#line:243
            O0OO0OO0OO00OO000 [O0OOOOOOOOOO0O000 ['cedent_type']]=O0OOOOOOOOOO0O000 ['filter_value']#line:245
            OOO0O0OO0OO0O0000 =OOO0O0OO0OO0O0000 +1 #line:246
        OO0O0O00O00O00000 =bin (O0OO0OO0OO00OO000 ['ante']&O0OO0OO0OO00OO000 ['succ']&O0OO0OO0OO00OO000 ['cond']).count ("1")#line:248
        OOO000O00O000OOOO =None #line:249
        OOO000O00O000OOOO =0 #line:250
        if OO0O0O00O00O00000 >0 :#line:259
            OOO000O00O000OOOO =bin (O0OO0OO0OO00OO000 ['ante']&O0OO0OO0OO00OO000 ['succ']&O0OO0OO0OO00OO000 ['cond']).count ("1")*1.0 /bin (O0OO0OO0OO00OO000 ['ante']&O0OO0OO0OO00OO000 ['cond']).count ("1")#line:260
        OOOOOOOOOO0OOOOOO =1 <<OOO000O00OOOO0000 .data ["rows_count"]#line:262
        O0O0OO000000O0OO0 =bin (O0OO0OO0OO00OO000 ['ante']&O0OO0OO0OO00OO000 ['succ']&O0OO0OO0OO00OO000 ['cond']).count ("1")#line:263
        OO0OO0O0O000O0O0O =bin (O0OO0OO0OO00OO000 ['ante']&~(OOOOOOOOOO0OOOOOO |O0OO0OO0OO00OO000 ['succ'])&O0OO0OO0OO00OO000 ['cond']).count ("1")#line:264
        O0OOOOOOOOOO0O000 =bin (~(OOOOOOOOOO0OOOOOO |O0OO0OO0OO00OO000 ['ante'])&O0OO0OO0OO00OO000 ['succ']&O0OO0OO0OO00OO000 ['cond']).count ("1")#line:265
        O000O00O000O000O0 =bin (~(OOOOOOOOOO0OOOOOO |O0OO0OO0OO00OO000 ['ante'])&~(OOOOOOOOOO0OOOOOO |O0OO0OO0OO00OO000 ['succ'])&O0OO0OO0OO00OO000 ['cond']).count ("1")#line:266
        OO0O0O0OOO0OOOO00 =0 #line:267
        if (O0O0OO000000O0OO0 +OO0OO0O0O000O0O0O )*(O0O0OO000000O0OO0 +O0OOOOOOOOOO0O000 )>0 :#line:268
            OO0O0O0OOO0OOOO00 =O0O0OO000000O0OO0 *(O0O0OO000000O0OO0 +OO0OO0O0O000O0O0O +O0OOOOOOOOOO0O000 +O000O00O000O000O0 )/(O0O0OO000000O0OO0 +OO0OO0O0O000O0O0O )/(O0O0OO000000O0OO0 +O0OOOOOOOOOO0O000 )-1 #line:269
        else :#line:270
            OO0O0O0OOO0OOOO00 =None #line:271
        OOO0O0OOOO00O0OOO =0 #line:272
        if (O0O0OO000000O0OO0 +OO0OO0O0O000O0O0O )*(O0O0OO000000O0OO0 +O0OOOOOOOOOO0O000 )>0 :#line:273
            OOO0O0OOOO00O0OOO =1 -O0O0OO000000O0OO0 *(O0O0OO000000O0OO0 +OO0OO0O0O000O0O0O +O0OOOOOOOOOO0O000 +O000O00O000O000O0 )/(O0O0OO000000O0OO0 +OO0OO0O0O000O0O0O )/(O0O0OO000000O0OO0 +O0OOOOOOOOOO0O000 )#line:274
        else :#line:275
            OOO0O0OOOO00O0OOO =None #line:276
        OO0OOOOO000OOO000 =True #line:277
        for OOOO00OOOOOOOOOOO in OOO000O00OOOO0000 .quantifiers .keys ():#line:278
            if OOOO00OOOOOOOOOOO =='Base':#line:279
                OO0OOOOO000OOO000 =OO0OOOOO000OOO000 and (OOO000O00OOOO0000 .quantifiers .get (OOOO00OOOOOOOOOOO )<=OO0O0O00O00O00000 )#line:280
            if OOOO00OOOOOOOOOOO =='RelBase':#line:281
                OO0OOOOO000OOO000 =OO0OOOOO000OOO000 and (OOO000O00OOOO0000 .quantifiers .get (OOOO00OOOOOOOOOOO )<=OO0O0O00O00O00000 *1.0 /OOO000O00OOOO0000 .data ["rows_count"])#line:282
            if OOOO00OOOOOOOOOOO =='pim':#line:283
                OO0OOOOO000OOO000 =OO0OOOOO000OOO000 and (OOO000O00OOOO0000 .quantifiers .get (OOOO00OOOOOOOOOOO )<=OOO000O00O000OOOO )#line:284
            if OOOO00OOOOOOOOOOO =='aad':#line:285
                if OO0O0O0OOO0OOOO00 !=None :#line:286
                    OO0OOOOO000OOO000 =OO0OOOOO000OOO000 and (OOO000O00OOOO0000 .quantifiers .get (OOOO00OOOOOOOOOOO )<=OO0O0O0OOO0OOOO00 )#line:287
                else :#line:288
                    OO0OOOOO000OOO000 =False #line:289
            if OOOO00OOOOOOOOOOO =='bad':#line:290
                if OOO0O0OOOO00O0OOO !=None :#line:291
                    OO0OOOOO000OOO000 =OO0OOOOO000OOO000 and (OOO000O00OOOO0000 .quantifiers .get (OOOO00OOOOOOOOOOO )<=OOO0O0OOOO00O0OOO )#line:292
                else :#line:293
                    OO0OOOOO000OOO000 =False #line:294
            O00O0O0OOOO0O00OO ={}#line:295
        if OO0OOOOO000OOO000 ==True :#line:296
            OOO000O00OOOO0000 .stats ['total_valid']+=1 #line:298
            O00O0O0OOOO0O00OO ["base"]=OO0O0O00O00O00000 #line:299
            O00O0O0OOOO0O00OO ["rel_base"]=OO0O0O00O00O00000 *1.0 /OOO000O00OOOO0000 .data ["rows_count"]#line:300
            O00O0O0OOOO0O00OO ["pim"]=OOO000O00O000OOOO #line:301
            O00O0O0OOOO0O00OO ["aad"]=OO0O0O0OOO0OOOO00 #line:302
            O00O0O0OOOO0O00OO ["bad"]=OOO0O0OOOO00O0OOO #line:303
            O00O0O0OOOO0O00OO ["fourfold"]=[O0O0OO000000O0OO0 ,OO0OO0O0O000O0O0O ,O0OOOOOOOOOO0O000 ,O000O00O000O000O0 ]#line:304
        return OO0OOOOO000OOO000 ,O00O0O0OOOO0O00OO #line:308
    def _verifysd4ft (O0OOOO0O0OO000O00 ,_OO00OO00OO000OOOO ):#line:310
        O0O0000OO000O000O ={}#line:311
        OO0O0O0OOOO0O00O0 =0 #line:312
        for OOOO0O0O000O00000 in O0OOOO0O0OO000O00 .task_actinfo ['cedents']:#line:313
            O0O0000OO000O000O [OOOO0O0O000O00000 ['cedent_type']]=OOOO0O0O000O00000 ['filter_value']#line:315
            OO0O0O0OOOO0O00O0 =OO0O0O0OOOO0O00O0 +1 #line:316
        OOO0O0000O0OO0OO0 =bin (O0O0000OO000O000O ['ante']&O0O0000OO000O000O ['succ']&O0O0000OO000O000O ['cond']&O0O0000OO000O000O ['frst']).count ("1")#line:318
        OO0OO000OO0O00000 =bin (O0O0000OO000O000O ['ante']&O0O0000OO000O000O ['succ']&O0O0000OO000O000O ['cond']&O0O0000OO000O000O ['scnd']).count ("1")#line:319
        OOO0OO0O00O00000O =None #line:320
        OO0OO0O00000O0OO0 =0 #line:321
        O00000000OOO0O000 =0 #line:322
        if OOO0O0000O0OO0OO0 >0 :#line:331
            OO0OO0O00000O0OO0 =bin (O0O0000OO000O000O ['ante']&O0O0000OO000O000O ['succ']&O0O0000OO000O000O ['cond']&O0O0000OO000O000O ['frst']).count ("1")*1.0 /bin (O0O0000OO000O000O ['ante']&O0O0000OO000O000O ['cond']&O0O0000OO000O000O ['frst']).count ("1")#line:332
        if OO0OO000OO0O00000 >0 :#line:333
            O00000000OOO0O000 =bin (O0O0000OO000O000O ['ante']&O0O0000OO000O000O ['succ']&O0O0000OO000O000O ['cond']&O0O0000OO000O000O ['scnd']).count ("1")*1.0 /bin (O0O0000OO000O000O ['ante']&O0O0000OO000O000O ['cond']&O0O0000OO000O000O ['scnd']).count ("1")#line:334
        O000OO0OO00O00O0O =1 <<O0OOOO0O0OO000O00 .data ["rows_count"]#line:336
        O0O00OO0OO0O0O0O0 =bin (O0O0000OO000O000O ['ante']&O0O0000OO000O000O ['succ']&O0O0000OO000O000O ['cond']&O0O0000OO000O000O ['frst']).count ("1")#line:337
        OOO000O0O0O0OO0OO =bin (O0O0000OO000O000O ['ante']&~(O000OO0OO00O00O0O |O0O0000OO000O000O ['succ'])&O0O0000OO000O000O ['cond']&O0O0000OO000O000O ['frst']).count ("1")#line:338
        O0O00OOO0000O0O00 =bin (~(O000OO0OO00O00O0O |O0O0000OO000O000O ['ante'])&O0O0000OO000O000O ['succ']&O0O0000OO000O000O ['cond']&O0O0000OO000O000O ['frst']).count ("1")#line:339
        OOO0O0O0000O0O0OO =bin (~(O000OO0OO00O00O0O |O0O0000OO000O000O ['ante'])&~(O000OO0OO00O00O0O |O0O0000OO000O000O ['succ'])&O0O0000OO000O000O ['cond']&O0O0000OO000O000O ['frst']).count ("1")#line:340
        OO00O0O0OO000000O =bin (O0O0000OO000O000O ['ante']&O0O0000OO000O000O ['succ']&O0O0000OO000O000O ['cond']&O0O0000OO000O000O ['scnd']).count ("1")#line:341
        O0O0OO000O00OO00O =bin (O0O0000OO000O000O ['ante']&~(O000OO0OO00O00O0O |O0O0000OO000O000O ['succ'])&O0O0000OO000O000O ['cond']&O0O0000OO000O000O ['scnd']).count ("1")#line:342
        O000OO0OOO0O000O0 =bin (~(O000OO0OO00O00O0O |O0O0000OO000O000O ['ante'])&O0O0000OO000O000O ['succ']&O0O0000OO000O000O ['cond']&O0O0000OO000O000O ['scnd']).count ("1")#line:343
        O000OOOOOO0OO0000 =bin (~(O000OO0OO00O00O0O |O0O0000OO000O000O ['ante'])&~(O000OO0OO00O00O0O |O0O0000OO000O000O ['succ'])&O0O0000OO000O000O ['cond']&O0O0000OO000O000O ['scnd']).count ("1")#line:344
        OO0OO00O0OOO000OO =True #line:345
        for O0O000OOO0000OOOO in O0OOOO0O0OO000O00 .quantifiers .keys ():#line:346
            if (O0O000OOO0000OOOO =='FrstBase')|(O0O000OOO0000OOOO =='Base1'):#line:347
                OO0OO00O0OOO000OO =OO0OO00O0OOO000OO and (O0OOOO0O0OO000O00 .quantifiers .get (O0O000OOO0000OOOO )<=OOO0O0000O0OO0OO0 )#line:348
            if (O0O000OOO0000OOOO =='ScndBase')|(O0O000OOO0000OOOO =='Base2'):#line:349
                OO0OO00O0OOO000OO =OO0OO00O0OOO000OO and (O0OOOO0O0OO000O00 .quantifiers .get (O0O000OOO0000OOOO )<=OO0OO000OO0O00000 )#line:350
            if (O0O000OOO0000OOOO =='FrstRelBase')|(O0O000OOO0000OOOO =='RelBase1'):#line:351
                OO0OO00O0OOO000OO =OO0OO00O0OOO000OO and (O0OOOO0O0OO000O00 .quantifiers .get (O0O000OOO0000OOOO )<=OOO0O0000O0OO0OO0 *1.0 /O0OOOO0O0OO000O00 .data ["rows_count"])#line:352
            if (O0O000OOO0000OOOO =='ScndRelBase')|(O0O000OOO0000OOOO =='RelBase2'):#line:353
                OO0OO00O0OOO000OO =OO0OO00O0OOO000OO and (O0OOOO0O0OO000O00 .quantifiers .get (O0O000OOO0000OOOO )<=OO0OO000OO0O00000 *1.0 /O0OOOO0O0OO000O00 .data ["rows_count"])#line:354
            if (O0O000OOO0000OOOO =='Frstpim')|(O0O000OOO0000OOOO =='pim1'):#line:355
                OO0OO00O0OOO000OO =OO0OO00O0OOO000OO and (O0OOOO0O0OO000O00 .quantifiers .get (O0O000OOO0000OOOO )<=OO0OO0O00000O0OO0 )#line:356
            if (O0O000OOO0000OOOO =='Scndpim')|(O0O000OOO0000OOOO =='pim2'):#line:357
                OO0OO00O0OOO000OO =OO0OO00O0OOO000OO and (O0OOOO0O0OO000O00 .quantifiers .get (O0O000OOO0000OOOO )<=O00000000OOO0O000 )#line:358
            if O0O000OOO0000OOOO =='Deltapim':#line:359
                OO0OO00O0OOO000OO =OO0OO00O0OOO000OO and (O0OOOO0O0OO000O00 .quantifiers .get (O0O000OOO0000OOOO )<=OO0OO0O00000O0OO0 -O00000000OOO0O000 )#line:360
            if O0O000OOO0000OOOO =='Ratiopim':#line:363
                if (O00000000OOO0O000 >0 ):#line:364
                    OO0OO00O0OOO000OO =OO0OO00O0OOO000OO and (O0OOOO0O0OO000O00 .quantifiers .get (O0O000OOO0000OOOO )<=OO0OO0O00000O0OO0 *1.0 /O00000000OOO0O000 )#line:365
                else :#line:366
                    OO0OO00O0OOO000OO =False #line:367
        O000OOOOO0OOO0OO0 ={}#line:368
        if OO0OO00O0OOO000OO ==True :#line:369
            O0OOOO0O0OO000O00 .stats ['total_valid']+=1 #line:371
            O000OOOOO0OOO0OO0 ["base1"]=OOO0O0000O0OO0OO0 #line:372
            O000OOOOO0OOO0OO0 ["base2"]=OO0OO000OO0O00000 #line:373
            O000OOOOO0OOO0OO0 ["rel_base1"]=OOO0O0000O0OO0OO0 *1.0 /O0OOOO0O0OO000O00 .data ["rows_count"]#line:374
            O000OOOOO0OOO0OO0 ["rel_base2"]=OO0OO000OO0O00000 *1.0 /O0OOOO0O0OO000O00 .data ["rows_count"]#line:375
            O000OOOOO0OOO0OO0 ["pim1"]=OO0OO0O00000O0OO0 #line:376
            O000OOOOO0OOO0OO0 ["pim2"]=O00000000OOO0O000 #line:377
            O000OOOOO0OOO0OO0 ["deltapim"]=OO0OO0O00000O0OO0 -O00000000OOO0O000 #line:378
            if (O00000000OOO0O000 >0 ):#line:379
                O000OOOOO0OOO0OO0 ["ratiopim"]=OO0OO0O00000O0OO0 *1.0 /O00000000OOO0O000 #line:380
            else :#line:381
                O000OOOOO0OOO0OO0 ["ratiopim"]=None #line:382
            O000OOOOO0OOO0OO0 ["fourfold1"]=[O0O00OO0OO0O0O0O0 ,OOO000O0O0O0OO0OO ,O0O00OOO0000O0O00 ,OOO0O0O0000O0O0OO ]#line:383
            O000OOOOO0OOO0OO0 ["fourfold2"]=[OO00O0O0OO000000O ,O0O0OO000O00OO00O ,O000OO0OOO0O000O0 ,O000OOOOOO0OO0000 ]#line:384
        if OO0OO00O0OOO000OO :#line:386
            print (f"DEBUG : ii = {OO0O0O0OOOO0O00O0}")#line:387
        return OO0OO00O0OOO000OO ,O000OOOOO0OOO0OO0 #line:388
    def _verifynewact4ft (OOOO00OO00O000OOO ,_O0000O00OOOO0O0O0 ):#line:390
        OOO0000000OOO0O0O ={}#line:391
        for O0O0O00OO0OO0OOOO in OOOO00OO00O000OOO .task_actinfo ['cedents']:#line:392
            OOO0000000OOO0O0O [O0O0O00OO0OO0OOOO ['cedent_type']]=O0O0O00OO0OO0OOOO ['filter_value']#line:394
        OOOO000OOOOOO00OO =bin (OOO0000000OOO0O0O ['ante']&OOO0000000OOO0O0O ['succ']&OOO0000000OOO0O0O ['cond']).count ("1")#line:396
        OOOO0OO0OO00OOOO0 =bin (OOO0000000OOO0O0O ['ante']&OOO0000000OOO0O0O ['succ']&OOO0000000OOO0O0O ['cond']&OOO0000000OOO0O0O ['antv']&OOO0000000OOO0O0O ['sucv']).count ("1")#line:397
        OO00O0OOOOO0OO00O =None #line:398
        O00O0OO0O0O000O0O =0 #line:399
        O00000O0O0OO0O00O =0 #line:400
        if OOOO000OOOOOO00OO >0 :#line:409
            O00O0OO0O0O000O0O =bin (OOO0000000OOO0O0O ['ante']&OOO0000000OOO0O0O ['succ']&OOO0000000OOO0O0O ['cond']).count ("1")*1.0 /bin (OOO0000000OOO0O0O ['ante']&OOO0000000OOO0O0O ['cond']).count ("1")#line:411
        if OOOO0OO0OO00OOOO0 >0 :#line:412
            O00000O0O0OO0O00O =bin (OOO0000000OOO0O0O ['ante']&OOO0000000OOO0O0O ['succ']&OOO0000000OOO0O0O ['cond']&OOO0000000OOO0O0O ['antv']&OOO0000000OOO0O0O ['sucv']).count ("1")*1.0 /bin (OOO0000000OOO0O0O ['ante']&OOO0000000OOO0O0O ['cond']&OOO0000000OOO0O0O ['antv']).count ("1")#line:414
        OOOOO0OOOO0O000OO =1 <<OOOO00OO00O000OOO .rows_count #line:416
        O0OOOO00O0OOOOO0O =bin (OOO0000000OOO0O0O ['ante']&OOO0000000OOO0O0O ['succ']&OOO0000000OOO0O0O ['cond']).count ("1")#line:417
        OOO0O000OO0OOOO0O =bin (OOO0000000OOO0O0O ['ante']&~(OOOOO0OOOO0O000OO |OOO0000000OOO0O0O ['succ'])&OOO0000000OOO0O0O ['cond']).count ("1")#line:418
        O000000O0O00O00OO =bin (~(OOOOO0OOOO0O000OO |OOO0000000OOO0O0O ['ante'])&OOO0000000OOO0O0O ['succ']&OOO0000000OOO0O0O ['cond']).count ("1")#line:419
        OO00000O0OOO0O000 =bin (~(OOOOO0OOOO0O000OO |OOO0000000OOO0O0O ['ante'])&~(OOOOO0OOOO0O000OO |OOO0000000OOO0O0O ['succ'])&OOO0000000OOO0O0O ['cond']).count ("1")#line:420
        OO0O0O0O0O0O0O000 =bin (OOO0000000OOO0O0O ['ante']&OOO0000000OOO0O0O ['succ']&OOO0000000OOO0O0O ['cond']&OOO0000000OOO0O0O ['antv']&OOO0000000OOO0O0O ['sucv']).count ("1")#line:421
        OOOO0O00000O0OOOO =bin (OOO0000000OOO0O0O ['ante']&~(OOOOO0OOOO0O000OO |(OOO0000000OOO0O0O ['succ']&OOO0000000OOO0O0O ['sucv']))&OOO0000000OOO0O0O ['cond']).count ("1")#line:422
        OO0OO00OO00O0000O =bin (~(OOOOO0OOOO0O000OO |(OOO0000000OOO0O0O ['ante']&OOO0000000OOO0O0O ['antv']))&OOO0000000OOO0O0O ['succ']&OOO0000000OOO0O0O ['cond']&OOO0000000OOO0O0O ['sucv']).count ("1")#line:423
        O00000000OOO0OO0O =bin (~(OOOOO0OOOO0O000OO |(OOO0000000OOO0O0O ['ante']&OOO0000000OOO0O0O ['antv']))&~(OOOOO0OOOO0O000OO |(OOO0000000OOO0O0O ['succ']&OOO0000000OOO0O0O ['sucv']))&OOO0000000OOO0O0O ['cond']).count ("1")#line:424
        OO00000000O000O0O =True #line:425
        for O00OO00000O0OO0OO in OOOO00OO00O000OOO .quantifiers .keys ():#line:426
            if (O00OO00000O0OO0OO =='PreBase')|(O00OO00000O0OO0OO =='Base1'):#line:427
                OO00000000O000O0O =OO00000000O000O0O and (OOOO00OO00O000OOO .quantifiers .get (O00OO00000O0OO0OO )<=OOOO000OOOOOO00OO )#line:428
            if (O00OO00000O0OO0OO =='PostBase')|(O00OO00000O0OO0OO =='Base2'):#line:429
                OO00000000O000O0O =OO00000000O000O0O and (OOOO00OO00O000OOO .quantifiers .get (O00OO00000O0OO0OO )<=OOOO0OO0OO00OOOO0 )#line:430
            if (O00OO00000O0OO0OO =='PreRelBase')|(O00OO00000O0OO0OO =='RelBase1'):#line:431
                OO00000000O000O0O =OO00000000O000O0O and (OOOO00OO00O000OOO .quantifiers .get (O00OO00000O0OO0OO )<=OOOO000OOOOOO00OO *1.0 /OOOO00OO00O000OOO .data ["rows_count"])#line:432
            if (O00OO00000O0OO0OO =='PostRelBase')|(O00OO00000O0OO0OO =='RelBase2'):#line:433
                OO00000000O000O0O =OO00000000O000O0O and (OOOO00OO00O000OOO .quantifiers .get (O00OO00000O0OO0OO )<=OOOO0OO0OO00OOOO0 *1.0 /OOOO00OO00O000OOO .data ["rows_count"])#line:434
            if (O00OO00000O0OO0OO =='Prepim')|(O00OO00000O0OO0OO =='pim1'):#line:435
                OO00000000O000O0O =OO00000000O000O0O and (OOOO00OO00O000OOO .quantifiers .get (O00OO00000O0OO0OO )<=O00O0OO0O0O000O0O )#line:436
            if (O00OO00000O0OO0OO =='Postpim')|(O00OO00000O0OO0OO =='pim2'):#line:437
                OO00000000O000O0O =OO00000000O000O0O and (OOOO00OO00O000OOO .quantifiers .get (O00OO00000O0OO0OO )<=O00000O0O0OO0O00O )#line:438
            if O00OO00000O0OO0OO =='Deltapim':#line:439
                OO00000000O000O0O =OO00000000O000O0O and (OOOO00OO00O000OOO .quantifiers .get (O00OO00000O0OO0OO )<=O00O0OO0O0O000O0O -O00000O0O0OO0O00O )#line:440
            if O00OO00000O0OO0OO =='Ratiopim':#line:443
                if (O00000O0O0OO0O00O >0 ):#line:444
                    OO00000000O000O0O =OO00000000O000O0O and (OOOO00OO00O000OOO .quantifiers .get (O00OO00000O0OO0OO )<=O00O0OO0O0O000O0O *1.0 /O00000O0O0OO0O00O )#line:445
                else :#line:446
                    OO00000000O000O0O =False #line:447
        OOO0OOO00OO000OOO ={}#line:448
        if OO00000000O000O0O ==True :#line:449
            OOOO00OO00O000OOO .stats ['total_valid']+=1 #line:451
            OOO0OOO00OO000OOO ["base1"]=OOOO000OOOOOO00OO #line:452
            OOO0OOO00OO000OOO ["base2"]=OOOO0OO0OO00OOOO0 #line:453
            OOO0OOO00OO000OOO ["rel_base1"]=OOOO000OOOOOO00OO *1.0 /OOOO00OO00O000OOO .data ["rows_count"]#line:454
            OOO0OOO00OO000OOO ["rel_base2"]=OOOO0OO0OO00OOOO0 *1.0 /OOOO00OO00O000OOO .data ["rows_count"]#line:455
            OOO0OOO00OO000OOO ["pim1"]=O00O0OO0O0O000O0O #line:456
            OOO0OOO00OO000OOO ["pim2"]=O00000O0O0OO0O00O #line:457
            OOO0OOO00OO000OOO ["deltapim"]=O00O0OO0O0O000O0O -O00000O0O0OO0O00O #line:458
            if (O00000O0O0OO0O00O >0 ):#line:459
                OOO0OOO00OO000OOO ["ratiopim"]=O00O0OO0O0O000O0O *1.0 /O00000O0O0OO0O00O #line:460
            else :#line:461
                OOO0OOO00OO000OOO ["ratiopim"]=None #line:462
            OOO0OOO00OO000OOO ["fourfoldpre"]=[O0OOOO00O0OOOOO0O ,OOO0O000OO0OOOO0O ,O000000O0O00O00OO ,OO00000O0OOO0O000 ]#line:463
            OOO0OOO00OO000OOO ["fourfoldpost"]=[OO0O0O0O0O0O0O000 ,OOOO0O00000O0OOOO ,OO0OO00OO00O0000O ,O00000000OOO0OO0O ]#line:464
        return OO00000000O000O0O ,OOO0OOO00OO000OOO #line:466
    def _verifyact4ft (OO00O0OO00OO0O000 ,_OOO0O0OO0OO0OO0OO ):#line:468
        O00OOO0O0O0O00OO0 ={}#line:469
        for OO000OO0OOOOOOO00 in OO00O0OO00OO0O000 .task_actinfo ['cedents']:#line:470
            O00OOO0O0O0O00OO0 [OO000OO0OOOOOOO00 ['cedent_type']]=OO000OO0OOOOOOO00 ['filter_value']#line:472
        OOOO0OOOO0OOO0O0O =bin (O00OOO0O0O0O00OO0 ['ante']&O00OOO0O0O0O00OO0 ['succ']&O00OOO0O0O0O00OO0 ['cond']&O00OOO0O0O0O00OO0 ['antv-']&O00OOO0O0O0O00OO0 ['sucv-']).count ("1")#line:474
        OO0OOO00O0OO00000 =bin (O00OOO0O0O0O00OO0 ['ante']&O00OOO0O0O0O00OO0 ['succ']&O00OOO0O0O0O00OO0 ['cond']&O00OOO0O0O0O00OO0 ['antv+']&O00OOO0O0O0O00OO0 ['sucv+']).count ("1")#line:475
        OOO0O00OOO0OOO000 =None #line:476
        O0O0OOOO00O00000O =0 #line:477
        OOOOOO0O0OO0OOOO0 =0 #line:478
        if OOOO0OOOO0OOO0O0O >0 :#line:487
            O0O0OOOO00O00000O =bin (O00OOO0O0O0O00OO0 ['ante']&O00OOO0O0O0O00OO0 ['succ']&O00OOO0O0O0O00OO0 ['cond']&O00OOO0O0O0O00OO0 ['antv-']&O00OOO0O0O0O00OO0 ['sucv-']).count ("1")*1.0 /bin (O00OOO0O0O0O00OO0 ['ante']&O00OOO0O0O0O00OO0 ['cond']&O00OOO0O0O0O00OO0 ['antv-']).count ("1")#line:489
        if OO0OOO00O0OO00000 >0 :#line:490
            OOOOOO0O0OO0OOOO0 =bin (O00OOO0O0O0O00OO0 ['ante']&O00OOO0O0O0O00OO0 ['succ']&O00OOO0O0O0O00OO0 ['cond']&O00OOO0O0O0O00OO0 ['antv+']&O00OOO0O0O0O00OO0 ['sucv+']).count ("1")*1.0 /bin (O00OOO0O0O0O00OO0 ['ante']&O00OOO0O0O0O00OO0 ['cond']&O00OOO0O0O0O00OO0 ['antv+']).count ("1")#line:492
        OOO00OOO0OO0000OO =1 <<OO00O0OO00OO0O000 .data ["rows_count"]#line:494
        O00000O00OO00O00O =bin (O00OOO0O0O0O00OO0 ['ante']&O00OOO0O0O0O00OO0 ['succ']&O00OOO0O0O0O00OO0 ['cond']&O00OOO0O0O0O00OO0 ['antv-']&O00OOO0O0O0O00OO0 ['sucv-']).count ("1")#line:495
        O0O00OOO0OOO0OO0O =bin (O00OOO0O0O0O00OO0 ['ante']&O00OOO0O0O0O00OO0 ['antv-']&~(OOO00OOO0OO0000OO |(O00OOO0O0O0O00OO0 ['succ']&O00OOO0O0O0O00OO0 ['sucv-']))&O00OOO0O0O0O00OO0 ['cond']).count ("1")#line:496
        OO0OO000O00OOOO00 =bin (~(OOO00OOO0OO0000OO |(O00OOO0O0O0O00OO0 ['ante']&O00OOO0O0O0O00OO0 ['antv-']))&O00OOO0O0O0O00OO0 ['succ']&O00OOO0O0O0O00OO0 ['cond']&O00OOO0O0O0O00OO0 ['sucv-']).count ("1")#line:497
        OO0OO000O000OOO00 =bin (~(OOO00OOO0OO0000OO |(O00OOO0O0O0O00OO0 ['ante']&O00OOO0O0O0O00OO0 ['antv-']))&~(OOO00OOO0OO0000OO |(O00OOO0O0O0O00OO0 ['succ']&O00OOO0O0O0O00OO0 ['sucv-']))&O00OOO0O0O0O00OO0 ['cond']).count ("1")#line:498
        OO000OOO000O0OOO0 =bin (O00OOO0O0O0O00OO0 ['ante']&O00OOO0O0O0O00OO0 ['succ']&O00OOO0O0O0O00OO0 ['cond']&O00OOO0O0O0O00OO0 ['antv+']&O00OOO0O0O0O00OO0 ['sucv+']).count ("1")#line:499
        OOO0O00OO0O0O0000 =bin (O00OOO0O0O0O00OO0 ['ante']&O00OOO0O0O0O00OO0 ['antv+']&~(OOO00OOO0OO0000OO |(O00OOO0O0O0O00OO0 ['succ']&O00OOO0O0O0O00OO0 ['sucv+']))&O00OOO0O0O0O00OO0 ['cond']).count ("1")#line:500
        O0OO00O0OO0OO0O00 =bin (~(OOO00OOO0OO0000OO |(O00OOO0O0O0O00OO0 ['ante']&O00OOO0O0O0O00OO0 ['antv+']))&O00OOO0O0O0O00OO0 ['succ']&O00OOO0O0O0O00OO0 ['cond']&O00OOO0O0O0O00OO0 ['sucv+']).count ("1")#line:501
        OOOOO00O00O0OO000 =bin (~(OOO00OOO0OO0000OO |(O00OOO0O0O0O00OO0 ['ante']&O00OOO0O0O0O00OO0 ['antv+']))&~(OOO00OOO0OO0000OO |(O00OOO0O0O0O00OO0 ['succ']&O00OOO0O0O0O00OO0 ['sucv+']))&O00OOO0O0O0O00OO0 ['cond']).count ("1")#line:502
        O0O0OOO0OO00OO0O0 =True #line:503
        for OO0O0OO0OOOO0000O in OO00O0OO00OO0O000 .quantifiers .keys ():#line:504
            if (OO0O0OO0OOOO0000O =='PreBase')|(OO0O0OO0OOOO0000O =='Base1'):#line:505
                O0O0OOO0OO00OO0O0 =O0O0OOO0OO00OO0O0 and (OO00O0OO00OO0O000 .quantifiers .get (OO0O0OO0OOOO0000O )<=OOOO0OOOO0OOO0O0O )#line:506
            if (OO0O0OO0OOOO0000O =='PostBase')|(OO0O0OO0OOOO0000O =='Base2'):#line:507
                O0O0OOO0OO00OO0O0 =O0O0OOO0OO00OO0O0 and (OO00O0OO00OO0O000 .quantifiers .get (OO0O0OO0OOOO0000O )<=OO0OOO00O0OO00000 )#line:508
            if (OO0O0OO0OOOO0000O =='PreRelBase')|(OO0O0OO0OOOO0000O =='RelBase1'):#line:509
                O0O0OOO0OO00OO0O0 =O0O0OOO0OO00OO0O0 and (OO00O0OO00OO0O000 .quantifiers .get (OO0O0OO0OOOO0000O )<=OOOO0OOOO0OOO0O0O *1.0 /OO00O0OO00OO0O000 .data ["rows_count"])#line:510
            if (OO0O0OO0OOOO0000O =='PostRelBase')|(OO0O0OO0OOOO0000O =='RelBase2'):#line:511
                O0O0OOO0OO00OO0O0 =O0O0OOO0OO00OO0O0 and (OO00O0OO00OO0O000 .quantifiers .get (OO0O0OO0OOOO0000O )<=OO0OOO00O0OO00000 *1.0 /OO00O0OO00OO0O000 .data ["rows_count"])#line:512
            if (OO0O0OO0OOOO0000O =='Prepim')|(OO0O0OO0OOOO0000O =='pim1'):#line:513
                O0O0OOO0OO00OO0O0 =O0O0OOO0OO00OO0O0 and (OO00O0OO00OO0O000 .quantifiers .get (OO0O0OO0OOOO0000O )<=O0O0OOOO00O00000O )#line:514
            if (OO0O0OO0OOOO0000O =='Postpim')|(OO0O0OO0OOOO0000O =='pim2'):#line:515
                O0O0OOO0OO00OO0O0 =O0O0OOO0OO00OO0O0 and (OO00O0OO00OO0O000 .quantifiers .get (OO0O0OO0OOOO0000O )<=OOOOOO0O0OO0OOOO0 )#line:516
            if OO0O0OO0OOOO0000O =='Deltapim':#line:517
                O0O0OOO0OO00OO0O0 =O0O0OOO0OO00OO0O0 and (OO00O0OO00OO0O000 .quantifiers .get (OO0O0OO0OOOO0000O )<=O0O0OOOO00O00000O -OOOOOO0O0OO0OOOO0 )#line:518
            if OO0O0OO0OOOO0000O =='Ratiopim':#line:521
                if (O0O0OOOO00O00000O >0 ):#line:522
                    O0O0OOO0OO00OO0O0 =O0O0OOO0OO00OO0O0 and (OO00O0OO00OO0O000 .quantifiers .get (OO0O0OO0OOOO0000O )<=OOOOOO0O0OO0OOOO0 *1.0 /O0O0OOOO00O00000O )#line:523
                else :#line:524
                    O0O0OOO0OO00OO0O0 =False #line:525
        O0O0O00OO00O00000 ={}#line:526
        if O0O0OOO0OO00OO0O0 ==True :#line:527
            OO00O0OO00OO0O000 .stats ['total_valid']+=1 #line:529
            O0O0O00OO00O00000 ["base1"]=OOOO0OOOO0OOO0O0O #line:530
            O0O0O00OO00O00000 ["base2"]=OO0OOO00O0OO00000 #line:531
            O0O0O00OO00O00000 ["rel_base1"]=OOOO0OOOO0OOO0O0O *1.0 /OO00O0OO00OO0O000 .data ["rows_count"]#line:532
            O0O0O00OO00O00000 ["rel_base2"]=OO0OOO00O0OO00000 *1.0 /OO00O0OO00OO0O000 .data ["rows_count"]#line:533
            O0O0O00OO00O00000 ["pim1"]=O0O0OOOO00O00000O #line:534
            O0O0O00OO00O00000 ["pim2"]=OOOOOO0O0OO0OOOO0 #line:535
            O0O0O00OO00O00000 ["deltapim"]=O0O0OOOO00O00000O -OOOOOO0O0OO0OOOO0 #line:536
            if (O0O0OOOO00O00000O >0 ):#line:537
                O0O0O00OO00O00000 ["ratiopim"]=OOOOOO0O0OO0OOOO0 *1.0 /O0O0OOOO00O00000O #line:538
            else :#line:539
                O0O0O00OO00O00000 ["ratiopim"]=None #line:540
            O0O0O00OO00O00000 ["fourfoldpre"]=[O00000O00OO00O00O ,O0O00OOO0OOO0OO0O ,OO0OO000O00OOOO00 ,OO0OO000O000OOO00 ]#line:541
            O0O0O00OO00O00000 ["fourfoldpost"]=[OO000OOO000O0OOO0 ,OOO0O00OO0O0O0000 ,O0OO00O0OO0OO0O00 ,OOOOO00O00O0OO000 ]#line:542
        return O0O0OOO0OO00OO0O0 ,O0O0O00OO00O00000 #line:544
    def _verify_opt (OOO0O00O0O0O000O0 ,OO0O0OO000OOO0O00 ,OOO00O0OOOOO0OOO0 ):#line:546
        O00O000000000OO0O =False #line:547
        if not (OO0O0OO000OOO0O00 ['optim'].get ('only_con')):#line:550
            return False #line:551
        O0OOOOO0O0OO0O0O0 ={}#line:552
        for OO0OO0O0O0OO0OO0O in OOO0O00O0O0O000O0 .task_actinfo ['cedents']:#line:553
            O0OOOOO0O0OO0O0O0 [OO0OO0O0O0OO0OO0O ['cedent_type']]=OO0OO0O0O0OO0OO0O ['filter_value']#line:555
        O000OO0OOOOO00000 =1 <<OOO0O00O0O0O000O0 .data ["rows_count"]#line:557
        OOOOO0O0OOO0OO00O =O000OO0OOOOO00000 -1 #line:558
        OOOOOOOO00000OOO0 =""#line:559
        O0000OO0OO00O00OO =0 #line:560
        if (O0OOOOO0O0OO0O0O0 .get ('ante')!=None ):#line:561
            OOOOO0O0OOO0OO00O =OOOOO0O0OOO0OO00O &O0OOOOO0O0OO0O0O0 ['ante']#line:562
        if (O0OOOOO0O0OO0O0O0 .get ('succ')!=None ):#line:563
            OOOOO0O0OOO0OO00O =OOOOO0O0OOO0OO00O &O0OOOOO0O0OO0O0O0 ['succ']#line:564
        if (O0OOOOO0O0OO0O0O0 .get ('cond')!=None ):#line:565
            OOOOO0O0OOO0OO00O =OOOOO0O0OOO0OO00O &O0OOOOO0O0OO0O0O0 ['cond']#line:566
        O000O00OOOO000000 =None #line:569
        if (OOO0O00O0O0O000O0 .proc =='CFMiner')|(OOO0O00O0O0O000O0 .proc =='4ftMiner'):#line:594
            O000O0OO0O00OOOO0 =bin (OOOOO0O0OOO0OO00O ).count ("1")#line:595
            for OOO000OO00O0O000O in OOO0O00O0O0O000O0 .quantifiers .keys ():#line:596
                if OOO000OO00O0O000O =='Base':#line:597
                    if not (OOO0O00O0O0O000O0 .quantifiers .get (OOO000OO00O0O000O )<=O000O0OO0O00OOOO0 ):#line:598
                        O00O000000000OO0O =True #line:599
                if OOO000OO00O0O000O =='RelBase':#line:601
                    if not (OOO0O00O0O0O000O0 .quantifiers .get (OOO000OO00O0O000O )<=O000O0OO0O00OOOO0 *1.0 /OOO0O00O0O0O000O0 .data ["rows_count"]):#line:602
                        O00O000000000OO0O =True #line:603
        return O00O000000000OO0O #line:606
        if OOO0O00O0O0O000O0 .proc =='CFMiner':#line:609
            if (OOO00O0OOOOO0OOO0 ['cedent_type']=='cond')&(OOO00O0OOOOO0OOO0 ['defi'].get ('type')=='con'):#line:610
                O000O0OO0O00OOOO0 =bin (O0OOOOO0O0OO0O0O0 ['cond']).count ("1")#line:611
                O0O000OOO0O0OO0O0 =True #line:612
                for OOO000OO00O0O000O in OOO0O00O0O0O000O0 .quantifiers .keys ():#line:613
                    if OOO000OO00O0O000O =='Base':#line:614
                        O0O000OOO0O0OO0O0 =O0O000OOO0O0OO0O0 and (OOO0O00O0O0O000O0 .quantifiers .get (OOO000OO00O0O000O )<=O000O0OO0O00OOOO0 )#line:615
                        if not (O0O000OOO0O0OO0O0 ):#line:616
                            print (f"...optimization : base is {O000O0OO0O00OOOO0} for {OOO00O0OOOOO0OOO0['generated_string']}")#line:617
                    if OOO000OO00O0O000O =='RelBase':#line:618
                        O0O000OOO0O0OO0O0 =O0O000OOO0O0OO0O0 and (OOO0O00O0O0O000O0 .quantifiers .get (OOO000OO00O0O000O )<=O000O0OO0O00OOOO0 *1.0 /OOO0O00O0O0O000O0 .data ["rows_count"])#line:619
                        if not (O0O000OOO0O0OO0O0 ):#line:620
                            print (f"...optimization : base is {O000O0OO0O00OOOO0} for {OOO00O0OOOOO0OOO0['generated_string']}")#line:621
                O00O000000000OO0O =not (O0O000OOO0O0OO0O0 )#line:622
        elif OOO0O00O0O0O000O0 .proc =='4ftMiner':#line:623
            if (OOO00O0OOOOO0OOO0 ['cedent_type']=='cond')&(OOO00O0OOOOO0OOO0 ['defi'].get ('type')=='con'):#line:624
                O000O0OO0O00OOOO0 =bin (O0OOOOO0O0OO0O0O0 ['cond']).count ("1")#line:625
                O0O000OOO0O0OO0O0 =True #line:626
                for OOO000OO00O0O000O in OOO0O00O0O0O000O0 .quantifiers .keys ():#line:627
                    if OOO000OO00O0O000O =='Base':#line:628
                        O0O000OOO0O0OO0O0 =O0O000OOO0O0OO0O0 and (OOO0O00O0O0O000O0 .quantifiers .get (OOO000OO00O0O000O )<=O000O0OO0O00OOOO0 )#line:629
                        if not (O0O000OOO0O0OO0O0 ):#line:630
                            print (f"...optimization : base is {O000O0OO0O00OOOO0} for {OOO00O0OOOOO0OOO0['generated_string']}")#line:631
                    if OOO000OO00O0O000O =='RelBase':#line:632
                        O0O000OOO0O0OO0O0 =O0O000OOO0O0OO0O0 and (OOO0O00O0O0O000O0 .quantifiers .get (OOO000OO00O0O000O )<=O000O0OO0O00OOOO0 *1.0 /OOO0O00O0O0O000O0 .data ["rows_count"])#line:633
                        if not (O0O000OOO0O0OO0O0 ):#line:634
                            print (f"...optimization : base is {O000O0OO0O00OOOO0} for {OOO00O0OOOOO0OOO0['generated_string']}")#line:635
                O00O000000000OO0O =not (O0O000OOO0O0OO0O0 )#line:636
            if (OOO00O0OOOOO0OOO0 ['cedent_type']=='ante')&(OOO00O0OOOOO0OOO0 ['defi'].get ('type')=='con'):#line:637
                O000O0OO0O00OOOO0 =bin (O0OOOOO0O0OO0O0O0 ['ante']&O0OOOOO0O0OO0O0O0 ['cond']).count ("1")#line:638
                O0O000OOO0O0OO0O0 =True #line:639
                for OOO000OO00O0O000O in OOO0O00O0O0O000O0 .quantifiers .keys ():#line:640
                    if OOO000OO00O0O000O =='Base':#line:641
                        O0O000OOO0O0OO0O0 =O0O000OOO0O0OO0O0 and (OOO0O00O0O0O000O0 .quantifiers .get (OOO000OO00O0O000O )<=O000O0OO0O00OOOO0 )#line:642
                        if not (O0O000OOO0O0OO0O0 ):#line:643
                            print (f"...optimization : ANTE: base is {O000O0OO0O00OOOO0} for {OOO00O0OOOOO0OOO0['generated_string']}")#line:644
                    if OOO000OO00O0O000O =='RelBase':#line:645
                        O0O000OOO0O0OO0O0 =O0O000OOO0O0OO0O0 and (OOO0O00O0O0O000O0 .quantifiers .get (OOO000OO00O0O000O )<=O000O0OO0O00OOOO0 *1.0 /OOO0O00O0O0O000O0 .data ["rows_count"])#line:646
                        if not (O0O000OOO0O0OO0O0 ):#line:647
                            print (f"...optimization : ANTE:  base is {O000O0OO0O00OOOO0} for {OOO00O0OOOOO0OOO0['generated_string']}")#line:648
                O00O000000000OO0O =not (O0O000OOO0O0OO0O0 )#line:649
            if (OOO00O0OOOOO0OOO0 ['cedent_type']=='succ')&(OOO00O0OOOOO0OOO0 ['defi'].get ('type')=='con'):#line:650
                O000O0OO0O00OOOO0 =bin (O0OOOOO0O0OO0O0O0 ['ante']&O0OOOOO0O0OO0O0O0 ['cond']&O0OOOOO0O0OO0O0O0 ['succ']).count ("1")#line:651
                O000O00OOOO000000 =0 #line:652
                if O000O0OO0O00OOOO0 >0 :#line:653
                    O000O00OOOO000000 =bin (O0OOOOO0O0OO0O0O0 ['ante']&O0OOOOO0O0OO0O0O0 ['succ']&O0OOOOO0O0OO0O0O0 ['cond']).count ("1")*1.0 /bin (O0OOOOO0O0OO0O0O0 ['ante']&O0OOOOO0O0OO0O0O0 ['cond']).count ("1")#line:654
                O000OO0OOOOO00000 =1 <<OOO0O00O0O0O000O0 .data ["rows_count"]#line:655
                OO0OOO00OO0O00OOO =bin (O0OOOOO0O0OO0O0O0 ['ante']&O0OOOOO0O0OO0O0O0 ['succ']&O0OOOOO0O0OO0O0O0 ['cond']).count ("1")#line:656
                O0O0O000000OOOO0O =bin (O0OOOOO0O0OO0O0O0 ['ante']&~(O000OO0OOOOO00000 |O0OOOOO0O0OO0O0O0 ['succ'])&O0OOOOO0O0OO0O0O0 ['cond']).count ("1")#line:657
                OO0OO0O0O0OO0OO0O =bin (~(O000OO0OOOOO00000 |O0OOOOO0O0OO0O0O0 ['ante'])&O0OOOOO0O0OO0O0O0 ['succ']&O0OOOOO0O0OO0O0O0 ['cond']).count ("1")#line:658
                O00OOOO000O0O0OO0 =bin (~(O000OO0OOOOO00000 |O0OOOOO0O0OO0O0O0 ['ante'])&~(O000OO0OOOOO00000 |O0OOOOO0O0OO0O0O0 ['succ'])&O0OOOOO0O0OO0O0O0 ['cond']).count ("1")#line:659
                O0O000OOO0O0OO0O0 =True #line:660
                for OOO000OO00O0O000O in OOO0O00O0O0O000O0 .quantifiers .keys ():#line:661
                    if OOO000OO00O0O000O =='pim':#line:662
                        O0O000OOO0O0OO0O0 =O0O000OOO0O0OO0O0 and (OOO0O00O0O0O000O0 .quantifiers .get (OOO000OO00O0O000O )<=O000O00OOOO000000 )#line:663
                    if not (O0O000OOO0O0OO0O0 ):#line:664
                        print (f"...optimization : SUCC:  pim is {O000O00OOOO000000} for {OOO00O0OOOOO0OOO0['generated_string']}")#line:665
                    if OOO000OO00O0O000O =='aad':#line:667
                        if (OO0OOO00OO0O00OOO +O0O0O000000OOOO0O )*(OO0OOO00OO0O00OOO +OO0OO0O0O0OO0OO0O )>0 :#line:668
                            O0O000OOO0O0OO0O0 =O0O000OOO0O0OO0O0 and (OOO0O00O0O0O000O0 .quantifiers .get (OOO000OO00O0O000O )<=OO0OOO00OO0O00OOO *(OO0OOO00OO0O00OOO +O0O0O000000OOOO0O +OO0OO0O0O0OO0OO0O +O00OOOO000O0O0OO0 )/(OO0OOO00OO0O00OOO +O0O0O000000OOOO0O )/(OO0OOO00OO0O00OOO +OO0OO0O0O0OO0OO0O )-1 )#line:669
                        else :#line:670
                            O0O000OOO0O0OO0O0 =False #line:671
                        if not (O0O000OOO0O0OO0O0 ):#line:672
                            O0OO00OO0O000OO00 =OO0OOO00OO0O00OOO *(OO0OOO00OO0O00OOO +O0O0O000000OOOO0O +OO0OO0O0O0OO0OO0O +O00OOOO000O0O0OO0 )/(OO0OOO00OO0O00OOO +O0O0O000000OOOO0O )/(OO0OOO00OO0O00OOO +OO0OO0O0O0OO0OO0O )-1 #line:673
                            print (f"...optimization : SUCC:  aad is {O0OO00OO0O000OO00} for {OOO00O0OOOOO0OOO0['generated_string']}")#line:674
                    if OOO000OO00O0O000O =='bad':#line:675
                        if (OO0OOO00OO0O00OOO +O0O0O000000OOOO0O )*(OO0OOO00OO0O00OOO +OO0OO0O0O0OO0OO0O )>0 :#line:676
                            O0O000OOO0O0OO0O0 =O0O000OOO0O0OO0O0 and (OOO0O00O0O0O000O0 .quantifiers .get (OOO000OO00O0O000O )<=1 -OO0OOO00OO0O00OOO *(OO0OOO00OO0O00OOO +O0O0O000000OOOO0O +OO0OO0O0O0OO0OO0O +O00OOOO000O0O0OO0 )/(OO0OOO00OO0O00OOO +O0O0O000000OOOO0O )/(OO0OOO00OO0O00OOO +OO0OO0O0O0OO0OO0O ))#line:677
                        else :#line:678
                            O0O000OOO0O0OO0O0 =False #line:679
                        if not (O0O000OOO0O0OO0O0 ):#line:680
                            OO0O0OO0O00OO000O =1 -OO0OOO00OO0O00OOO *(OO0OOO00OO0O00OOO +O0O0O000000OOOO0O +OO0OO0O0O0OO0OO0O +O00OOOO000O0O0OO0 )/(OO0OOO00OO0O00OOO +O0O0O000000OOOO0O )/(OO0OOO00OO0O00OOO +OO0OO0O0O0OO0OO0O )#line:681
                            print (f"...optimization : SUCC:  bad is {OO0O0OO0O00OO000O} for {OOO00O0OOOOO0OOO0['generated_string']}")#line:682
                O00O000000000OO0O =not (O0O000OOO0O0OO0O0 )#line:683
        if (O00O000000000OO0O ):#line:684
            print (f"... OPTIMALIZATION - SKIPPING BRANCH at cedent {OOO00O0OOOOO0OOO0['cedent_type']}")#line:685
        return O00O000000000OO0O #line:686
    def _print (O0OOO00000O000OO0 ,OOO0O0OO0O00OO00O ,_OOO0O000O00O00O0O ,_O0O0O0OO0O0O0OOOO ):#line:689
        if (len (_OOO0O000O00O00O0O ))!=len (_O0O0O0OO0O0O0OOOO ):#line:690
            print ("DIFF IN LEN for following cedent : "+str (len (_OOO0O000O00O00O0O ))+" vs "+str (len (_O0O0O0OO0O0O0OOOO )))#line:691
            print ("trace cedent : "+str (_OOO0O000O00O00O0O )+", traces "+str (_O0O0O0OO0O0O0OOOO ))#line:692
        OOOOOO0O0OO0OO0O0 =''#line:693
        for OO00000OO0OOOO000 in range (len (_OOO0O000O00O00O0O )):#line:694
            OO000O00O000OO00O =O0OOO00000O000OO0 .data ["varname"].index (OOO0O0OO0O00OO00O ['defi'].get ('attributes')[_OOO0O000O00O00O0O [OO00000OO0OOOO000 ]].get ('name'))#line:695
            OOOOOO0O0OO0OO0O0 =OOOOOO0O0OO0OO0O0 +O0OOO00000O000OO0 .data ["varname"][OO000O00O000OO00O ]+'('#line:697
            for OOOO00OO0O0O000OO in _O0O0O0OO0O0O0OOOO [OO00000OO0OOOO000 ]:#line:698
                OOOOOO0O0OO0OO0O0 =OOOOOO0O0OO0OO0O0 +O0OOO00000O000OO0 .data ["catnames"][OO000O00O000OO00O ][OOOO00OO0O0O000OO ]+" "#line:699
            OOOOOO0O0OO0OO0O0 =OOOOOO0O0OO0OO0O0 +')'#line:700
            if OO00000OO0OOOO000 +1 <len (_OOO0O000O00O00O0O ):#line:701
                OOOOOO0O0OO0OO0O0 =OOOOOO0O0OO0OO0O0 +' & '#line:702
        return OOOOOO0O0OO0OO0O0 #line:706
    def _print_hypo (O0OOO0OO0OO00O0O0 ,OOO0OOOO00OOOO00O ):#line:708
        print ('Hypothesis info : '+str (OOO0OOOO00OOOO00O ['params']))#line:709
        for O0OOO0O00O0OOO000 in O0OOO0OO0OO00O0O0 .task_actinfo ['cedents']:#line:710
            print (O0OOO0O00O0OOO000 ['cedent_type']+' = '+O0OOO0O00O0OOO000 ['generated_string'])#line:711
    def _genvar (O00OOOOOO0O00000O ,OO0OOOO00O000OO0O ,O000OO00O00000000 ,_O00O0O0000OO0O000 ,_O0OOOO00OOO000OO0 ,_O0O000O00000OOOO0 ,_OOO00OOO000O000OO ,_OOO00OO00O0OO0O00 ):#line:713
        for O0OO0OO00O00OOO00 in range (O000OO00O00000000 ['num_cedent']):#line:714
            if len (_O00O0O0000OO0O000 )==0 or O0OO0OO00O00OOO00 >_O00O0O0000OO0O000 [-1 ]:#line:715
                _O00O0O0000OO0O000 .append (O0OO0OO00O00OOO00 )#line:716
                O000000000O0O00O0 =O00OOOOOO0O00000O .data ["varname"].index (O000OO00O00000000 ['defi'].get ('attributes')[O0OO0OO00O00OOO00 ].get ('name'))#line:717
                _OO00OO0O0OOOO000O =O000OO00O00000000 ['defi'].get ('attributes')[O0OO0OO00O00OOO00 ].get ('minlen')#line:718
                _O0O0O0OOOOOO00O00 =O000OO00O00000000 ['defi'].get ('attributes')[O0OO0OO00O00OOO00 ].get ('maxlen')#line:719
                _OOO00O0O00OO000O0 =O000OO00O00000000 ['defi'].get ('attributes')[O0OO0OO00O00OOO00 ].get ('type')#line:720
                OO00O00OOO0OO0000 =len (O00OOOOOO0O00000O .data ["dm"][O000000000O0O00O0 ])#line:721
                _OO00O0OO0OO0O0000 =[]#line:722
                _O0OOOO00OOO000OO0 .append (_OO00O0OO0OO0O0000 )#line:723
                _O0OOOO00O0000OOO0 =int (0 )#line:724
                O00OOOOOO0O00000O ._gencomb (OO0OOOO00O000OO0O ,O000OO00O00000000 ,_O00O0O0000OO0O000 ,_O0OOOO00OOO000OO0 ,_OO00O0OO0OO0O0000 ,_O0O000O00000OOOO0 ,_O0OOOO00O0000OOO0 ,OO00O00OOO0OO0000 ,_OOO00O0O00OO000O0 ,_OOO00OOO000O000OO ,_OOO00OO00O0OO0O00 ,_OO00OO0O0OOOO000O ,_O0O0O0OOOOOO00O00 )#line:725
                _O0OOOO00OOO000OO0 .pop ()#line:726
                _O00O0O0000OO0O000 .pop ()#line:727
    def _gencomb (OO0OO0000OOOO0000 ,O0O0O0OOOOOO0O0OO ,O000OO000O0O000OO ,_O0O000OO0000OOOO0 ,_OOO00OOOO0OOOO0O0 ,_O00OO0OOO0O000OOO ,_O00OOOOO0O00O0OOO ,_OOOOO0000OOOO0O00 ,OO0OO00O0O0OO00O0 ,_O0OO000O0000OOO0O ,_O0OO0OOOOO000O0OO ,_OOO0OO0OO00O0O000 ,_OOOO0O0O00OOOO0OO ,_O000O0OOO0OOO00OO ):#line:729
        _OOO000OO0OO0O0O0O =[]#line:730
        if _O0OO000O0000OOO0O =="subset":#line:731
            if len (_O00OO0OOO0O000OOO )==0 :#line:732
                _OOO000OO0OO0O0O0O =range (OO0OO00O0O0OO00O0 )#line:733
            else :#line:734
                _OOO000OO0OO0O0O0O =range (_O00OO0OOO0O000OOO [-1 ]+1 ,OO0OO00O0O0OO00O0 )#line:735
        elif _O0OO000O0000OOO0O =="seq":#line:736
            if len (_O00OO0OOO0O000OOO )==0 :#line:737
                _OOO000OO0OO0O0O0O =range (OO0OO00O0O0OO00O0 -_OOOO0O0O00OOOO0OO +1 )#line:738
            else :#line:739
                if _O00OO0OOO0O000OOO [-1 ]+1 ==OO0OO00O0O0OO00O0 :#line:740
                    return #line:741
                O0O00OOO00O0OOOO0 =_O00OO0OOO0O000OOO [-1 ]+1 #line:742
                _OOO000OO0OO0O0O0O .append (O0O00OOO00O0OOOO0 )#line:743
        elif _O0OO000O0000OOO0O =="lcut":#line:744
            if len (_O00OO0OOO0O000OOO )==0 :#line:745
                O0O00OOO00O0OOOO0 =0 ;#line:746
            else :#line:747
                if _O00OO0OOO0O000OOO [-1 ]+1 ==OO0OO00O0O0OO00O0 :#line:748
                    return #line:749
                O0O00OOO00O0OOOO0 =_O00OO0OOO0O000OOO [-1 ]+1 #line:750
            _OOO000OO0OO0O0O0O .append (O0O00OOO00O0OOOO0 )#line:751
        elif _O0OO000O0000OOO0O =="rcut":#line:752
            if len (_O00OO0OOO0O000OOO )==0 :#line:753
                O0O00OOO00O0OOOO0 =OO0OO00O0O0OO00O0 -1 ;#line:754
            else :#line:755
                if _O00OO0OOO0O000OOO [-1 ]==0 :#line:756
                    return #line:757
                O0O00OOO00O0OOOO0 =_O00OO0OOO0O000OOO [-1 ]-1 #line:758
            _OOO000OO0OO0O0O0O .append (O0O00OOO00O0OOOO0 )#line:760
        elif _O0OO000O0000OOO0O =="one":#line:761
            if len (_O00OO0OOO0O000OOO )==0 :#line:762
                O00O00OOOOOOO0000 =OO0OO0000OOOO0000 .data ["varname"].index (O000OO000O0O000OO ['defi'].get ('attributes')[_O0O000OO0000OOOO0 [-1 ]].get ('name'))#line:763
                try :#line:764
                    O0O00OOO00O0OOOO0 =OO0OO0000OOOO0000 .data ["catnames"][O00O00OOOOOOO0000 ].index (O000OO000O0O000OO ['defi'].get ('attributes')[_O0O000OO0000OOOO0 [-1 ]].get ('value'))#line:765
                except :#line:766
                    print (f"ERROR: attribute '{O000OO000O0O000OO['defi'].get('attributes')[_O0O000OO0000OOOO0[-1]].get('name')}' has not value '{O000OO000O0O000OO['defi'].get('attributes')[_O0O000OO0000OOOO0[-1]].get('value')}'")#line:767
                    exit (1 )#line:768
                _OOO000OO0OO0O0O0O .append (O0O00OOO00O0OOOO0 )#line:769
                _OOOO0O0O00OOOO0OO =1 #line:770
                _O000O0OOO0OOO00OO =1 #line:771
            else :#line:772
                print ("DEBUG: one category should not have more categories")#line:773
                return #line:774
        else :#line:775
            print ("Attribute type "+_O0OO000O0000OOO0O +" not supported.")#line:776
            return #line:777
        for OOOO00OOOO0O0OO0O in _OOO000OO0OO0O0O0O :#line:780
                _O00OO0OOO0O000OOO .append (OOOO00OOOO0O0OO0O )#line:782
                _OOO00OOOO0OOOO0O0 .pop ()#line:783
                _OOO00OOOO0OOOO0O0 .append (_O00OO0OOO0O000OOO )#line:784
                _O00OOOO0OO0000O00 =_OOOOO0000OOOO0O00 |OO0OO0000OOOO0000 .data ["dm"][OO0OO0000OOOO0000 .data ["varname"].index (O000OO000O0O000OO ['defi'].get ('attributes')[_O0O000OO0000OOOO0 [-1 ]].get ('name'))][OOOO00OOOO0O0OO0O ]#line:788
                _OO0O0OO00OOO00O00 =1 #line:790
                if (len (_O0O000OO0000OOOO0 )<_O0OO0OOOOO000O0OO ):#line:791
                    _OO0O0OO00OOO00O00 =-1 #line:792
                if (len (_OOO00OOOO0OOOO0O0 [-1 ])<_OOOO0O0O00OOOO0OO ):#line:794
                    _OO0O0OO00OOO00O00 =0 #line:795
                _O000000OOOOO0O0O0 =0 #line:797
                if O000OO000O0O000OO ['defi'].get ('type')=='con':#line:798
                    _O000000OOOOO0O0O0 =_O00OOOOO0O00O0OOO &_O00OOOO0OO0000O00 #line:799
                else :#line:800
                    _O000000OOOOO0O0O0 =_O00OOOOO0O00O0OOO |_O00OOOO0OO0000O00 #line:801
                O000OO000O0O000OO ['trace_cedent']=_O0O000OO0000OOOO0 #line:802
                O000OO000O0O000OO ['traces']=_OOO00OOOO0OOOO0O0 #line:803
                O000OO000O0O000OO ['generated_string']=OO0OO0000OOOO0000 ._print (O000OO000O0O000OO ,_O0O000OO0000OOOO0 ,_OOO00OOOO0OOOO0O0 )#line:804
                O000OO000O0O000OO ['filter_value']=_O000000OOOOO0O0O0 #line:805
                O0O0O0OOOOOO0O0OO ['cedents'].append (O000OO000O0O000OO )#line:806
                O0OO0O0OO00O00OO0 =OO0OO0000OOOO0000 ._verify_opt (O0O0O0OOOOOO0O0OO ,O000OO000O0O000OO )#line:807
                if not (O0OO0O0OO00O00OO0 ):#line:813
                    if _OO0O0OO00OOO00O00 ==1 :#line:814
                        if len (O0O0O0OOOOOO0O0OO ['cedents_to_do'])==len (O0O0O0OOOOOO0O0OO ['cedents']):#line:816
                            if OO0OO0000OOOO0000 .proc =='CFMiner':#line:817
                                OO00000000O000000 ,O0OO0OO000000OO00 =OO0OO0000OOOO0000 ._verifyCF (_O000000OOOOO0O0O0 )#line:818
                            elif OO0OO0000OOOO0000 .proc =='4ftMiner':#line:819
                                OO00000000O000000 ,O0OO0OO000000OO00 =OO0OO0000OOOO0000 ._verify4ft (_O00OOOO0OO0000O00 )#line:820
                            elif OO0OO0000OOOO0000 .proc =='SD4ftMiner':#line:821
                                OO00000000O000000 ,O0OO0OO000000OO00 =OO0OO0000OOOO0000 ._verifysd4ft (_O00OOOO0OO0000O00 )#line:822
                            elif OO0OO0000OOOO0000 .proc =='NewAct4ftMiner':#line:823
                                OO00000000O000000 ,O0OO0OO000000OO00 =OO0OO0000OOOO0000 ._verifynewact4ft (_O00OOOO0OO0000O00 )#line:824
                            elif OO0OO0000OOOO0000 .proc =='Act4ftMiner':#line:825
                                OO00000000O000000 ,O0OO0OO000000OO00 =OO0OO0000OOOO0000 ._verifyact4ft (_O00OOOO0OO0000O00 )#line:826
                            else :#line:827
                                print ("Unsupported procedure : "+OO0OO0000OOOO0000 .proc )#line:828
                                exit (0 )#line:829
                            if OO00000000O000000 ==True :#line:830
                                OOO0OO00O0OO0OO00 ={}#line:831
                                OOO0OO00O0OO0OO00 ["hypo_id"]=OO0OO0000OOOO0000 .stats ['total_valid']#line:832
                                OOO0OO00O0OO0OO00 ["cedents"]={}#line:833
                                for OOO0OO000O000OO0O in O0O0O0OOOOOO0O0OO ['cedents']:#line:834
                                    OOO0OO00O0OO0OO00 ['cedents'][OOO0OO000O000OO0O ['cedent_type']]=OOO0OO000O000OO0O ['generated_string']#line:835
                                OOO0OO00O0OO0OO00 ["params"]=O0OO0OO000000OO00 #line:837
                                OOO0OO00O0OO0OO00 ["trace_cedent"]=_O0O000OO0000OOOO0 #line:838
                                OO0OO0000OOOO0000 ._print_hypo (OOO0OO00O0OO0OO00 )#line:839
                                OOO0OO00O0OO0OO00 ["traces"]=_OOO00OOOO0OOOO0O0 #line:842
                                OO0OO0000OOOO0000 .hypolist .append (OOO0OO00O0OO0OO00 )#line:843
                            OO0OO0000OOOO0000 .stats ['total_cnt']+=1 #line:844
                    if _OO0O0OO00OOO00O00 >=0 :#line:845
                        if len (O0O0O0OOOOOO0O0OO ['cedents_to_do'])>len (O0O0O0OOOOOO0O0OO ['cedents']):#line:846
                            OO0OO0000OOOO0000 ._start_cedent (O0O0O0OOOOOO0O0OO )#line:847
                    O0O0O0OOOOOO0O0OO ['cedents'].pop ()#line:848
                    if (len (_O0O000OO0000OOOO0 )<_OOO0OO0OO00O0O000 ):#line:849
                        OO0OO0000OOOO0000 ._genvar (O0O0O0OOOOOO0O0OO ,O000OO000O0O000OO ,_O0O000OO0000OOOO0 ,_OOO00OOOO0OOOO0O0 ,_O000000OOOOO0O0O0 ,_O0OO0OOOOO000O0OO ,_OOO0OO0OO00O0O000 )#line:850
                else :#line:851
                    O0O0O0OOOOOO0O0OO ['cedents'].pop ()#line:852
                if len (_O00OO0OOO0O000OOO )<_O000O0OOO0OOO00OO :#line:853
                    OO0OO0000OOOO0000 ._gencomb (O0O0O0OOOOOO0O0OO ,O000OO000O0O000OO ,_O0O000OO0000OOOO0 ,_OOO00OOOO0OOOO0O0 ,_O00OO0OOO0O000OOO ,_O00OOOOO0O00O0OOO ,_O00OOOO0OO0000O00 ,OO0OO00O0O0OO00O0 ,_O0OO000O0000OOO0O ,_O0OO0OOOOO000O0OO ,_OOO0OO0OO00O0O000 ,_OOOO0O0O00OOOO0OO ,_O000O0OOO0OOO00OO )#line:854
                _O00OO0OOO0O000OOO .pop ()#line:855
    def _start_cedent (OOOO00O00OO0O00OO ,O00OOOOO00O0O0OOO ):#line:857
        if len (O00OOOOO00O0O0OOO ['cedents_to_do'])>len (O00OOOOO00O0O0OOO ['cedents']):#line:858
            _O00OO00OO0OOO00O0 =[]#line:859
            _O00000OO0O000O00O =[]#line:860
            O0O000O00O0O000OO ={}#line:861
            O0O000O00O0O000OO ['cedent_type']=O00OOOOO00O0O0OOO ['cedents_to_do'][len (O00OOOOO00O0O0OOO ['cedents'])]#line:862
            O00000O0OO00O0000 =O0O000O00O0O000OO ['cedent_type']#line:863
            if ((O00000O0OO00O0000 [-1 ]=='-')|(O00000O0OO00O0000 [-1 ]=='+')):#line:864
                O00000O0OO00O0000 =O00000O0OO00O0000 [:-1 ]#line:865
            O0O000O00O0O000OO ['defi']=OOOO00O00OO0O00OO .kwargs .get (O00000O0OO00O0000 )#line:867
            if (O0O000O00O0O000OO ['defi']==None ):#line:868
                print ("Error getting cedent ",O0O000O00O0O000OO ['cedent_type'])#line:869
            _O0O0O0OO00O0O000O =int (0 )#line:870
            O0O000O00O0O000OO ['num_cedent']=len (O0O000O00O0O000OO ['defi'].get ('attributes'))#line:875
            if (O0O000O00O0O000OO ['defi'].get ('type')=='con'):#line:876
                _O0O0O0OO00O0O000O =(1 <<OOOO00O00OO0O00OO .data ["rows_count"])-1 #line:877
            OOOO00O00OO0O00OO ._genvar (O00OOOOO00O0O0OOO ,O0O000O00O0O000OO ,_O00OO00OO0OOO00O0 ,_O00000OO0O000O00O ,_O0O0O0OO00O0O000O ,O0O000O00O0O000OO ['defi'].get ('minlen'),O0O000O00O0O000OO ['defi'].get ('maxlen'))#line:878
    def _calc_all (O0OO00000000000OO ,**OO000O000O000000O ):#line:881
        O0OO00000000000OO ._prep_data (O0OO00000000000OO .kwargs .get ("df"))#line:882
        O0OO00000000000OO ._calculate (**OO000O000O000000O )#line:883
    def _check_cedents (OOO0000OOOOO000O0 ,OO0OO00000OO00O0O ,**OO0000O0OOO0O0O0O ):#line:885
        O0000O0OOOOO00O0O =True #line:886
        if (OO0000O0OOO0O0O0O .get ('quantifiers',None )==None ):#line:887
            print (f"Error: missing quantifiers.")#line:888
            O0000O0OOOOO00O0O =False #line:889
            return O0000O0OOOOO00O0O #line:890
        if (type (OO0000O0OOO0O0O0O .get ('quantifiers'))!=dict ):#line:891
            print (f"Error: quantifiers are not dictionary type.")#line:892
            O0000O0OOOOO00O0O =False #line:893
            return O0000O0OOOOO00O0O #line:894
        for O00O0000OO0OO000O in OO0OO00000OO00O0O :#line:896
            if (OO0000O0OOO0O0O0O .get (O00O0000OO0OO000O ,None )==None ):#line:897
                print (f"Error: cedent {O00O0000OO0OO000O} is missing in parameters.")#line:898
                O0000O0OOOOO00O0O =False #line:899
                return O0000O0OOOOO00O0O #line:900
            OO00OOO0O00OO0OOO =OO0000O0OOO0O0O0O .get (O00O0000OO0OO000O )#line:901
            if (OO00OOO0O00OO0OOO .get ('minlen'),None )==None :#line:902
                print (f"Error: cedent {O00O0000OO0OO000O} has no minimal length specified.")#line:903
                O0000O0OOOOO00O0O =False #line:904
                return O0000O0OOOOO00O0O #line:905
            if not (type (OO00OOO0O00OO0OOO .get ('minlen'))is int ):#line:906
                print (f"Error: cedent {O00O0000OO0OO000O} has invalid type of minimal length ({type(OO00OOO0O00OO0OOO.get('minlen'))}).")#line:907
                O0000O0OOOOO00O0O =False #line:908
                return O0000O0OOOOO00O0O #line:909
            if (OO00OOO0O00OO0OOO .get ('maxlen'),None )==None :#line:910
                print (f"Error: cedent {O00O0000OO0OO000O} has no maximal length specified.")#line:911
                O0000O0OOOOO00O0O =False #line:912
                return O0000O0OOOOO00O0O #line:913
            if not (type (OO00OOO0O00OO0OOO .get ('maxlen'))is int ):#line:914
                print (f"Error: cedent {O00O0000OO0OO000O} has invalid type of maximal length.")#line:915
                O0000O0OOOOO00O0O =False #line:916
                return O0000O0OOOOO00O0O #line:917
            if (OO00OOO0O00OO0OOO .get ('type'),None )==None :#line:918
                print (f"Error: cedent {O00O0000OO0OO000O} has no type specified.")#line:919
                O0000O0OOOOO00O0O =False #line:920
                return O0000O0OOOOO00O0O #line:921
            if not ((OO00OOO0O00OO0OOO .get ('type'))in (['con','dis'])):#line:922
                print (f"Error: cedent {O00O0000OO0OO000O} has invalid type. Allowed values are 'con' and 'dis'.")#line:923
                O0000O0OOOOO00O0O =False #line:924
                return O0000O0OOOOO00O0O #line:925
            if (OO00OOO0O00OO0OOO .get ('attributes'),None )==None :#line:926
                print (f"Error: cedent {O00O0000OO0OO000O} has no attributes specified.")#line:927
                O0000O0OOOOO00O0O =False #line:928
                return O0000O0OOOOO00O0O #line:929
            for O0OOO0O00OO0OO0O0 in OO00OOO0O00OO0OOO .get ('attributes'):#line:930
                if (O0OOO0O00OO0OO0O0 .get ('name'),None )==None :#line:931
                    print (f"Error: cedent {O00O0000OO0OO000O} / attribute {O0OOO0O00OO0OO0O0} has no 'name' attribute specified.")#line:932
                    O0000O0OOOOO00O0O =False #line:933
                    return O0000O0OOOOO00O0O #line:934
                if not ((O0OOO0O00OO0OO0O0 .get ('name'))in OOO0000OOOOO000O0 .data ["varname"]):#line:935
                    print (f"Error: cedent {O00O0000OO0OO000O} / attribute {O0OOO0O00OO0OO0O0.get('name')} not in variable list. Please check spelling.")#line:936
                    O0000O0OOOOO00O0O =False #line:937
                    return O0000O0OOOOO00O0O #line:938
                if (O0OOO0O00OO0OO0O0 .get ('type'),None )==None :#line:939
                    print (f"Error: cedent {O00O0000OO0OO000O} / attribute {O0OOO0O00OO0OO0O0.get('name')} has no 'type' attribute specified.")#line:940
                    O0000O0OOOOO00O0O =False #line:941
                    return O0000O0OOOOO00O0O #line:942
                if not ((O0OOO0O00OO0OO0O0 .get ('type'))in (['rcut','lcut','seq','subset','one'])):#line:943
                    print (f"Error: cedent {O00O0000OO0OO000O} / attribute {O0OOO0O00OO0OO0O0.get('name')} has unsupported type {O0OOO0O00OO0OO0O0.get('type')}. Supported types are 'subset','seq','lcut','rcut','one'.")#line:944
                    O0000O0OOOOO00O0O =False #line:945
                    return O0000O0OOOOO00O0O #line:946
                if (O0OOO0O00OO0OO0O0 .get ('minlen'),None )==None :#line:947
                    print (f"Error: cedent {O00O0000OO0OO000O} / attribute {O0OOO0O00OO0OO0O0.get('name')} has no minimal length specified.")#line:948
                    O0000O0OOOOO00O0O =False #line:949
                    return O0000O0OOOOO00O0O #line:950
                if not (type (O0OOO0O00OO0OO0O0 .get ('minlen'))is int ):#line:951
                    if not (O0OOO0O00OO0OO0O0 .get ('type')=='one'):#line:952
                        print (f"Error: cedent {O00O0000OO0OO000O} / attribute {O0OOO0O00OO0OO0O0.get('name')} has invalid type of minimal length.")#line:953
                        O0000O0OOOOO00O0O =False #line:954
                        return O0000O0OOOOO00O0O #line:955
                if (O0OOO0O00OO0OO0O0 .get ('maxlen'),None )==None :#line:956
                    print (f"Error: cedent {O00O0000OO0OO000O} / attribute {O0OOO0O00OO0OO0O0.get('name')} has no maximal length specified.")#line:957
                    O0000O0OOOOO00O0O =False #line:958
                    return O0000O0OOOOO00O0O #line:959
                if not (type (O0OOO0O00OO0OO0O0 .get ('maxlen'))is int ):#line:960
                    if not (O0OOO0O00OO0OO0O0 .get ('type')=='one'):#line:961
                        print (f"Error: cedent {O00O0000OO0OO000O} / attribute {O0OOO0O00OO0OO0O0.get('name')} has invalid type of maximal length.")#line:962
                        O0000O0OOOOO00O0O =False #line:963
                        return O0000O0OOOOO00O0O #line:964
        return O0000O0OOOOO00O0O #line:965
    def _calculate (OOO00OO0O00OOO0OO ,**OO000OO0000OOO0O0 ):#line:967
        if OOO00OO0O00OOO0OO .data ["data_prepared"]==0 :#line:968
            print ("Error: data not prepared")#line:969
            return #line:970
        OOO00OO0O00OOO0OO .kwargs =OO000OO0000OOO0O0 #line:971
        OOO00OO0O00OOO0OO .proc =OO000OO0000OOO0O0 .get ('proc')#line:972
        OOO00OO0O00OOO0OO .quantifiers =OO000OO0000OOO0O0 .get ('quantifiers')#line:973
        OOO00OO0O00OOO0OO ._init_task ()#line:975
        OOO00OO0O00OOO0OO .stats ['start_proc_time']=time .time ()#line:976
        OOO00OO0O00OOO0OO .task_actinfo ['cedents_to_do']=[]#line:977
        OOO00OO0O00OOO0OO .task_actinfo ['cedents']=[]#line:978
        if OO000OO0000OOO0O0 .get ("proc")=='CFMiner':#line:981
            OOO00OO0O00OOO0OO .task_actinfo ['cedents_to_do']=['cond']#line:982
            if OO000OO0000OOO0O0 .get ('target',None )==None :#line:983
                print ("ERROR: no target variable defined for CF Miner")#line:984
                return #line:985
            if not (OOO00OO0O00OOO0OO ._check_cedents (['cond'],**OO000OO0000OOO0O0 )):#line:986
                return #line:987
            if not (OO000OO0000OOO0O0 .get ('target')in OOO00OO0O00OOO0OO .data ["varname"]):#line:988
                print ("ERROR: target parameter is not variable. Please check spelling of variable name in parameter 'target'.")#line:989
                return #line:990
        elif OO000OO0000OOO0O0 .get ("proc")=='4ftMiner':#line:992
            if not (OOO00OO0O00OOO0OO ._check_cedents (['ante','succ'],**OO000OO0000OOO0O0 )):#line:993
                return #line:994
            _OO0OO00O0OO0OOOO0 =OO000OO0000OOO0O0 .get ("cond")#line:996
            if _OO0OO00O0OO0OOOO0 !=None :#line:997
                OOO00OO0O00OOO0OO .task_actinfo ['cedents_to_do'].append ('cond')#line:998
            else :#line:999
                O0OO0OOO0OO000OO0 =OOO00OO0O00OOO0OO .cedent #line:1000
                O0OO0OOO0OO000OO0 ['cedent_type']='cond'#line:1001
                O0OO0OOO0OO000OO0 ['filter_value']=(1 <<OOO00OO0O00OOO0OO .data ["rows_count"])-1 #line:1002
                O0OO0OOO0OO000OO0 ['generated_string']='---'#line:1003
                OOO00OO0O00OOO0OO .task_actinfo ['cedents_to_do'].append ('cond')#line:1005
                OOO00OO0O00OOO0OO .task_actinfo ['cedents'].append (O0OO0OOO0OO000OO0 )#line:1006
            OOO00OO0O00OOO0OO .task_actinfo ['cedents_to_do'].append ('ante')#line:1010
            OOO00OO0O00OOO0OO .task_actinfo ['cedents_to_do'].append ('succ')#line:1011
        elif OO000OO0000OOO0O0 .get ("proc")=='NewAct4ftMiner':#line:1012
            _OO0OO00O0OO0OOOO0 =OO000OO0000OOO0O0 .get ("cond")#line:1015
            if _OO0OO00O0OO0OOOO0 !=None :#line:1016
                OOO00OO0O00OOO0OO .task_actinfo ['cedents_to_do'].append ('cond')#line:1017
            else :#line:1018
                O0OO0OOO0OO000OO0 =OOO00OO0O00OOO0OO .cedent #line:1019
                O0OO0OOO0OO000OO0 ['cedent_type']='cond'#line:1020
                O0OO0OOO0OO000OO0 ['filter_value']=(1 <<OOO00OO0O00OOO0OO .data ["rows_count"])-1 #line:1021
                O0OO0OOO0OO000OO0 ['generated_string']='---'#line:1022
                print (O0OO0OOO0OO000OO0 ['filter_value'])#line:1023
                OOO00OO0O00OOO0OO .task_actinfo ['cedents_to_do'].append ('cond')#line:1024
                OOO00OO0O00OOO0OO .task_actinfo ['cedents'].append (O0OO0OOO0OO000OO0 )#line:1025
            OOO00OO0O00OOO0OO .task_actinfo ['cedents_to_do'].append ('antv')#line:1026
            OOO00OO0O00OOO0OO .task_actinfo ['cedents_to_do'].append ('sucv')#line:1027
            OOO00OO0O00OOO0OO .task_actinfo ['cedents_to_do'].append ('ante')#line:1028
            OOO00OO0O00OOO0OO .task_actinfo ['cedents_to_do'].append ('succ')#line:1029
        elif OO000OO0000OOO0O0 .get ("proc")=='Act4ftMiner':#line:1030
            _OO0OO00O0OO0OOOO0 =OO000OO0000OOO0O0 .get ("cond")#line:1033
            if _OO0OO00O0OO0OOOO0 !=None :#line:1034
                OOO00OO0O00OOO0OO .task_actinfo ['cedents_to_do'].append ('cond')#line:1035
            else :#line:1036
                O0OO0OOO0OO000OO0 =OOO00OO0O00OOO0OO .cedent #line:1037
                O0OO0OOO0OO000OO0 ['cedent_type']='cond'#line:1038
                O0OO0OOO0OO000OO0 ['filter_value']=(1 <<OOO00OO0O00OOO0OO .data ["rows_count"])-1 #line:1039
                O0OO0OOO0OO000OO0 ['generated_string']='---'#line:1040
                print (O0OO0OOO0OO000OO0 ['filter_value'])#line:1041
                OOO00OO0O00OOO0OO .task_actinfo ['cedents_to_do'].append ('cond')#line:1042
                OOO00OO0O00OOO0OO .task_actinfo ['cedents'].append (O0OO0OOO0OO000OO0 )#line:1043
            OOO00OO0O00OOO0OO .task_actinfo ['cedents_to_do'].append ('antv-')#line:1044
            OOO00OO0O00OOO0OO .task_actinfo ['cedents_to_do'].append ('antv+')#line:1045
            OOO00OO0O00OOO0OO .task_actinfo ['cedents_to_do'].append ('sucv-')#line:1046
            OOO00OO0O00OOO0OO .task_actinfo ['cedents_to_do'].append ('sucv+')#line:1047
            OOO00OO0O00OOO0OO .task_actinfo ['cedents_to_do'].append ('ante')#line:1048
            OOO00OO0O00OOO0OO .task_actinfo ['cedents_to_do'].append ('succ')#line:1049
        elif OO000OO0000OOO0O0 .get ("proc")=='SD4ftMiner':#line:1050
            if not (OOO00OO0O00OOO0OO ._check_cedents (['ante','succ','frst','scnd'],**OO000OO0000OOO0O0 )):#line:1053
                return #line:1054
            _OO0OO00O0OO0OOOO0 =OO000OO0000OOO0O0 .get ("cond")#line:1055
            if _OO0OO00O0OO0OOOO0 !=None :#line:1056
                OOO00OO0O00OOO0OO .task_actinfo ['cedents_to_do'].append ('cond')#line:1057
            else :#line:1058
                O0OO0OOO0OO000OO0 =OOO00OO0O00OOO0OO .cedent #line:1059
                O0OO0OOO0OO000OO0 ['cedent_type']='cond'#line:1060
                O0OO0OOO0OO000OO0 ['filter_value']=(1 <<OOO00OO0O00OOO0OO .data ["rows_count"])-1 #line:1061
                O0OO0OOO0OO000OO0 ['generated_string']='---'#line:1062
                print (O0OO0OOO0OO000OO0 ['filter_value'])#line:1063
                OOO00OO0O00OOO0OO .task_actinfo ['cedents_to_do'].append ('cond')#line:1064
                OOO00OO0O00OOO0OO .task_actinfo ['cedents'].append (O0OO0OOO0OO000OO0 )#line:1065
            OOO00OO0O00OOO0OO .task_actinfo ['cedents_to_do'].append ('frst')#line:1066
            OOO00OO0O00OOO0OO .task_actinfo ['cedents_to_do'].append ('scnd')#line:1067
            OOO00OO0O00OOO0OO .task_actinfo ['cedents_to_do'].append ('ante')#line:1068
            OOO00OO0O00OOO0OO .task_actinfo ['cedents_to_do'].append ('succ')#line:1069
        else :#line:1070
            print ("Unsupported procedure")#line:1071
            return #line:1072
        print ("Will go for ",OO000OO0000OOO0O0 .get ("proc"))#line:1073
        OOO00OO0O00OOO0OO .task_actinfo ['optim']={}#line:1076
        O0O00OO0OOOO000OO =True #line:1077
        for OO0OOO0OO0OOO00O0 in OOO00OO0O00OOO0OO .task_actinfo ['cedents_to_do']:#line:1078
            try :#line:1079
                OO0O00O00OO0O000O =OOO00OO0O00OOO0OO .kwargs .get (OO0OOO0OO0OOO00O0 )#line:1080
                if OO0O00O00OO0O000O .get ('type')!='con':#line:1083
                    O0O00OO0OOOO000OO =False #line:1084
            except :#line:1085
                OOO00OO0OOO0O0OO0 =1 <2 #line:1086
        if "opts"in OO000OO0000OOO0O0 :#line:1088
            if "no_optimizations"in OO000OO0000OOO0O0 .get ('opts'):#line:1089
                O0O00OO0OOOO000OO =False #line:1090
                print ("No optimization will be made.")#line:1091
        O0O00O00O00O0OOO0 ={}#line:1093
        O0O00O00O00O0OOO0 ['only_con']=O0O00OO0OOOO000OO #line:1094
        OOO00OO0O00OOO0OO .task_actinfo ['optim']=O0O00O00O00O0OOO0 #line:1095
        print ("Starting to mine rules.")#line:1103
        OOO00OO0O00OOO0OO ._start_cedent (OOO00OO0O00OOO0OO .task_actinfo )#line:1104
        OOO00OO0O00OOO0OO .stats ['end_proc_time']=time .time ()#line:1106
        print ("Done. Total verifications : "+str (OOO00OO0O00OOO0OO .stats ['total_cnt'])+", hypotheses "+str (OOO00OO0O00OOO0OO .stats ['total_valid'])+",control number:"+str (OOO00OO0O00OOO0OO .stats ['control_number'])+", times: prep "+str (OOO00OO0O00OOO0OO .stats ['end_prep_time']-OOO00OO0O00OOO0OO .stats ['start_prep_time'])+", processing "+str (OOO00OO0O00OOO0OO .stats ['end_proc_time']-OOO00OO0O00OOO0OO .stats ['start_proc_time']))#line:1109
        OOOOO0OOO00000000 ={}#line:1110
        O0000OOOO0O000O00 ={}#line:1111
        O0000OOOO0O000O00 ["task_type"]=OO000OO0000OOO0O0 .get ('proc')#line:1112
        O0000OOOO0O000O00 ["target"]=OO000OO0000OOO0O0 .get ('target')#line:1114
        O0000OOOO0O000O00 ["self.quantifiers"]=OOO00OO0O00OOO0OO .quantifiers #line:1115
        if OO000OO0000OOO0O0 .get ('cond')!=None :#line:1117
            O0000OOOO0O000O00 ['cond']=OO000OO0000OOO0O0 .get ('cond')#line:1118
        if OO000OO0000OOO0O0 .get ('ante')!=None :#line:1119
            O0000OOOO0O000O00 ['ante']=OO000OO0000OOO0O0 .get ('ante')#line:1120
        if OO000OO0000OOO0O0 .get ('succ')!=None :#line:1121
            O0000OOOO0O000O00 ['succ']=OO000OO0000OOO0O0 .get ('succ')#line:1122
        if OO000OO0000OOO0O0 .get ('opts')!=None :#line:1123
            O0000OOOO0O000O00 ['opts']=OO000OO0000OOO0O0 .get ('opts')#line:1124
        OOOOO0OOO00000000 ["taskinfo"]=O0000OOOO0O000O00 #line:1125
        OO000OO0OO0O00OOO ={}#line:1126
        OO000OO0OO0O00OOO ["total_verifications"]=OOO00OO0O00OOO0OO .stats ['total_cnt']#line:1127
        OO000OO0OO0O00OOO ["valid_hypotheses"]=OOO00OO0O00OOO0OO .stats ['total_valid']#line:1128
        OO000OO0OO0O00OOO ["time_prep"]=OOO00OO0O00OOO0OO .stats ['end_prep_time']-OOO00OO0O00OOO0OO .stats ['start_prep_time']#line:1129
        OO000OO0OO0O00OOO ["time_processing"]=OOO00OO0O00OOO0OO .stats ['end_proc_time']-OOO00OO0O00OOO0OO .stats ['start_proc_time']#line:1130
        OO000OO0OO0O00OOO ["time_total"]=OOO00OO0O00OOO0OO .stats ['end_prep_time']-OOO00OO0O00OOO0OO .stats ['start_prep_time']+OOO00OO0O00OOO0OO .stats ['end_proc_time']-OOO00OO0O00OOO0OO .stats ['start_proc_time']#line:1131
        OOOOO0OOO00000000 ["summary_statistics"]=OO000OO0OO0O00OOO #line:1132
        OOOOO0OOO00000000 ["hypotheses"]=OOO00OO0O00OOO0OO .hypolist #line:1133
        OOOOO0OOOO0000OO0 ={}#line:1134
        OOOOO0OOOO0000OO0 ["varname"]=OOO00OO0O00OOO0OO .data ["varname"]#line:1135
        OOOOO0OOOO0000OO0 ["catnames"]=OOO00OO0O00OOO0OO .data ["catnames"]#line:1136
        OOOOO0OOO00000000 ["datalabels"]=OOOOO0OOOO0000OO0 #line:1137
        OOO00OO0O00OOO0OO .result =OOOOO0OOO00000000 #line:1139
