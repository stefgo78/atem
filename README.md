cd atem-panel
docker build -t atem-panel

docker run -d -p 3000:3000 --name atem-panel atem-panel

http://localhost:3000
