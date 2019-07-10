def percent(cut_amount,original_amount):
   if not(type(cut_amount) == int and type(original_amount) == int):
        return("Invalid arguements")
   if(original_amount <= 0):
        return("Original amount cannot be zero") 
   if(cut_amount == original_amount):
        return("Cannot discount 100%")
   return((cut_amount/original_amount)*100)

