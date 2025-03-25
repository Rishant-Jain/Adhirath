package com.adhirath.service;

import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;

@Service
public class AIService {
    private final String AI_SERVICE_URL = "http://localhost:5000";
    private final RestTemplate restTemplate;
    
    public AIService(RestTemplate restTemplate) {
        this.restTemplate = restTemplate;
    }
    
    public String analyzeEmotion(String imageData) {
        String url = AI_SERVICE_URL + "/analyze-emotion";
        // Make request to AI service
        return restTemplate.postForObject(url, imageData, String.class);
    }
}