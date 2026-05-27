# Moving Light Database

Searchable dashboard of moving light fixtures — by brand, type, specs, and application.

## Working on the project

```bash
npm install      # first time only, or after pulling new dependencies
npm run dev      # local dev server — open the printed localhost URL
npm run build    # production build (Vercel does this automatically)
```

## Adding fixtures

Edit `src/fixtures.json` only. Never edit `src/App.jsx` to add data.
See `OPERATIONS.md` for the full schema and add-a-fixture process.

## Two-machine workflow

This project syncs between machines via GitHub, not Dropbox.

- **Before starting work:** `git pull`
- **After finishing work:** `git add -A && git commit -m "..." && git push`
- **Never** edit on both machines at once without pulling first.

## Deployment

Connected to Vercel. Every push to `main` auto-deploys within ~1 minute.
