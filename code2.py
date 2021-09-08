import plotly.figure_factory as ff
import plotly.graph_objects as go 
import statistics as st
import random as rd
import pandas as pd
import csv

df = pd.read_csv("School2.csv")
data = df["Math_score"].tolist()
mean = st.mean(data)
std = st.stdev(data)
print("mean: ", mean)
print("standard deviation: ", std)

def random_mean(counter):
    dataset = []

    for i in range(0,counter):
        random_index = rd.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = st.mean(dataset)
    return mean

mean_list = []
for i in range(0, 1000):
    set_mean = random_mean(100)
    mean_list.append(set_mean)

mean_sample = st.mean(mean_list)
std_sample = st.stdev(mean_list)
print("mean: ", mean_sample)

first_std_start, first_std_end = mean_sample- std_sample, mean_sample + std_sample
second_std_start, second_std_end = mean_sample- (2*std_sample), mean_sample + (2*std_sample)
third_std_start, third_std_end = mean_sample- (3*std_sample), mean_sample + (3*std_sample)

#fig = ff.create_distplot([mean_list], ["Student Marks"], show_hist= False)
#fig.add_trace(go.Scatter(x = [mean, mean], y = [0,0.17], mode = "lines", name = "Mean"))
#fig.add_trace(go.Scatter(x = [first_std_start, first_std_start], y = [0,0.17], mode = "lines", name = "First std start"))
#fig.add_trace(go.Scatter(x = [first_std_end, first_std_end], y = [0,0.17], mode = "lines", name = "First std end"))
#fig.add_trace(go.Scatter(x = [second_std_start, second_std_start], y = [0,0.17], mode = "lines", name = "second std start"))
#fig.add_trace(go.Scatter(x = [second_std_end, second_std_end], y = [0,0.17], mode = "lines", name = "second std end"))
#fig.add_trace(go.Scatter(x = [third_std_start, third_std_start], y = [0,0.17], mode = "lines", name = "third std start"))
#fig.add_trace(go.Scatter(x = [third_std_end, third_std_end], y = [0,0.17], mode = "lines", name = "third std end"))

#fig.show()

df = pd.read_csv("School_1_Sample.csv")
data = df["Math_score"].tolist()
mean_of_sample_one = st.mean(data)
print("Mean of kids who got Ipads: ", mean_of_sample_one)
fig = ff.create_distplot([mean_list], ["Student Marks"], show_hist= False)
fig.add_trace(go.Scatter(x = [mean, mean], y = [0,0.17], mode = "lines", name = "Mean"))
fig.add_trace(go.Scatter(x = [mean_of_sample_one, mean_of_sample_one], y = [0,0.17], mode = "lines", name = "Mean of sample one"))
fig.add_trace(go.Scatter(x = [first_std_end, first_std_end], y = [0,0.17], mode = "lines", name = "First std end"))
fig.show()

df = pd.read_csv("School_2_Sample.csv")
data = df["Math_score"].tolist()
mean_of_sample_two = st.mean(data)
print("Mean of kids who got extra classes: ", mean_of_sample_two)
fig = ff.create_distplot([mean_list], ["Student Marks"], show_hist= False)
fig.add_trace(go.Scatter(x = [mean, mean], y = [0,0.17], mode = "lines", name = "Mean"))
fig.add_trace(go.Scatter(x = [mean_of_sample_two, mean_of_sample_two], y = [0,0.17], mode = "lines", name = "Mean of sample two"))
fig.add_trace(go.Scatter(x = [first_std_end, first_std_end], y = [0,0.17], mode = "lines", name = "First std end"))
fig.add_trace(go.Scatter(x = [second_std_end, second_std_end], y = [0,0.17], mode = "lines", name = "second std end"))
fig.show()

df = pd.read_csv("School_3_Sample.csv")
data = df["Math_score"].tolist()
mean_of_sample_3 = st.mean(data)
print("Mean of kids who got extra worksheets: ", mean_of_sample_3)
fig = ff.create_distplot([mean_list], ["Student Marks"], show_hist= False)
fig.add_trace(go.Scatter(x = [mean, mean], y = [0,0.17], mode = "lines", name = "Mean"))
fig.add_trace(go.Scatter(x = [mean_of_sample_3, mean_of_sample_3], y = [0,0.17], mode = "lines", name = "Mean of sample three"))
fig.add_trace(go.Scatter(x = [first_std_end, first_std_end], y = [0,0.17], mode = "lines", name = "First std end"))
fig.add_trace(go.Scatter(x = [second_std_end, second_std_end], y = [0,0.17], mode = "lines", name = "second std end"))
fig.add_trace(go.Scatter(x = [third_std_end, third_std_end], y = [0,0.17], mode = "lines", name = "third std end"))
fig.show()

z_score = (mean_of_sample_one - mean)/std_deviation
