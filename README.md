# AutoClipUploader-CLI

Archived in favour for the [new app version](https://github.com/notMarkMP1/AutoClipUpload). Should still work as a CLI, however.  


A personal project to make it easier for me to upload my clips to YouTube. Uses Python and YouTube's Data API to function.

## TODO:
- [X] ~~Automatically upload videos from command line~~
- [X] ~~File selection GUI~~ 
- [ ] Progress Bar GUI
- [ ] Configuration settings GUI
- [ ] Video preview
- [ ] Trim videos
- [ ] Compress videos
- [ ] Account Switching
 
## Set-up

Create client_secrets.json in the same directory as the python files.

### client_secrets.json
```json
{
  "web": {
    "client_id": "[[YOUR ID]]",
    "client_secret": "[[YOUR SECRET KEY]]",
    "redirect_uris": [],
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://accounts.google.com/o/oauth2/token"
  }
}
```
