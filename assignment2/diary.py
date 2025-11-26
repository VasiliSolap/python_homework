import traceback

try:
    first_prom = True
    with open("diary.txt", "a") as f:
        while True:
            if first_prom == True:
                text =  input("What happened today? ")
                first_prom = False
            else:
                text = input("What else? ")

            f.write(text + "\n")

            if text == "done for now":
                break


except Exception as e:
   trace_back = traceback.extract_tb(e.__traceback__)
   stack_trace = list()
   for trace in trace_back:
      stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
   print(f"Exception type: {type(e).__name__}")
   message = str(e)
   if message:
      print(f"Exception message: {message}")
   print(f"Stack trace: {stack_trace}")