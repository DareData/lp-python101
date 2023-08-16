In this assignment, we switched the order of the script and jupyter notebook because we will need to do the script before doing the notebook


# Script

Create a script `auto.py` with three functions, a `load_auto` function that loads the `auto-mpg.csv` [auto-mpg dataset](https://archive.ics.uci.edu/ml/datasets/auto+mpg). Then, a function `clean_auto` that splits the `car name` into new `brand` and `model` columns since then we would like to have a third `create_report` function that prints the following info:
- What is the average miles per galon?
- Are there any missing values?
- Do we have repeated car names?
- How many Fords, Dodges and VWs we have?

# Jupyter notebook

Can you replicate the plots below using the `auto` DataFrame? You can plot them one by one, but pay attention to the titles.
<p float='left'>
    <img src=media/exercise-mpg_per_year.png width="300" />
    <img src=media/exercise-models_per_cylinders.png width="300" />
    <img src=media/exercise-weight_acceleration.png width="300" />
</p>

Tip: you can copy-paste (boring!!) the functions that you will create for the script OR you can import the functions FROM the script (feels-like-hacking!)
