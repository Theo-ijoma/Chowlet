import "dotenv/config";
import { PrismaPg } from "@prisma/adapter-pg";
import { PrismaClient, UserRole } from "@prisma/client";

const databaseUrl = process.env.DATABASE_URL;

if (!databaseUrl) {
  throw new Error("Missing DATABASE_URL");
}

const adapter = new PrismaPg({ connectionString: databaseUrl });
const prisma = new PrismaClient({ adapter });

const defaultSchoolName = process.env.SEED_SCHOOL_NAME ?? "Chowlet University";
const defaultSchoolSlug = process.env.SEED_SCHOOL_SLUG ?? "chowlet-university";

const adminSupabaseUserId =
  process.env.SEED_ADMIN_SUPABASE_USER_ID ?? "seed-admin-supabase-user-id";
const adminEmail = process.env.SEED_ADMIN_EMAIL ?? "admin@chowlet.local";
const adminFullName = process.env.SEED_ADMIN_FULL_NAME ?? "Chowlet Admin";

async function main() {
  const school = await prisma.school.upsert({
    where: { slug: defaultSchoolSlug },
    update: {
      name: defaultSchoolName,
    },
    create: {
      name: defaultSchoolName,
      slug: defaultSchoolSlug,
    },
  });

  const adminProfile = await prisma.profile.upsert({
    where: { supabaseUserId: adminSupabaseUserId },
    update: {
      email: adminEmail,
      fullName: adminFullName,
      role: UserRole.ADMIN,
      schoolId: null,
    },
    create: {
      supabaseUserId: adminSupabaseUserId,
      email: adminEmail,
      fullName: adminFullName,
      role: UserRole.ADMIN,
      schoolId: null,
    },
  });

  console.log("Seeded starter data:");
  console.log(`- School: ${school.name} (${school.slug})`);
  console.log(`- Admin: ${adminProfile.fullName} <${adminProfile.email}>`);
}

main()
  .catch((error) => {
    console.error("Seed failed:", error);
    process.exitCode = 1;
  })
  .finally(async () => {
    await prisma.$disconnect();
  });
