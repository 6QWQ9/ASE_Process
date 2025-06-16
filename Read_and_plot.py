%matplotlib inline
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import seaborn as sns
rootdir="E:/linux_trans/Elas/"
phase_name=[];
Bulk_Voigt=[];Shear_Voigt=[];Young_Voigt=[];Possion_Voigt=[]
Bulk_Reuss=[];Shear_Reuss=[];Young_Reuss=[];Possion_Reuss=[]
Bulk_Avg=[];Shear_Avg=[];Young_Avg=[];Possion_Avg=[]
dir_list = next(os.walk(rootdir))[1]
for count, value in enumerate(dir_list):
    if value[0]!='.':
        fname=rootdir+value+'/Modulus.txt'
        print('open file in '+value)
        with open (fname) as f:
            data=f.readlines()
            df=pd.DataFrame(data[7:11])
            df=df.iloc[:,0].str.split(expand=True)
            P=pd.DataFrame(df.iloc[3,:].T)
            P.drop(P.columns[5],axis=1,inplace=True)
            P.drop(P.columns[1],axis=1,inplace=True)
            df.drop(index=3,axis=0,inplace=True)
            df.drop(df.columns[1],axis=1,inplace=True)
            df.drop(df.columns[1],axis=1,inplace=True)
            df.columns=['Property','Voigt','Reuss','Avg']
            P.columns=df.columns
            df=pd.concat([df,P])
            phase_name.append(value[0:-5])
            #Voigt
            Bulk_Voigt.append(df['Voigt'][0])
            Shear_Voigt.append(df['Voigt'][1])
            Young_Voigt.append(df['Voigt'][2])
            Possion_Voigt.append(df['Voigt'][3])
            #Reuss
            Bulk_Reuss.append(df['Reuss'][0])
            Shear_Reuss.append(df['Reuss'][1])
            Young_Reuss.append(df['Reuss'][2])
            Possion_Reuss.append(df['Reuss'][3])
            # Average
            Bulk_Avg.append(df['Avg'][0])
            Shear_Avg.append(df['Avg'][1])
            Young_Avg.append(df['Avg'][2])
            Possion_Avg.append(df['Avg'][3])

data_Voigt={'phase_name':phase_name,'Bulk':Bulk_Voigt,'Shear':Shear_Voigt,
           'Young':Young_Voigt,'Possion':Possion_Voigt}
data_Reuss={'phase_name':phase_name,'Bulk':Bulk_Reuss,'Shear':Shear_Reuss,
            'Young':Young_Reuss,'Possion':Possion_Reuss}
data_Avg={'phase_name':phase_name,'Bulk':Bulk_Avg,'Shear':Shear_Avg,
          'Young':Young_Avg,'Possion':Possion_Avg}
df_Voigt=pd.DataFrame(data_Voigt)
df_Reuss=pd.DataFrame(data_Reuss)
df_Avg=pd.DataFrame(data_Avg)
df_Voigt.iloc[:,1:4]=df_Voigt.iloc[:,1:4].astype(float)
print(df_Voigt)
type(df_Voigt.iloc[1,1])

df_Voigt = df_Voigt.sort_values(by='phase_name')
df_Reuss = df_Reuss.sort_values(by='phase_name')
df_Avg = df_Avg.sort_values(by='phase_name')


# 函数定义部分

def plotcurveLegend(title,xlim=[0,5],ylim=[0,100],**kwargs):
    font_dict = dict(fontsize=24,color='k',weight='bold',style='normal') #titleLe
    font_dict2 = dict(fontsize=18,color='k',weight='semibold',style='normal') #tick
    font_dict3 = dict(fontsize=12,color='k',weight='light',style='normal') #tick
    
    plt.rcParams.update({'text.usetex': True, "font.family": "cambrria math"})
    fig = plt.figure(figsize=(5,5))
    axs1 = fig.add_axes([0.2,0.2,0.9,0.9])
    
    print(kwargs.items())
    i=1
    for key,value in kwargs.items():
        if value.shape[0] == 1:
            return print('please check the format of input data')
        axs1.plot(value[0],value[1],'.-')
        i = i+1
    del i
    
    axs1.set_xlabel('Phase', fontdict=font_dict2)
    axs1.set_ylabel('Modulus(MPa)', fontdict=font_dict2)
    axs1.legend(Legend, fontsize=16)
    
    # ytick = [ele for ele in range(ylim[0],ylim[1],10)]
    axs1.set_ylim(ylim)
    axs1.set_yticks(ytick)
    
    #xlabel=['Al','Mg','Si','r$1\beta$','r$2\beta$','r$\beta$','U1','U2','B','Q','Q2n',r'$\beta$']
    axs1.set_xticks(value[0], labels=xlabel)
    axs1.tick_params(axis='both', labelsize=16)
    axs1.set_title(title, fontdict=font_dict)

# 数据准备部分
Legend = ['Bulk','Shear','Young']
title = 'Voigt'

y1 = pd.to_numeric(df_Voigt['Bulk']) # 重要：绘图命令不能直接读取字符串
y2 = pd.to_numeric(df_Voigt['Shear'])
y3 = pd.to_numeric(df_Voigt['Young'])

xy1 = np.array([df_Voigt['phase_name'], y1])
xy2 = np.array([df_Voigt['phase_name'], y2])
xy3 = np.array([df_Voigt['phase_name'], y3])

sns.set_theme()
sns.set_style("whitegrid")
plotcurve(Legend,title,ylim=[0,160],xy1=xy1,xy2=xy2,xy3=xy3)
