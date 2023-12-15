# -*- coding: utf-8 -*-
import pandas as pd

from plotnine import *

surveydf = pd.read_csv("/Users/jujjino/Documents/GitHub/ARDAResearch/ResearchPaper/Data analysis/Data.csv")
surveydf.drop('Timestamp',inplace = True, axis=1) #Delete timestamp column because useless

#Chart that display the count of programming years of experience

chart = ggplot(surveydf, aes(x='programming_years')) + \
geom_histogram(binwidth=0.5, fill="#69b3a2",
color="#e9ecef", alpha=0.9)+ \
labs(title = "Programming years of IT students", x="Programming years")

print(chart)

#Chart that display the count of git years of experience

chart2 = ggplot(surveydf, aes(x='git_years')) + \
geom_histogram(binwidth=0.5, fill="#69b3a2",
color="#e9ecef", alpha=0.9)+ \
labs(title = "GIT years of experience of IT students", x="Git years of experience")

print(chart2)

#Chart of interface preferred by IT students

chart3 = ggplot(surveydf, aes(x='primarily_interface')) + \
geom_histogram(binwidth=0.5, fill="#69b3a2",
color="#e9ecef", alpha=0.9)+ \
labs(title = "Interface preferred by IT students", x="")

print(chart3)

#Chart of reasons why users choose GUI

surveydfGUI = surveydf.query("primarily_interface == 'Graphical User Interface (ex. Github Desktop)'")

surveydfGUI['reason'] = surveydfGUI['reason'].str.split(', ')

reasonDfGUI = pd.DataFrame(surveydfGUI['reason'].explode())

chart4 = ggplot(reasonDfGUI, aes(x='reason', fill='reasons')) + \
    geom_bar(fill='#008000') +\
    labs(title="Reasons why users use the GUI interface",
         x="Reason",
         y="Count") +\
        scale_x_discrete(labels=["Faster", "Complex Tasks", "Efficient", "More functionalities", "User friendly","Visual Appealing"])

print(chart4)


#Chart of reasons why users choose CLI

surveydfCLI = surveydf.query("primarily_interface == 'Command Line Interface (CLI)'")

surveydfCLI['reason'] = surveydfCLI['reason'].str.split(', ')

reasonDfCLI = pd.DataFrame(surveydfCLI['reason'].explode())

chart5 = ggplot(reasonDfCLI, aes(x='reason', fill='reasons')) + \
    geom_bar(fill='#008000') +\
    labs(title="Reasons why users use the CLI interface",
         x="Reason",
         y="Count") +\
        scale_x_discrete(labels=["Faster", "Complex Tasks", "Efficient", "More functionalities", "Visual Appealing"])

print(chart5)

#Chart to display if operating systems influence the coice of interface

surveydfFilterOS = surveydf.query("os == 'Mac' | os == 'Linux' | os == 'Windows' ")

chart6=ggplot(surveydfFilterOS, aes(x='os', fill='primarily_interface')) + \
    geom_bar(position='dodge')+ \
    labs(title="Operating System vs Preferred Interface",
         x="Operating System",
         y="Count",
         fill="Preferred Interface")

print(chart6)

#Chart to display average minutes per hour spent on git based on interface

chart7 = ggplot(surveydf, aes(x='primarily_interface', fill='average_time')) + \
    geom_bar(position='dodge')+ \
    labs(title="Minutes per Hours spent on Git",
         x="Current Interface",
         y="Amount of people",
         fill="Time spent on Git")+\
         scale_x_discrete(labels=["CLI", "GUI"])
    
print(chart7)

#Chart to display if years of git usage influence interface

chart8 = ggplot(surveydf, aes(x='primarily_interface', fill='git_years')) + \
    geom_bar(position='dodge')+ \
    labs(title="Years of Git usage and current interface",
         x="Current Interface",
         y="Amount of people",
         fill="Years of  Git usage")+\
         scale_x_discrete(labels=["CLI", "GUI"])
    
print(chart8)

#Chart to display if people that use CLI ever considered to switch interface

chart9 = ggplot(surveydfCLI, aes(x='switching', fill='factor(switching)')) + \
    geom_histogram(binwidth=1, color="#e9ecef", alpha=0.9) + \
    labs(title="Wanting to switch from command line to GUI", x="", fill = "Answer")+\
    scale_fill_manual(values=['#e15759', '#69b3a2'])

print(chart9)

#Chart to display if people that use CLI ever considered to switch interface

chart10 = ggplot(surveydfGUI, aes(x='switching', fill='factor(switching)')) + \
    geom_histogram(binwidth=1, color="#e9ecef", alpha=0.9) + \
    labs(title="Wanting to switch from GUI to CLI", x="", fill = "Answer")+\
    scale_fill_manual(values=['#e15759', '#69b3a2'])

print(chart10)

#Chart to display if people that considered switching think they will be faster

surveydfSwitch = surveydf[(surveydf['switching'] == 'Yes') & (surveydf['speed_switch'].notna()) & (surveydf['efficient_switch'].notna())]

chart11 = ggplot(surveydfSwitch, aes(x='efficient_switch', fill=('factor(efficient_switch)'))) + \
    geom_histogram(binwidth=0.5, color="#e9ecef", alpha=0.9) + \
    labs(title="Do people who want to switch think they will be more efficient?", x="", fill="")

