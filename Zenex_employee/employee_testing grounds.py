from zenex_employee import Zenex_manager as zm
from zenex_employee import Zenex_Xmanager as zx
from zenex_employee import Zenex_CEO as CEO
import random
with open('sec.txt') as f:
    sectors = f.read()
sectors = sectors.split(',')

Lear = zx('engineering','rh_kL^&(`;CqQg)WyUv/hVn"WJ]3EB','Navre Jahamas','JahamasPeak')
smallbrain = zx('cleaning','\@D{!i;4/<gqdFQ$-6M$D:Cq+U{17<','All for one','Dumbpoateo')
sneaky = zx('marketing','mO?G.3%+<^toVSbURtS:d*[]7Do,FY','Danielle Milton','TDMSTUD')
bigbrain = zx('science','36tTyhyt[}}C],2wd;T4*f?%0qh|)b','Wenjie Evans','bigbrain123')
fun = zx('animation','Ey$K+M9]97vno-Ua7Cz=$TAFPSI(Wh','Tenko Shigaraki','LOVking22')
Paul = CEO('Paul osei Afriyie','pythonforluv856','animation')


















"""
code for creating a ton of employees
for s in sectors:
    for i in range(100):
        gender = ['Female','Male']
        name = ['Jahmas', 'Belle', 'Stacy','Bob','You','Me','Pomeqm','Ohemaa','Arron','Sad']
        sal = range(15,40)
        race = ['Black','White','Pacific Islander','Asian']
        if s == 'engineering':
            e = ['Electrical engineer', 'Bio engineer', 'Mechanical engineer']
            Lear.create_employee(random.choice(name),random.choice(e),random.choice(race),random.choice(sal),random.choice(gender))
        elif s == 'cleaning':
            e = ['janitor','Mower/Shoveler']
            smallbrain.create_employee(random.choice(name),random.choice(e),random.choice(race),random.choice(sal),random.choice(gender))
        elif s == 'marketing':
            e = ['Actor','Marketer','Social media','Producer']
            sneaky.create_employee(random.choice(name),random.choice(e),random.choice(race),random.choice(sal),random.choice(gender))
        elif s == 'science':
            e = ['Neuroscientist','astronomer','Computer scientist','Chemist']
            bigbrain.create_employee(random.choice(name),random.choice(e),random.choice(race),random.choice(sal),random.choice(gender))
        elif s == 'animation':
            e = ['Background Animator','Action Animator','Sound effects','Animator']
            fun.create_employee(random.choice(name),random.choice(e),random.choice(race),random.choice(sal),random.choice(gender))
"""

"""
code for ppromoting some of them
for s in sectors:
    for i in range(40):
        yes = ['Yes','No']
        yes = random.choice(yes)
        if yes == 'Yes':
            if s == 'engineering':
                r = Lear.get_all_values('ID')
                try:
                    Lear.promote_ID(random.choice(r))
                except Exception:
                    pass
            elif s == 'cleaning':
                r = smallbrain.get_all_values('ID')
                try:
                    smallbrain.promote_ID(random.choice(r))
                except Exception:
                    pass
            elif s == 'marketing':
                r = sneaky.get_all_values('ID')
                try:
                    sneaky.promote_ID(random.choice(r))
                except Exception:
                    pass
            elif s == 'science':
                r = bigbrain.get_all_values('ID')
                try:
                    bigbrain.promote_ID(random.choice(r))
                except Exception:
                    pass
            elif s == 'animation':
                r = fun.get_all_values('ID')
                try:
                    fun.promote_ID(random.choice(r))
                except Exception:
                    pass
    else:
        pass
"""