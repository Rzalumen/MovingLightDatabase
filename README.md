# Moving Light Database

Searchable dashboard of moving light fixtures — by brand, type, specs, and application.

## Working on the project

```bash
npm install      # first time only
npm run dev      # local dev server
npm run build    # production build (Vercel runs this automatically)
```

## Adding fixtures

Edit `src/fixtures.json` only. Never edit `src/App.jsx` to add data.
See `OPERATIONS.md` for the schema and process.

## Two-machine workflow (GitHub-synced)

- Before working: `git pull`
- After working: `git add -A && git commit -m "..." && git push`
- Never edit on both machines at once without pulling first.

## Deployment

Connected to Vercel. Every push to `main` auto-deploys within ~1 minute.
