import Youtube_GoogleTrends 
import Youtube_Search
import Youtube_Downloader
import Youtube_Upload2Cloud

# Argument setting
keyword_path = './Input/InputList.xlsx' # Modified for different disease, Input the keyword list
keyword_ref = 'diabetes causes' # use the first keyword for comparison in each iteration. Suggestion: "Disease name + causes"
DEVELOPER_KEY = "AIzaSyBxztRZEw8u6EjuMgV77dBS1Soel5bOXnk" # Key for Ruoyu Zhang
credential_path= "/youtube-project-351220-44b975bbe749.json"  # You have to create your own json credential
BUCKET_NAME = 'youtube-project-351220.appspot.com' # You have to create your bucket and download the bucket name

# Getting google trends
Youtube_GoogleTrends.main(keyword_path, keyword_ref)

# Running google search and return videoID.txt
Youtube_Search.main()

# Download the video to local machine
Youtube_Downloader.main()

# Upload the video to GCP platform 
Youtube_Upload2Cloud.main()


