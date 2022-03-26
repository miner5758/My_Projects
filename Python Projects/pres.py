import pandas as pd
import matplotlib.pyplot as plt
state_names = ["Alabama","Alaska","Arizona","Arkansas","California","Colorado",
  "Connecticut","Delaware","Florida","Georgia","Hawaii","Idaho","Illinois",
  "Indiana","Iowa","Kansas","Kentucky","Louisiana","Maine","Maryland",
  "Massachusetts","Michigan","Minnesota","Mississippi","Missouri","Montana",
  "Nebraska","Nevada","New Hampshire","New Jersey","New Mexico","New York",
  "North Carolina","North Dakota","Ohio","Oklahoma","Oregon","Pennsylvania",
  "Rhode Island","South Carolina","South Dakota","Tennessee","Texas","Utah",
  "Vermont","Virginia","Washington","West Virginia","Wisconsin","Wyoming","District of Columbia"]

data = pd.read_csv(r"president_county_candidate.csv")
def plot_election(state):
    if state == 'Choices' or state == 'choices':
        print(state_names)
    else:
        Dem = data[data['state'] == state]
        Dem = Dem[Dem['candidate'] == 'Joe Biden']
        Dem = Dem.loc[:,['candidate','total_votes']]
        Dem['total_votes'] = Dem['total_votes'].sum(axis = 0, skipna = True)
        Dem = Dem.iloc[:1]
        Rep = data[data['state'] == state]
        Rep = Rep[Rep['candidate'] == 'Donald Trump']
        Rep = Rep.loc[:,['candidate','total_votes']]
        Rep['total_votes'] = Rep['total_votes'].sum(axis = 0, skipna = True)
        Rep = Rep.iloc[:1]
        Lib = data[data['state'] == state]
        Lib = Lib[Lib['candidate'] == 'Jo Jorgensen']
        Lib = Lib.loc[:,['candidate','total_votes']]
        Lib['total_votes'] = Lib['total_votes'].sum(axis = 0, skipna = True)
        Lib = Lib.iloc[:1]
        GRN = data[data['state'] == state]
        GRN = GRN[GRN['candidate'] == 'Howie Hawkins']
        GRN = GRN.loc[:,['candidate','total_votes']]
        GRN['total_votes'] = GRN['total_votes'].sum(axis = 0, skipna = True)
        GRN = GRN.iloc[:1]
        WRI = data[data['state'] == state]
        WRI = WRI[WRI['party'] == 'WRI']
        WRI = WRI.loc[:,['candidate','total_votes']]
        WRI['total_votes'] = WRI['total_votes'].sum(axis = 0, skipna = True)
        WRI = WRI.iloc[:1]
        CST = data[data['state'] == state]
        CST = CST[CST['candidate'] == 'Don Blankenship']
        CST = CST.loc[:,['candidate','total_votes']]
        CST['total_votes'] = CST['total_votes'].sum(axis = 0, skipna = True)
        CST = CST.iloc[:1]
        ASP = data[data['state'] == state]
        ASP = ASP[ASP['candidate'] == 'Brian Carroll']
        ASP = ASP.loc[:,['candidate','total_votes']]
        ASP['total_votes'] = ASP['total_votes'].sum(axis = 0, skipna = True)
        ASP = ASP.iloc[:1]
        ALI = data[data['state'] == state]
        ALI = ALI[ALI['candidate'] == 'Rocky De La Fuente']
        ALI = ALI.loc[:,['candidate','total_votes']]
        ALI['total_votes'] = ALI['total_votes'].sum(axis = 0, skipna = True)
        ALI = ALI.iloc[:1]
        SWP = data[data['state'] == state]
        SWP = SWP[SWP['candidate'] == 'Alyson Kennedy']
        SWP = SWP.loc[:,['candidate','total_votes']]
        SWP['total_votes'] = SWP['total_votes'].sum(axis = 0, skipna = True)
        SWP = SWP.iloc[:1]
        APV = data[data['state'] == state]
        APV = APV[APV['candidate'] == 'Gloria La Riva']
        APV = APV.loc[:,['candidate','total_votes']]
        APV['total_votes'] = APV['total_votes'].sum(axis = 0, skipna = True)
        APV = APV.iloc[:1]
        IND = data[data['state'] == state]
        IND = IND[IND['candidate'] == 'Brock Pierce']
        IND = IND.loc[:,['candidate','total_votes']]
        IND['total_votes'] = IND['total_votes'].sum(axis = 0, skipna = True)
        IND = IND.iloc[:1]
        KW = data[data['state'] == state]
        KW = KW[KW['candidate'] == 'Kanye West']
        KW = KW.loc[:,['candidate','total_votes']]
        KW['total_votes'] = KW['total_votes'].sum(axis = 0, skipna = True)
        KW = KW.iloc[:1]
        PRO = data[data['state'] == state]
        PRO = PRO[PRO['candidate'] == 'Phil Collins']
        PRO = PRO.loc[:,['candidate','total_votes']]
        PRO['total_votes'] = PRO['total_votes'].sum(axis = 0, skipna = True)
        PRO = PRO.iloc[:1]
        PSL = data[data['state'] == state]
        PSL = PSL[PSL['candidate'] == 'Blake Huber']
        PSL = PSL.loc[:,['candidate','total_votes']]
        PSL['total_votes'] = PSL['total_votes'].sum(axis = 0, skipna = True)
        PSL = PSL.iloc[:1]
        PRG = data[data['state'] == state]
        PRG = PRG[PRG['candidate'] == 'Dario Hunter']
        PRG = PRG.loc[:,['candidate','total_votes']]
        PRG['total_votes'] = PRG['total_votes'].sum(axis = 0, skipna = True)
        PRG = PRG.iloc[:1]
        SEP = data[data['state'] == state]
        SEP = SEP[SEP['candidate'] == 'Joseph Kishore']
        SEP = SEP.loc[:,['candidate','total_votes']]
        SEP['total_votes'] = SEP['total_votes'].sum(axis = 0, skipna = True)
        SEP = SEP.iloc[:1]
        UNA = data[data['state'] == state]
        UNA = UNA[UNA['candidate'] == 'Joe McHugh']
        UNA = UNA.loc[:,['candidate','total_votes']]
        UNA['total_votes'] = UNA['total_votes'].sum(axis = 0, skipna = True)
        UNA = UNA.iloc[:1]
        UNN = data[data['state'] == state]
        UNN = UNN[UNN['candidate'] == 'Jordan Scott']
        UNN = UNN.loc[:,['candidate','total_votes']]
        UNN['total_votes'] = UNN['total_votes'].sum(axis = 0, skipna = True)
        UNN = UNN.iloc[:1]
        IAP = data[data['state'] == state]
        IAP = IAP[IAP['candidate'] == 'Kyle Kopitke']
        IAP = IAP.loc[:,['candidate','total_votes']]
        IAP['total_votes'] = IAP['total_votes'].sum(axis = 0, skipna = True)
        IAP = IAP.iloc[:1]
        UNP = data[data['state'] == state]
        UNP = UNP[UNP['candidate'] == 'Princess Jacob-Fambro']
        UNP = UNP.loc[:,['candidate','total_votes']]
        UNP['total_votes'] = UNP['total_votes'].sum(axis = 0, skipna = True)
        UNP = UNP.iloc[:1]
        INQ = data[data['state'] == state]
        INQ = INQ[INQ['candidate'] == 'Mark Charles']
        INQ = INQ.loc[:,['candidate','total_votes']]
        INQ['total_votes'] = INQ['total_votes'].sum(axis = 0, skipna = True)
        INQ = INQ.iloc[:1]
        UTY = data[data['state'] == state]
        UTY = UTY[UTY['candidate'] == 'Bill Hammons']
        UTY = UTY.loc[:,['candidate','total_votes']]
        UTY['total_votes'] = UTY['total_votes'].sum(axis = 0, skipna = True)
        UTY = UTY.iloc[:1]
        All = [Dem, Rep, Lib, GRN, WRI, CST, ASP, ALI, SWP, APV, IND, KW, PRO, PSL, PRG, SEP, UNA, UNN, IAP, UNP, INQ, UTY ]
        result = pd.concat(All)
        result.index = result['candidate']
        fig,axs = plt.subplots(figsize=(14,6))
        result.plot.bar(ax=axs, color='Red')
        plt.xlabel('Candidates',fontsize=14)
        plt.ylabel('Number of votes',fontsize=14)
        plt.title(state)
        plt.legend(['Votes'])
        print(result)
        
# if you want to plot all the states at once. PS(that might kill your laptop)
"""
for State in state_names:
    plot_election(State)
"""
