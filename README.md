# COVID Assistant

## Introduction
This is the repository for the project COVID Assistant, a system that aids the elderly people who live alone on essential tasks such as grocery shopping or providing quick response on sudden health problems. The project serves originally as an idea for Australian Computer Society's Flatten The Curve Hack, April 2020.

Mentor: Has Fakira

## Implementation
Some intended implementation of the system, to be fit with the current situation:

### Sensory inputs

The system will take the sensory inputs of the resident to track their health condition, such as:
* Detect and distinguish coughing sound and shortness of breath, which can be reconised through machine learning.
* Measure body temperature using infrared camera.
* Retrieve heartbeat rate through red light sensors.
* Track respiratory vibration frequency.

### Location activity

Provides prediction and report about location activity such as markets and parks. The information will be collected by Google Maps.
It will provide information about if the resident is travelling into a hotspot, or their travelling habit. This is to aid when the resident needs to go out for essential reasons like shopping or excercise.

### Local connection

Connects the assistant with the stores in the local area. The idea involves helping local shops to implement the necessary IT infrastructure to take orders through voice assistants. The order can be delivered through different delivery services such as UberEats, Deliveroo, etc. or the store's delivery systems. This can help reducing the amount of crowded orders in big supermarkets and reallocate them to the local area.
 
### Further ideas
Include different parameters for predictions relevant to COVID-19 such as domestic and international travel information.

## Specifications

This repository consists of a sample system that takes a command speech as input and execute tasks based on the speech content.

### Text to Speech Function

* Pre-requirement Packages: `pyttsx3 pip install pyttsx3`
* Running Environment: Windows for the first function `phSpeak()`, Linux/Windows for the second function `pySpeak()`

### Sample dialogues

```
Input: Ah-choo      # Heavy cough sound detected
Assistant: Hi James, would you like to measure your fever?

Input.fever() > heat.THRESHOLD == True
Assistant: Your fever is 37 degrees and you have recently been overseas, would you like to go to the Prince of Wales hospital?

Input: How crowded is hyde park?
Assistant: The crowd level is medium

Input: Hi Google, order meat pie
Assistant: Ordering meat pie from Jack’s meat pies
```

## Who are we?

### Pandemic Hunters

We are a team that consists of 5 members from different backgrounds, with the same goal aim: to be able to help the people in need during the Covid-19 Pandemic and cut down its vulnerability, hence the team name. Team members include:
* Hoang Anh Ngo: hoang-anh.ngo@polytechnique.edu
* Sinan Bingul: sinan.bingul@gmail.com
* Fredy Zhang: fredy.zhang.au@gmail.com
* Thai Nam Hoang: hoangnt@beloit.edu
* Tuan Khoi Nguyen: tuankhoin@student.unimelb.edu.au

