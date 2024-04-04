def century(year):
    cent = year // 100 + 1 if year % 100 != 0 else year / 100
    return cent