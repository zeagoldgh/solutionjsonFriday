mkdir fancyApi

echo "zip files for server"
cd source
zip ../fancyApi/source.zip requirements.txt worker.py

echo "upload to s3"
aws s3 cp fancyApi/source.zip s3://jobapi-bucket/