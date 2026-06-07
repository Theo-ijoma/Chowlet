import { Router } from 'express';
import { prisma } from '../lib/prisma';
import { authenticate } from '../middleware/auth';
import { authorize } from '../middleware/authorize';

export const profilesRouter = Router();

profilesRouter.get('/me', authenticate, async (req, res) => {
  return res.json({ profile: req.currentUser });
});

profilesRouter.patch('/me', authenticate, async (req, res) => {
  const fullName = typeof req.body.fullName === 'string' ? req.body.fullName.trim() : undefined;
  const phoneNumber = typeof req.body.phoneNumber === 'string' ? req.body.phoneNumber.trim() : undefined;

  if (!fullName && phoneNumber === undefined) {
    return res.status(400).json({ error: 'Provide at least one field to update' });
  }

  const profile = await prisma.profile.update({
    where: { id: req.currentUser!.id },
    data: {
      ...(fullName ? { fullName } : {}),
      ...(phoneNumber !== undefined ? { phoneNumber: phoneNumber || null } : {}),
    },
  });

  res.json({ profile });
});

profilesRouter.get('/', authenticate, authorize('ADMIN'), async (_req, res) => {
  const profiles = await prisma.profile.findMany({
    include: {
      school: true,
    },
    orderBy: { createdAt: 'desc' },
  });

  res.json({ profiles });
});
