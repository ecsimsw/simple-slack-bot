import uvicorn
from fastapi import FastAPI

import slackSender
import scheduler

url = "https://hooks.slack.com/services/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"
ygSlackId = "U067TDGK3PZ"
jhSlackId = "U02DWRS37FY"

app = FastAPI()


@app.get("/")
def health():
    howl()
    return {"slack sender test"}


def howl():
    howler_msg = "<@{}> 너 오늘 코테 안했다잉: \n*<https://github.com/Giggle-projects/our-howler|Github - our howler>*"
    slackSender.send(url, howler_msg.format(jhSlackId))
    print("hi")


if __name__ == "__main__":
    scheduler.addScheduleEveryday("00:00", howl)
    scheduler.runScheduler(1)
    uvicorn.run(app, port=7777)