print(chart11)


#Chart to display if people that considered switching think they will be faster

chart12 = ggplot(surveydfSwitch, aes(x='speed_switch', fill=('factor(speed_switch)'))) + \
    geom_histogram(binwidth=1, color="#e9ecef", alpha=0.9) + \
    labs(title="Do people who want to switch think they will be faster?", x="", fill="")+\
    scale_fill_manual(values=['#e15759', '#69b3a2'])

print(chart12)

#Chart to display wheter people that didnt switch think they are using the faster method

surveydfNoSwitch = surveydf[(surveydf['switching'] == 'No') & (surveydf['speed_noswitch'].notna()) & (surveydf['efficient_noswitch'].notna())]

chart13 = ggplot(surveydfNoSwitch, aes(x='speed_noswitch', fill=('factor(speed_noswitch)'))) + \
    geom_histogram(binwidth=1, color="#e9ecef", alpha=0.9) + \
    labs(title="Do people that didn't switch think they are using the faster method?", x="", fill="")+\
    scale_fill_manual(values=['#e15759', '#69b3a2'])

print(chart13)

#Chart to display wheter people that didnt switch think they are using the most efficient method

chart14 = ggplot(surveydfNoSwitch, aes(x='efficient_noswitch', fill=('factor(efficient_noswitch)'))) + \
    geom_histogram(binwidth=1, color="#e9ecef", alpha=0.9) + \
    labs(title="Do people that didn't switch think they are using the most efficient method?", x="", fill="")+\
    scale_fill_manual(values=['#e15759', '#69b3a2'])

print(chart14)

#Chart to display which words are associated to CLI according to CLI users

surveydfCLI['words_cli'] = surveydfCLI['words_cli'].str.split(', ')

wordDfCLICLI = pd.DataFrame(surveydfCLI['words_cli'].explode())

chart15 = ggplot(wordDfCLICLI, aes(x='words_cli', fill='words_cli')) + \
    geom_bar(fill='#008000') +\
    labs(title="Words associated to CLI according to CLI users",
         x="Words",
         y="Count")
    
print(chart15)

#Chart to display which words are associated to GUI according to CLI users

surveydfCLI['words_gui'] = surveydfCLI['words_gui'].str.split(', ')

wordDfGUICLI = pd.DataFrame(surveydfCLI['words_gui'].explode())

chart16 = ggplot(wordDfGUICLI, aes(x='words_gui', fill='words_gui')) + \
    geom_bar(fill='#008000') +\
    labs(title="Words associated to GUI according to CLI users",
         x="Words",
         y="Count")
    
print(chart16)

#Chart to display which words are associated to CLI according to GUI users

surveydfGUI['words_cli'] = surveydfGUI['words_cli'].str.split(', ')

wordDfCLIGUI = pd.DataFrame(surveydfGUI['words_cli'].explode())

chart17 = ggplot(wordDfCLIGUI, aes(x='words_cli', fill='words_cli')) + \
    geom_bar(fill='#008000') +\
    labs(title="Words associated to CLI according to GUI users",
         x="Words",
         y="Count")
    
print(chart17)

#Chart to display which words are associated to GUI according to GUI users

surveydfGUI['words_gui'] = surveydfGUI['words_gui'].str.split(', ')

wordDfGUIGUI = pd.DataFrame(surveydfGUI['words_gui'].explode())

chart18 = ggplot(wordDfGUIGUI, aes(x='words_gui', fill='words_gui')) + \
    geom_bar(fill='#008000') +\
    labs(title="Words associated to GUI according to GUI users",
         x="Words",
         y="Count")
    
print(chart18)


#EXPERIMENT PLOTS#



experimentdf = pd.read_csv("/Users/jujjino/Documents/GitHub/ARDAResearch/ResearchPaper/Data analysis/Experiment.csv")

#Chart that displays which are the average times for the experiment from gui and cli

averageCLI = experimentdf['time_CLI'].mean()

averageGUI = experimentdf['time_GUI'].mean()

avg_times_df = pd.DataFrame({'Interface': ['CLI', 'GUI'], 'Average Time': [averageCLI, averageGUI]})

chart19 = ggplot(avg_times_df, aes(x='Interface', y='Average Time', fill='Interface')) + \
    geom_bar(stat='identity') + \
    labs(title='Average Time for experiment completion CLI and GUI', y='Time')+\
    scale_fill_manual(values=['#e15759', '#69b3a2'])

print(chart19)

#Chart that displays all the results of the CLI experiment

chart20 = ggplot(experimentdf, aes(x='factor(candidate)', y='Cli_original')) + \
    geom_bar(stat='identity', fill='#69b3a2', position='dodge') + \
    labs(title='Time of CLI completion for Each Candidate', x='Candidate Number', y='Time (minutes)')
    
print(chart20)

#Chart that displays all the results of the CLI experiment

chart21 = ggplot(experimentdf, aes(x='factor(candidate)', y='GUI_original')) + \
    geom_bar(stat='identity', fill='#69b3a2', position='dodge') + \
    labs(title='Time of GUI completion for Each Candidate', x='Candidate Number', y='Time (minutes)')
    
print(chart21)







