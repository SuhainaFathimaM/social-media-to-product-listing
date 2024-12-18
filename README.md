# Amazon Smbhav Hackathon 2024  
## Prototype Phase Submission  
### Project Name: Social2Amazon  

---

## Overview

**Social2Amazon** bridges the gap between social media content and Amazon's marketplace. The solution leverages AI and data analysis to identify trending products, optimize listings, and create seamless shopping experiences based on user preferences and trends from platforms like Instagram, TikTok, and Twitter.

---

## Problem Statement

Social media significantly influences purchase decisions, yet identifying and capitalizing on trends in real time remains a challenge. **Social2Amazon** empowers small and medium businesses (SMBs) to:

- Detect trending products.
- Enhance their Amazon listings.
- Stay ahead of market trends.
- Maximize revenue from viral products.

---

## Solution

**Social2Amazon**:

- Processes images, videos, and text from social media to identify potential products.
- Generates optimized product listings with titles, descriptions, and keywords using AI.
- Integrates with Amazon's seller tools for easy product management.

---

## Key Features

1. **Social Media Scraper**:
   - Collects trending posts and identifies key product attributes.

2. **AI-Based Product Analysis**:
   - Uses Machine Learning to classify products.
   - Predicts demand based on trend patterns.

3. **Automated Listing Generator**:
   - Generates SEO-optimized titles and descriptions.
   - Suggests pricing, tags, and categories.

4. **Interactive Dashboard**:
   - Visualizes trending products.
   - Provides actionable insights for SMBs.

---

## Prototype Details

### Backend:
- **Framework**: FastAPI
- **Technologies**:
  - Image and video processing: TensorFlow, MobileNetV2
  - Text processing: SpaCy
  - Video processing: MoviePy
- **APIs**:
  - Social media API integrations (e.g., Instagram, Twitter).
  - OpenWeatherMap (for trend analysis correlation).

### Frontend:
- **Technologies**: HTML, CSS, JavaScript
- **UI**: Simple and intuitive UI
- **Dashboard**: Interactive product insights and listing suggestions.

### Static File Management:
- Folder structure includes:
  - `uploads/` for media inputs.
  - `processed/` for generated outputs.

### Deployment:
- Hosted using Render for seamless integration.
- Gunicorn and Uvicorn for backend server deployment.

- Visit: [https://youtu.be/3Ssp3tG-Idc?si=ifdoKb41N4DU-rE-]

---

## How to Run Locally

### Prerequisites:
- Python 3.10+
- Node.js (optional for advanced frontend features)

### Steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/social-media-to-product-listing.git
   cd social-media-to-product-listing

2. Install dependencies:
   ```bash
   pip install -r requirements.txt

3. Start the application:
   ```bash
   gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app

4. Open http://127.0.0.1:8000 in your browser.

---

### Technologies Used

- **Backend**: FastAPI, TensorFlow, SpaCy, MoviePy
- **Frontend**: HTML, CSS, JavaScript
- **Deployment**: Render
- **Database**: SQLite (for prototype)

---

## Team Members
- **Suhaina Fathima M**:
  - B.E in CSE in Government College Of Engineering, Salem
  - Contact: suhainafathimam@gmail.com
 
---
### Future Enhancements
  1. Expand API support for additional social media platforms.
  2. Enhance AI for deeper trend prediction.
  3. Integrate Amazon MWS API for automated listing uploads.
  4. Add advanced analytics features for SMBs.

---

We look forward to the opportunity to present Social2Amazon and help SMBs thrive in the competitive e-commerce ecosystem.
