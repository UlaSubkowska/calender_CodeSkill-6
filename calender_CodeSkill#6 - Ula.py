#do godzin "jednocyfrowych" dodane 0 z przodu, żeby indeksowanie było takie same

def calender (current_calender, new_event):
    answers=[]
    for i in range(len(current_calender)):
        if current_calender[i][:10]==new_event[:10]:
            current_start=int(current_calender[i][14:16])
            current_end= int(current_calender[i][23:25])
            start=int(new_event[14:16])
            end=int(new_event[23:25])

            if current_start==start or current_end==end:
                current_minute_start = int(current_calender[i][17:19])
                current_minute_end = int(current_calender[i][26:28])
                minute_start = int(new_event[17:19])
                minute_end = int(new_event[26:28])

                if current_minute_start<=minute_start<=current_minute_end or current_minute_start<=minute_end<=current_minute_end:
                    answers.append(False)
                elif current_minute_end<minute_start or current_minute_start>minute_end:
                    answers.append(True)

            elif current_start<start<=current_end or current_start<=end<current_end: answers.append(False)   #początek, albo koniec wydarzenia nowego zawiera się pomiedzy początkiem a koncem wydarzenia z kalendarza
            elif start<current_start<end or start<current_end<end: answers.append(False)    #początek, albo koniec wydarzenia z kalendarza zawiera sie pomiedzy początkiem a koncem nowego wydarzenia
            elif current_end<start or current_start>end: answers.append(True) #żeby zaczeło się po, lub przed
        else: answers.append(True)

    if False in answers: answer='false'
    else: answer='true'
    return answer

current_calender=['2016-01-01 od 08:00 do 09:00 - śniadanie',
                  '2016-01-01 od 13:20 do 13:40 - jogging',
                  '2016-01-01 od 18:00 do 22:00 - CodeSkill#6']

print(calender(current_calender,'2016-01-01 od 13:00 do 13:35'))
