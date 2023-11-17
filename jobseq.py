def job_sequencing_with_deadlines(jobs):
    # Sort the jobs in descending order of their profits
    jobs.sort(key=lambda x: x[2], reverse=True)

    max_deadline = max(jobs, key=lambda x: x[1])[1]
    schedule = [-1] * max_deadline  # Initialize a schedule with -1 representing empty slots
    total_profit = 0

    for job in jobs:
        job_id, deadline, profit = job
        for i in range(min(max_deadline, deadline) - 1, -1, -1):
            if schedule[i] == -1:
                schedule[i] = job_id
                total_profit += profit
                break

    return schedule, total_profit

# Example usage
jobs = [(1, 2, 100), (2, 1, 19), (3, 2, 27), (4, 1, 25), (5, 3, 15)]
schedule, profit = job_sequencing_with_deadlines(jobs)
print("Job Schedule:", schedule)
print("Total Profit:", profit)
