import uvicorn
from fastapi import FastAPI, Form

from starlette.requests import Request
import slackSender
import scheduler

signiture = "HOW DARE YOU STEAL THAT CAR! I AM ABSOLUTELY DISGUSTED! YOUR FATHER'S IS NOW FACING AN INQUIRY AT WORK, AND IT'S ENTIRELY YOUR FAULT! IF YOU PUT ANOTHER TOE OUT OF LINE, WE'LL BRING YOU STRAIGHT HOME!: \n" \
             "*<https://github.com/Giggle-projects/our-howler|Github - our howler>*"


ygSlackId = "U067TDGK3PZ"
jhSlackId = "U02DWRS37FY"

app = FastAPI()


@app.post("/")
async def say_anything(
    request: Request
):
    form = await request.form()

    # These are from slack slash command request
    # This request contains a data payload describing the source command and who invoked it.

    token = form["token"]
    team_id = form["team_id"]
    team_domain = form["team_domain"]
    enterprise_id = form["enterprise_id"]
    enterprise_name = form["enterprise_name"]
    channel_id = form["channel_id"]
    channel_name = form["channel_name"]
    user_id = form["user_id"]
    user_name = form["user_name"]
    command = form["command"]
    text = form["text"]
    response_url = form["response_url"]
    trigger_id = form["trigger_id"]
    api_app_id = form["api_app_id"]
    return "<@{}>".format(user_id) + signiture


@app.post("/hey")
def health():
    return "hi"


def howl():
    slackSender.send("howler-alert", signiture)


if __name__ == "__main__":
    howl()
    scheduler.addScheduleEveryday("23:59", howl)
    scheduler.runScheduler(20)
    uvicorn.run(app, host="0.0.0.0", port=7777)
