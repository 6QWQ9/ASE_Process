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
