from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse, Response
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, EmailStr
import os
import asyncpg
from datetime import datetime
import logging
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize FastAPI app
app = FastAPI(title="Rosy AI Landing Page", version="1.0.0")

# Mount static files (CSS, JS, images)
app.mount("/assets", StaticFiles(directory="assets"), name="assets")

# Pydantic models
class WaitlistEmail(BaseModel):
    email: EmailStr

# Database connection
async def get_db_connection():
    """Get database connection from Supabase URL"""
    database_url = os.getenv("DATABASE_URL")
    if not database_url:
        raise HTTPException(status_code=500, detail="Database URL not configured")
    
    try:
        conn = await asyncpg.connect(database_url)
        return conn
    except Exception as e:
        logging.error(f"Database connection failed: {e}")
        raise HTTPException(status_code=500, detail="Database connection failed")

# Initialize database table
async def init_db():
    """Create waitlist table if it doesn't exist"""
    conn = await get_db_connection()
    try:
        await conn.execute("""
            CREATE TABLE IF NOT EXISTS waitlist (
                id SERIAL PRIMARY KEY,
                email VARCHAR(255) UNIQUE NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        logging.info("Database table initialized")
    except Exception as e:
        logging.error(f"Database initialization failed: {e}")
    finally:
        await conn.close()

# Routes
@app.get("/", response_class=HTMLResponse)
async def get_index():
    """Serve the main landing page"""
    try:
        with open("index.html", "r", encoding="utf-8") as file:
            html_content = file.read()
        return HTMLResponse(content=html_content, status_code=200)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Index page not found")
    except Exception as e:
        logging.error(f"Error serving index page: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

@app.post("/api/waitlist")
async def submit_waitlist_email(waitlist_data: WaitlistEmail):
    """Submit email to waitlist"""
    conn = await get_db_connection()
    
    try:
        # Check if email already exists
        existing_email = await conn.fetchrow(
            "SELECT email FROM waitlist WHERE email = $1", 
            waitlist_data.email
        )
        
        if existing_email:
            return {
                "success": False, 
                "message": "You're already on our waitlist! We'll be in touch soon."
            }
        
        # Insert new email
        await conn.execute(
            "INSERT INTO waitlist (email) VALUES ($1)", 
            waitlist_data.email
        )
        
        logging.info(f"New waitlist signup: {waitlist_data.email}")
        
        return {
            "success": True,
            "message": "Thank you for joining the waitlist! We'll be in touch soon."
        }
        
    except asyncpg.UniqueViolationError:
        return {
            "success": False,
            "message": "You're already on our waitlist! We'll be in touch soon."
        }
    except Exception as e:
        logging.error(f"Error adding email to waitlist: {e}")
        raise HTTPException(status_code=500, detail="Failed to add email to waitlist")
    
    finally:
        await conn.close()

@app.get("/api/waitlist/count")
async def get_waitlist_count():
    """Get total number of waitlist signups"""
    conn = await get_db_connection()
    
    try:
        count = await conn.fetchval("SELECT COUNT(*) FROM waitlist")
        return {"count": count}
    except Exception as e:
        logging.error(f"Error getting waitlist count: {e}")
        raise HTTPException(status_code=500, detail="Failed to get waitlist count")
    finally:
        await conn.close()

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "timestamp": datetime.utcnow()}

# Startup event
@app.on_event("startup")
async def startup_event():
    """Initialize database on startup"""
    await init_db()

# Add route to serve CSS file
@app.get("/styles.css")
async def get_styles():
    """Serve the CSS file"""
    try:
        with open("styles.css", "r", encoding="utf-8") as file:
            css_content = file.read()
        return Response(content=css_content, media_type="text/css")
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="CSS file not found")

# Favicon routes
@app.get("/favicon.ico")
async def get_favicon_ico():
    """Serve favicon.ico"""
    try:
        with open("assets/icons/favicon.ico", "rb") as file:
            favicon_content = file.read()
        return Response(content=favicon_content, media_type="image/x-icon")
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Favicon not found")

@app.get("/favicon-{size}.png")
async def get_favicon_png(size: str):
    """Serve PNG favicon files"""
    try:
        filename = f"assets/icons/favicon-{size}.png"
        with open(filename, "rb") as file:
            favicon_content = file.read()
        return Response(content=favicon_content, media_type="image/png")
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Favicon PNG not found")

# Remove the problematic error handlers - FastAPI handles these automatically

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)