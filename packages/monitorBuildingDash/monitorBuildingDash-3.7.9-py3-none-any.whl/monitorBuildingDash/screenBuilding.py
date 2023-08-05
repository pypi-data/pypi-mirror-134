#!/bin/python
# #######################
# #   GLOBAL VARIABLES  #
# # COMPUTER DEPENDENT  #
# #######################
import sys, glob, re, os, time, datetime as dt,importlib,pickle,glob
import pandas as pd,numpy as np
from dorianUtils.utilsD import Utils
import dorianUtils.comUtils as comUtils
importlib.reload(comUtils)
import socket
namePC = socket.gethostname()
DATABASE_SIZE_SECONDS = 60*2
PARKING_TIME = 60*1
DB_PARAMETERS = {
    'host'     : "localhost",
    'port'     : "5432",
    'dbname'   : "bigbrother",
    'user'     : "postgres",
    'password' : "sylfenbdd"
    }

if 'sylfen' in os.getenv('HOME'):
    baseFolder   = '/home/sylfen/share/dataScientismProd/MonitoringBatiment/'
else:
    baseFolder = '/home/dorian/data/sylfenData/'

FOLDERPKL = baseFolder + 'monitoringData/'

FileSystem = comUtils.FileSystem
fs = FileSystem()
appdir = os.path.dirname(os.path.realpath(__file__))
parentdir = fs.getParentDir(appdir)
CONFFOLDER = parentdir+'monitorBuildingDash/confFiles/'
# ==============================================================================
#                           CONFIGURATIONS
StreamingVisualisationMaster = comUtils.StreamerVisualisationMaster
Configurator = comUtils.Configurator
SuperDumper = comUtils.SuperDumper

# screeningBuildingConfig = Configurator(FOLDERPKL,CONFFOLDER,DB_PARAMETERS,
#             dbTimeWindow=DATABASE_SIZE_SECONDS,parkingTime=PARKING_TIME)
# screeningBuilding_dumper = SuperDumper(FOLDERPKL,CONFFOLDER,DB_PARAMETERS,
            # dbTimeWindow=DATABASE_SIZE_SECONDS,parkingTime=PARKING_TIME)

class ScreeningBuilding_dumper(SuperDumper):
    def __init__(self):
        SuperDumper.__init__(self,FOLDERPKL,CONFFOLDER,DB_PARAMETERS,
                        dbTimeWindow=DATABASE_SIZE_SECONDS,parkingTime=PARKING_TIME)

import plotly.express as px
import plotly.graph_objects as go

