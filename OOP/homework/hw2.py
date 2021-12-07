import datetime

def input_date():
        year = int(input('연도를 입력하세요'))
        month = int(input('월을 입력하세요'))
        day = int(input('일을 입력하세요'))
        
        return year, month, day  
     
def is_leap(year):
    if year % 4 == 0:
        if year % 400 ==0:
            return True
        elif year % 100 == 0:
            return False
        else:
            return True
    else:
        return False


class DayName:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
    
    def get_day_name(self):
        dt = datetime.datetime(self.year, self.month, self.day)
        dt = int(dt.strftime('%j'))
        count_day = 0
        for i in range(1, self.year):
            if is_leap(i) == True:
                count_day += 366
            else:
                count_day += 365
        count = (count_day + dt) % 7
    
        return {0:'일요일', 1:'월요일', 2:'화요일', 3:'수요일', 4:'목요일', 5:'금요일', 6:'토요일'}[count]


    
if __name__ == "__main__":
    year, month, day = input_date()
    day_name = DayName(year, month, day)
    print(day_name.get_day_name())
    if is_leap(day_name.year) == True:
         print('입력하신 {}는 윤년입니다'.format(year))