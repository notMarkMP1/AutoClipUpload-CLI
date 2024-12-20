import os
import tkinter as tk

from tkinter import filedialog
from googleapiclient.errors import HttpError
from oauth2client.tools import argparser

import upload
from upload import VALID_PRIVACY_STATUSES

if __name__ == '__main__':
  argparser.add_argument("--file", help="Video file to upload")
  argparser.add_argument("--title", help="Video title")
  argparser.add_argument("--description", help="Video description")
  argparser.add_argument("--category",
    help="Numeric video category. " +
      "See https://developers.google.com/youtube/v3/docs/videoCategories/list")
  argparser.add_argument("--keywords", help="Video keywords, comma separated",)
  argparser.add_argument("--privacyStatus", help="Video privacy status.")
  args = argparser.parse_args()

  if args.file is None:
    root = tk.Tk()
    root.withdraw()
    args.file = filedialog.askopenfilename()

  if args.title is None: args.title = input("Enter the video title (default: untitled video): ") or "untitled video"
  if args.description is None: args.description = input("Enter the video description (default: empty): ") or ""
  if args.category is None: args.category = input("Enter the numeric video category (default: ): ") or ""
  if args.keywords is None: args.keywords = input("Enter the video keywords, comma separated (default: ''): ") or ""
  if args.privacyStatus is None: args.privacyStatus = input(f"Enter the video privacy status (choices: {', '.join(VALID_PRIVACY_STATUSES)}, default: {VALID_PRIVACY_STATUSES[0]}): ") or VALID_PRIVACY_STATUSES[0]

  if args.privacyStatus not in VALID_PRIVACY_STATUSES:
    exit("Invalid privacy status.")

  if args.file[0] == args.file[-1] and args.file.startswith(("'", '"')):
    args.file = args.file[1:-1]

  if not os.path.exists(args.file):
    exit("Please specify a valid file using the --file= parameter.")

  youtube = upload.get_authenticated_service(args)
  try:
    upload.initialize_upload(youtube, args)
  except HttpError as e:
    print("An HTTP error %d occurred:\n%s" % (e.resp.status, e.content))