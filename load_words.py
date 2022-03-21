import syllables
import pandas as pd

words_df = pd.read_csv('words.csv')

# Count syllables in each word

# i = 0
# num_syll = len(words_df)*[0]
# for x in words_df['word']:
#     num_syll[i] = syllables.estimate(x)
#     i = i+1;
# words_df['syll'] = num_syll
# words_df.to_csv('words.csv')

# Split string of parts of speech into list of parts

i = 0
pos_list = len(words_df)*[0]
for x in words_df['pos']:
    pos_list[i] = words_df['pos'][i].split(",")
    i = i+1
words_df['pos_list'] = pos_list

# Check that it actually split into list

# for x in words_df['pos_list'][1524]:
#     print(x)