    
import os
import datetime
date = datetime.datetime.now()
level = 4
with open('SCORE_RECORDS_CLICK.txt') as s:
    records = open('SCORE_RECORDS_CLICK.txt','a')
    records.write(str(12)) #score
    records.write(' clicks on ')
    records.write(str(level)) # creating the score records line-by-line, level mode
    records.write(' difficulty ')
    records.write(date.strftime('%Y/%m/%d %H:%M')) #time records was made
    records.write('\n')
    records.close()