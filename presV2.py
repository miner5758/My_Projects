import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv(r"C:\Users\paula\Downloads\president_county_candidate.csv")
state_names = ["Alabama","Alaska","Arizona","Arkansas","California","Colorado",
  "Connecticut","Delaware","Florida","Georgia","Hawaii","Idaho","Illinois",
  "Indiana","Iowa","Kansas","Kentucky","Louisiana","Maine","Maryland",
  "Massachusetts","Michigan","Minnesota","Mississippi","Missouri","Montana",
  "Nebraska","Nevada","New Hampshire","New Jersey","New Mexico","New York",
  "North Carolina","North Dakota","Ohio","Oklahoma","Oregon","Pennsylvania",
  "Rhode Island","South Carolina","South Dakota","Tennessee","Texas","Utah",
  "Vermont","Virginia","Washington","West Virginia","Wisconsin","Wyoming","District of Columbia"]
def plot_election(state):
    if state == 'Choices' or state == 'choices':
        print(state_names)
    else:
        result = data[data['state'] == state]
        result = result.groupby(['candidate']).sum()
        result = result[['total_votes']]
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