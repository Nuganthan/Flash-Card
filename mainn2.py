import pandas
from tkinter import *
data = pandas.read_csv("french_words.csv")
learn = data.to_dict(orient="records")
print(learn)
window = Tk()
window.after()
window.mainloop()