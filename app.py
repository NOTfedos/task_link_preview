import uvicorn

from fastapi import FastAPI
from fastapi.responses import JSONResponse

from requests.exceptions import RequestException, HTTPError

from linkpreview import Link, LinkPreview, LinkGrabber

from models import LinkUrl, PreviewResponse, PreviewErrorResp

# from previewlink import preview_link
# from webpreview import webpreview


app = FastAPI()


@app.post("/content/parse",
          response_model=PreviewResponse,
          responses={
              400: {"model": PreviewErrorResp}
          },
          response_model_exclude_unset=True
          )
async def parse_url_preview(url_obj: LinkUrl):

    # Init grabber for parsing
    grabber = LinkGrabber(
        initial_timeout=5,
        maxsize=262144,
        receive_timeout=5,
        chunk_size=512,
    )

    # Parse url site
    try:
        content, url = grabber.get_content(url_obj.url)
    except HTTPError as e:
        msg = e.args[0]
        return JSONResponse(status_code=400, content={"error": {"message": msg}})
    except RequestException as e:
        msg = e.args[0].reason.args[-1]
        return JSONResponse(status_code=400, content={"error": {"message": msg}})

    # Get the preview from content
    link = Link(url, content)
    preview = LinkPreview(link)

    # Form the response
    resp = {
        "title": preview.title,
    }

    if preview.description is not None:
        resp["description"] = preview.description

    if preview.absolute_image is not None:
        resp["imageUrl"] = preview.absolute_image

    return PreviewResponse(**resp)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=80, debug=True)
