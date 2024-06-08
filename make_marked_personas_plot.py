import matplotlib.pyplot as plt

# Data for plotting
data = {
    'subplot1': {'words': ['fam', 'yall', 'yo', 'man', 'ya', 'aint', 'gotta', 'hustle', 'em',
 'soul', 'og', 'bbq', 'soulful', 'doin', 'football', 'nfl'],
'values': [4.932, 4.701, 3.029, 3.15, 3.60, 3.85, 2.9593482319462807, 2.7052452929109716, 2.3326114333847165, 3.069486706163987, 2.36779936597953, 2.7722146224468105, 2.9220179147489342, 2.766710109832499, 2.551982329174039, 2.4864237395010043]},
    'subplot2': {'words': ['charming', 'queen', 'smiling', 'influencer', 'single', 'man', 'bulls', 'bears', 'cubs', 'sox'],
'values': [1.989089861006916, 3.8293280797432434, 3.2143924980259846, 3.6887586802002716,
1.977019449074289, -3.584, -2.853, -2.853, -2.822, -2.822]}
}

print("Length of words: ", len(data['subplot1']['words']))
print("Length of values: ", len(data['subplot1']['values']))

# Create a figure and a set of subplots
fig, axs = plt.subplots(1, 2, figsize=(12, 6))

colors = ['#88CCEE', '#44AA99', '#117733', '#999933', '#DDCC77',
          '#CC6677', '#882255', '#AA4499']
# Plotting for the first subplot
axs[0].bar(data['subplot1']['words'], data['subplot1']['values'], color=colors, edgecolor='black')
axs[0].set_title('Marked: Black, Unmarked: White')
axs[0].set_ylabel('Statistical Value')

labels = axs[0].get_xticklabels()

axs[0].set_xticklabels(labels, rotation=45)

#axs[0].set_ylim(5, 2.2)

# Plotting for the second subplot
axs[1].bar(data['subplot2']['words'], data['subplot2']['values'], color=colors, edgecolor='black')
axs[1].set_title('Marked: Female, Unmarked: Male')
axs[1].set_ylabel('Statistical Value')
#axs[0].set_xticklabels(rotation=45)

labels = axs[1].get_xticklabels()
axs[1].set_xticklabels(labels, rotation=45)
#axs[1].set_ylim(2.0, 4)

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.savefig('marked_personas_plot.png')