class ScreenBuildingMaster():
    def __init__(self):
        self.listComputation    = ['power enveloppe','consumed energy','energyPeriodBarPlot']
        self.utils = Utils()

    def exportToxcel(self,df):
        df.index = [t.astimezone(pytz.timezone('Etc/GMT-2')).replace(tzinfo=None) for t in df.index]
        df.to_excel(dt.date.today().strftime('%Y-%m-%d')+'.xlsx')
    #                       COMPUTATIONS FUNCTIONS
    # ==========================================================================
    def computePowerEnveloppe(self,timeRange,compteur = 'EM_VIRTUAL',rs='auto'):
        listTags = self.getTagsTU(compteur+'.+[0-9]-JTW','kW')
        df = self.df_loadTimeRangeTags(timeRange,listTags,rs='5s')
        L123min = df.min(axis=1)
        L123max = df.max(axis=1)
        L123moy = df.mean(axis=1)
        L123sum = df.sum(axis=1)
        df = pd.concat([df,L123min,L123max,L123moy,L123sum],axis=1)

        from dateutil import parser
        ts=[parser.parse(t) for t in timeRange]
        deltaseconds=(ts[1]-ts[0]).total_seconds()
        if rs=='auto':rs = '{:.0f}'.format(max(1,deltaseconds/1000)) + 's'
        df = df.resample(rs).apply(np.mean)
        dfmin = L123min.resample(rs).apply(np.min)
        dfmax = L123max.resample(rs).apply(np.max)
        df = pd.concat([df,dfmin,dfmax],axis=1)
        df.columns=['L1_mean','L2_mean','L3_mean','PminL123_mean','PmaxL123_mean',
                    'PmoyL123_mean','PsumL123_mean','PminL123_min','PmaxL123_max']
        return df

    def _integratePowerCol(self,df,tag,pool):
        print(tag)
        x1=df[df.tag==tag]
        if not x1.empty:
            timestamp=x1.index
            x1['totalSecs']=x1.index.to_series().apply(lambda x: (x-x1.index[0]).total_seconds())/3600
            x1=pd.DataFrame(integrate.cumulative_trapezoid(x1.value,x=x1.totalSecs))
            x1.index=timestamp[1:]
            x1.columns=[tag]
        return x1

    def compute_kWhFromPower(self,timeRange,compteurs=['B001'],rs='raw'):
        generalPat='('+'|'.join(['(' + c + ')' for c in compteurs])+')'
        listTags = self.getTagsTU(generalPat+'.*sys-JTW')

        df = self.df_loadTimeRangeTags(timeRange,listTags,rs=rs,applyMethod='mean',pool=True)
        dfs=[]
        for tag in listTags:
            dftmp = self._integratePowerCol(df,tag,True)
            if not dftmp.empty:dfs.append(dftmp)

        try : df=pd.concat(dfs,axis=1)
        except : df = pd.DataFrame()
        return df.ffill().bfill()

    def compute_kWhFromCompteur(self,timeRange,compteurs=['B001']):
        generalPat='('+'|'.join(['(' + c + ')' for c in compteurs])+')'
        listTags = self.getTagsTU(generalPat+'.+kWh-JTWH')
        df = self.df_loadTimeRangeTags(timeRange,listTags,rs='raw',applyMethod='mean')
        df = df.drop_duplicates()
        dfs=[]
        for tag in listTags:
            x1=df[df.tag==tag]
            dfs.append(x1['value'].diff().cumsum()[1:])
        try :
            df = pd.concat(dfs,axis=1)
            df.columns = listTags
        except : df = pd.DataFrame()
        return df.ffill().bfill()

    def plot_compare_kwhCompteurvsPower(self,timeRange,compteurs=['B001'],rs='600s'):
        dfCompteur = self.compute_kWhFromCompteur(timeRange,compteurs)
        dfPower = self.compute_kWhFromPower(timeRange,compteurs)
        df = self.utils.prepareDFsforComparison([dfCompteur,dfPower],
                            ['energy from compteur','enery from Power'],
                            group1='groupPower',group2='compteur',
                            regexpVar='\w+-\w+',rs=rs)

        fig=px.line(df,x='timestamp',y='value',color='compteur',line_dash='groupPower',)
        fig=self.utils.quickLayout(fig,'energy consumed from integrated power and from energy counter',ylab='kWh')
        fig.update_layout(yaxis_title='energy consommée en kWh')
        return fig

    def energyPeriodBarPlot(self,timeRange,period='1d',compteurs = ['A003','B001']):
        dfCompteur   = self.compute_kWhFromCompteur(timeRange,compteurs)
        df = dfCompteur.resample(period).first().diff()[1:]
        fig = px.bar(df,title='répartition des énergies consommées par compteur')
        fig.update_layout(yaxis_title='énergie en kWh')
        fig.update_layout(bargap=0.5)
        return fig
    # ==========================================================================
    #                       for website monitoring
    # ==========================================================================
    def generateFilename(self,proprietaire='MJ',client='*',batiment='*',local='*'):
        return '-'.join([proprietaire,client,batiment,local])

    def getListTagsAutoConso(self,compteurs):
        pTotal = [self.getTagsTU(k + '.*sys-JTW')[0] for k in compteurs]
        pvPower = self.getTagsTU('PV.*-JTW-00')[0]
        listTagsPower = pTotal + [pvPower]
        energieTotale = [self.getTagsTU(k + '.*kWh-JTWH')[0] for k in compteurs]
        pvEnergie = self.getTagsTU('PV.*-JTWH-00')[0]
        listTagsEnergy = energieTotale + [pvEnergie]
        return pTotal,pvPower,listTagsPower,energieTotale,pvEnergie,listTagsEnergy

    def computeAutoConso(self,timeRange,compteurs,formula='g+f-e+pv'):
        pTotal,pvPower,listTagsPower,energieTotale,pvEnergie,listTagsEnergy = self.getListTagsAutoConso(compteurs)
        # df = self.df_loadTimeRangeTags(timeRange,listTagsPower,'600s','mean')
        df = self.df_loadTimeRangeTags(timeRange,listTagsPower,'600s','mean')
        if formula=='g+f-e+pv':
            g,e,f = [self.getTagsTU(k+'.*sys-JTW')[0] for k in ['GENERAL','E001','F001',]]
            df['puissance totale'] = df[g] + df[f] - df[e] + df[pvPower]
        elif formula=='sum-pv':
            df['puissance totale'] = df[pTotal].sum(axis=1) - df[pvPower]
        elif formula=='sum':
            df['puissance totale'] = df[pTotal].sum(axis=1)

        df['diffPV']=df[pvPower]-df['puissance totale']
        dfAutoConso = pd.DataFrame()
        df['zero'] = 0
        dfAutoConso['part rSoc']     = 0
        dfAutoConso['part batterie'] = 0
        dfAutoConso['part Grid']     = -df[['diffPV','zero']].min(axis=1)
        dfAutoConso['Consommation du site']      = df['puissance totale']
        dfAutoConso['surplus PV']    = df[['diffPV','zero']].max(axis=1)
        dfAutoConso['part PV']       = df[pvPower]-dfAutoConso['surplus PV']
        # dfAutoConso['Autoconsommation'] = df[pvPower]-dfAutoConso['PV surplus']
        return dfAutoConso

    def consoPowerWeek(self,timeRange,compteurs,formula='g+f-e+pv'):
        pTotal,pvPower,listTagsPower,energieTotale,pvEnergie,listTagsEnergy = self.getListTagsAutoConso(compteurs)
        # df = self.df_loadTimeRangeTags(timeRange,listTagsPower,'1H','mean')
        df = self.df_loadTimeRangeTags(timeRange,listTagsPower,'1H','mean')

        if formula=='g+f-e+pv':
            g,e,f = [self.getTagsTU(k+'.*sys-JTW')[0] for k in ['GENERAL','E001','F001',]]
            df['puissance totale'] = df[g] + df[f] - df[e] + df[pvPower]
        elif formula=='sum-pv':
            df['puissance totale'] = df[pTotal].sum(axis=1) - df[pvPower]
        elif formula=='sum':
            df['puissance totale'] = df[pTotal].sum(axis=1)

        df = df[['puissance totale',pvPower]]
        df.columns = ['consommation bâtiment','production PV']
        return df

    def compute_EnergieMonth(self,timeRange,compteurs,formula='g+f-e+pv'):
        pTotal,pvPower,listTagsPower,energieTotale,pvEnergie,listTagsEnergy = self.getListTagsAutoConso(compteurs)
        # df = self.df_loadTimeRangeTags(timeRange,listTagsEnergy,rs='raw',applyMethod='mean')
        df = self.df_loadTimeRangeTags(timeRange,listTagsEnergy,rs='raw',applyMethod='mean')
        df = df.drop_duplicates()

        df=df.pivot(columns='tag',values='value').resample('1d').first().ffill().bfill()
        newdf=df.diff().iloc[1:,:]
        newdf.index = df.index[:-1]
        if formula=='g+f-e+pv':
            g,e,f = [self.getTagsTU(k + '.*kWh-JTWH')[0] for k in ['GENERAL','E001','F001',]]
            newdf['energie totale'] = newdf[g] + newdf[f] - newdf[e] + newdf[pvEnergie]
        elif formula=='sum-pv':
            newdf['energie totale'] = newdf[pTotal].sum(axis=1) - newdf[pvEnergie]
        elif formula=='sum':
            newdf['energie totale'] = newdf[energieTotale].sum(axis=1)

        newdf = newdf[['energie totale',pvEnergie]]
        newdf.columns = ['kWh consommés','kWh produits']
        return newdf

    def get_compteur(self,timeDate,compteurs,formula='g+f-e+pv'):
        timeRange = [k.isoformat() for k in [timeDate - dt.timedelta(seconds=600),timeDate]]
        pTotal,pvPower,listTagsPower,energieTotale,pvEnergie,listTagsEnergy = self.getListTagsAutoConso(compteurs)
        df = self.df_loadTimeRangeTags(timeRange,listTagsEnergy,rs='20s',applyMethod='mean')
        g,e,f = [self.getTagsTU(k + '.*kWh-JTWH')[0] for k in ['GENERAL','E001','F001',]]
        if formula=='g+f-e+pv':
            df['energie totale'] = df[g] + df[f] - df[e] + df[pvEnergie]
        elif formula=='sum':
            df['energie totale'] = df[energieTotale].sum(axis=1)
        return df.iloc[-1,:]
    # ==============================================================================
    #                   graphic functions
    # ==============================================================================
    def update_lineshape_fig(self,fig,style='default'):
        if style=='default':
            fig.update_traces(line_shape="linear",mode='lines+markers')
        elif style in ['markers','lines','lines+markers']:
            fig.update_traces(line_shape="linear",mode=style)
        elif style =='stairs':
            fig.update_traces(line_shape="hv",mode='lines')

class ScreenBuildingComputer(ScreenBuildingMaster,StreamingVisualisationMaster):
    def __init__(self):
        StreamingVisualisationMaster.__init__(self,FOLDERPKL,CONFFOLDER,DB_PARAMETERS,
                        dbTimeWindow=DATABASE_SIZE_SECONDS,parkingTime=PARKING_TIME)
        ScreenBuildingMaster.__init__(self)
