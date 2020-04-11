# -*- coding: utf-8 -*-
# @Author: fredy
# @Date:   2020-04-11 15:50:51
# @Last Modified by:   fredy
# @Last Modified time: 2020-04-11 15:54:33
import textToSpeech

if __name__ == "__main__":
    question_1 = "How crowded is hyde park?"
    answer_1 = "The crowd level is medium."
    question_2 = "Hi Google, order meat pie."
    answer_2 = "Ordering meat pie, from Jack’s meat pies."

    textToSpeech.pySpeak(question_1)
    textToSpeech.pySpeak(answer_1)
    textToSpeech.pySpeak(answer_2)