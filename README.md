1. Install Jaeger in Docker:
docker run -d --name jaeger \
  -e COLLECTOR_ZIPKIN_HOST_PORT=:9411 \
  -p 16686:16686 -p 6831:6831/udp -p 6832:6832/udp \
  -p 5778:5778 -p 14268:14268 -p 14250:14250 -p 9411:9411 \
  jaegertracing/all-in-one:1.55
2. Install all requirements from file
3. Start code and check Jaeger interface
  
<img width="1263" height="1198" alt="Снимок экрана 2025-07-19 в 06 02 03" src="https://github.com/user-attachments/assets/a937ada9-00d3-4628-9c9a-b803bf3561f9" />
