import pandas as pd 
import pickle 
import matplotlib.pyplot as plt 

# import stereotype lexicon
file = open("data/stereo_dict.pkl",'rb')
e_s_d = pickle.load(file)

df = pd.read_csv('data/all_mitigation_warning.csv')
#df = pd.read_csv('data/all_mitigation.csv')
#df = df[df['mitigation'] == 'warning']

df['text_clean'] = df['text'].str.lower().str.replace('[^\w\s]','',regex=True)

eth_counts = dict()

#plt.rcParams["figure.figsize"] = (12,16)
#fontsizeval=35

df.dropna(inplace=True)

word_counts_per_ethnic_group = {}

for ethnic, stereolist in e_s_d['person'].items():
    eth_counts[ethnic] = []
    word_counts_per_ethnic_group[ethnic] = {}

    for i,ro in df.iterrows():
        if (ro['text'] != ro['text']):
            continue
        count = 0
        for word in stereolist:
#            print("row cleaned text: ", ro['text_clean'], ro['text'])
            count += ro['text_clean'].count(word)

            if (ro['text_clean'].count(word) > 0):
                if (word not in word_counts_per_ethnic_group[ethnic]):
                    word_counts_per_ethnic_group[ethnic][word] = 0
                word_counts_per_ethnic_group[ethnic][word] += 1

        count /= len(ro['text_clean'].split(' '))
        eth_counts[ethnic].append(count)

print("Word counts per ethnic group: ", word_counts_per_ethnic_group)
for k, v in eth_counts.items():
    df[k] = v

df.to_csv('stereotype_lexicon_annotated.csv')

races = ['Black', 'Latino', 'Middle-Eastern', 'White', 'Asian']

columns_needed = ['model', 'Black', 'Latino', 'Middle-Eastern', 'White', 'Asian']
df = df[columns_needed]

grouped_df = df.groupby('model').agg(['mean', 'std']).reset_index()

fig, ax = plt.subplots()

# List of races
races = ['Black', 'White']

# Bar positions and width
total_width = 0.6
individual_width = total_width / len(races)
indexes = range(len(grouped_df['model']))

colors = ['#66CCEE', '#228833']

print("grouped df: ", grouped_df)

# Plotting each race with error bars
for i, race in enumerate(races):
    means = grouped_df[(race, 'mean')]
    stds = grouped_df[(race, 'std')]

    print("means ", means)
    print("stds ", stds)
    ax.bar([index + i * individual_width for index in indexes],
           means,
#           yerr=stds,
           color = colors[i],
            edgecolor='black',  # Setting the outline color
           width=individual_width,
           capsize=5,
           label=race)

# Adjusting the x-axis labels
ax.set_xticks([index + total_width / 2 - individual_width / 2 for index in indexes])
ax.set_xticklabels(grouped_df['model'])

# Adding labels and title
ax.set_xlabel('Model')
ax.set_ylabel('Percentage')
ax.set_title('Percentage of Stereotype Words for Each Model')

# Adding a legend
ax.legend()

plt.ylim(0, 0.0010)

# Show the plot
plt.savefig('stereotype_lexicon_warning.png')