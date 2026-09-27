tasks = ["Learn Git", "Push to GitHub", "Containerize with Docker"]

print("=== My Learning Checklist ===")
for index, task in enumerate(tasks, start=1):
    print(f"{index}. [ ] {task}")