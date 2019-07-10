from pythonfunc import percent

def test_percent():
   percentage = percent(10,100)
   assert percentage == 10
   a = "10"   
   b = "0"
   percentage = percent(a,b)
   assert percentage == "Invalid arguements"
   dis = 100
   tot = 100
   percentage = percent(dis,tot)
   assert percentage == "Cannot discount 100%"
