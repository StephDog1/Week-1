from statistics import mean
import sys

Degrees = "C"

if len(sys.argv) != 7:
    print("Usage: python temperature_stats.py <8am> <10am> <12pm> <2pm> <4pm> <6pm>")
    sys.exit(1)

try:
    temp8am = int(sys.argv[1])
    temp10am = int(sys.argv[2])
    temp12pm = int(sys.argv[3])
    temp2pm = int(sys.argv[4])
    temp4pm = int(sys.argv[5])
    temp6pm = int(sys.argv[6])

    print(f"The highest temp is: {max(temp8am, temp10am, temp12pm, temp2pm, temp4pm, temp6pm)}{Degrees}")
    print(f"The lowest temp is: {min(temp8am, temp10am, temp12pm, temp2pm, temp4pm, temp6pm)}{Degrees}")

    inp_lst = [temp8am, temp10am, temp12pm, temp2pm, temp4pm, temp6pm]
    list_average = int(mean(inp_lst))
    print(f"The average is: {list_average}{Degrees}")
except ValueError:
    print("Invalid input. Please provide valid temperature values.")
