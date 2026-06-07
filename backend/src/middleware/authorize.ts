// src/middleware/authorize.ts
import type { NextFunction, Request, Response } from 'express';

export function authorize(...allowedRoles: string[]) {
  return (req: Request, res: Response, next: NextFunction) => {
    if (!req.currentUser) {
      return res.status(401).json({ error: 'Not authenticated' });
    }
    if (!allowedRoles.includes(req.currentUser.role)) {
      return res.status(403).json({ error: 'Insufficient permissions' });
    }
    next();
  };
}

// Example: Middleware that ensures the user belongs to a specific school (for students/restaurants)
export function restrictToSchool(paramName = 'schoolId') {
  return (req: Request, res: Response, next: NextFunction) => {
    const user = req.currentUser!;
    const targetSchoolId = req.params[paramName] || req.body.schoolId;

    // Platform admins bypass
    if (user.role === 'ADMIN') return next();

    if (!user.schoolId || user.schoolId !== targetSchoolId) {
      return res.status(403).json({ error: 'Access denied to this school' });
    }
    next();
  };
}
