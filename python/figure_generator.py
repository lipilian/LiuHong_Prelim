# %% 
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams.update({'font.size': 15})
data = {'Brutal force':1911.45, 'SIMD': 774.524, 'OpenMP': 290.699, 'MPI':75.851, 'CUDA': 65.073}
courses = list(data.keys())
values = list(data.values())
fig = plt.figure()
plt.bar(courses, values,
        width = 0.4)
plt.ylabel('Running time(ms)')
plt.savefig('running_time.png')



# %%
