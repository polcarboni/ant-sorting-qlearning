import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("white")
sns.set_context("talk")

import pynetlogo


netlogo = pynetlogo.NetLogoLink(
    gui=True,
    jvm_path="/Users/jhkwakkel/Downloads/jdk-19.0.2.jdk/Contents/MacOS/libjli.dylib"
    
)


netlogo.load_model("ant-sorting.nlogo")
netlogo.command("setup")
