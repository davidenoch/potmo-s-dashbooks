import matplotlib.pyplot as plt
import seaborn as sns
# %matplotlib inline

plt.style.use("ggplot");
"""  available styles: ['Solarize_Light2', '_classic_test_patch', 'bmh', 'classic', 
'dark_background', 'fast', 'fivethirtyeight', 'ggplot', 'grayscale',
'seaborn', 'seaborn-bright','seaborn-colorblind', 'seaborn-dark',
'seaborn-dark-palette', 'seaborn-darkgrid', 'seaborn-deep','seaborn-muted',
'seaborn-notebook', 'seaborn-paper', 'seaborn-pastel', 'seaborn-poster', 
'seaborn-talk', 'seaborn-ticks', 'seaborn-white', 'seaborn-whitegrid', 
'tableau-colorblind10'] """

sns.set_context('poster'); # 'paper', 'notebook','talk', 'poster']

colorbrewer_palettes = ['Set1','Set2','Set3','Accent', 'Paired','Pastel1','Pastel2' ,'Pastel3', 'Dark2']
for pal in colorbrewer_palettes:
    sns.palplot(pal=sns.color_palette(pal))
    plt.title(pal,loc='left')
