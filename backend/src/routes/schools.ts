import { Router } from 'express';
import { prisma } from '../lib/prisma';
import { authenticate } from '../middleware/auth';
import { authorize } from '../middleware/authorize';

export const schoolsRouter = Router();

function makeSlug(value: string) {
  return value
    .trim()
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, '-')
    .replace(/^-+|-+$/g, '');
}

schoolsRouter.get('/', async (_req, res) => {
  const schools = await prisma.school.findMany({
    orderBy: { createdAt: 'desc' },
  });

  res.json({ schools });
});

schoolsRouter.get('/:slug', async (req, res) => {
  const school = await prisma.school.findUnique({
    where: { slug: req.params.slug },
  });

  if (!school) {
    return res.status(404).json({ error: 'School not found' });
  }

  res.json({ school });
});

schoolsRouter.post('/', authenticate, authorize('ADMIN'), async (req, res) => {
  const name = typeof req.body.name === 'string' ? req.body.name.trim() : '';
  const slugInput = typeof req.body.slug === 'string' ? req.body.slug.trim() : '';
  const slug = makeSlug(slugInput || name);

  if (!name) {
    return res.status(400).json({ error: 'School name is required' });
  }

  if (!slug) {
    return res.status(400).json({ error: 'A valid slug could not be generated' });
  }

  const school = await prisma.school.create({
    data: {
      name,
      slug,
    },
  });

  res.status(201).json({ school });
});
