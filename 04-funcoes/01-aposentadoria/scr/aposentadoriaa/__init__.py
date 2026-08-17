import datetime

def calculateyr(yearbirth):

    hoje = datetime.date.today()

    age = hoje.year - yearbirth

    return age

def retirementageBR(hireyr, yearbirt,):
    min_ageBR = 65
    min_contribution = 20

    age_in_hireyear = hireyr - yearbirt
    year_for_contribution = age_in_hireyear + min_contribution

    return max(min_ageBR , year_for_contribution)
