from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import Body, Depends
from fastapi.responses import RedirectResponse
from pydantic import HttpUrl
from datetime import datetime, timezone
from sqlalchemy.orm import Session
from gen_short import gen_short_url
from db import ShortenedUrl, get_db_session

app = FastAPI()


@app.get("/api/test")
async def api_check():
    """is API reachable"""
    return {
        "check": "API OK"
    }


@app.post("/api/create-short")
def shorten(db: Session = Depends(get_db_session), input_url: HttpUrl = Body(..., embed=True)):
    """ Endpoint takes long url, returns short url plus original url """
    if not input_url:
        raise HTTPException(status_code=404, detail="input_url field is required")
    timestamp = datetime.now().replace(tzinfo=timezone.utc).timestamp()
    mini = gen_short_url(input_url, timestamp)
    domain = "http://127.0.0.1/"
    short_link = domain + mini
    print(short_link)

    url_obj = ShortenedUrl(original_url=input_url, short_link=short_link)
    db.add(url_obj)
    db.commit()

    return {
        "shortened_url": short_link,
        "input_url": input_url
    }


@app.get("/{short_url}")
def visit_shortened(short_url: str, db: Session = Depends(get_db_session)):
    domain = "http://127.0.0.1/"
    short_link = domain + short_url

    """ Endpoint takes short url, maps to original url and visits original url"""

    url_obj = db.query(ShortenedUrl).filter_by(short_link=short_link).order_by(ShortenedUrl.id.desc()).first()
    print(url_obj.original_url)
    print(type(url_obj))

    if url_obj is None:
        raise HTTPException(
            status_code=404, detail=f"The link: {short_url} does not exist, could not redirect."
        )
    return RedirectResponse(url=url_obj.original_url)
