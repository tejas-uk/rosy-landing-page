#!/usr/bin/env python3
"""
Rosy AI Landing Page Server
Run this script to start the FastAPI server
"""

import uvicorn
import os

if __name__ == "__main__":
    # Check if .env file exists
    if not os.path.exists(".env"):
        print("⚠️  Warning: .env file not found!")
        print("📝 Please create a .env file with your DATABASE_URL")
        print("💡 See .env.example for reference")
        print("Example:")
        print("DATABASE_URL=postgresql://postgres:[PASSWORD]@db.[PROJECT-REF].supabase.co:5432/postgres")
        print()
    
    print("🚀 Starting Rosy AI Landing Page Server...")
    print("📡 Server will be available at: http://localhost:8000")
    print("📊 API docs available at: http://localhost:8000/docs")
    print("💾 Make sure your DATABASE_URL is set in .env file")
    print("🔄 Press Ctrl+C to stop the server")
    print()
    
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )