import cl_information as ci
import search_information as si

states = ci.States
state_list = si.SelectionKeys.state_keys

tot_list = []
tot_crushed = []
area_list = []
area_crushed = []

for i in state_list:
    item = eval(f'states.{i}')
    if 'focus_dist' not in item:
        tot_list.append([k for k,v in item.items()])
    else:
        tot_list.append([k for k,v in item.items()])
        area_list.append([v for k,v in item['focus_dist'].items()])
for i in tot_list:
    tot_crushed.extend(i)

for i in area_list:
    for j in i:
        area_crushed.extend(j)

tot_crushed.extend(area_crushed)
tot_set = set(tot_crushed)
tot_set.remove('focus_dist')

print(len(tot_set))


