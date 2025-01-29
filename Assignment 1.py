from typing import List, Tuple

"""Converts time in HHMM format to minutes """
def convert_to_minutes(time_str: str) -> int:

    hours = int(time_str[:2])
    minutes = int(time_str[2:])
    return hours * 60 + minutes

"""This function performs the job scheduling using dynamic programming to maximize profit.
It returns the list of remaining jobs and their total earnings for other employees.
"""
def job_scheduling(jobs: List[Tuple[int, int, int]]) -> Tuple[List[int], int]:

    n = len(jobs)
    

    jobs.sort(key=lambda x: x[1])
    

    dp = [0] * n
    
    # Binary search helper function 
    def latest_non_conflict(index):
        low = 0
        high = index - 1
        while low <= high:
            mid = (low + high) // 2
            if jobs[mid][1] <= jobs[index][0]:  
                if jobs[mid + 1][1] <= jobs[index][0]:
                    low = mid + 1
                else:
                    return mid
            else:
                high = mid - 1
        return -1

    for i in range(n):
   
        last = latest_non_conflict(i)
        

        include_profit = jobs[i][2]
        if last != -1:
            include_profit += dp[last]  
        
        # Either include the current job or exclude it, take the maximum of both options
        dp[i] = max(include_profit, dp[i-1] if i > 0 else 0)
    




    # Backtrack to find which jobs were selected by Lokesh
    selected_jobs = []
    i = n - 1
    while i >= 0:
        if i == 0 or dp[i] != dp[i-1]:
            # If including the current job gives a better profit than excluding it
            selected_jobs.append(i)
            last = latest_non_conflict(i)
            i = last
        else:
            i -= 1
    
    # Reverse the selected jobs list 
    selected_jobs.reverse()
    
    # Calculate remaining jobs and their total profit
    selected_set = set(selected_jobs)
    remaining_jobs = [i for i in range(n) if i not in selected_set]
    remaining_profit = sum(jobs[i][2] for i in remaining_jobs)
    
    return remaining_jobs, remaining_profit

"""
    Main function
"""

def main():

    n = int(input("Enter the number of Jobs: "))
    jobs = []
    

    for _ in range(n):
        start_time = convert_to_minutes(input("Enter job start time: ").strip())
        end_time = convert_to_minutes(input("Enter job end time: ").strip())
        profit = int(input("Enter job earnings: ").strip())
        jobs.append((start_time, end_time, profit))
    
    # remaining jobs and  earnings after Lokesh picks his jobs
    remaining_jobs, remaining_profit = job_scheduling(jobs)
    

    print(f"The number of tasks and earnings available for others")
    print(f"Task: {len(remaining_jobs)}")
    print(f"Earnings: {remaining_profit}")

if __name__ == "__main__":
    main()