<<<<<<< HEAD:PY/Learn.py
from turtle import pu


fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        break
    print(x)

pulledFruits = ["green", "orange", "red", "blue"]
for y in pulledFruits:
    print(y)
    
=======
import nidaqmx
with nidaqmx.Task() as task:
    task.ai_channels.add_ai_voltage_chan("SimDev1/ai0")
    print(task.read())
>>>>>>> master:Python/Learn.py
