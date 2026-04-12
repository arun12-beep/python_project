dict={'sunsari':'inaruwa',
      'ilam':'ilam',
      'dhankuta':'dhankuta',
      'kathmandu':'kathmandu',
      'panchtaar':'phidim',
      'tanahu':'labdi',
      'morang':'biratnagar',
      'saptari':'rajbiraj'

      }
print("items in dictionary:")
for k,v in dict.items():
    print(f"{k}: {v}")
print("districts having headquater name same as district name are:")
for k,v in dict.items():
    if k.lower()==v.lower():   #lower() function is used for case-sensitivity matching
        print(k)