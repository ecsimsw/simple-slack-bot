import uvicorn
from fastapi import FastAPI, Form


import slackSender
import scheduler

signiture = "HOW DARE YOU STEAL THAT CAR! I AM ABSOLUTELY DISGUSTED! YOUR FATHER'S IS NOW FACING AN INQUIRY AT WORK, AND IT'S ENTIRELY YOUR FAULT! IF YOU PUT ANOTHER TOE OUT OF LINE, WE'LL BRING YOU STRAIGHT HOME!: \n" \
             "*<https://github.com/Giggle-projects/our-howler|Github - our howler>*"


ygSlackId = "U067TDGK3PZ"
jhSlackId = "U02DWRS37FY"

app = FastAPI()


@app.post("/")
def say_anything(
    token: str = Form(),
    team_id: str = Form(),
    team_domain: str = Form(),
    enterprise_id: str = Form(),
    enterprise_name: str = Form(),
    channel_id: str = Form(),
    channel_name: str = Form(),
    user_id: str = Form(),
    user_name: str = Form(),
    command: str = Form(),
    text: str = Form(),
    response_url: str = Form(),
    trigger_id: str = Form(),
    api_app_id: str = Form()
):
    return "<@{}>".format(user_name) + signiture


@app.post("/hey")
def health():
    return "hi"


def howl():
    slackSender.send(signiture)


if __name__ == "__main__":
    howl()
    scheduler.addScheduleEveryday("23:59", howl)
    scheduler.runScheduler(20)
    uvicorn.run(app, host="0.0.0.0", port=7777)
