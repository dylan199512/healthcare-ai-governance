import seaborn as sns
import matplotlib.pyplot as plt

binary_df = df[["data_diverse","human_oversight","explainability","high_risk"]]
binary_df = binary_df.replace({"yes":1, "no":0})

fig, ax = plt.subplots()
sns.heatmap(binary_df, annot=True, cmap="Blues", ax=ax)
st.pyplot(fig)
