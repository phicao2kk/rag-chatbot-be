sudo nginx -c /home/marcus/projects/nckh2627/rag-chatbot-be/nginx.conf
sudo nginx -s stop
curl -i http://localhost:1234/api/rate-limiting.html

chmod o+x /home/marcus/projects/nckh2627/rag-chatbot-be/static
chmod o+x /home/marcus/projects/nckh2627/rag-chatbot-be/static/rate-limiting.html