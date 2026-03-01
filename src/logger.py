import datetime as dt

def log(role: str, text: str):
    dt_now = dt.datetime.now()
    date_today = dt.date.today()
    time = dt_now.strftime("%H:%M:%S")
    print(time)
    with open(f"Logs/agent_{date_today}.md", "a") as file:
        file.write(f"""###### {time} | {role}\n```\n{text}\n```\n\n""")