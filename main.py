# -*- coding: utf-8 -*-
# @Author: fredy
# @Date:   2020-04-11 15:50:51
# @Last Modified by:   fredy
# @Last Modified time: 2020-04-11 19:46:56
import textToSpeech
import speechtotext

if __name__ == "__main__":
    import time
    """
    Question 1:
        What is my temparature?
        Your temperature is 36.5 degrees. You may go outside!
    Question 2:
        coughing, i don't feel good.
        You are coughing. Your temperature is 38 degrees. You should go to Prince of Wales Hospital.
    Qestion 3:
        How crawded is Aldi?
        The crowded level is, medium.
    Question 4:
        Order pasta and milk from Woolworths.
        Order pasta and milk from Woolworths. The total is 7.99 dollar.
    Question 5:
        Call an ambulance!
        Call an ambulance from Prince of Wales Hospital.
    Quetion 6:
        Order meat pie.
        Ordering meat pie from Jack's meat pie.
    """
    an_1 = "Your temperature is 36.5 degrees. You may go outside!"
    an_2 = "You are coughing. Your temperature is 38 degrees. You should go to Prince of Wales Hospital."
    an_3 = "The crowded level is, medium."
    an_4 = "Order pasta and milk from Woolworths. The total is 7.99 dollar."
    an_5 = "Call an ambulance from Prince of Wales Hospital."
    an_6 = "Ordering meat pie from Jack's meat pie."
    while True:
        question = speechtotext.myCommand()
        if "temperature" in question:
            textToSpeech.pySpeak(an_1)
        elif "feel good" in question:
            textToSpeech.pySpeak(an_2)
        elif "How crawded" in question:
            textToSpeech.pySpeak(an_3)
        elif "pasta and milk" in question:
            textToSpeech.pySpeak(an_4)
        elif "ambulance" in question:
            textToSpeech.pySpeak(an_5)
        elif "meat pie" in question:
            textToSpeech.pySpeak(an_6)
