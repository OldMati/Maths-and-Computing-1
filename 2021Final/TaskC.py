# 02730341

import matplotlib.pyplot as plt

no_first_dose = 0
no_second_dose = 0
# day, number
max_vacc = (0, 0)
pfizer_total = 0
astra_total = 0
first_dose_per_day = []
second_dose_per_day = []


with open('2021Final/Vax.txt', 'r') as f:
    data = f.readlines()
    for i in range(0, len(data), 5):
        first_dose = int(data[i + 1]) + int(data[i + 2])
        second_dose = int(data[i + 3]) + int(data[i + 4])

        first_dose_per_day.append(first_dose)
        second_dose_per_day.append(second_dose)

        no_first_dose += first_dose
        no_second_dose += second_dose

        total = first_dose + second_dose

        if total > max_vacc[1]:
            max_vacc = (i // 5 + 1, total)
        
        pfizer_total += int(data[i + 1]) + int(data[i + 3])
        astra_total += int(data[i + 2]) + int(data[i + 4])
        
print('The overall number of first dose vaccinations inoculated in the given period: ', no_first_dose)
print('The overall number of second dose vaccinations inoculated in the given period: ', no_second_dose)
print('The day with the largest overall number of vaccinations: ', max_vacc[0])
print(f'The overall number of vaccinations done with Pfizer: {pfizer_total}, and those with AstraZeneca: {astra_total}')

fig, ax = plt.subplots(2, 1)

days = [i + 1 for i in range(len(first_dose_per_day))]

ax[0].plot(days, first_dose_per_day)
ax[1].plot(days, second_dose_per_day)

plt.show()