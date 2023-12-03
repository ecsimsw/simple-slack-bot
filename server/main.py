import uvicorn
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

import slackSender
import scheduler

url = "https://hooks.slack.com/services/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"
ygSlackId = "U067TDGK3PZ"
jhSlackId = "U02DWRS37FY"

app = FastAPI()


@app.get("/", response_class=ORJSONResponse)
def health():
    howl()
    data = {"msg" : "howl"}
    return ORJSONResponse([data])


def howl():
    howler_msg = "<@{}> HOW DARE YOU STEAL THAT CAR! I AM ABSOLUTELY DISGUSTED! YOUR FATHER'S IS NOW FACING AN INQUIRY AT WORK, AND IT'S ENTIRELY YOUR FAULT! IF YOU PUT ANOTHER TOE OUT OF LINE, WE'LL BRING YOU STRAIGHT HOME!: \n" \
                 "*<https://github.com/Giggle-projects/our-howler|Github - our howler>*"
    slackSender.send(howler_msg.format(ygSlackId))
    print("hi")


if __name__ == "__main__":
    scheduler.addScheduleEveryday("23:59", howl)
    scheduler.runScheduler(1)
    uvicorn.run(app, host="0.0.0.0", port=7777)
