__author__ = 'Artemko'

# from prettytable import *
# from numpy import *



def func(prof):
    file_profs_skills = "career/profs_skills_all.txt"
    f = open(file_profs_skills, "r")
    data = []

    for line in f:
        data.append(line.split("|"))

    # print [item[1] for item in data[:100]]
    # print data[0][2]

    hr_prof = []
    for item in data:
        if prof in item[2]:
            # print item[3]
            hr_prof.append(item[3])

    skills_hr = []
    for skills in hr_prof:
        skills_hr.append(skills.split(", "))

    # print skills_hr
    new_skills_hr = []

    for skills in skills_hr:
        for skill in skills:
            str = skill.replace(" [", "").replace("'", "").replace("]\n", "").replace("...", "")
            new_skills_hr.append(str)

    skills_list = list(set(new_skills_hr))
    # print len(skills_list)
    # print skills_list

    skills_dict = {}
    for skill in skills_list:
        counter = 0
        for s in new_skills_hr:
            if skill == s:
                counter += 1
        skills_dict[skill] = counter

    # print sorted(skills_dict.items(), key=lambda x: x[1])
    # print sorted([item for item in skills_dict.items() if item[1] > 7], key=lambda x: x[1])
    hr_list = [item[0] for item in sorted([item for item in skills_dict.items()], key=lambda x: x[1], reverse=True)[:10]]
    f.close()
    return hr_list


# pretty_table = PrettyTable(["Skills", "#"])
# for item in hr_list:
#     pretty_table.add_row(item)
# pretty_table.sortby = "#"
# pretty_table.reversesort = True
# print pretty_table
# plt.scatter(hr_list.keys(), hr_list.values())
# plt.ticklabel_format(useOffset=False)




# print skills_hr[0]
# print skills_hr


