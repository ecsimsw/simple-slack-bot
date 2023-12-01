import uvicorn
from fastapi import FastAPI

import slackSender

url = "https://hooks.slack.com/services/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"
ygSlackId = "U067TDGK3PZ"
jhSlackId = "U02DWRS37FY"

app = FastAPI()

@app.get("/")
def health():
    slackSender.send(url, "<@{}> 너 오늘 코테 안했다잉: \n*<https://github.com/Giggle-projects/our-howler|Github - our howler>*".format(jhSlackId))
    return {"slack sender test"}

if __name__ == "__main__":
    uvicorn.run(app, port=7777)
