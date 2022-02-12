from datetime import date, timedelta

def tag_def(arr):
    for i in arr:
        if i[0:2] == 'ID':
            return i[3:]

def t_convert(s): 
    s = s %(24*3600)
    h= s//3600
    s %= 3600
    m= s//60
    s%=60
    return "%d:%02d:%02d" % (h,m,s)

def k_value(num):
    if num==0:
        return '2D GPS'
    if num==1:
        return '3D GPS'
    if num==2:
        return '2D DGPS'
    if num==3:
        return '3D DGPS'
    if num==9:
        return 'Unknown'

def l_value(num):
    if num==0:
        return 'Not available'
    if num==1:
        return 'Older than 10 seconds'
    if num==2:
        return 'Fresh, less than 10 seconds'
    if num==9:
        return 'GPS Failure'

def text_EV(a):
    try:
        code = a[0:3]
        event_Definition = int(a[3:5])
        date0 = int(a[5:9])
        day = int(a[9])
        date1 = date(1980, 1, 6)
        date_final = date1 + timedelta(days= date0*7+day)
        time = int(a[10:15])
        final_time = t_convert(time)
        sign_lat = a[15]
        lat = float(a[16:23])/100000
        final_latitude = sign_lat +str(lat)
        sign_lon = a[23]
        lon = float(a[24:32])/100000
        final_longitude = sign_lon+ str(lon)
        speed = int(a[32:35])
        v_heading = int(a[35:38])
        k = k_value(int(a[38]))
        l = l_value(int(a[39]))

        return [date_final, final_time, final_latitude, final_longitude]
    except:
        print("Error!")

def extended_EV(b):
    try:
        val = b[41:]
        s =''
        arr = []
        for i in val:
            if i==';':
                arr.append(s)
                s=''
            else:
                s+=i
        arr.append(s)
        return tag_def(arr)
    except:
        print("Error!")
