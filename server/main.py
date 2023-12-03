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
    print(form)
    return form["user_id"]
    # query_word = request.form['text']
    # user = request.form['user_id']
    # return "<@{}>".format(user_name) + signiture


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
