from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Dict, Any, Optional
import uvicorn
import os
from dotenv import load_dotenv

load_dotenv()

# Initialize FastAPI app
app = FastAPI(
    title="Altibbe AI Service",
    description="AI-powered question generation and transparency scoring",
    version="1.0.0",
)

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Pydantic models
class ProductData(BaseModel):
    name: str
    category: str
    manufacturer: str
    description: Optional[str] = None
    ingredients: List[str]

class QuestionRequest(BaseModel):
    product_data: ProductData
    category: str
    max_questions: int = 5

class GeneratedQuestion(BaseModel):
    id: str
    text: str
    type: str = "text"
    category: str
    reasoning: str

# Health check endpoint
@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "Altibbe AI Service", "version": "1.0.0"}

# Question generation endpoint
@app.post("/generate-questions")
async def generate_questions(request: QuestionRequest):
    # Placeholder implementation
    sample_questions = [
        {
            "id": "q1",
            "text": f"What specific certifications does {request.product_data.name} have for {request.category}?",
            "type": "text",
            "category": request.category,
            "reasoning": f"Important to verify {request.category} claims"
        },
        {
            "id": "q2", 
            "text": f"How do you measure and validate {request.category} practices for {request.product_data.name}?",
            "type": "text",
            "category": request.category,
            "reasoning": f"Transparency in {request.category} methodology"
        }
    ]
    
    return {
        "questions": sample_questions[:request.max_questions],
        "category": request.category,
        "reasoning": f"Generated questions for {request.category} assessment",
        "confidence": 0.8
    }

# Transparency scoring endpoint
@app.post("/transparency-score")
async def calculate_score(product_data: ProductData):
    # Placeholder scoring logic
    base_score = 75
    if product_data.description:
        base_score += 5
    if len(product_data.ingredients) > 3:
        base_score += 10
    
    return {
        "overall_score": min(base_score, 100),
        "category_scores": {
            "sustainability": 80,
            "ethics": 75,
            "health": 85,
            "transparency": 70
        },
        "recommendations": [
            "Consider adding more detailed ingredient information",
            "Provide third-party certifications for transparency",
            "Include sustainability metrics and measurements"
        ]
    }

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=int(os.getenv("PORT", 8001)),
        reload=True
    )
