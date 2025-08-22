import express from 'express';
import cors from 'cors';
import helmet from 'helmet';
import compression from 'compression';
import rateLimit from 'express-rate-limit';
import dotenv from 'dotenv';

dotenv.config();

const app = express();
const PORT = process.env.PORT || 3000;

// Security middleware
app.use(helmet());

// Rate limiting
const limiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 100, // limit each IP to 100 requests per windowMs
  message: 'Too many requests from this IP, please try again later.',
});

app.use(limiter);

// CORS configuration
app.use(cors({
  origin: process.env.NODE_ENV === 'production' 
    ? process.env.FRONTEND_URL 
    : 'http://localhost:3000',
  credentials: true,
}));

// Body parsing middleware
app.use(compression());
app.use(express.json({ limit: '10mb' }));
app.use(express.urlencoded({ extended: true, limit: '10mb' }));

// Basic routes
app.get('/api/health', (req, res) => {
  res.status(200).json({
    status: 'OK',
    message: 'Altibbe Product Transparency Platform API',
    timestamp: new Date().toISOString(),
    uptime: process.uptime(),
  });
});

// Placeholder API routes
app.get('/api/products', (req, res) => {
  res.json({ message: 'Products API endpoint - to be implemented' });
});

app.post('/api/products', (req, res) => {
  res.json({ message: 'Create product endpoint - to be implemented', data: req.body });
});

app.get('/api/reports/:id', (req, res) => {
  res.json({ message: `Report ${req.params.id} endpoint - to be implemented` });
});

app.post('/api/auth/login', (req, res) => {
  res.json({ message: 'Authentication endpoint - to be implemented' });
});

// Start server
app.listen(PORT, () => {
  console.log(`🚀 Altibbe Backend Server running on port ${PORT}`);
  console.log(`📱 Environment: ${process.env.NODE_ENV || 'development'}`);
});

export default app;
