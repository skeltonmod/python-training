import facebook
import schedule
import time
import os
from dotenv import load_dotenv

load_dotenv()

FB_ACCESS_TOKEN = os.getenv("FB_ACCESS_TOKEN")
PAGE_ID = os.getenv("PAGE_ID")

# The old hacky way
# graph = facebook.GraphAPI(access_token=FB_ACCESS_TOKEN, version="8.0")
# try:
#     graph.put_photo(
#         image=open("assets/jamespogi.jpg", "rb"), message="James"
#     )
# except facebook.GraphAPIError:
#     print("Something went wront")
# except FileNotFoundError:
#     print("Error with the file")
# else:
#     print("All good!")
# finally:
#     print("We can clean up resources here")

# The pro programmer way


class FaceBot:
    def __init__(self, token, page_id, image=None, message=""):
        self.page_id = PAGE_ID
        self.image = image
        self.message = message
        self.graph = facebook.GraphAPI(access_token=token, version="8.0")

    def post_message(self):
        self.graph.put_object(
            parent_object="me", connection_name="feed", message=self.message
        )

    def post_photo(self):
        if self.image is None:
            return
        self.graph.put_photo(
            image=open("assets/jamespogi.jpg", "rb"), message=self.message
        )


if __name__ == "__main__":
    fbot = FaceBot(
        FB_ACCESS_TOKEN, PAGE_ID, open("assets/jamespogi.jpg", "rb"), "James"
    )

    def job():
        fbot.post_photo()

    schedule.every(1).minutes.do(job)

    while True:
        schedule.run_pending()
        time.sleep(1)
