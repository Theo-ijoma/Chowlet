// src/middleware/auth.ts
import type { NextFunction, Request, Response } from 'express';
import jwt, { type JwtPayload } from 'jsonwebtoken';
import { prisma } from '../lib/prisma';
const JWT_SECRET: string =
  process.env.SUPABASE_JWT_SECRET ?? (() => { throw new Error('Missing SUPABASE_JWT_SECRET'); })();

// Extend Express Request to include current user
declare global {
  namespace Express {
    interface Request {
      currentUser?: {
      id: string;
      supabaseUserId: string;
      email: string;
      fullName: string;
      role: string;
      schoolId: string | null;
      phoneNumber: string | null;
    };
  }
}
}

export async function authenticate(req: Request, res: Response, next: NextFunction) {
  const authHeader = req.headers.authorization;
  if (!authHeader || !authHeader.startsWith('Bearer ')) {
    return res.status(401).json({ error: 'Missing or invalid token' });
  }

  const token = authHeader.split(' ')[1];
  if (!token) {
    return res.status(401).json({ error: 'Missing or invalid token' });
  }

  try {
    const decoded = jwt.verify(token, JWT_SECRET) as JwtPayload & { email?: string };
    const supabaseUserId = decoded.sub;
    const email = typeof decoded.email === 'string' ? decoded.email.trim() : '';

    if (!supabaseUserId || typeof supabaseUserId !== 'string') {
      return res.status(401).json({ error: 'Invalid token payload' });
    }

    if (!email) {
      return res.status(401).json({ error: 'Token is missing an email claim' });
    }

    // Bootstrap the profile the first time a Supabase session reaches the backend.
    const user =
      (await prisma.profile.findUnique({
        where: { supabaseUserId },
        select: {
          id: true,
          supabaseUserId: true,
          email: true,
          fullName: true,
          role: true,
          schoolId: true,
          phoneNumber: true,
        },
      })) ??
      (await prisma.profile.create({
        data: {
          supabaseUserId,
          email,
          fullName: email,
        },
        select: {
          id: true,
          supabaseUserId: true,
          email: true,
          fullName: true,
          role: true,
          schoolId: true,
          phoneNumber: true,
        },
      }));

    req.currentUser = user;
    next();
  } catch (err) {
    return res.status(401).json({ error: 'Invalid or expired token' });
  }
}
