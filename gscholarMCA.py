import prince
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('MCA_df.csv')
mca = prince.MCA(df, n_components=-1)

mca.plot_rows(show_points=True, show_labels=False, color_by='2014', ellipse_fill=True)



plt.show()
