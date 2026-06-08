import cors from 'cors';
import express from 'express';
import { schoolsRouter } from './src/routes/schools.ts';
import { profilesRouter } from './src/routes/profiles.ts';

const app = express();
const port = Number(process.env.PORT ?? 3000);

app.use(cors());
app.use(express.json());

app.get('/health', (_req, res) => {
  res.json({
    ok: true,
    service: 'chowlet-backend',
  });
});

app.use('/api/schools', schoolsRouter);
app.use('/api/profiles', profilesRouter);

app.use((_req, res) => {
  res.status(404).json({ error: 'Route not found' });
});

app.listen(port, () => {
  console.log(`Chowlet backend listening on http://localhost:${port}`);
});
