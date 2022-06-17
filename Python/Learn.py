import nidaqmx
with nidaqmx.Task() as task:
    task.ai_channels.add_ai_voltage_chan("SimDev1/ai0")
    print(task.read())