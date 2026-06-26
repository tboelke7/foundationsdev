import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

// IMPORTANT: set this to your real domain before launch.
export default defineConfig({
  site: 'https://foundationsdev.com',
  integrations: [sitemap()],
});
