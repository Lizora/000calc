def calc(_10000, _5000, _1000, _500, _100, _50, _10, _5, _1, flag):

    if _10000 == 31:
        return "アイス"

    res = {1:0, 5:0, 10:0, 50:0, 100:0, 500:0, 1000:0, 5000:0}
    before = {1000:0, 5000:0, 10000:0}
    cnt = 0

    need10 = 210 if flag else 195
    need50 = 80 if flag else 75
    need100 = 182 if flag else 172
    need500 = 41 if flag else 36
    need1000 = 42 if flag else 34
    need5000 = 10 if flag else 9

    if _1 <= 15 or _5 <= 10:
        res[1] = 1
        res[5] = 1
        res[100] = 2 
        need100 -= 2
        cnt += 500

    while _10 < need10:
        res[10] += 1
        need10 -= 50
        cnt += 500
    
    while _50 < need50:
        res[50] += 1
        need50 -= 50
        cnt += 2500
    
    while _100 < need100:
        res[100] += 5
        need100 -= 5
        cnt += 500
    
    need_5_100 = 10 - ((res[100] % 50) // 5)

    if _500 < need500:
        d = need500 - _500
        res[500] += d
        cnt += 500 * d
    
    if _1000 < need1000:
        d = need1000 - _1000
        res[1000] += d
        cnt += 1000 * d
    
    if _5000 < need5000:
        d = need5000 - _5000
        res[5000] += d
        cnt += 5000 * d

    if cnt == 0:
        return "両替不要"
    
    if cnt <= _10000 * 10000:   #上手くいきそうなとき
        use = min((cnt-1) // 10000 + 2, _10000) #使う１万円の枚数
        d = use * 10000 - cnt
        before[10000] = use
        while d > 0:

            if 0 < need_5_100 <= 3 and d >= 500 * need_5_100:
                res[100] += 5 * need_5_100
                d -= 500 * need_5_100
                need_5_100 = 0
                continue

            elif d >= 10000:
                res[5000] += 1
                res[1000] += 4
                res[500] += 2
                d -= 10000
                continue

            elif d >= 6500 and res[5000] + _5000 <= need5000 + 1:
                res[5000] += 1
                d -= 5000
                continue

            elif d >= 5000:
                res[1000] += 3
                res[500] += 3
                d -= 4500
                continue

            elif d >= 1000:
                if res[500] + _500 <= need500 + 2:
                    res[500] += 1
                    d -= 500
                else:
                    res[1000] += 1
                    d -= 1000
                continue
                
            else:
                res[500] += 1
                d -= 500
        
    else:
        prepare = 10000 * _10000
        before[10000] = _10000

        while prepare < cnt:

            if _5000 > need5000:
                before[5000] += 1
                prepare += 5000
                _5000 -= 1
                continue

            elif _1000 > need1000:
                before[1000] += 1
                prepare += 1000
                _1000 -= 1
                continue

            else:
                return "お手上げ"
        
        d = prepare - cnt

        while d > 0:
            if d >= 1000:
                res[1000] += 1
                d -= 1000
                continue
                
            else:
                res[500] += 1
                d -= 500
    
    res_str = "【両替前】\n"

    if before[10000] > 0:
        res_str += f"10000円 : {before[10000]}枚\n"
    if before[5000] > 0:
        res_str += f" 5000円 : {before[5000]}枚\n"
    if before[1000] > 0:
        res_str += f" 1000円 : {before[1000]}枚\n"
    
    res_str += "\n【両替後】\n"
    
    if res[5000] > 0:
        res_str += f" 5000円 : {res[5000]}枚\n"
    if res[1000] > 0:
        res_str += f" 1000円 : {res[1000]}枚\n"
    if res[500] > 0:
        res_str += f"  500円 : {res[500]}枚\n"
    if res[100] > 0:
        if res[100] // 50 > 0:
            res_str += f"  100円 : {res[100] // 50}本"
            if res[100] % 50 > 0:
                res_str += f" + {res[100] % 50}枚"
        else:
            if res[100] > 0:
                res_str += f"  100円 : {res[100]}枚"
        res_str += "\n"
    if res[50] > 0:
        res_str += f"   50円 : {res[50]}本\n"
    if res[10] > 0:
        res_str += f"   10円 : {res[10]}本\n"
    if res[5] > 0: #この時、res[1]も1
        res_str += f"    5円 : 1本\n    1円 : 1本\n"
    
    return res_str


        


    


    
    
    

    

