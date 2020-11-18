import math

Bingbong = [39, 40, 40.4, 39.5, 38]


### Input: Liste med målinger
### Output: Standarddavvik
def Standarddavvik(maalinger):

    gjennomsnitt = 0
    for maling in maalinger:
        gjennomsnitt += maling
        #print(gjennomsnitt)

    gjennomsnitt /= len(maalinger)
    #print("Gjennomsnittet er: " + str(gjennomsnitt))

    diff = []
    for maling in maalinger:
        diff.append(gjennomsnitt - maling)
    #print("Differansene fra gjennomsnittet er:" + str(diff))

    diff_srqd = []
    for dif in diff:
        diff_srqd.append(dif**2)
    #print("Roten av alle differansene er: " + str(diff_srqd))

    varianse = 0
    for dif in diff_srqd:
        varianse += dif

    varianse /= len(diff_srqd)
    #print("Variansen er: " + str(varianse))

    stdavvik = math.sqrt(varianse)
    #print("Standarddavviket er: " + str(standarddavvik))

    return stdavvik



print(Standarddavvik(Bingbong))

