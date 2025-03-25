# Use official Java 17 image
FROM openjdk:17
WORKDIR /app
COPY target/backend.jar backend.jar
EXPOSE 8080
ENTRYPOINT ["java", "-jar", "backend.jar"]
