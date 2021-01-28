package_pen = 5.80
marker_package = 7.20
cleaning_agent_liter = 1.20

package_pen_counts = int(input())
marker_package_counts = int(input())
cleaning_agent_liter_counts = float(input())
discount_percentage = int(input())

total_sum = package_pen*package_pen_counts + marker_package*marker_package_counts + cleaning_agent_liter*cleaning_agent_liter_counts
total_sum -= total_sum * discount_percentage/100

print(f"{total_sum:.3f}")