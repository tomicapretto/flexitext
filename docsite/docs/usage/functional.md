**WIP**


```python
import matplotlib as mpl
import matplotlib.pyplot as plt

from flexitext import flexitext

mpl.rcParams["figure.figsize"] = (9, 6)
```


```python
colors = ["#ff5c67", "#fe7974", "#ffb382", "#c5e099", "#64a5ff"]
```


```python
fig, ax = plt.subplots()

flexitext(
    0.05, 0.9, 
    "<size:24, color:#ff5c67>Mix <weight:bold>bold</> and <weight:light>light</></>"
)

flexitext(
    0.05, 0.8, 
    "<size:22>Highlight <weight:bold, color:#64a5ff>information</></>"
)


text = (
    "<size:22, name:Lato>Use breaklines\n"
    + "and make text\n<size:36>BIGGER</>\n"
    + "<size:12>and also smaller</></>"
)

flexitext(
    0.5, 0.5, 
    text,
    ha="center",
    ma="center"
)

text = (
    "<size:28, name:Lobster Two>Pull text to a <color:#c5e099, weight:bold, name:Special Elite>corner</></>"
)

flexitext(
    1, 0, 
    text,
    ha="right",
    va="bottom"
);
```


    
![png](functional_files/functional_3_0.png)
    



```python
fig, ax = plt.subplots()
fig.subplots_adjust(top=0.8)

flexitext(0, 1, "<size:28><color:red>Axes</> fraction</>", va="top");

flexitext(
    0.9, 0.82, 
    "<size:28><color:red>Figure</> fraction</>", 
    va="bottom", ha="right", 
    xycoords="figure fraction"
);

flexitext(
    0.9, 0.05, 
    "Usefool for <style:italic, weight:bold>captions</>", 
    ha="right", 
    xycoords="figure fraction"
);

flexitext(
    0.5, 0.6, 
    "<size:36>Some <alpha:0.3>transparency</></>",
    ha="center"
);

flexitext(
    0.5, 0.4, 
    "<size:36>And <family:monospace, color:red>monospace</> too</>",
    ha="center"
);
```


    
![png](functional_files/functional_4_0.png)
    

